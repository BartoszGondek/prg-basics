def f(n):
   astero = "*"
   slash = "/"
   if n > 0:
       number = n * (astero + slash)
       number = number[:-1]
       return number 
   else:
      return False
   
print(f(0))


   
       