def benefit(t, n, k):
    if t > 0 and n > 0 and k > 0:
        total_amount = n * ((1 + t / 100) ** k)
        print(f"Số tiền nhận được sau {k} tháng với lãi suất {t}%/tháng là: {total_amount:.2f}")
    else:
        print("Lãi suất, số vốn và số tháng phải là các số dương.")
try:
    t = float(input("Nhập lãi suất tiết kiệm (%/tháng): "))
    n = float(input("Nhập số vốn ban đầu: "))
    k = int(input("Nhập số tháng gửi: "))
    benefit(t, n, k)
except ValueError:
    print("Vui lòng nhập các giá trị hợp lệ.")
print('Tran Quang Anh, 235752021610095')
