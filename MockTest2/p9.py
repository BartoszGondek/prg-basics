def f(x, y, digit):
    digit_str = str(digit)
    count = 0
    for num in range(x, y + 1):
        count += str(num).count(digit_str)
    return count

print(f(10,15,1))
print(f(28,32,2))
print(f(100,105,6))
print(f(100,101,0))