# Uses python3
import sys

def lcm_naive(a, b):
    for l in range(1, a*b + 1):
        if l % a == 0 and l % b == 0:
            return l

    return a*b

# fails at larger numbers
def lcm_better(a,b):
    if a == b:
        return a
    elif a > b:
        a, b = b, a

    a_primes = prime_factors(a)
    b_primes = prime_factors(b)

    b_product = 1

    missing_prime = []
    for num in a_primes:
        if num not in b_primes:
            missing_prime.append(num)
    
    for num in missing_prime:
        b_primes.append(num)
    print(missing_prime)
    print(b_primes)

    for num in b_primes:
        b_product *= num

    return b_product # if the lcm is not found in the loop above

def lcm_much_better(a, b) :
    return a * b // gcd_better(a, b)

# helper method
def prime_factors(n):
    i = 2 # 0 and 1 are not prime
    factors = []
    while i ** 2 <= n:
        if n % i:
            i += 1
        else:
            n = n // i # integer division - 
            factors.append(i)
    if n > 1:
        factors.append(n) # always a factor of itself
    # print(factors)
    return factors

# helper method
def gcd_better(a, b):
    if b == 0: # base case
        return a

    remainder = a % b # get the remainder of dividing a by b
    current_gcd = gcd_better(b, remainder)
    return current_gcd


if __name__ == '__main__':
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(lcm_much_better(a, b))

# print(lcm_better(12, 80))
# print(lcm_better(18, 35))
# print(lcm_better(9947312, 6057151))