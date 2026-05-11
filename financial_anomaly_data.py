import pandas as pd

# 1. Đọc dữ liệu
df = pd.read_csv("C:/Users/ADMIN/OneDrive/Desktop/KHDL va AI/financial_anomaly_data.csv")

# 2. Xử lý dữ liệu
df = df.drop(columns=["TransactionID"])

df["Timestamp"] = pd.to_datetime(df["Timestamp"], format="mixed", dayfirst=True)

df["Hour"] = df["Timestamp"].dt.hour

df = df.drop(columns=["Timestamp"])

# 3. Encode dữ liệu
df = pd.get_dummies(df)

# 4. Chuẩn hóa
from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()
X_scaled = scaler.fit_transform(df)

# 5. Isolation Forest
from sklearn.ensemble import IsolationForest

model = IsolationForest(
    contamination=0.01,
    random_state=42
)

model.fit(X_scaled)

# 6. Dự đoán
df["anomaly"] = model.predict(X_scaled)

# 7. Kết quả
print(df["anomaly"].value_counts())

# 8. Giao dịch bất thường
fraud = df[df["anomaly"] == -1]

print(fraud.head())