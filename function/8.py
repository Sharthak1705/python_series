#when multiple value are coming in the form of argument and 
#it can handle key and value pair
def print_kwar(**kwargs):
    for key,value in kwargs.items():
        print(f"{key} : {value}")


print_kwar(power='Shaktiman')
print_kwar(name="Shakt")
print_kwar(power='Shaktiman',name="Shakt", enemy = "dr")