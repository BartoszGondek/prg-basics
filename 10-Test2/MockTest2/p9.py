import csv

def f(value):
    count = 0
    with open("data.csv", "r") as file:
            content = csv.DictReader(file)  
            for row in content:
                    salary = float(row['salary'])  
                    if salary >= value:
                        count += 1
    return count

print(f(9200) )
print(f(11640) )
