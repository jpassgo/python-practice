def merge(array1, array2):
    sorted_array = []
    i, j = 0, 0
    while i < len(array1) and j < len(array2):
        if array1[i] < array2[j]:
            sorted_array.append(array1[i])
            i += 1
        else:
            sorted_array.append(array2[j])
            j += 1
    while i < len(array1):
        sorted_array.append(array1[i])
        i += 1
    while j < len(array2):
        sorted_array.append(array2[j])
        j += 1

    return sorted_array

def merge_sort(array):
    if len(array) < 2:
        return array[:]
    else:
        middle = len(array)//2
        l1 = merge_sort(array[:middle])
        l2 = merge_sort(array[middle:])
        return merge(l1, l2)


l3 = [900, 89, 1, 323, 4, 5, 6, 8998]

sortedList = merge_sort(l3)
print(sortedList)