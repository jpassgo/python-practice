# print('Well hello {name}')
#
# x = 10
# y = 3
#
# result = x / y
# mod = x % y
# integer_division = x // y
#
# print(f'result: {result}, mod: {mod}, integer_division: {integer_division}')

# num = input('Number: ')
# print(int(num) - 5)


# hello = 'hello'.upper()
#
# print(f'{hello}')

# x = input('Name: ')
#
# if x == 'Jeff':
#    print('Your are great!')
# elif x == 'Johnny':
#    print('Hi Johnny')
# else:
#    print("You're not Jeff..")
#

# x = [4, True, 'hi']
# x.append('hello')
# x.extend([4,5,5,5,5,56,6])
#
# print(x.pop())
# print(len(x))
# print(x[1])

# x = (0, 4, 6, 7)

# start, stop, step
# for i in range(10):
#    print(i)

# `for i in range(10, -1, -1):
# `    print(i)

x = [3, 4, 23, 54, 3, 7]

# for i, element in enumerate(x):
#     print(i, element)

# i = 0
#
# while i < 10:
#    print('run')
#    i += 1

# x = [0,1,2,3,4,5,6,7,8]
# y = ['hi', 'hello', 'goodbye', 'cya', 'sure']
# s = 'hello'
#
## start:stop:step
# sliced = x[0:4:2]
# reversed = x[::-1]
# print(sliced)

# s = set()
# s.extend([4,32,2,2])
# s = {4, 12, 4} this is a set literal

# x = {'key': 4}
# print(x['key'])
#
# x['key2'] = 5
#
# print('key2' in x)
#
# print(list(x.values())
#
# del x['key2']
#
# for key, value in x.items():
#      print(key, value)

# x = [x for x in range(5)]
# print(x)

# y = [[0 for x in range(100) for x in range(5)]]
# print(y)

# z = [i for i in range(100) if i % 5 == 0]
# print(z)
#
# a = {a:0 for i in range(100) if i % 5 == 0}
# print(a)

# def funct(x, y, z=None):
#    print('Run', x, y, z)
#    return x * y, x / y
#
# r1, r2 = funct(4, 5, 6)
# print(r1, r2)

# def func(x):
#     def func2():
#         print(x)

#     return func2

# print(func(3)())

# x = func(3)
# x()

# x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(*x)
# print(x)
#
# def func(x, y):
#    print(x, y)
#
# pairs = [(1, 2), (3, 4), (5, 6)]
#
# for pair in pairs:
#    func(*pair)

# func(**{'x': 2, 'y': 3})

# def func(*args, **kwargs):
#    print(args, kwargs)
#
# func(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, x=1, y=2, z=3)

# x = 'jeff'

# def func(name):
#     x = name

# print(x)
# func('changed')
# print(x)

# x = 'jeff'

# def func(name):
#     global x
#     x = name

# print(x)
# func('changed')
# print(x)

# raise FileExistsError('File already exists')

# try:
#    x = 7 / 0
# except Exception as e:
#    print(e)
# finally:
#    print('Run this no matter what')

# x = lambda x: x + 5

# print(x(2))

x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# mp = map(lambda i: i + 2, x)
# filtered = filter(lambda x: x % 2 == 0, x)
# print(list(filtered))

# def func(i):
#    i = i * 3
#    return i % 2 == 0
#
# mp = filter(func, x)
# print(list(mp))
