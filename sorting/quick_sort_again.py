from typing import List
import numpy


def quick_sort(arr: List[int]) -> List[int]:
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return quick_sort(left) + middle + quick_sort(right)


arr = numpy.random.randint(1, 10, size=9)
print(arr)
print(quick_sort(arr))
