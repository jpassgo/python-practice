def maxArea(height: List[int]) -> int:
    i, j = 0, len(height) - 1
    max_area = float("-inf")

    while i < j:
        max_area = max(max_area, min(height[i], height[j]) * (j - i))
        if height[i] < height[j]:
            i += 1
        else:
            j -= 1

    return max_area
