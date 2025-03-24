def f(n):
 n = str(n)
 odd_digits = []
 for char in n:
    num = int(char)
    if num % 2 == 1:
     odd_digits = odd_digits + [num]
 if not odd_digits:
  return -1 
 result = max(odd_digits) - min(odd_digits)
 return result
print(f(10852))
print(f(723597))
print(f(4388))
print(f(846206))