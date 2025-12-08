# Operator overloading

print( 1+5 )
print( "1"+"5")

print( 2*5 )
print( "kalyan\t"*5)

# magic methods
print(int.__add__(3,5))
print(str.__add__("kalyan\t", "pavan"))


class Complex:
    def __init__(self , r , i):
        self.real = r
        self.imaginery = i
    
    def __add__(self, other):
        return f"{self.real + other.real} + {self.imaginery + other.imaginery}i"

    def __str__(self):
        return f"{self.real} + {self.imaginery}i"
    
    def __eq__(self, value):
        return self.real == value.real and self.imaginery == value.imaginery
    
    def __gt__(self, other):
        return self.real > other.real and self.imaginery > other.imaginery

c1 = Complex(2,1)
c2 = Complex(3,5)

print(c1)
print(c2)

print(c1 == c1)
print(c1 == c2)


print(c1+c2) 

print(c1 > c2)
print(c2 > c1)