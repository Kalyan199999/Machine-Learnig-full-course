# class
class Person:

    # constructor
    def __init__(self, name="John", age=30, gender="male"):
        self.name = name
        self.age = age
        self.gender = gender
    
    # class methods
    def walking(self):
        print(f"{self.name} is walking")

    def eating(self):
        print(f"{self.name} is eating")
    
    def displayPerson(self):
        print(f"Name:{self.name}, Age:{self.age}, Gender:{self.gender}")

if __name__ == "__main__":

    # creating object
    per1 = Person()
    per1.walking()
    per1.eating()
    per1.displayPerson()

    print()

    per2 = Person(name="Kalyani",age=25,gender="female")
    per2.walking()
    per2.eating()
    per2.displayPerson()

    print(f"Type of persion is:{type(per1)}")