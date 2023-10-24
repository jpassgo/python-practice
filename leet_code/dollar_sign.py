def is_dollar_delete_equal(array) -> bool:
    current_size = 0

    for i in range(len(array)):
        cleaned_string = remove_dollar_signs(list(array[i]))

        if current_size != 0 and current_size != len(cleaned_string):
            return False
        else:
            current_size = len(cleaned_string)

    return True


def remove_dollar_signs(current_string) -> str:
    for i in range(len(current_string)):
        if i < len(current_string) and current_string[i] == "$":
            del current_string[i]
            del current_string[i - 1]

    return current_string


print(is_dollar_delete_equal(["f$ec", "ec$"]))
print(is_dollar_delete_equal(["ab$$", "c$d$"]))
