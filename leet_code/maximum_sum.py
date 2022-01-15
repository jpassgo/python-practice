# 
# Given an array of integers and an integer k
#  calculate the maximum sum using k consecutive integers
# 

def maximum_sum(array, k):
    array_len = len(array)
    
    window_sum = sum(array[:k])
    maximum_sum = window_sum

    if array_len < k:
        return 0

    for i in range(array_len - k):
        window_sum = window_sum - array[i] + array[i+k]
        maximum_sum = max(window_sum, maximum_sum)

    return maximum_sum
    

arr = [1, 5, 2, 3, 7, 1]
k = 3
print(maximum_sum(arr, k))