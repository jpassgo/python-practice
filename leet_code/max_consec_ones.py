# 1004. Max Consecutive Ones III
# 
# Given a binary array nums and an integer k, return the maximum number of consecutive 
# 1's in the array if you can flip at most k 0's.
# 
# https://leetcode.com/problems/max-consecutive-ones-iii/
# 
from typing import List

def max_consecutive_ones(nums: List[int], k: int) -> int:
    current_max = float('-inf')
    current_zeroes = 0

    start_range = 0
    current_index = 0

    while current_index < len(nums):
        if nums[current_index] == 0 and current_zeroes < k:
            current_zeroes += 1

        if current_zeroes < k:
            current_index += 1
        elif current_zeroes == k:
            current_max = max(current_max, ((current_index + 1) - start_range))
            start_range += 1
            if start_range > 0 and nums[start_range-1] == 0:
                current_zeroes -= 1
            if start_range == current_index:
                current_index += 1

    return current_max

# size == 11
nums = [1,1,1,0,0,0,1,1,1,1,0]
k = 2
print(max_consecutive_ones(nums, k))


nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1]
k = 3
print(max_consecutive_ones(nums, k))
