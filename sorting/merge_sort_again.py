

def merge_sort(arr, l, r):
    if l < r:
        m = int(l + (r-l)/2)
        merge_sort(arr, l, m)
        merge_sort(arr, m+1, r)
        return merge(arr, l, m, r)


def merge(arr, l, m, r):
    l_len = m - l+1
    r_len = r - m

    l_arr = []
    r_arr = []

    for i in range(l_len):
        l_arr.append(arr[l+i])

    for i in range(r_len):
        r_arr.append(arr[m+1+i])

    i = l
    l_index = 0
    r_index = 0
    while l_index < l_len and r_index < r_len:
        if l_arr[l_index] <= r_arr[r_index]:
            arr[i] = l_arr[l_index]
            l_index += 1
        else:
            arr[i] = r_arr[r_index]
            r_index += 1

        i += 1
    
    while l_index < l_len:
        arr[i] = l_arr[l_index]
        l_index += 1

    while r_index < r_len:
        arr[i] = r_arr[r_index]
        r_index += 1

    return arr
    

arr = [900, 89, 1, 323, 4, 5, 6, 8998]
print(arr)
merge_sort(arr, 0, len(arr) -1 )
print(arr)
