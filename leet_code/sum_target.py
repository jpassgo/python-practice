# 
# Given a list and a target value, determine if two numbers in the list sum up to the target
# 


def target_sum(arr, target):

    compliment_dict = {}
    for item in arr:
        compliment = target - item
        if compliment in compliment_dict.keys():
            return (compliment, item)
        else:
            compliment_dict[item] = compliment

    return None


print(target_sum([1, 20, 23, 3, 8, 15, 35, 17], 58))