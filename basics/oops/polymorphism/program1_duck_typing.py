# Duck typing is the type or class of an object is less important than the methods it defines

def square(x):
    return x*x

# during runtime the datatype will be checked
print( square(10) )

print( square(10.5) )

class Duck:
    def swim(self):
        print("Duck swims in water")
    def speak(self):
        print("Duck speaks quack quack")

class Dog:
    def swim(self):
        print("Dog swims in water")
    def speak(self):
        print("Dog speaks bow bow")

def classify(animal):
    animal.swim()
    animal.speak()
    print()

duck = Duck()
dog = Dog()

classify(duck)
classify(dog)