def f(text):
    if not text:
        return '""'
    result = text[0] 
    for char in range(1, len(text)):
          result += "-" + text[char]  
    
    return result
    
print (f(""))