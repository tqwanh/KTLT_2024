# Nhập câu từ người dùng
cau = input("Nhập một câu: ")

# Đếm số chữ cái và số chữ số
so_chu_cai = sum(ch.isalpha() for ch in cau)
so_chu_so = sum(ch.isdigit() for ch in cau)

# In kết quả
print(f"Số chữ cái là: {so_chu_cai}")
print(f"Số chữ số là: {so_chu_so}")
print('Tran Quang Anh, 235752021610095')
