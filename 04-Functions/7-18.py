def f(number):
    sum = 0
    str_number = str(number)
    
    for char in range(1, 10):
        count = 0
        for digit in str_number:
            if digit == str(char):
                count += 1
        if count > 1:
            sum += char * count
    return sum 

print (f(230335))