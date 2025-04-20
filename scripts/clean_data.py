import pandas as pd

def load_and_clean_data(file_path):
    df = pd.read_csv(file_path, encoding='ISO-8859-1')
    
    # ลบ missing values
    df.dropna(inplace=True)

    # แปลงข้อมูลวันที่
    df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])

    # สร้างคอลัมน์ยอดขาย
    df['TotalPrice'] = df['Quantity'] * df['UnitPrice']

    # กรองเฉพาะข้อมูลที่ Quantity > 0
    df = df[df['Quantity'] > 0]

    return df

if __name__ == "__main__":
    cleaned_df = load_and_clean_data('data/raw/data.csv')
    cleaned_df.to_csv('data/cleaned_data.csv', index=False)
    print("Data cleaned and saved.")