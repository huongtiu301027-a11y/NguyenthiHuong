import pandas as pd

# 1. Đọc dữ liệu
df = pd.read_csv("C:/Users/ADMIN/OneDrive/Desktop/KHDL va AI/financial_anomaly_data.csv")

# 2. Xử lý cơ bản
# Bỏ ID (không có ý nghĩa cho model)
df = df.drop(columns=["TransactionID"])

# Chuyển thời gian → giờ
df["Timestamp"] = pd.to_datetime(df["Timestamp"], format="mixed", dayfirst=True)
df["Hour"] = df["Timestamp"].dt.hour
df = df.drop(columns=["Timestamp"])

# 3. Encode dữ liệu chữ → số
df = pd.get_dummies(df)

# 4. Chuẩn hóa
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
X_scaled = scaler.fit_transform(df)

# 5. Model: Isolation Forest
from sklearn.ensemble import IsolationForestcd 
model = IsolationForest(contamination=0.01, random_state=42)
model.fit(X_scaled)

# 6. Dự đoán anomaly
df["anomaly"] = model.predict(X_scaled)

# 7. Kết quả
print("Phân bố kết quả:")
print(df["anomaly"].value_counts())

# 8. Lấy các giao dịch bất thường
fraud = df[df["anomaly"] == -1]
print("\nMột số giao dịch bất thường:")
print(())