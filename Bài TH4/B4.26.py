# Khởi tạo số dư tài khoản ban đầu là 0
so_du = 0

# Nhập nhật ký giao dịch
while True:
    # Nhập một dòng giao dịch
    giao_dich = input("Nhập giao dịch (hoặc nhấn Enter để dừng): ")
    
    # Nếu chuỗi nhập vào trống, dừng nhập liệu
    if not giao_dich:
        break
    
    # Tách thông tin giao dịch thành loại giao dịch và số tiền
    loai_giao_dich, so_tien = giao_dich.split()
    so_tien = int(so_tien)  # Chuyển số tiền thành số nguyên
    
    # Kiểm tra loại giao dịch
    if loai_giao_dich == 'D':  # Tiền gửi
        so_du += so_tien
    elif loai_giao_dich == 'W':  # Tiền rút
        so_du -= so_tien

# In ra số tiền còn lại trong tài khoản
print("Số tiền thực trong tài khoản:", so_du)
print('Tran Quang Anh, 235752021610095')
