def append_text_to_file(file_path, text):
    with open(file_path, 'a', encoding='utf-8') as file:  # Thêm encoding='utf-8'
        file.write(text + '\n')  # Thêm một dòng mới
    print("Nội dung đã thêm vào tệp.")

# Ví dụ sử dụng
append_text_to_file('file.txt', 'Nội dung mới')  # Thay 'file.txt' và nội dung bạn muốn thêm
print('Tran Quang Anh, 235752021610095')
