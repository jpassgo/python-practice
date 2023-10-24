import time


def count_down(t):
    if t == 0:
        pass
    else:
        print(t)
        time.sleep(1)
        count_down(t - 1)


count_down(5)
