def read_from_file(name):
   with open(name) as file:
      content = file.read()
   return content

file_content = read_from_file('pets.txt')
file_content = file_content.split()

total = 0
for char in file_content:
   total += 1 
     

print('Words:', total)
    
