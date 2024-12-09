
def f(detector):
    sum=0
    for char in detector:
        if char == "+":
            sum+= 1 
        elif char == "-":
            sum-= 1 
        if sum >= 3:
           return True 
    return False 

print(f("+-+-+-+-"))
    

