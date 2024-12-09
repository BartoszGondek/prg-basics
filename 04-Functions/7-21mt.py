def f(name):
    acronym=''
    words=name.split()
    for char in words:
        acronym=acronym+char[0]
    return acronym
    

print(f("Internet of Things"))