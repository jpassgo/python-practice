class Solution:
    def isHappy(self, n: int) -> bool:
        n_as_str = str(n) 
        
        sums = []
                        
        sum_value = 0
        i = 0
        while i <= len(n_as_str) - 1: 
            print(int(n_as_str[i]) ** 2)
            sum_value += int(n_as_str[i]) ** 2                        
            print(sum_value)
            
            if i == len(n_as_str) - 1:
                if sum_value == 1:
                    return True
                n_as_str = str(sum_value)
                
                if sum_value in sums:
                    return False
                
                sums.append(sum_value)
                sum_value = 0
                i = 0
            else:
                i += 1
                