# Weekly expenses for different categories
# [Food, Transport, Utilities]
monthly_expenses = [
   [200, 50, 100],  # Week 1
   [180, 60, 110],  # Week 2
   [220, 55, 105],  # Week 3
   [210, 65, 95]    # Week 4
]

# Calculates expenses
# Use loop statements
count_food = 0 
count_transport = 0
count_utilites = 0 
countweek1 = 0
countweek2 = 0
countweek3 = 0
countweek4 = 0
for week in monthly_expenses:
    count_food = count_food + week[0]
for week in monthly_expenses:
    count_transport = count_transport + week[1]
for week in monthly_expenses:
    count_utilites = count_utilites + week[2]
countweek1 = sum(monthly_expenses[0])
total = sum(monthly_expenses)
...

# Print expenses
print('MONTHLY EXPENSES')
print('----------------')
print('Food:',count_food)
print('Transport:', count_transport)
print('Utilities:',count_utilites)
print('Week 1:',countweek1)
print('Week 2:',...)
print('Week 3:',...)
print('Week 4:',...)
print('---------------')
print('TOTAL:',total)
