def f(uid):
    seen = set()
    for user_id in uid:
        if user_id in seen:
            return False
        seen.add(user_id)
    return True

print(f(["john5","ann123","JOHN5","xxx","abc333","a10"]))
print(f(["abc123","ann","abc123","a10"]))
print(f(["bob2","BOB2"]))
