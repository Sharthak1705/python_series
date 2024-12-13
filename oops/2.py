#inheritance in python using super keyword and function 
#to use the class which is declared in above class
class Car:
    def __init__(self, brand,model):
        self.brand = brand
        self.model = model

    def fullname(self):
        return f"{self.brand} {self.model}"
    
class Electric(Car):
    def __init__(self, brand,model, battery_size):
         super().__init__(brand,model)
         self.battery_size = battery_size


tesla = Electric("Tesla","Model S", "85kwh")
print(tesla.fullname())


my_car = Car("Tata", "Jaguar")
my = Car("Nexon", "Safari")

print(my_car.brand)
print(my.brand)        