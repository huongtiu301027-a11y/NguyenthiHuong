von = float(input("Nhập số vốn ban đầu: "))
lai_suat = float(input("Nhập lãi suất (%): ")) / 100
so_ky = int(input("Nhập số kỳ (tháng/năm): "))

tien_cuoi = von * (1 + lai_suat) ** so_ky
loi_nhuan = tien_cuoi - von

print("Số tiền sau cùng:", tien_cuoi

