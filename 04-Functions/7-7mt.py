def f(amount_to_pay):
    coins_5 = amount_to_pay//5
    rest = amount_to_pay % 5
    coins_2 = rest // 2
    rest = rest % 2
    coins_1 = rest
    return coins_5 + coins_2 + coins_1

print(f(23))  

