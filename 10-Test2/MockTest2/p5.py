def f(first_letter, last_letter):
    with open('data.txt', 'r', encoding='utf8') as file:
        content = file.read()
    words = content.split()
    count = 0 
    for char in words:
     if char[0] == first_letter and char[-1] == last_letter:
        count+= 1 
    return count 

print(f("w","d") )



