
def factorial(n, product):
    print(f"n:{n}, product: {product}")
    if n == 1:
        return product    
    else:
        if product != 0:
            product = product * (n-1)
        else:
            product = n * (n-1)

        return factorial(n-1, product)

print(factorial(3, 0))