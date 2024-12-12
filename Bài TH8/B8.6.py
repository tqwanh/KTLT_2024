from tkinter import *
# Hàm xử lý sự kiện khi chọn "New"
def NewFile():
    print("New File!")
# Hàm xử lý sự kiện khi chọn "About"
def About():
    print("This is a simple example of a menu")
# Tạo cửa sổ chính
root = Tk()
root.title("Menu Example")  # Đặt tiêu đề cho cửa sổ
root.geometry("300x200")  # Thiết lập kích thước cửa sổ
# Tạo menu chính
menu = Menu(root)
root.config(menu=menu)
# Tạo menu "File"
filemenu = Menu(menu, tearoff=0)
menu.add_cascade(label="File", menu=filemenu)
filemenu.add_command(label="New", command=NewFile)  # Thêm mục "New" trong menu "File"
filemenu.add_command(label="Open")  # Thêm mục "Open" trong menu "File"
filemenu.add_command(label="Exit", command=root.quit)  # Thêm mục "Exit" để thoát chương trình
# Tạo menu "Insert"
insertmenu = Menu(menu, tearoff=0)
menu.add_cascade(label="Insert", menu=insertmenu)
insertmenu.add_command(label="Text")  # Thêm mục "Text" trong menu "Insert"
insertmenu.add_command(label="Picture")  # Thêm mục "Picture" trong menu "Insert"
# Tạo menu "Help"
helpmenu = Menu(menu, tearoff=0)
menu.add_cascade(label="Help", menu=helpmenu)
helpmenu.add_command(label="About...", command=About)  # Thêm mục "About" trong menu "Help"
# Bắt đầu vòng lặp sự kiện
root.mainloop()
print('Tran Quang Anh, 235752021610095')
