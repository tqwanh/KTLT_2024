import math
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)
circle = Circle(5)
print("Diện tích hình tròn:", circle.area())
print('Tran Quang Anh, 235752021610095')
