# main.py

import sort
# Nhập số lượng phần tử trong danh sách
n = int(input("Nhập số lượng phần tử trong danh sách: "))

# Nhập các giá trị cho danh sách
nlist = []
for i in range(n):
    value = int(input(f"Nhập giá trị cho phần tử thứ {i+1}: "))
    nlist.append(value)

print("Danh sách trước khi sắp xếp:", nlist)

# Sắp xếp danh sách bằng hàm bubbleSort
sorted_list = sort.bubbleSort(nlist)

print("Danh sách sau khi sắp xếp:", sorted_list)
print('Tran Quang Anh, 235752021610095')
