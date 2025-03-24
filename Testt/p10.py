def f(computer, smartphone):
   friends = computer | smartphone
   return len(friends)

computer = {'John', 'Peter'}
smartphone = {'Peter', 'Frank', 'Ann'}
print(f(computer, smartphone))
computer = {'Breeze', 'Hunter', 'Walker', 'Chasaer', 'Camper', 'Owl'}
smartphone = {'Breeze', 'Owl', 'Storm', 'Walker'}
print(f(computer, smartphone))