def f(array):
    count = 0
    for char in array:
        if len(char) >= 4 and len(char) <= 12:
         for letter in char:
          if not (letter.islower() or letter.isdigit() or letter == "_"):
           break 
         else :
          count += 1 
    return count 

print(f(["uek","water_7_a","anna.may","7ab_c_d_e_f","water_7"]) ) 
 
