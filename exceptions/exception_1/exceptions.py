def addition(a,b ):
    try:
        return a+b+c
    except TypeError as e:
        print("TypeError: Both arguments must be numbers {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

def division( a,b ):
    try:
        return a/b
    except ZeroDivisionError as e:
        print(f"ZeroDivisionError: Division by zero is not allowed {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

def array(l):
    try:
        return l[10]
    except IndexError as e:
        print(f"IndexError: Index out of range -> {e}")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        print("This will always be executed")

print( addition(5,10) )
print( division(5,0) )
print( array([1,2,3,4,5]) )