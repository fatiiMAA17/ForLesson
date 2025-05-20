# def fib(n):
#     sum = 2
#     for i in range(3, n + 1):
#         current = f + s
#         s , f = f , current
#     return sum
# print(fib(3))
def fibonacci(n):
    if n == 1 or n == 2 :
        return 1
    return fib(n -1) + fib(n - 2)
print(fibonacci(10))