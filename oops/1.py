# class and objects 
#constructor is used in this method which are init


class Car:
   def __init__(self,brand,model):
#attributes of car
     self.brand =brand
     self.model =model
   
   #adding the functionaity in using function
   def full_name(self):
      return f"{self.brand}{self.model}"

#instance 1
my_car = Car("Toyota", "Corolla")
print(my_car.brand)
print(my_car.model)
print(my_car.full_name()) #adding functionality in function 


#instances 2
my_new_car = Car("Tata", "Safari")
print(my_new_car.model)
print(my_new_car.full_name()) #adding functionalityin function




