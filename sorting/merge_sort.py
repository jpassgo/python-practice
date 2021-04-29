import numpy as np


def merge_sort(arr, l, r):

    if l < r:
        mid = int((l + (r - 1)) / 2)
        print(f"left: {l}, mid {mid}, right: {r}")

        merge_sort(arr, l, mid)
        merge_sort(arr, mid+1, r)
        merge(arr, l, mid, r)



def merge(arr, l, m, r):    
    # print(f"merge = left: {l}, mid: {m}, right: {r}")

    

    left = []
    i = l
    while i < m:
        left[i] = arr[l]
        i += 1

    right = []
    i = m+1
    while i < r:
        right[i] = arr[i + 1]
        i += 1

    i = 0
    j = 0
    k = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1                  
        else:
            arr[k] = right[j]
            j += 1
        k += 1
        

    while i < len(left):
        arr[k] = left[i]
        i += 1
        k += 1

    while j < len(right):
        arr[k] = right[j]
        j += 1
        k += 1

        

    
    
arr = [900, 89, 1, 323, 4, 5, 6, 8998]
print(arr)
merge_sort(arr, 0, len(arr) - 1)
print(arr)
