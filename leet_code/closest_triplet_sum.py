# Given an array of integers and a target value find three values whose sum is closest to the target value.


def closest_sum(array, target):
    array.sort()

    closest_sum = float("inf")

    for i in range(len(array) - 2):
        left_ptr = i + 1
        right_ptr = len(array) - 1

        sum = array[i] + array[left_ptr] + array[right_ptr]

        # If the difference between the target and the current sum is less than the target
        # and the previous closest sum then update the closest sum
        if abs(target - sum) < abs(target - closest_sum):
            closest_sum = sum

        if closest_sum > target:
            left_ptr += 1
        else:
            right_ptr += 1

    return closest_sum


array = [-1, 2, 1, -4]
print(closest_sum(array, 1))
