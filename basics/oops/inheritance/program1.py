# single inheritance

class Human:
    def __init__(self):
        print("Human class constructor")
        self.eyes = 2
        self.nose = 1

    def walk(self):
        print("Human walks")

    def talk(self):
        print("Human talks")

# inheritating Human class (single inheritance)
class Men(Human):
    def __init__(self,name="Kalyan"):
        # calling super class constructor
        # to use super class properties we have to call super class constructor
        super().__init__()

        self.name = name
        print("Men class constructor")
    
    # own method
    def flirt(self):
        print("Men is flirting")

    # override
    def walk(self):
        # calling parent class method
        super().walk()
        print("Men is walking")
    
    def display(self):
        print(f"hey,this is {self.name} and I have {self.eyes} eyes and {self.nose} nose")
        


if __name__ == '__main__':

    m = Men()

    m.talk()

    m.walk()

    m.flirt()
    m.display()

    print(m.eyes)