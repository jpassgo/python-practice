def hasSingleCycle(array):
    arrLen = len(array) - 1
    indicesArray = [x for x in range(arrLen + 1)]
    print(array)
    print(indicesArray)

    previousIndex = 0
    while indicesArray:
        index = array[previousIndex]

        index += previousIndex
        if index < 0:
            index += arrLen
        elif index > arrLen:
            index -= arrLen

        previousIndex = index
        if index not in indicesArray:
            break
        indicesArray.remove(index)

    return len(indicesArray) == 0
