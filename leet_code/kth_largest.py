#
# 215. Kth Largest Element in an Array
#
# Given an integer array nums and an integer k, return the kth largest element in the array.
# Note that it is the kth largest element in the sorted order, not the kth distinct element.
#
# https://leetcode.com/problems/kth-largest-element-in-an-array/submissions/
#
from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums.sort()
        num_of_nums = len(nums)
        i = num_of_nums - 1
        while i >= 0:
            current = nums[i]
            if num_of_nums - i == k:
                return current
            i -= 1


solution = Solution()

assert solution.findKthLargest([3, 2, 1, 5, 6, 4], 2) == 5
print(solution.findKthLargest([3, 2, 1, 5, 6, 4], 2))
