import pandas as pd
df=pd.read_csv("E:\Workplace\python\Lab\Lab06\sales_data.csv")

print(df)

# xuất hàng dữ liệu của tháng có lợi nhuận cao nhất
df=df.iloc[::-1][df.total_profit==df['total_profit'].max()]
print(df)

# Xuất hàng dữ liệu của tháng bán nhiều mặt hàng nhất
df=df.iloc[::-1][df.total_units==df['total_units'].max()]
print(df)

# Xuất hàng dữ liệu của tháng bán nhiều kem đánh răng nhất:
df=df.iloc[::-1][df.toothpaste==df['toothpaste'].max()]
print(df)

# cho biết tổng lợi nhuận của cả năm
# sum_profit=df[['total_profit']].sum('total_profit')
# print(sum_profit)