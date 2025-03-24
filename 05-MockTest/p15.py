def f(n):
    f0 = 0
    f1 = 1 
    result = f0 + f1 
    for char in range(3, n+1):
        result = f0 + f1
        f0 = f1 
        f1 = result 
    return result 