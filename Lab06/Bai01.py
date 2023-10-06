import pandas as pd
df=pd.read_csv("E:\Workplace\python\Lab\Lab06\Automobile_data.csv")

# xuất dữ liệu đọc từ tập tin Automobile_data.csv
# mặc định sẽ hiển thị 5 dòng đầu và 5 dòng cuối
print(df)

# xuất 6 dòng đầu tiên
print(df.head(6))

# xuất 7 dòng cuối cùng
print(df.tail(7))

# xuất 11 dòng đầu tiên
print(df.head(11))

# xuất ra màn hình tên công ty có ô tô đắt nhất
df=df[['company','price']][df.price==df['price'].max()]
print(df)

# xuất ra màn hình chi tiết tất cả xe ô tô thuộc hãng Toyota
# car_Manufacturers=df.groupby('company')
# toyotaDf=car_Manufacturers.get_group('toyota')
# print(toyotaDf)

# đếm số xe của từng hãng
print(df['company'].value_counts())

# hiển thị giá xe cao nhất của mỗi hãng
car_Manufacturers=df.groupby('company')
priceDf=car_Manufacturers[['company','price']].max('price')
print(priceDf)

# hiển thị giá xe trung bình của mỗi hãng
car_Manufacturers=df.groupby('company')
priceDf=car_Manufacturers[['company','price']].mean('price')
print(priceDf)

