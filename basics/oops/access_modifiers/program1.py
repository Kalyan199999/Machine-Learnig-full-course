class Student:
    def __init__(self , name,age,roll):
        # by default all the variables are public
        self.name = name

        self._roll = roll # protected variable

        self.__age = age #private variable

    # protected method 
    def _faculty(self):
        print("This is a faculty member of protected\n")

    # private method
    def __staff(self):
        print("This is a staff member of private\n")

    def display(self):
        print(f"Hello,this is {self.name} with roll number:{self._roll} and my age is {self.__age}\n")
    
    def getAge(self):
        return self.__age
    
    def getRoll(self):
        return self._roll


class Branch(Student):
    def __init__(self,name,age,roll,branch):
        super().__init__(name,age,roll)
        self.branch = branch



s1 = Student("Rahul",20 , 101)
print(s1.name) # public variable
# print(s1.__age) # private variable -> not accessable
print(s1.getAge())
s1._faculty()

s1.display()


b1 = Branch("Kalyan" , 21, 201,'cse')
print( b1.name)
print(b1._roll) # protected variable
print(b1.branch)
b1._faculty()

# valid s1 object members to access
print( dir(s1) )