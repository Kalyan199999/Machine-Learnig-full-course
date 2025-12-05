# return statement in function

def add(a,b):
    return a+b

def square(nums):
    return [ num**2 for num in nums ]

def even(num):
    return (num&1) == 0

# def

result = add(10,20)
print(f"Addition is:{result}")

result  = square([1,2,3,4])
print(f"Square of list is:{result}")

print(f"Is 10 even? {even(10)}")