# closure reference value is comes together in Python
x =99
def func3():
  global x
  x= 45


func3() 
print(x)


def fun():
  x = 88
  def fun1():
      print(x)
  return fun1

result = fun()
result() 



def chai(num):
   def actual(x):
      return x ** num
   return actual

# def chai(2):
#    def actual(x):
#       return x ** 2
#    return actual


f = chai(2)
g = chai(3)

print(f(3))
print(f(3))