def f(password):
    if len(password) <= 6:
       return False 
    elif len(set(password)) != len(password):
       return False 
    else: 
       return True 
    
print (f("ax12"))
