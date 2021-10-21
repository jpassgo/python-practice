# https://leetcode.com/problems/rotate-array/ 
# 
# Given an array, rotate the array to the right by k steps, where k is non-negative.
# 

def rotate(array, k):
    size = len(array)
    temp_size = size
    
    temp_array = [0] * temp_size
    
    for index in range(size):
        temp_array[calculcate_new_index(index, k, size)] = array[index]

    return temp_array
        
def calculcate_new_index(index, k, size):
    new_index = index + k
    if new_index <= (size - 1):
        return new_index
    else:
        return abs(size - new_index)


print(rotate([1, 2, 3, 4, 5], 2))
print(rotate([1, 2, 3, 4, 5, 6, 7, 8], 3))
