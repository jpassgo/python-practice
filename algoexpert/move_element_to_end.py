def move_element_to_end(array, toMove):

    k = 0
    for index, value in enumerate(array):
        if value == toMove:
            k += 1
        elif k > 0:
            array[index - k] = value
            array[index] = toMove

    return array

