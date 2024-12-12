import turtle

# Tạo màn hình vẽ
window = turtle.Screen()
window.bgcolor("white")

# Tạo bút vẽ
pen = turtle.Turtle()
pen.speed(0)  # Đặt tốc độ bút vẽ tối đa
pen.width(2)  # Đặt độ dày của nét vẽ

# Danh sách màu sắc cho các vòng tròn
colors = ["red", "green", "blue"]

# Vẽ các vòng tròn lồng nhau
for i in range(36):  # Lặp 36 lần để tạo ra 36 hình tròn
    pen.color(colors[i % 3])  # Thay đổi màu sau mỗi lần vẽ
    pen.circle(100)  # Vẽ hình tròn bán kính 100
    pen.right(10)  # Xoay bút một góc 10 độ

# Ẩn bút và giữ cửa sổ mở
pen.hideturtle()
window.mainloop()
print('Tran Quang Anh, 235752021610095')
