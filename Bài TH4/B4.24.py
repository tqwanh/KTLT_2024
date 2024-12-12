# Nhập câu từ người dùng
cau = input("Nhập một câu: ")

# Đếm số chữ hoa và chữ thường
chu_hoa = sum(ch.isupper() for ch in cau)
chu_thuong = sum(ch.islower() for ch in cau)

# In kết quả
print(f"Chữ hoa: {chu_hoa}")
print(f"Chữ thường: {chu_thuong}")
print('Tran Quang Anh, 235752021610095')
