l = [1,2,3,4]
print( l )
print(len(l))
print(type(l))

# dunder methods
class Employee:
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary

    def __len__(self):
        return len(self.name)

    def __str__(self):
        return f"Employee name is {self.name} and salary is {self.salary}"

    def __del__(self):
        print(f"Employee {self.name} is deleted")

emp1 = Employee("Kalyan" , 30000)
print(type(emp1))
print(emp1)
print(len(emp1))

del emp1 # employee is deleted!

# print(emp1)