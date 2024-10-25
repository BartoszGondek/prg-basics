###
# Calculates the area of a triangle based on the lengths
# of the triangle's sides
#
def triangle_area(a, b, c):
    import math 
    area = (0.5 * (a + b + c))
    result = math.sqrt(area*(area - a)*(area - b)*(area - c))
    return result
a = int(input("Enter first side "))
b = int(input("Enter second side "))
c = int(input("Enter third side "))
value = triangle_area(a, b, c)

print(f'The area of ​​a triangle with sides {a}, {b}, {c} is {value}  ')
