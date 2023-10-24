def insertion_sort(array):
    index = 1
    while index < len(array):
        if array[index] < array[index - 1]:
            array[index], array[index - 1] = array[index - 1], array[index]
            workingIndex = index - 1
            while array[workingIndex] < array[workingIndex - 1] and workingIndex != 0:
                array[workingIndex], array[workingIndex - 1] = (
                    array[workingIndex - 1],
                    array[workingIndex],
                )
                workingIndex -= 1
        index += 1


l = [18, 9, 2, 2323, 5, 3, 4, 1, 98, 2, 323]

print(l)
insertion_sort(l)
print(l)
