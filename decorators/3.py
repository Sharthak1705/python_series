#decorators returned the cache value in a function with same arguments
import time

def cache(func):
    caches = {}
    print(caches)
    def wrapper(*args):
        if args in caches:
            return caches[args]
        result = func(*args)
        caches[args] = result
        return result
    return wrapper

@cache
def long_runnning_function(a, b):
    time.sleep(4)
    return a + b

print (long_runnning_function(2,3))
print (long_runnning_function(2,3))
print (long_runnning_function(4,3))


