

def search(arr, val):
    mid = int(len(arr) / 2)
    mid_value = arr[mid]    
    if len(arr) == 0:
        return False
    elif val == mid_value:        
        return True
    elif val < mid_value:
        return search(arr[:mid], val)
    else:
        return search(arr[-mid:], val)
    

print(search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 22, 23, 25, 35, 44], 9))
