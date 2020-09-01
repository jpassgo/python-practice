from random import randint

print(list(map(lambda num: num+1, [randint(1, 10000) for num in range(100)])))
