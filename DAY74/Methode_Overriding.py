class Shape:
    # Constructor of Shape class
    # It stores two values: x and y
    def __init__(self, num1, num2):
        self.x = num1
        self.y = num2

    # Area method for Shape
    # For a rectangle-like shape, area = x * y
    def Area(self):
        return self.x * self.y


class Circle(Shape):
    # Constructor of Circle class
    # It takes only radius as input
    def __init__(self, radius):
        self.radius = radius   # store radius separately

        # Call parent class constructor
        # Here x = radius and y = radius
        # so parent Area() gives radius * radius
        super().__init__(radius, radius)

    # Area method of Circle
    # Formula: 3.14 * radius * radius
    def Area(self):
        # super().Area() returns radius * radius
        return 3.14 * super().Area()


# Creating object of Shape class
# Here it acts like a rectangle with length = 3 and breadth = 5
Rectangle = Shape(3, 5)
print(Rectangle.Area())   # Output: 15

# Creating object of Circle class with radius = 5
circle = Circle(5)
print(circle.Area())      # Output: 78.5