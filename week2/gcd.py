# Uses python3
import sys

'''
    For integers, a and b, their greatest common divisor, or gcd(a,b)
    is the largest integer d so that d divides both a and b
'''
def gcd_naive(a, b):
    current_gcd = 1
    for d in range(2, min(a, b) + 1):
        if a % d == 0 and b % d == 0:
            if d > current_gcd:
                current_gcd = d

    return current_gcd

'''
    The Euclidean Algorithm
    If A = 0 then GCD(A,B)=B, since the GCD(0,B)=B, and we can stop.  
    If B = 0 then GCD(A,B)=A, since the GCD(A,0)=A, and we can stop.  
    Write A in quotient remainder form (A = B⋅Q + R)
    Find GCD(B,R) using the Euclidean Algorithm since GCD(A,B) = GCD(B,R)
'''

def gcd_better(a, b):
    if b == 0: # base case
        return a

    remainder = a % b # get the remainder of dividing a by b
    current_gcd = gcd_better(b, remainder)
    return current_gcd

if __name__ == "__main__":
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(gcd_better(a, b))
