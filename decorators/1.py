# decorators in python is predefined keyword
#time function execution

import time 

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result =  func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} ran in {end-start} time")
        return result
    return wrapper

@timer
def example(n):
    time.sleep(n)

example(2) 