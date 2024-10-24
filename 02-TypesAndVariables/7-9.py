import random
diceroll = random.randint(1,6) 
special = (diceroll == 1) or (diceroll == 6)
print(f'Dice rolled: {diceroll}, Special number (1 or 6): {special}')