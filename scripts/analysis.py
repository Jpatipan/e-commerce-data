import pandas as pd

def top_selling_products(df, n=5):
    result = (
        df.groupby('Description')['TotalPrice']
        .sum()
        .sort_values(ascending=False)
        .head(n)
    )
    return result

def monthly_sales(df):
    df['Month'] = df['InvoiceDate'].astype(str).str[:7]
    return df.groupby('Month')['TotalPrice'].sum()

def repeat_customers(df):
    repeat_df = df.groupby('CustomerID')['InvoiceNo'].nunique()
    return repeat_df[repeat_df > 1].count()

if __name__ == "__main__":
    df = pd.read_csv('data/cleaned_data.csv')
    
    print("Top 5 สินค้าขายดี:")
    print(top_selling_products(df))

    print("\nยอดขายรายเดือน:")
    print(monthly_sales(df))

    print(f"\nจำนวนลูกค้าที่กลับมาซื้อซ้ำ: {repeat_customers(df)} คน")
