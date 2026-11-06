# duck typing another way to achieve polymorphism besides inheritance 
#               object must have minimum necessary attributs/methods/
#             if it looks like a duvk and quacks like a duck , it must be a duck 



class Animal:
    alive =True

class Dog(Animal):
    def speak(self):
     print("WOOF")

class Cat(Animal):
    def speak(self):
       print("MEOW")


class car:           # car does not have animal property but we can print it by adding speak 
   alive = False

   def speak(self):
     print("HONK")

     


animals = [Dog(),Cat(),car()]

for animal in animals:
   animal.speak()
   print(animal.alive)
