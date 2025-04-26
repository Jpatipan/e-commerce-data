# 🛒 E-Commerce Data Analysis Project

โปรเจกต์นี้มุ่งเน้นการวิเคราะห์ข้อมูลการขายจากธุรกิจ e-commerce โดยใช้ภาษา Python และไลบรารีต่าง ๆ เช่น Pandas, Matplotlib และ Seaborn เพื่อทำความเข้าใจพฤติกรรมการซื้อของลูกค้า แนวโน้มการขายสินค้า และข้อมูลเชิงลึกอื่น ๆ ที่สามารถนำไปใช้ในการตัดสินใจทางธุรกิจได้

## 📁 โครงสร้างโปรเจกต์

```
e-commerce-data/
├── notebooks/
│   └── E-commerce Sales Overview.pbix
├── data/
│   ├── raw/
│   │   └── data.csv
│   ├── cleaned_datafiltered.csv
│   ├── cleaned_data.csv
│   └── rfm_customers.csv
├── notebooks/
│   ├── 01_exploration.ipynb
│   ├── 02_daily_sales_analysis.ipynb
│   ├── 03_product_trend.ipynb
│   ├── 04_sales_daily.ipynb
│   └── 05_totalprice_vs_quantity.ipynb
├── scripts/
│   ├── analysis.py
│   ├── clean_data.py
│   ├── customer_segmentation.py
│   ├── daily_sales_stats.py
│   ├── outliers_removal.py
│   └── product_trends.py
├── README.md
└── requirements.txt
```

## 🧰 การติดตั้งและใช้งาน

### โคลนโปรเจกต์
```bash
git clone https://github.com/Jpatipan/e-commerce-data.git
```

### ติดตั้ง Dependencies
```bash
pip install -r requirements.txt
```

## 📊 ฟีเจอร์หลัก

### การทำความสะอาดข้อมูล
- ลบข้อมูลที่ไม่สมบูรณ์หรือผิดปกติ
- กำจัด outliers โดยใช้วิธี IQR

### การวิเคราะห์ข้อมูล
- ยอดขายรวม (Total Revenue)
- จำนวนรวมออเดอร์
- จำนวนสินค้าที่ขาย
- ยอดขายต่อออเดอร์
- ราคาสินค้าสูงสุด
- ราคาสินค้าต่ำสุด

### การแสดงกราฟข้อมูล
- 10 สินค้าที่ขายดีที่สุด
- 10 สินค้าที่ทำรายได้สูงที่สุด
- ยอดขายสินค้ารายเดือน
- จำนวนลูกค้าครั้งเดียว vs ลูกค้าซื้อซ้ำ
