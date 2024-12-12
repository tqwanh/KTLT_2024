import re

def kiem_tra_mat_khau(passwords):
    # Định dạng mật khẩu hợp lệ
    pattern = re.compile(r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[$#@])[A-Za-z\d$#@]{6,12}$")
    
    # Lọc các mật khẩu hợp lệ
    valid_passwords = [pw for pw in passwords if pattern.match(pw)]
    
    # Kết quả là các mật khẩu hợp lệ, ngăn cách bởi dấu phẩy
    return ",".join(valid_passwords)

# Nhập mật khẩu và chia thành danh sách các mật khẩu
input_passwords = input("Nhập các mật khẩu, ngăn cách nhau bởi dấu phẩy: ").split(',')

# Kiểm tra mật khẩu và in kết quả
print("Các mật khẩu hợp lệ:", kiem_tra_mat_khau(input_passwords))
print("Tran Quang Anh, 235752021610095")
