# Find the kth largest num in an unsorted array


# The idea behind this solution is to use partitioning to sort the array only until we hit the kth index.
# If we start at the end of the array and work backwards, once we get to the kth index we will know
# that all values to the left of the kth indexed value will be less than it and to right are greater values.
def find_kth_largest_value(array, k):
    left = 0
    right = len(array) - 1

    while left <= right:
        pivot_index = partition(array, left, right)
        if pivot_index == len(array) - k:
            return array[pivot_index]
        elif pivot_index > len(array) - k:
            right = pivot_index - 1
        else:
            left = pivot_index + 1

    return -1


def partition(array, left, right):
    pivot = array[right]
    index = left
    for j in range(left, right):
        if array[j] <= pivot:
            array[j], array[index] = array[index], array[j]
            index += 1
    array[index], array[right] = array[right], array[index]
    return index


print(find_kth_largest_value([5, 7, 2, 3, 4, 1, 6], 3))
