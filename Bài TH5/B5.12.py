import numpy as np
# Dữ liệu id sinh viên và chiều cao
student_ids = np.array([101, 102, 103, 104, 105])
heights = np.array([1.75, 1.65, 1.80, 1.70, 1.60])

# Sử dụng hàm lexsort để sắp xếp theo chiều cao tăng dần
# Lưu ý rằng để sắp xếp tăng dần, chúng ta cần chiều cao âm
sorted_indices = np.lexsort((heights, student_ids))

# In chỉ số sắp xếp
print("Indices that describe the order of sorting:")
print(sorted_indices)

# In dữ liệu đã sắp xếp
sorted_student_ids = student_ids[sorted_indices]
sorted_heights = heights[sorted_indices]

print("\nSorted student IDs and their heights:")
for idx in range(len(sorted_student_ids)):
    print(f"ID: {sorted_student_ids[idx]}, Height: {sorted_heights[idx]}")
print('Tran Quang Anh, 235752021610095')
