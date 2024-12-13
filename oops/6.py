class Car:
    def __init__(self, brand,model):
        self.brand = brand
        self.model = model
        
class Elect(Car):
    def __init__(self, brand , model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size
    def full_name(self):
        return f"{self.brand} {self.model}"
    def fuel_type(self):
        return "Electric or Petrol"
    @staticmethod
    def get():
        return " This messgae are passed by ai and it contain mistake"
    def model(self):
        return self.__model


my_car = Elect("Tata","Nexon", "78kmh")

print(isinstance(my_car, Car))
print(isinstance(my_car, Elect))


Tesla = Car("Tesla","S model")
print(Tesla.model)   

