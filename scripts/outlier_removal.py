import pandas as pd

def remove_outliers_iqr(df, columns):
    """
    กรอง outlier จาก DataFrame โดยใช้ IQR
    :param df: pandas DataFrame
    :param columns: list ของชื่อคอลัมน์ที่ต้องการกรอง outlier
    :return: DataFrame ที่กรองแล้ว
    """
    filtered_df = df.copy()
    for col in columns:
        Q1 = filtered_df[col].quantile(0.25)
        Q3 = filtered_df[col].quantile(0.75)
        IQR = Q3 - Q1
        lower_bound = Q1 - 1.5 * IQR
        upper_bound = Q3 + 1.5 * IQR
        filtered_df = filtered_df[(filtered_df[col] >= lower_bound) & (filtered_df[col] <= upper_bound)]
    return filtered_df

def filter_and_save(csv_path, output_path, columns):
    """
    โหลด csv, กรอง outlier และบันทึกเป็นไฟล์ใหม่
    :param csv_path: path ของไฟล์ input
    :param output_path: path ของไฟล์ output ที่จะบันทึก
    :param columns: คอลัมน์ที่จะใช้กรอง
    """
    df = pd.read_csv(csv_path, parse_dates=['InvoiceDate'])
    filtered_df = remove_outliers_iqr(df, columns)
    filtered_df.to_csv(output_path, index=False)
    print(f"✔️ กรอง Outliers แล้ว และบันทึกไปยัง: {output_path}")
