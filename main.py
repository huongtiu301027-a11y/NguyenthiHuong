import pandas as pd
from sklearn.ensemble import IsolationForest
from sklearn.preprocessing import StandardScaler

# đọc dữ liệu
df = pd.read_csv("sap_data.csv")

# chuyển dữ liệu dạng chữ thành số
df = pd.get_dummies(df, columns=['Doc_Type','User_ID','Company_Code'])

# chọn feature
features = [col for col in df.columns if col != 'Document_No']
X = df[features]

# chuẩn hoá dữ liệu
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# model phát hiện bất thường
model = IsolationForest(contamination=0.05, random_state=42)
df['anomaly'] = model.fit_predict(X_scaled)

# in kết quả
print("Thống kê:")
print(df['anomaly'].value_counts())

print("\nMột số dòng bất thường:")
print(df[df['anomaly'] == -1].head())