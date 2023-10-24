def selection_sort(array):
    for marker in range(len(array)):
        for index in range(marker, len(array)):
            if array[marker] > array[index]:
                array[marker], array[index] = array[index], array[marker]


l = [18, 9, 2, 2323, 5, 3, 4, 1, 98, 2, 323]

print(l)
selection_sort(l)
print(l)
