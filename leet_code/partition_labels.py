# 
# 763. Partition Labels
# 
# You are given a string s. We want to partition the string into as many parts as possible so that each letter appears in at most one part.
# Return a list of integers representing the size of these parts.
# 
# https://leetcode.com/problems/partition-labels/
# 
from typing import List

class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        partition_ranges = {}

        for i in range(len(s)):
            if s[i] not in partition_ranges:                
                partition_ranges[s[i]] = {'start_index': i, 'end_index': i}
            else:
                partition_ranges[s[i]]['end_index'] = i

        parts = {}
        for k,v in partition_ranges.items():
            start_index = v['start_index']
            end_index = v['end_index']
            # If the start of the index is already in the parts and we need to increase the range of that part
            if start_index in parts and end_index > parts[start_index]: 
                parts[start_index] = end_index        
            else:
                value_updated = False
                # Check if the current character range overlaps with another range
                for k, v in parts.items():
                    if start_index < k and end_index > k:                        
                        del parts[k]
                        parts[start_index] = v
                        value_updated = True
                    elif start_index < v and end_index > v:
                        parts[k] = end_index
                        value_updated = True
                    elif start_index > k and end_index < v:
                        value_updated = True
                
                if start_index not in parts and value_updated == False:
                    # If our character range isn't already present and it doesn't overlap then just add it
                    parts[start_index] = end_index
                        
                                            

        return [(v+1) - k for k,v in parts.items()]




solution = Solution()
print(solution.partitionLabels('eccbbbbdec'))
print(solution.partitionLabels('ababcbacadefegdehijhklij'))
assert solution.partitionLabels('eccbbbbdec') == [10]
assert solution.partitionLabels('ababcbacadefegdehijhklij') == [9,7,8]