#
# Find the largest range of 1's seperated by a single 0
# 9
# '111011101111011110000011110'
#


def largest_range(nums):
    current_max = float("-inf")

    zero_found = False
    one_found = False

    window_start = 0
    next_window_start = 0

    for i in range(len(nums) - 1):
        print(f"{nums[i]} - zero_found {zero_found} - one_found {one_found}")
        if one_found == False and nums[i] == "1":
            one_found = True
            window_start = i
        elif nums[i] == "1":
            pass
        elif zero_found == False and nums[i] == "0":
            zero_found = True
            next_window_start = i + 1
            if i < len(nums) - 1 and nums[i + 1] == "0":
                one_found = False
                zero_found = False
        elif one_found == True and zero_found == True and nums[i] == "0":
            current_max = max(current_max, (i - window_start))
            one_found = False
            zero_found = False
            if i < len(nums) - 1 and nums[i + 1] == "0":
                zero_found = False
            window_start = next_window_start

    return current_max


print(largest_range("111011101111011110000011110"))
