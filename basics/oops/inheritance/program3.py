# Multilevel Inheritance

class Human:
    def eat(self):
        print("Human is eating")


class Boy(Human):

    def walk(self):
        print("Boy is walking")

    def eat(self):
        print("Boy is eating")


class Man(Boy):
    def sleep(self):
        print("Man is sleeping")

    def eat(self):
        Human.eat(self)
        super().eat()
        print("Man is eating")


if __name__ == '__main__':
    m = Man()
    m.eat()
    m.sleep()
    m.walk()