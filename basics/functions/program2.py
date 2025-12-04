# Types of arguments

def greet(name , dept):
    print(f"Hello {name}")
    print(f"Are you from {dept} department\n")

# default argument
def add(num1,num2=0):
    print(f"Sum of {num1} and {num2} is {num1+num2}")

# positional arguments
greet("Pavan","CSE")
greet("CSE","Pavan")

# keyword arguments
greet( name="Pavan" , dept="Mech" )
greet( dept="EEE" , name="Kalyan" )

# positional argument should be followed by  keyword arguments
greet("Pavani",dept="Mech")
# greet(dept="Mech","Pavani")  # error

add(10,10)
add(10)
add(num2=20,num1=10)


# accept multiple arguments
def addition(*numbers):
    sum = 0
    for num in numbers:
        sum += num
    print(f"Sum of {numbers} is {sum}")

addition(10,20,30,40,50)