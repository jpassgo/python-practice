def merge_sort(array, left, right):
    if left < right:
        mid = int((left + right) / 2)
        merge_sort(array, left, mid)
        merge_sort(array, mid + 1, right)
        merge(array, left, right)


def merge(array, left, right):
    left_end = (left + right) / 2
    right_start = left_end + 1

    temp = []
    l = left
    r = right_start
    index = 0
    while l <= left_end and r <= right:
        if array[l] <= array[r]:
            temp[index] = array[l]
            l += 1
        else:
            temp[index] = array[r]
            r += 1
        index += 1

    while l < left_end:
        temp[index] = array[l]
        l += 1
        index += 1

    while r < right:
        temp[index] = array[r]
        r += 1
        index += 1

    i = left
    temp_size = len(temp)
    while i < temp_size:
        array[i] = temp[i]
        i += 1


arr = [900, 89, 1, 323, 4, 5, 6, 8998]
print(arr)
merge_sort(arr, 0, len(arr) - 1)
print(arr)
