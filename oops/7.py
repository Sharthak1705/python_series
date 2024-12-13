#multiple class will inherit the property of electric car
class Car:
    def __init__(self ,brand, model):
        self.brand = brand
        self.model = model

class Battery:
    def battery_info(self):
        return " this is a Battery and this contain the duration.."
class Engine:
    def engine_info(self):
        return " this will help to get the information of engine.."
class Electric(Battery, Engine, Car):
    pass
car = Electric("Tesla", "S model")

print(car.engine_info())
print(car.battery_info())