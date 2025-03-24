###
# Bubble sort
#
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):  # Outer loop for passes
        for j in range(0, n - i - 1):  # Inner loop for comparisons
            if arr[j] > arr[j + 1]:  # Swap if elements are in the wrong order
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr
car_fuel_consumption = [7.2, 6.8, 7.5, 7.0, 7.1, 6.9, 7.3]
print(car_fuel_consumption)
sorted_car_fuel_consumption = bubble_sort(car_fuel_consumption) 
print(sorted_car_fuel_consumption)

bank_transactions = [-150, -20, 300, -45, -60, 500, -120]
print(bank_transactions)
sorted_bank = bubble_sort(bank_transactions)
print(sorted_bank)
print(sorted(bank_transactions))
...
...
...