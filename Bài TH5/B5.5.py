# main.py
import list_utils
# Nhập số lượng phần tử của danh sách
n = int(input("Nhập số lượng phần tử của danh sách: "))

# Nhập các giá trị cho danh sách
lst = []
for i in range(n):
    value = float(input(f"Nhập giá trị cho phần tử thứ {i+1}: "))
    lst.append(value)

# Sắp xếp danh sách
sorted_lst = list_utils.sort_list(lst)
print("Danh sách sau khi sắp xếp:", sorted_lst)

# Tìm phần tử lớn nhất và nhỏ nhất
max_value = list_utils.find_max(lst)
min_value = min(lst)  # Tìm phần tử nhỏ nhất trực tiếp

print("Phần tử lớn nhất trong danh sách:", max_value)
print("Phần tử nhỏ nhất trong danh sách:", min_value)
print('Tran Quang Anh, 235752021610095')
