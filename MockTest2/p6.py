import re

def f(mnumbers):
    pattern = r"^[+-]?[1-7a-dA-D]+$"
    return sum(1 for num in mnumbers if re.match(pattern, num))




print(f(["A15","-31","7abC","+D1","-gH"])) 
print(f(["A05","-3+1","7ab8C","+D1","-22k"])) 
