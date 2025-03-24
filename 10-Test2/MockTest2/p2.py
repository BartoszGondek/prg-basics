def f(arr):
    if arr[0] == arr[1]:
        comon = arr[0]
    else:
        if arr[0] == arr[2]:
          comon = arr[0]
        else:
            comon = arr[1]  
    for number in arr:
       if number != comon:
        return number 

print(f([7,7,7,7,7,5,7,7]) )
print(f([7,2,7,7,7,7,7,7]) )