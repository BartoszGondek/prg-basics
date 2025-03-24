def avg_speed(distance,hours,minutes):
    avg = distance/(hours+(minutes/60))
    avg = round(avg, 1)
    return avg
distance = int(input('Enter distance: '))
hours = int(input('Enter hours: '))
minutes = int(input('Enter minutes: '))
print(f'{avg_speed(distance,hours,minutes)} km/h')

