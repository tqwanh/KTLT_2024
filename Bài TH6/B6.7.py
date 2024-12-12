import math 

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)

    def circumference(self):
        return 2 * math.pi * self.radius

# Ví dụ sử dụng
circle = Circle(9)
print("Diện tích:", circle.area())
print("Chu vi:", circle.circumference())
print('Tran Quang Anh, 235752021610095')
