import math

def Tinh(R):
    if R > 0:
        chu_vi = 2 * math.pi * R
        dien_tich = math.pi * R ** 2
        print(f"Chu vi hình tròn với bán kính {R} là: {chu_vi:.2f}")
        print(f"Diện tích hình tròn với bán kính {R} là: {dien_tich:.2f}")
    else:
        print("Bán kính phải là một số dương.")
try:
    R = float(input("Nhập bán kính của hình tròn: "))
    Tinh(R)
except ValueError:
    print("Vui lòng nhập một số hợp lệ.")

print('Tran Quang Anh, 235752021610095')
