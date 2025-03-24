def f(arr2D):
    num_columns = len(arr2D[0])
    
    column_sums = set()
    
    for col in range(num_columns):
        col_sum = sum(row[col] for row in arr2D)
        
        if col_sum in column_sums:
            return True
        
        column_sums.add(col_sum)

    return False

arr = [[3,4,2,0],[2,2,2,0],[5,0,0,5],[4,7,0,2],[0,2,0,0]]
print(f([[3,4,2],[5,1,6]]))
print(f([[3,4,2],[5,1,7]])) 