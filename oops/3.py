#encsulation 

class Car:
    def __init__(self,brand,model):
        self.__brand = brand
        self.model = model

    def fullname(self):
        return f"{self.__brand} {self.model}"
    
    def get_brand(self):
        return self.__brand + "?"

class Elect(Car):
    def __init__(self, brand, model, battery):
        super().__init__(brand, model)
        self.battery = battery

tesla = Elect("Tesla","Model S", "85kwh")
# print(tesla.get_brand())
print(tesla.chai_brand())