def compress_string(val):
    lc = 1
    cc = ""

    val_length = len(val)
    for i in range(val_length):
        if i + 1 >= len(val) or (val[i] != val[i + 1]):
            cc += val[i] + str(lc)
            lc = 1
        else:
            lc += 1

    if len(val) > len(cc):
        return cc
    else:
        return val


print(compress_string("aaaabbbcccccdd"))
