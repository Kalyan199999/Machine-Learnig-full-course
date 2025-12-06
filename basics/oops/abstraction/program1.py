from abc import ABC, abstractmethod

# abstract class
class Vehicle(ABC):

    def __init__(self, n):
        self.no_of_tyres = n
        print("Initialized!")

    # abstract method 
    @abstractmethod
    def start():
        pass

    # normal method
    def stop(self):
        print("Vehicle is stoped!")