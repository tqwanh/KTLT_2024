# Bước 1: Nhập chuỗi các từ cách nhau bởi dấu cách
chuoi_dau_vao = input("Nhập chuỗi các từ cách nhau bởi dấu cách: ")

# Bước 2: Tách chuỗi thành danh sách các từ
danh_sach_tu = chuoi_dau_vao.split()

# Bước 3: Sắp xếp danh sách các từ theo thứ tự từ điển
danh_sach_tu.sort()

# Bước 4: In ra từng từ trong danh sách đã sắp xếp
for tu in danh_sach_tu:
    print(tu)
print('Tran Quang Anh, 235752021610095')
