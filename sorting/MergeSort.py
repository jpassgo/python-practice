def merge_sort(array1, array2):
    sorted_array = []
    i, j = 0, 0
    while i < len(array1) and j < len(array2):
        print(f"Left list index i is {i} with value of {array1[i]}")
        print(f"Left list index j is {j} with value of {array2[j]}")
        if array1[i] < array2[j]:
            sorted_array.append(array1[i])
            i += 1
        else:
            sorted_array.append(array2[j])
            j += 1
        
    while j < len(array2):
        sorted_array.append(array2[j])
        j += 1
    while i < len(array1):
        sorted_array.append(array1[i])
        i += 1

    return sorted_array

l1 = [1, 2, 3, 6, 7, 9, 10]
l2 = [19, 999, 2323432]

print(merge_sort(l1, l2))