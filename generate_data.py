import pandas as pd
import numpy as np

np.random.seed(42)
n = 5000

df = pd.DataFrame({
    "Document_No": np.arange(100000, 100000+n),
    "Company_Code": np.random.choice(['1000','2000','3000'], n),
    "Account": np.random.choice([400000,400001,500000], n),
    "Amount": np.random.normal(5000000, 800000, n),
    "Doc_Type": np.random.choice(['SA','KR'], n),
    "Posting_Key": np.random.choice([40,50,31], n),
    "User_ID": np.random.choice(['U001','U002','U003'], n)
})

# tạo anomaly
idx = np.random.choice(n, int(0.05*n), replace=False)
df.loc[idx, "Amount"] *= 8

df.to_csv("sap_data.csv", index=False)

print("Đã tạo dữ liệu!")