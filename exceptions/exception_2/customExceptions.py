
class CustomeException(Exception):
    pass


class DobException(CustomeException):
    print(CustomeException)
    pass 


year = int(input("Enter DOB year:"))
age = 2025 - year

try:
    if( age<=30 and age>=20 ):
        print("Valid age")
    else:
        raise DobException
except DobException:
    print("Sorry the age is not valid!")