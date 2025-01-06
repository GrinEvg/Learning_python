# факториал через обычный цикл
def factorial(n):
    res = 1
    for i in range(1, n + 1):
        res *= i
    return res

# факториал через рекурсию

def factorial2(n):
    if n == 1:
        return 1
    return factorial2(n-1) * n

# ряд Фибоначи (след число = сумме 2 предыдущих)
def fib(n):
    if n == 1:
        return 0
    if n == 2:
        return 1
    a, b = 0, 1
    cnt = 2
    
    while cnt <= n:
        a, b = b, a+b
        cnt += 1
        
    return a