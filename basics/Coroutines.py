def my_coroutine():
    try:
        value = yield
        print(value)
    except GeneratorExit:
        print("Exiting coroutine")


coroutine = my_coroutine()
next(coroutine)

coroutine.send("Hello")
