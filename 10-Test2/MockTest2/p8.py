def f(expression):
   
    tokens = expression.split()
    stack = []
    
    for token in tokens:
        if token.isdigit():  
            stack.append(int(token))
        elif token == '+': 
            b = stack.pop()
            a = stack.pop()
            stack.append(a + b)
        elif token == '-':  
            b = stack.pop()
            a = stack.pop()
            stack.append(a - b)
    
    
    return stack.pop()


print(f("2 3 +"))  
print(f("2 6 + 4 5 - +")) 
print(f("11 7 + 15 - 14 +"))  