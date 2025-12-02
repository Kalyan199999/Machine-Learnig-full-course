class Circle:
    # class attribute -->can be accessed by all objects of the class
    pi = 3.14

    def __init__(self, radius=5):
        self.radius = radius

    def area(self):
        return Circle.pi * self.radius * self.radius

    def circumference(self):
        return 2 * self.pi * self.radius

c1 = Circle()
c2 = Circle(4)

print(c1.pi)
c1.pi = 5
print(c1.pi)

print(c2.pi)

Circle.pi = 7

print(c1.pi)


print(f"Area of object1 is {c1.area()}")

print(f"Area of object-2 is:{c2.area()}")