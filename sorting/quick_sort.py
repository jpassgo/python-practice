
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


l = [32, 1, 434, 29, 100, 99, 2, 3, 89898, 23]
print(quicksort(l))
