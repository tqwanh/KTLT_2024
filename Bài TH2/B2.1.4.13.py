import math

def giai_phuong_trinh_bac_2(a, b, c):
    # Kiểm tra nếu a bằng 0 thì phương trình không phải bậc 2
    if a == 0:
        print("Đây không phải là phương trình bậc 2.")
        return
    
    # Tính delta
    delta = b**2 - 4*a*c
    
    # Kiểm tra các trường hợp của delta
    if delta > 0:
        x1 = (-b + math.sqrt(delta)) / (2 * a)
        x2 = (-b - math.sqrt(delta)) / (2 * a)
        print(f"Phương trình có 2 nghiệm phân biệt: x1 = {x1}, x2 = {x2}")
    elif delta == 0:
        x = -b / (2 * a)
        print(f"Phương trình có nghiệm kép: x = {x}")
    else:
        print("Phương trình vô nghiệm.")

# Nhập hệ số a, b, c từ bàn phím
a = float(input("Nhập hệ số a: "))
b = float(input("Nhập hệ số b: "))
c = float(input("Nhập hệ số c: "))

# Gọi hàm giải phương trình
giai_phuong_trinh_bac_2(a, b, c)
print("Tran Quang Anh, 235752021610095")
