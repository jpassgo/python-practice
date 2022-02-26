# 
# Minimum number of passes of a matrix to convert all negative integers to positive.
# You can only convert a negative integer to positive if it has a positive adjacent integer. 
# 
# 

def minimumPassesOfMatrix(matrix):
	negative_exists = True
	pass_count = 1
	
	row_len = len(matrix)
	col_len = len(matrix[0])
	
	while negative_exists:
		negative_exists = False
		
		for i in range(row_len):
			for j in range(col_len):
				if i != 0 and i != row_len:
					negative_exists = vertical_adj_positive(matrix, i, j)
				
				if j != 0 and j != row_len:
					negative_exists = horizontal_adj_positive(matrix, i, j)							
		if negative_exists:
			pass_count += 1
	
    return pass_count

def vertical_adj_positive(matrix, i, j):
	return True if matrix[i][j+1] or matrix[i][j-1] else False
	
def horizontal_adj_positive(matrix, i, j):
	return True if matrix[i+1][j] or matrix[i-1][j] else False
		