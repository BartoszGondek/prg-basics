def f(sentence):
    result = ""
    for char in sentence:
        if char != " ":
         result += char 
    return result 
         
print(f("a b c"))