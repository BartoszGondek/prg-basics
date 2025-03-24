def f(player1, player2):
    card_values = {'A': 10, 'K': 10, 'Q': 10, 'J': 10, 'T': 10, '2' : 2, '3' : 3, '4' : 4, 
                   '5' : 5, '6' : 6, '7' : 7, '8' : 8, '9' :9}
    count1 = 0 
    count2 = 0
    for char in player1:
        count1 = count1 + card_values[char]
    for char2 in player2:
        count2 = count2 + card_values[char2] 
    if count1 == count2 or count1 > count2:
        return True
    else: return False 
        
print(f("AJ972","AQT72"))
print(f("9532","K8") )

