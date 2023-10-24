import numpy as np


def merge_sort(array, left, right):
    if left < right:
        middle = int(left + (right - left) / 2)
        merge_sort(array, left, middle)
        merge_sort(array, middle + 1, right)
        merge(array, left, middle, right)


def merge(array, l, m, r):
    n1 = m - l + 1
    n2 = r - m
    la = []
    ra = []
    for i in range(n1):
        la.append(array[l + i])

    for i in range(n2):
        ra.append(array[m + 1 + i])

    i, j, k = 0, 0, l
    while i < n1 and j < n2:
        if la[i] <= ra[j]:
            array[k] = la[i]
            i += 1
        else:
            array[k] = ra[j]
            j += 1
        k += 1

    while i < n1:
        array[k] = la[i]
        k += 1
        i += 1

    while j < n2:
        array[k] = ra[j]
        k += 1
        j += 1


arr = [900, 89, 1, 323, 4, 5, 6, 8998]
print(arr)
merge_sort(arr, 0, len(arr) - 1)
print(arr)
