def factorial(n):
    product = 1
    while n > 1:
        product  *= n
        print(product)
        n = n-1
    return product
factorial(5)
5
20
60
120
120
a,b = 0, 1
def fibonacci(a,b,n):
    for i in range(n):
        b = a + b
        a = b - a
        print(b)
        
fibonacci(0,1,5)
1
2
3
5
8
