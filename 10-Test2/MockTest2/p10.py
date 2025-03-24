def f(array):
    smallest_value = array[0][0] 
    smallest_row, smallest_col = 0, 0   

    for i in range(len(array)):
        for j in range(len(array[i])):
            if array[i][j] < smallest_value:
                smallest_value = array[i][j]
                smallest_row, smallest_col = i, j

    return smallest_row == smallest_col


print(f([
[7,5],
[5,3],
[9,4]]))
print(f([[7, 8, 5, 3], [9, 4, 2, 6]]))