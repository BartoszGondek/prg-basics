###
# Reads from file, line by line
#
i=0
with open('countries.txt', 'r') as file:
    for line in file:
        i+=1 
        print(f"{i}. {line}", end="")