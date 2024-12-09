def f(product_code):
    if len(product_code) > 4:
        return "Too long"
    if (int(product_code[0]) + int(product_code[1]) + int(product_code[2])) % 7 == int(product_code[3]):
        return True
    else:
        return False

    
        
print(f("51487"))