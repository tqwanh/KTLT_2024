import tkinter as tk
from tkinter import messagebox
# Tạo cửa sổ chính
root = tk.Tk()
root.title("Welcome")
# Tạo biến để lưu trữ lựa chọn của nút radio
selected_option = tk.IntVar()
selected_option.set(1)  # Mặc định chọn tùy chọn đầu tiên
# Định nghĩa hàm hiển thị lựa chọn khi nhấn nút
def show_selection():
    selection = selected_option.get()
    messagebox.showinfo("Lựa chọn", f"Bạn đã chọn tùy chọn {selection}")
# Tạo các nút radio
radio1 = tk.Radiobutton(root, text="First", variable=selected_option, value=1)
radio2 = tk.Radiobutton(root, text="Second", variable=selected_option, value=2)
radio3 = tk.Radiobutton(root, text="Third", variable=selected_option, value=3)
# Đặt các nút radio vào cửa sổ
radio1.pack(side=tk.LEFT, padx=5)
radio2.pack(side=tk.LEFT, padx=5)
radio3.pack(side=tk.LEFT, padx=5)
# Tạo nút "Click Me"
click_button = tk.Button(root, text="Click Me", command=show_selection)
click_button.pack(side=tk.LEFT, padx=5)
# Chạy vòng lặp sự kiện chính
root.mainloop()
print('Tran Quang Anh, 235752021610095')
