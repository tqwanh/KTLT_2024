full_name = input("Nhập tên người: ")
parts = full_name.split()
if len(parts) >= 2:
    ho = parts[0]  
    ten_rieng = parts[-1] 
    print(f"Họ: {ho}")
    print(f"Tên riêng: {ten_rieng}")
print('Tran Quang Anh, 235752021610095')
