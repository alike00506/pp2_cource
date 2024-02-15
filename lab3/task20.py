class Shape:
    def __init__(self):
        pass

    def area(self):
        return 0

class Rectangle(Shape):
    def __init__(self, length, width):
        super().__init__()
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width


shape_instance = Shape()
print("Area of generic shape:", shape_instance.area())

rectangle_instance = Rectangle(4, 6)
print("Area of rectangle:", rectangle_instance.area())
