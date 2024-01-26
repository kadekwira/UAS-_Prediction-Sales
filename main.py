import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# Baca data dari file Excel
df = pd.read_excel('data_penjualan.xlsx')

# Ubah kolom tanggal ke format datetime dan tetapkan indeks
df['Date'] = pd.to_datetime(df['Date'])
df.set_index('Date', inplace=True)

# Ekstrak fitur waktu
df['Week'] = df.index.isocalendar().week
df['Month'] = df.index.month
df['Year'] = df.index.year

# Hitung penjualan mingguan, bulanan, dan tahunan
weekly_sales = df['Sales'].resample('W').sum()
monthly_sales = df['Sales'].resample('M').sum()
yearly_sales = df['Sales'].resample('Y').sum()

# Bagi data menjadi set pelatihan dan pengujian
X = df[['Week', 'Month', 'Year']]
y = df['Sales']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Bangun model prediksi menggunakan regresi linear
model = LinearRegression()
model.fit(X_train, y_train)

# Evaluasi kinerja model
predictions = model.predict(X_test)
mse = mean_squared_error(y_test, predictions)
print(f'Mean Squared Error: {mse}')

# Hitung rata-rata penjualan per tahun, per bulan, dan per minggu
average_sales_per_year = df['Sales'].resample('Y').mean()
average_sales_per_month = df['Sales'].resample('M').mean()
average_sales_per_week = df['Sales'].resample('W').mean()

# Tampilkan rata-rata penjualan ke konsol
print("\nRata-rata Penjualan Per Tahun:")
print(average_sales_per_year)

print("\nRata-rata Penjualan Per Bulan:")
print(average_sales_per_month)

print("\nRata-rata Penjualan Per Minggu:")
print(average_sales_per_week)




# Visualisasikan data
st.title('Data Prediksi')
fig = plt.figure(figsize=(12, 6))
st.line_chart(weekly_sales)
st.line_chart(monthly_sales)
st.line_chart(yearly_sales)
plt.plot(weekly_sales, label='Weekly Sales')
plt.plot(monthly_sales, label='Monthly Sales')
plt.plot(yearly_sales, label='Yearly Sales')
plt.legend()
plt.show()

