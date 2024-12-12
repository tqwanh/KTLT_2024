def read_last_n_lines(file_path, n):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        for line in lines[-n:]:
            print(line.rstrip())

# Ví dụ sử dụng
read_last_n_lines('file.txt', 3)  # Thay 'file.txt' và số dòng bạn muốn đọc
print('Tran Quang Anh, 235752021610095')
