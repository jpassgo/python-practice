# f0 = 0
# f1 = 1
# f2 = 1
# f3 = 2
# f4 = 3
# f5 = 5
# f6 = 8
# f7 = 13


def getNthFib(n):
    return fib(n)


def fib(n, memo={}):
    if n == 1:
        return 0
    elif n == 2:
        return 1

    memo[n] = fib(n - 2) + fib(n - 1)

    return memo[n]


print(getNthFib(6))
