def f(sentence):
    sum = 0 
    for char in sentence:
        if char == "a" or char == "e" or char == "i" or  char == "o" or char == "u" or char == "y":
            sum += 1
    return sum 

print (f("hello word"))