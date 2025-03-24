def f(d):
    in_park = set()  
    
    for reg_num, action in d:
        if action == "in":
            in_park.add(reg_num)
        elif action == "out":
            in_park.discard(reg_num)
    return sorted(in_park)


print(f([["KR234","in"],["BA123","in"],["GX444","in"],["KR234","out"], ["BA111","in"],["BA123","out"],["KR234","in"]]))
print(f([["KR234","in"],["KR234","out"]]))
