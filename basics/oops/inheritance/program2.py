class Human:
    def __init__(self):
        print("Human constructor called")
        self.eyes = 2
        self.hands = 2
        self.legs = 2

    def walk(self):
        print("Human is walking")

    def talk(self):
        print("Human is talking")

class Boy:
    def __init__(self):
        print("Boy constructor called")
        self.nose = 1
        self.mouth = 1
    
    def play(self):
        print("Boy is playing")
    
    def fun(self):
        print("Boy is having fun")

    def walk(self):
        print("Boy is walking")

class Men(Human,Boy):
    def __init__(self,name="Kalyan"):
        super().__init__()

        # calling both class constructures
        Human.__init__(self) 
        Boy.__init__(self)

        print("Men constructor called")
        self.name = name

    # own method
    def flirt(self):
        print("Men is flirting")
    
    def work(self):
        print("Men is working")


if __name__ == '__main__':
    m = Men()
    print(m.eyes)

    # walk is in both the classes so to access a specific class method we have to use class name
    m.walk()
    Human.walk(m)
    Boy.walk(m)
    