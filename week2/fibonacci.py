# Uses python3
def calc_fib(n):
    if (n <= 1):
        return n
    elif (n == 2):
        return 1

    return (n - 1) + (n - 2)

n = int(input())
print(calc_fib(n))