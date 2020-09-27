# Uses python3
import sys

def get_fibonacci_last_digit_naive(n):
    if n <= 1:
        return n

    previous = 0
    current  = 1

    for _ in range(n - 1):
        previous, current = current, previous + current

    return current % 10

def get_fibonacci_last_digit_better(n):
    # modular arithmetic should allow me to use remainders to reduce complexity
    # https://en.wikipedia.org/wiki/Modular_arithmetic
    # a_n + b_n = (a + b)n
    # https://mathworld.wolfram.com/FibonacciNumber.html
    # Ending digits of Fibonacci recycle every 60 iterations
    if n <= 1:
        return n

    previous = 0
    current = 1

    for num in range(2, n + 1):
        modulo_result = (previous + current) % 10
        previous = current # (n - 2)
        current = modulo_result # (n - 1)

    return modulo_result # (n - 2) + (n - 1)

if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    print(get_fibonacci_last_digit_better(n))
