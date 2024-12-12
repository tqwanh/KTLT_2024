class StringHandler:
    def get_String(self):
        self.user_string = input("Nhập chuỗi: ")

    def print_String(self):
        print(self.user_string.upper())

# Ví dụ sử dụng
handler = StringHandler()
handler.get_String()
handler.print_String()
print('Tran Quang Anh, 235752021610095')
