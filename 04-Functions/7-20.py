def f(number1 , number2, number3):
  biggest_number = max(number1, number2, number3)
  smallest_number = min(number1, number2, number3)
  result = biggest_number - smallest_number
  return result 

print (f(2, 12, 8))