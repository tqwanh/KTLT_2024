def tam_giac_pascal(n):
    triangle = [[1]]
    for i in range(1, n):
        row = [1]
        for j in range(1, i):
            row.append(triangle[i-1][j-1] + triangle[i-1][j])
        row.append(1)
        triangle.append(row)
    return triangle

# Nhập số n
n = int(input("Nhập n: "))

# In ra n dòng đầu tiên của tam giác Pascal
pascal_triangle = tam_giac_pascal(n)
for row in pascal_triangle:
    print(row)
print('Tran Quang Anh, 235752021610095')
