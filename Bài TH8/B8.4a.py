import tkinter as tk  # Thư viện Tkinter để tạo giao diện đồ họa
# Tạo cửa sổ chính
window = tk.Tk()
window.title("Cửa sổ đồ họa Tkinter với Button tùy chỉnh")
window.geometry("400x300")

# Hàm xử lý sự kiện khi bấm nút
def on_button_click():
    print("Button đã được bấm!")  # Hiển thị thông báo khi nút được bấm

# Tạo một button widget với màu nền và màu chữ tùy chỉnh
button = tk.Button(window, text="Click Me!", command=on_button_click, bg="blue", fg="white")
button.pack(pady=20)

# Hiển thị cửa sổ
window.mainloop()
print('Tran Quang Anh, 235752021610095')
