#安裝pip install pandas matplotlib seaborn sqlalchemy pyodbc
# -*- coding: utf-8 -*-

import pandas as pd
from sqlalchemy import create_engine
import matplotlib.pyplot as plt
import seaborn as sns

# 連接到MSSQL數據庫 create_engine('mssql+pyodbc://your_username:your_password@your_server/your_database?driver=ODBC+Driver+17+for+SQL+Server')
engine = create_engine('mssql+pyodbc://帳號:密碼@IP/DB名稱?driver=ODBC+Driver+17+for+SQL+Server')
query = 'SELECT * FROM AbsDetail_test'

# 使用pandas讀取數據
df = pd.read_sql(query, engine)

# 數據檢查
print(df.head())

# 使用Matplotlib進行圖示化
plt.figure(figsize=(10, 6))
plt.plot(df['EmpNo'], df['AbsHour'], marker='o')
plt.title('EmpNo vs AbsHour')
plt.xlabel('EmpNo')
plt.ylabel('AbsHour')
plt.grid(True)
plt.show()

# 使用Seaborn進行圖示化
plt.figure(figsize=(10, 6))
sns.scatterplot(x='EmpNo', y='AbsHour', data=df)
plt.title('EmpNo vs AbsHour')
plt.xlabel('EmpNo')
plt.ylabel('AbsHour')
plt.show()
