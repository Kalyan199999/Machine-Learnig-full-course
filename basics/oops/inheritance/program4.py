# hierarchial inheritance

class Shape:
    def __init__(self):
        print("Shape constructor called")
    
    def area(self):
        print("Area of a shape")
    
    def circumference(self):
        print("Circumference of a shape")
    

class Circle(Shape):
    def __init__(self, radius):
        super().__init__()
        print("Circle constructor called")
        self.radius = radius
    
    def area(self):
        return 3.14 * self.radius * self.radius
    
    def circumference(self):
        return 2*3.14*self.radius


class Rectangle(Shape):
    def __init__(self, length, breadth):
        super().__init__()
        print("Rectangle constructor called")
        self.length = length
        self.breadth = breadth

    def area(self):
        return self.length * self.breadth

    def circumference(self):
        return 2*(self.length + self.breadth)
    


# Create objects of Circle and Rectangle
circle = Circle(5)
rectangle = Rectangle(4, 6)

print(f"Area of a circle: {circle.area()}")
print(f"Area of a Rectangle: {rectangle.area()}")

print(f"Circumference of a circle:{round( circle.circumference() , 2)}")
print(f"Circumference of a Rectangle:{rectangle.circumference()}")