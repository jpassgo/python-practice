


def quicksort(array, left, right):
    if left < right:
        mid = int((left + right) / 2)
        partition(array, left, right)
        quicksort(array, left, mid)
        quicksort(array, mid+1, right)
        


def partition(array, left, right):
    pivot = len(array) - 1 
    while left <= right:
        if array[left] > array[pivot]:
            

