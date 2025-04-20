import pandas as pd
from datetime import timedelta

def assign_score(series, score_labels):
    """ใช้ qcut หากเป็นไปได้ ไม่เช่นนั้น fallback ไปที่ rank()"""
    try:
        return pd.qcut(series, q=len(score_labels), labels=score_labels, duplicates='drop')
    except ValueError:
        # fallback แบบง่าย ถ้าไม่สามารถแบ่ง qcut ได้
        return pd.qcut(series.rank(method='first'), q=len(score_labels), labels=score_labels)

def rfm_analysis(df):
    df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])
    snapshot_date = df['InvoiceDate'].max() + timedelta(days=1)

    rfm = df.groupby('CustomerID').agg({
        'InvoiceDate': lambda x: (snapshot_date - x.max()).days,
        'InvoiceNo': 'nunique',
        'TotalPrice': 'sum'
    }).reset_index()

    rfm.columns = ['CustomerID', 'Recency', 'Frequency', 'Monetary']

    # กำหนด score ด้วยฟังก์ชัน assign_score
    rfm['R_score'] = assign_score(rfm['Recency'], [4, 3, 2, 1])
    rfm['F_score'] = assign_score(rfm['Frequency'], [1, 2, 3, 4])
    rfm['M_score'] = assign_score(rfm['Monetary'], [1, 2, 3, 4])

    # รวมคะแนน
    rfm['RFM_Score'] = rfm['R_score'].astype(str) + rfm['F_score'].astype(str) + rfm['M_score'].astype(str)

    return rfm

if __name__ == '__main__':
    df = pd.read_csv('data/cleaned_data.csv')
    rfm_result = rfm_analysis(df)
    rfm_result.to_csv('data/rfm_customers.csv', index=False)
    print("✅ บันทึกไฟล์ rfm_customers.csv เรียบร้อยแล้ว")
