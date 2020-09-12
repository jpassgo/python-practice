def quicksort(array):
    if len(array) < 2:
        return array
    else:
        pivot = array[-1]
        smaller, equal, larger = [], [], []
        for num in array:
            if num < pivot:
                smaller.append(num)
            elif num == pivot:
                equal.append(num)
            else:
                larger.append(num)
    return quicksort(smaller) + equal + quicksort(larger)