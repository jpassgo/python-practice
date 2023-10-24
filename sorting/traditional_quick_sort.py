def traditional_quicksort(array):
    return quicksort(array, 0, len(array) - 1)


def quicksort(array, low, high):
    if low >= high:
        return array

    pivot = partition(array, low, high)
    quicksort(array, low, pivot - 1)
    return quicksort(array, pivot, high)


def partition(array, low, high):
    pivot = array[int(low + (high - low) / 2)]
    while low <= high:
        while array[low] < pivot:
            low += 1
        while array[high] > pivot:
            high -= 1
        if low <= high:
            array[low], array[high] = array[high], array[low]
            low += 1
            high -= 1

    return low


l = [32, 1, 434, 29, 100, 99, 2, 3, 89898, 23]
print(traditional_quicksort(l))
