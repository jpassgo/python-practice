# 
# Given a 2d array of 1s and 0s return an array of the length of contiguous 1s representing a river.
# 

# I'll want to use depth first search here.
# One consideration to be made is that the river can be an L shape
def riverSizes(matrix):
    temp_matrix = matrix
    river_sizes = []
    for i in range(len(temp_matrix)):
        for j in range(len(temp_matrix[i])):   
            if temp_matrix[i][j] == 1:
                river_size = recursive_river_search(temp_matrix, i, j)         
                if river_size > 0:
                    river_sizes.append(river_size)

    return river_sizes

def recursive_river_search(temp_matrix, i, j, river_size=1):
    temp_matrix[i][j] = 0
    if i+1 < len(temp_matrix) and temp_matrix[i+1][j] == 1:
        river_size += 1        
        recursive_river_search(temp_matrix, i+1, j, river_size)
    if j+1 < len(temp_matrix[j]) and temp_matrix[i][j+1] == 1:
        river_size += 1        
        recursive_river_search(temp_matrix, i, j+1, river_size)
    else:
        return river_size



print(riverSizes([
  [1, 0, 0, 1, 0],
  [1, 0, 1, 0, 0],
  [0, 0, 1, 0, 1],
  [1, 0, 1, 0, 1],
  [1, 0, 1, 1, 0]
]))
