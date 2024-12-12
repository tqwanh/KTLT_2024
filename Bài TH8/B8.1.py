import turtle
def draw_square():
    window = turtle.Screen()
    window.bgcolor("white")
    
    pen = turtle.Turtle()
    pen.color("blue")
    pen.pensize(2)

    for _ in range(4):
        pen.forward(100)
        pen.right(90)

    window.mainloop()

draw_square()
print('Tran Quang Anh, 235752021610095')
