from random import randint


def divide_arr(arr):
    if len(arr) < 2:
        print(f"Base condition reached with {arr[:]}")
        return arr[:]
    else:
        middle = len(arr) // 2
        print(f"Current list to work with: {arr[:]}")
        print(f"Left split: {arr[:middle]}")
        print(f"Right split: {arr[middle:]}")
        l1 = divide_arr(arr[:middle])
        l2 = divide_arr(arr[middle:])


divide_arr([randint(1, 100) for i in range(10)])
