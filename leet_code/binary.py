def longest_contiguous_ones(number):
    binary_string = format(number, "b")
    binary_len = len(binary_string) - 1

    current_max_range = 0
    window_start = 0
    next_window_start = 0
    zero_encountered = False
    one_encountered = False

    for i in range(binary_len):
        current_num = binary_string[i]
        print(current_num)

        if current_num == "1" and not one_encountered:
            one_encountered = True
            window_start = i
        elif current_num == "1":
            pass
        elif current_num == "0" and not zero_encountered:
            if i < binary_len and binary_string[i + 1] == "1" and one_encountered:
                zero_encountered = True
            else:
                one_encountered = False
                zero_encountered = False
        elif current_num == "0" and zero_encountered:
            # Zero encountered for second time so calculate max range
            current_range = i - window_start
            current_max_range = max(current_max_range, current_range)
            zero_encountered = False
            one_encountered = False

    return current_max_range


# 10011010010
print(longest_contiguous_ones(1234))
