import numpy as np

def merge_sort(array, left, right):
    if(left < right):
        middle = int(left + (right - left)/2)
        merge_sort(array, left, middle)
        merge_sort(array, middle + 1, right)
        merge(array, left, right)

def merge(array, left_start, right_end):
    left_end = int((right_end + left_start)/2)
    right_start = left_end + 1
    size = right_end - left_start + 1

    temp = [0] * size

    left, right, index = left_start,right_start,left_start
    while(left < left_end and right < right_end):
        if(array[left] <= array[right]):
            temp[index] = array[left]            
            left += 1
        else:
            temp[index] = array[right]      
            right += 1
        index += 1

    while(left < left_end):
        temp[index] = array[left]        
        left += 1
        index += 1

    while(right < right_end):
        temp[index] = array[right]        
        right += 1
        index += 1
    
    for i in range(len(temp)-1):
        if(temp[i] != 0):
            array[i] = temp[i]

        
    
arr = [900, 89, 1, 323, 4, 5, 6, 8998]
print(arr)
merge_sort(arr, 0, len(arr) - 1)
print(arr)
