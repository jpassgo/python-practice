#
# 75. Sort Colors
#
# Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.
#  We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.
# You must solve this problem without using the library's sort function.
#
# https://leetcode.com/problems/sort-colors/
from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        colors = {0: 0, 1: 0, 2: 0}
        for index, value in enumerate(nums):
            colors[value] = colors[value] + 1

        for index, value in enumerate(nums):
            if index <= colors[0]:
                nums[index] = 0
            elif index <= colors[0] + colors[1]:
                nums[index] = 1
            elif index <= colors[0] + colors[1] + colors[2]:
                nums[index] = 2


nums = [0, 1, 2, 2, 2, 1, 1, 0, 1, 0, 2, 1, 0, 1, 2]

print(nums)
solution = Solution()
solution.sortColors(nums)
print(nums)
