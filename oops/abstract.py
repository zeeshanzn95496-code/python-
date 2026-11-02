# abstract class is a class that cannot be instantiated on its own ; meant to be subclassed 
#                 they contain abstract methods which are declared but have no implementation 
#         benefits:
#        1. prevents instantiation of class itself
#        2. requires children to use inherited abstract methods


from  abc import ABC, abstractmethod

class Vehicle(ABC):

    @abstractmethod
    def go(self):
        pass


    @abstractmethod
    def stop(self):
        pass

class Car(Vehicle):
    def go(self):
        print("car is moving")

    def stop(self):
        print("car stopped")
class Motercycle(Vehicle):

    def go(self):
        print("you drive motercycle")

    def stop(self):
        print("motercycle stopped")

car=Car()
motercycle=Motercycle()

motercycle.go()
motercycle.stop()
car.stop()
car.go()