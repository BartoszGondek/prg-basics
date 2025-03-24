def f(a, b):
   f0 = 0 
   f1 = 1
   f0b = 0
   f1b = 1
   
   result = f0 + f1
   result2= f0b + f1b 
   for  char in range(3, a+1):
      result = f0 + f1
      f0 = f1
      f1 = result
   for char2 in range(3,b+1):
      result2 = f0b + f1b
      f0b = f1b
      f1b = result2
   return result + result2

print(f(5,8))
    










    