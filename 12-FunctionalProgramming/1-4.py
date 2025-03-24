ms = int(input('Enter car speed: '))
ms_to_kmh = lambda ms : ms * 3.6
print(f'{int(ms_to_kmh(ms))} km/h')
