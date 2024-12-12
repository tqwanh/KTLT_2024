import tkinter as tk  # Thư viện Tkinter để tạo giao diện đồ họa
# Tạo cửa sổ chính
window = tk.Tk()
window.title("Chọn ngôn ngữ lập trình yêu thích")
window.geometry("250x200")

# Tiêu đề
label = tk.Label(window, text="Choose your favourite\nprogramming language:", font=("Arial", 10))
label.pack(pady=10)

# Biến lưu giá trị của lựa chọn radio button
selected_language = tk.StringVar(value="Python 1")  # Giá trị mặc định

# Hàm xử lý sự kiện khi lựa chọn thay đổi
def on_radio_button_change():
    print(f"Bạn đã chọn: {selected_language.get()}")  # In ra lựa chọn hiện tại

# Tạo các radio button như các indicator
languages = [("Python 1", "Python 1"), ("Perl 2", "Perl 2"), 
             ("Java 3", "Java 3"), ("C++ 4", "C++ 4"), ("C 5", "C 5")]

for text, value in languages:
    radio = tk.Radiobutton(window, text=text, variable=selected_language, value=value, 
                           command=on_radio_button_change, indicatoron=False, width=20, padx=5, pady=5)
    radio.pack(anchor="w", padx=10, pady=2)

# Hiển thị cửa sổ
window.mainloop()
print('Tran Quang Anh, 235752021610095')
