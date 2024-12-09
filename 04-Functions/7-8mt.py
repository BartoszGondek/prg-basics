def f(number, even):
    sum = 0
    for char in str(number):
        digit = int(char)
        
        if even == True:
         if digit % 2 == 0:
            sum += digit
        elif even == False:
          if digit % 2 != 0:
            sum += digit
    return sum

print (f(3124, False))