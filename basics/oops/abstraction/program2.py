from program1 import Vehicle

class Bike(Vehicle):
    def __init__(self, n,color):
        super().__init__(n)
        self.color = color

    def start(self):
        print("Bike is starting")

    # def stop(self):
    #     print("Bike is stopping")

    def move(self):
        print("Bike is moving")

    def turn(self):
        print("Bike is turning")

class Car(Vehicle):
    def __init__(self, n,color,gears):
        super().__init__(n)
        self.color = color
        self.gears = gears

    def start(self):
        print("Car is starting")

    def stop(self):
        print("Car is stopping")

# bike instance
b = Bike(2,'gray')
print(f"Bike is having the {b.no_of_tyres} tyres!")
b.start()
b.stop()

print()

# car instance
c = Car(4,'red',5)
print(f"Car is having the {c.no_of_tyres} tyres!")
c.start()
c.stop()
