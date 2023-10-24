#
# 1762. Buildings With an Ocean View
#
# There are n buildings in a line. You are given an integer array heights of
# size n that represents the heights of the buildings in the line.
# The ocean is to the right of the buildings. A building has an ocean view if the building can see the ocean without obstructions.
# Formally, a building has an ocean view if all the buildings to its right have a smaller height.
# Return a list of indices (0-indexed) of buildings that have an ocean view, sorted in increasing order.
#
# https://leetcode.com/problems/buildings-with-an-ocean-view/
#


class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        buildings_with_ocean_view = []
        max_value = float("-inf")

        i = len(heights) - 1
        while i >= 0:
            if heights[i] > max_value:
                buildings_with_ocean_view.insert(0, i)
                max_value = heights[i]

            i -= 1

        return buildings_with_ocean_view
