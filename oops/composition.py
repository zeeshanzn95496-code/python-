# composition the composed object directly owns its components,which cannot exist independently
#               owns a relationship


class engine:
    def __init__(self,horse_power):
        self.horse_power=horse_power

class wheel:
    def __init__(self,size):
        self.size=size

class Car:
    def __init__(self,make,model,horse_power,wheel_size):
        self.make= make 
        self.model = model
        self.engine = engine(horse_power)
        self.wheels=[wheel(wheel_size) for _ in range(4)] 

    def display_Car(self):
        return f"{self.make}  {self.model} {self.engine.horse_power}(hp) {self.wheels[0].size}"

car = Car("ford","mustang",500,10)       
print(car.display_Car())            