class Shape:
    def area(self):
        return 0
    
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    def area(self):
        return self.length*self.width


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return 3.14*self.radius*self.radius


rect = Rectangle(5,10)
area  = rect.area()
print(area)

circle = Circle(7)
are = circle.area()

print(are)