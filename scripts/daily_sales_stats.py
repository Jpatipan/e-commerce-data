import pandas as pd

def daily_sales(df):
    df['Date'] = df['InvoiceDate'].dt.date
    return df.groupby('Date')['TotalPrice'].sum().reset_index()
