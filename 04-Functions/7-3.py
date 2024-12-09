def f(word):
    
    sum=0
    for char in str(word):
        if char == 'e':
            sum += 1
    return sum 

print (f("You never get a second chance to make a first impression")) 
