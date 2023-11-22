def mover_um_para_inicio(arr):
    next_position = 0
    
    for i in range(len(arr)):
        if arr[i] == 1:
            arr[i], arr[next_position] = arr[next_position], arr[i]
            next_position += 1

array = [2, 1, 5, 2, 5, 2, 1, 1, 1, 7, 9, 13, 127, 21]

mover_um_para_inicio(array)

print(array)
