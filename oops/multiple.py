# multiple inheritance = inherit from more than one parent class
#                      c(A,B)


# multilevel inheritance = inherit from a parent which inherits from another parent 
#                      c(B) <- B(A) <- A
class Animal:

    def __init__(self,name):
        self.name = name


    def eat(self):
        print(f"this {self.name} is eating")
    def sleep(self):
        print(f"this {self.name} is sleeping")




class Prey(Animal):
    def flee(self):
       print("the animal is fleeing")

class Predator(Animal):
    def hunt(self):
        print("this animal is hunting")



class Rabbit(Prey):
    pass 
class Hawk(Predator):
    pass
class Fish(Prey,Predator):
    pass


rabbit = Rabbit("bug")
Hawk = Hawk("tony")
fish = Fish("nemo")

rabbit.flee()
Hawk.hunt()


rabbit.eat()

