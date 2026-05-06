# Nhập số tiền ban đầu và lãi suất (%/tháng)
tien_ban_dau = float(input("Nhập số tiền ban đầu: "))
lai_suat = float(input("Nhập lãi suất (%/tháng): ")) / 100

so_thang = 12

tien_cuoi = tien_ban_dau * (1 + lai_suat) ** so_thang

print("Số tiền sau 12 tháng là:", tien_cuoi)
print("Lợi nhuận:", tien_cuoi - tien_ban_dau)