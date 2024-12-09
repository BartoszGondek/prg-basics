def f(x, y):
    sum = 0
    for char in range(x, y + 1):  
        if char % 6 == 0 and char % 4 != 0:  
            sum += char  
    return sum


print(f(10,30))