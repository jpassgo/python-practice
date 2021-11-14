# 
# 451. Sort Characters By Frequency
# 
# Given a string s, sort it in decreasing order based on the frequency of the characters. 
# The frequency of a character is the number of times it appears in the string.
# Return the sorted string. If there are multiple answers, return any of them.
# 
# https://leetcode.com/problems/sort-characters-by-frequency/
# 

# input = acbaabd

# frequency dict
{'a': 3, 'c': 1, 'b': 2, 'd': 1}

# permutation dict
{3: ['a'], 2: ['b'], 1: ['c', 'd']}

class Solution:
    def frequencySort(self, s: str) -> str:
        frequency_dict = {}

        for c in s:
            if c in frequency_dict.keys():
                frequency_dict[c] = frequency_dict[c]+1                
            else:
                frequency_dict[c] = 1

        permutation_dict = {}
        for k, v in frequency_dict.items():
            if v in permutation_dict.keys():
                permutation_dict[v].append(k)             
            else:
                permutation_dict[v] = [k]
    
        permutation_dict = sorted(permutation_dict.items(), reverse=True)
        
        sorted_string = ''
        for k in permutation_dict:
            for v in k[1]:
                sorted_string += v*k[0]

        return sorted_string

        



solution = Solution()

print(solution.frequencySort('acbaabd'))
print(solution.frequencySort('Acbaabd'))
        