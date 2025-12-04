# Arbitrary Positional Arguments
# Arbitrary Keyword argument 
# *args vs **kwargs

def addition(*numbers) ->int :
    # It handles all the arguments as a tuple
    print(numbers)
    print(type(numbers))
    sum = 0
    for i in numbers:
        sum += i
    return sum

def sum(*numbers , name):
    print(numbers)
    print(name)
    print()

def keywordArgs(**kwargs) -> None:
    # It handles all the arguments as a dictionary
    print(kwargs)
    print(type(kwargs) )

    for key in kwargs:
        print(f"{key} : {kwargs[key]}")
    
    # for key,value in kwargs.items():
    #     print(f"{key} : {value}")
    
    # print( "name" in kwargs )
    print()

def arbitaryKeywordArgs(*args , **kwargs) -> None:
    print(f"args : {args} and \nits type is:{type(args)}\n")
    print(f"kwargs : {kwargs} and \nits type is:{type(kwargs)}\n")

print(f"Sum is:{addition(1,2,3,4,5,6,7,8,9,10)}\n")
print(f"Sum is:{addition(1,2,3)}\n")
print(f"Sum is:{addition(1)}\n")

sum(1,2,3,4,name="kalyan")

keywordArgs(name="kalyan",age=24,location="Hyderabad")

arbitaryKeywordArgs( 1,2,3,4,5,6,7,8,9,10,name="kalyan",age=24,location="Hyderabad")