class Animal:

    def __init__(self,name):
        self.name = name
        self.is_alive = True

    def eat(self):
        print(f"{self.name} is eating")

    def sleep(self):
        print(f"{self.name} is sleeping")

class Dog(Animal):
    def speak(self):
        print("WOOF WOOF")

class Cat(Animal):
    def speak(self):
        print("MEOW MEOW")


dog = Dog("scooby")
cat = Cat("garfield")


print(dog.name)
print(dog.is_alive)
dog.eat()
dog.speak()