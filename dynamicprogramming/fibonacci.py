# Fibonacci Sequence:
# 1, 1, 2, 3, 5, 8, 13, etc...
# Starts with two 1's then sum the previous two numbers to calculate the next number in the sequence.

# Recursion
def fibonacci(n): 
    if n == 1 or n == 2:
        result = 1
    else:
        result = fibonacci(n-1) + fibonacci(n-2)
    return result 
    

print(fibonacci(10))

def memoized_fibonacci(n, memo):
    try:
        if memo[n] != None:
            return memo[n]
    except:
        pass
    
    if n == 1 or n == 2:
        result = 1
    else:
        result = fibonacci(n-1) + fibonacci(n-2)
    memo.insert(n, result)

    return result

memo = []
print(memoized_fibonacci(10, memo))

