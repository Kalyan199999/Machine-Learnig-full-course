# Identity operators -> compars the objects memory location
# is and is not

a = 10
b = 10
c = 15

print(a is b)  # True
print(a is c)  # False

print(f"memory location of a: {id(a)}")
print(f"memory location of b: {id(b)}")

print(a is not c)  

b += 1
print(a is b)  # False


print(f"memory location of a: {id(a)}")
print(f"memory location of b: {id(b)}")

a = 10
b = '10'
print(a is b)  # False
print(f"memory location of a: {id(a)}")
print(f"memory location of b: {id(b)}")