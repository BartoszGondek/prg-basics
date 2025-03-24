def f(x, y, d):
    for char in range(x, y + 1):
        if d in str(char):
            return True
    return False

print(f(10,15,"14"))
print(f(100,120,"11")) 
print(f(205,210,"04")) 