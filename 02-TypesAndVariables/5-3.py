###
# A program that calculates the volume
# and surface area of ​​a cuboid with sides a, b, and c.
# Read the dimensions of the cuboid from the keyboard.
#
a_side_string = input('a=')
a = int(a_side_string)
b_side_string = input ('b=')
b = int(b_side_string)
c_side_string = input ('c=')
c = int(c_side_string)
cuboid_volume = (a*b*c) 
cuboid_surface_area = 2*(a*b + a*c + b*c)
print(f'The volume of a cuboid with sides {a, b, c} is {cuboid_volume} ')
print(f'The surface area of a cuboid with sides {a, b, c} is {cuboid_surface_area}')
