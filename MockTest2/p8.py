def f(word):
    return '-'.join([word[:i] + word[i].upper() + word[i+1:].lower() for i in range(len(word))])

print(f("book"))
print(f("ok"))