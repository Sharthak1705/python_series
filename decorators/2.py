#decorators for debugging function calls
#name of function adn also  passed the argument

def debug(func):
    def wrapper(*args,**kwargs):
       argsa = ', '.join(str(arg) for arg in args)
       kwargsa = ', '.join(f'{k}={v}' for k, v in kwargs.items())
       print(f"Calling :{func.__name__} with args{argsa} and kwargs{kwargsa}")
       return func(*args,**kwargs)
    
    return wrapper

@debug
def hello():
    print("hello")

@debug
def greet(name, greetings="Hello"):
    print(f"{greetings}, {name}")

greet("Chai", greetings="Hanji")