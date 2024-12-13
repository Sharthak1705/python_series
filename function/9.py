#yield
# value not return it genrate the value 
#it will store the value in memory and also give store in function

def even(limit):
   for i in range(2,limit+1,2):
      yield i
    
for num in even(10):
   print(num)