def f(vname):
    if len(vname) < 1 or len(vname) > 5:
        return False
    
    if not (vname[0].isalpha() or vname[0] == "_"):
        return False
    
    for char in vname[1:]:
        if not (char.isalpha() or char.isdigit() or char == "_"):
            return False
    
    return True

print(f("abc"))
print(f("Abc"))
print(f("aBC"))
print(f("_ab_c"))
print(f("abcdef"))
print(f("8abc"))
print(f("_aB8_"))
print(f("_4x"))