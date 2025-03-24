def f(subjects): 
    average= {}
    for subject, grades  in subjects.items():
        average[subject] = sum(grades) / len(grades)
    max_average = max(average.values())    
    for sub, av in average.items():
        if av == max_average:
            return sub
    
    

print(f({"math":[3,4,4],"geo":[5,4,4,4],"comp":[5,4]}) )
