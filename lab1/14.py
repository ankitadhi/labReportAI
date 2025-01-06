class Circle:
    def __init__(self, radius):
        self.radius = radius


    def area(self):
        area = 3.14*self.radius*self.radius
        return area
    
    def perimeter(self):
        perimeter = 2*3.14*self.radius
        return perimeter
circle =Circle(7)
area = circle.area()

print("Area of circle: ", area)