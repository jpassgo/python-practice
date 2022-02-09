# 
# Given an array of integers and a number k. 
# Return the largest sum of k consecutive elements in the given array.
# 

def largest_sum(array, k):
    window = sum(array[i] for i in range(k))
    largest_sum = window

    n = len(array)
    for i in range(n - k):
        window = window - array[i] + array[k+i]
        largest_sum = max(window, largest_sum)    

    return largest_sum