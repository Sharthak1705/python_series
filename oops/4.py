#polymorphism

class Car:
    def __init__(self,brand,model):
        self.__brand = brand
        self.model = model

    def fullname(self):
        return f"{self.__brand} {self.model}"
    
    def fuel_type(self):
        return "Petrol or Diesel"

class Elect(Car):
    def __init__(self, brand, model, battery):
        super().__init__(brand, model)
        self.battery = battery

    def fuel_type(self):
        return "Electric Charge"


tesla = Elect("Tesla","Model S", "85kwh")
print(tesla.fuel_type())
safari  = Car("tata", "Safari")
print(safari.fuel_type())
