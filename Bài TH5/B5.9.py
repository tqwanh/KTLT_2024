# main.py

import search
# Nhập số lượng phần tử trong danh sách
n = int(input("Nhập số lượng phần tử trong danh sách: "))

# Nhập các giá trị cho danh sách
dlist = []
for i in range(n):
    value = int(input(f"Nhập giá trị cho phần tử thứ {i+1}: "))
    dlist.append(value)

# Sắp xếp danh sách trước khi tìm kiếm nhị phân
dlist.sort()
print("Danh sách sau khi sắp xếp:", dlist)

# Nhập phần tử cần tìm
value = int(input("Nhập phần tử cần tìm: "))

# Tìm kiếm phần tử bằng hàm binary_search
found = search.binary_search(dlist, value)

# In kết quả
if found:
    print(f"Phần tử '{value}' có trong danh sách.")
else:
    print(f"Phần tử '{value}' không có trong danh sách.")
print('Tran Quang Anh, 235752021610095')
