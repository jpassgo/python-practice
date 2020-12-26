# Fibonacci Sequence:
# 1, 1, 2, 3, 5, 8, 13, etc...
# Starts with two 1's then sum the previous two numbers to calculate the
# next number in the sequence.

# Recursion
def fibonacci(n):
    if n == 1 or n == 2:
        result = 1
    else:
        result = fibonacci(n - 1) + fibonacci(n - 2)
    return result


print(fibonacci(10))


# Recursion with Memoization
def memoized_fibonacci(n, memo):
    try:
        if memo[n] is not None:
            return memo[n]
    except BaseException:
        pass

    if n == 1 or n == 2:
        result = 1
    else:
        result = fibonacci(n - 1) + fibonacci(n - 2)
    memo.insert(n, result)

    return result


memo = []
print(memoized_fibonacci(10, memo))

# Bottom up approach


def bottom_up_fibonacci(n):
    if n == 1 or n == 2:
        return 1
    bottom_up = [None for i in range(n + 1)]
    bottom_up[1] = 1
    bottom_up[2] = 1

    for i in range(3, n + 1):
        bottom_up[i] = bottom_up[i - 1] + bottom_up[i - 2]

    return bottom_up[n]


print(bottom_up_fibonacci(10))
