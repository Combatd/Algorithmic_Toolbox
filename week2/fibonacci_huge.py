# Uses python3
import sys

def get_fibonacci_huge_naive(n, m):
    if n <= 1:
        return n

    previous = 0
    current  = 1

    for _ in range(n - 1):
        previous, current = current, previous + current

    return current % m

def get_fibonacci_huge_better(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    elif n == 2:
        return 1
    elif n == 3:
        return 2
    elif n == 4:
        return 3
    elif n == 5:
        return 5
    elif n == 6:
        return 8
    
    f1 = 0
    f2 = 1
    fibArray = [f1, f2] # we will try to grab the last number
    i = 0
    while i < n:
        original_f1 = 0 + f1
        f1 = f2
        f2 = original_f1 + f2 # needs to add the previous number
        fibArray.append(f2)
        i += 1
        
    # n is always going to be one more than the array index
    return fibArray[len(fibArray) - 2]

if __name__ == '__main__':
    input = sys.stdin.read();
    n, m = map(int, input.split())
    print(get_fibonacci_huge_better(n, m))