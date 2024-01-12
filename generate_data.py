# generate_data.py
import numpy as np
import pandas as pd

def generate_data():
    np.random.seed(42)
    dates = pd.date_range(start="2022-01-01", end="2023-12-31", freq="D")
    sales = np.random.randint(50, 200, size=(len(dates)))
    df = pd.DataFrame({"Date": dates, "Sales": sales})

    # Ekstrak nilai numerik dari kolom tanggal
    df["Date"] = df["Date"].dt.strftime('%Y/%m/%d')

    df.to_excel("data_penjualan.xlsx", index=False)

if __name__ == "__main__":
    generate_data()
