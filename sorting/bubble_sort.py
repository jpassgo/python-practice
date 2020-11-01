
def bubble_sort(array):
    isNotSorted = True
    while isNotSorted:
        isNotSorted = False
        for index in range(len(array)-1):
            if array[index] > array[index+1]:
                isNotSorted = True
                array[index], array[index+1] =  array[index+1], array[index]        

l = [18, 9, 2, 2323, 5, 3, 4, 1, 98, 2, 323]

print(l)
bubble_sort(l)
print(l)
