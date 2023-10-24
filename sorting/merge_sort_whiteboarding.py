def merge_sort(arr, l, r):
    if l < r:
        m = int(l + (r - l) / 2)
        merge_sort(arr, l, m)
        merge_sort(arr, m + 1, r)
        return merge(arr, l, m, r)


def merge(arr, l, m, r):
    l_len = m - l + 1
    r_len = r - m
    l_arr = []
    r_arr = []
    [l_arr.append(arr[l + i]) for i in range(l_len)]
    [r_arr.append(arr[(m + 1) + i]) for i in range(r_len)]

    i = l
    li = 0
    ri = 0
    while li < l_len and ri < r_len:
        if l_arr[li] <= r_arr[ri]:
            arr[i] = l_arr[li]
            li += 1
        else:
            arr[i] = r_arr[ri]
            ri += 1
        i += 1

    while li < l_len:
        arr[i] = l_arr[li]
        li += 1
        i += 1

    while ri < r_len:
        arr[i] = r_arr[ri]
        ri += 1
        i += 1

    return arr


arr = [900, 89, 1, 323, 4, 5, 6, 8998]
print(arr)
merge_sort(arr, 0, len(arr) - 1)
print(arr)
