def f(x, y):
    sum = 0
    for number in range(x, y + 1): 
        if number < 0 and number % 2 == 0:  
            sum += 1  
    return sum  

print (f(-10,-2))

      

