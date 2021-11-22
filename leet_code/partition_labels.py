# 
# 763. Partition Labels
# 
# You are given a string s. We want to partition the string into as many parts as possible so that each letter appears in at most one part.
# Return a list of integers representing the size of these parts.
# 
# https://leetcode.com/problems/partition-labels/
# 


class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        partition_ranges = {}
        
        for i in range(len(s)):
            if s[i] not in partition_ranges:                
                partition_ranges[s[i]] = {'start_index': i, 'end_index': 0}
            else:
                partition_ranges[s[i]]['end_index'] = i

            
        


