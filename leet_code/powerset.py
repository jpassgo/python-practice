#
# Create a function that will return the powerset of a given array.
#
# p([1, 2]) = [[], [1], [2], [1, 2]]
#
#


def powerset(array):
    subsets = [[]]
    for element in array:
        for i in range(len(subsets)):
            currentSubset = subsets[i]
            subsets.append(currentSubset + [element])
    return subsets
