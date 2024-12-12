def read_first_n_lines(file_path, n):
    with open(file_path, 'r') as file:
        for _ in range(n):
            print(file.readline().rstrip())

# Ví dụ sử dụng
read_first_n_lines('file.txt', 5)  # Thay 'file.txt' và số dòng bạn muốn đọc
print('Tran Quang Anh, 235752021610095')
