#  static method are used as a decorator
# static method is used
#  usinfg the functionality to addd on static
class Car:
    def __init__(self, brand, model):
       self.brand = brand
       self.model = model
    @staticmethod
    def general():
        return "Cars are means of transport"

tesla = Car("Tesla", " Model S")
tesla.model = "Tata"

print(tesla.model) 