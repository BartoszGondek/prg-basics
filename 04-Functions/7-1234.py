def f(sentence):
    sum = 0
    for char in sentence:
        sum = sum + ord(char) 
    if sum % 3 == 0:
            return True 
    else: 
            return False 
        
        
    
print(f("hello world"))
