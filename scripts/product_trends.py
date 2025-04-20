import pandas as pd
import matplotlib.pyplot as plt

def product_trend(df, product_name):
    """
    วิเคราะห์แนวโน้มการขายของสินค้าตามชื่อสินค้าที่ระบุ โดยคำนวณยอดขายรวมในแต่ละเดือน

    Parameters:
    df (pandas.DataFrame): DataFrame ที่มีข้อมูลการขายสินค้า
    product_name (str): ชื่อสินค้าที่ต้องการวิเคราะห์

    Returns:
    pandas.Series: แนวโน้มการขายของสินค้าตามเดือน
    """
    # สร้างคอลัมน์ 'Month' จากวันที่ซื้อ (คัดแค่ปีและเดือน)
    df['Month'] = df['InvoiceDate'].astype(str).str[:7]
    
    # กรองข้อมูลสินค้าที่ต้องการและคำนวณยอดขายรวมในแต่ละเดือน
    trend = df[df['Description'].str.contains(product_name, case=False)].groupby('Month')['Quantity'].sum()
    
    return trend