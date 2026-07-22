import duckdb
import pandas as pd

# ตั้งค่าให้ Pandas แสดงคอลัมน์ทั้งหมดไม่โดนตัด
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 1000)

# 1. เชื่อมต่อฐานข้อมูล DuckDB
conn = duckdb.connect('northwind_dw_duckdb/dev.duckdb')

# 2. แสดงรายชื่อตารางทั้งหมดในระบบ
print("Tables in dev.duckdb:")
tables = conn.execute("SELECT table_name FROM information_schema.tables WHERE table_schema = 'main'").fetchall()
for table in tables:
    print(f" - {table[0]}")

print("\n" + "=" * 80)
print("Table: stg_customers")
print("=" * 80)

# 3. ดึงข้อมูลจากตาราง stg_customers มาแสดง 20 รายการแรก
df = conn.execute("SELECT * FROM main.stg_customers LIMIT 20").df()
print(df)