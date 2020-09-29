# Uses python3
import sys

'''
Task. The goal in this problem is to find the minimum number of coins needed to change the input value
(an integer) into coins with denominations 1, 5, and 10.

Input Format. The input consists of a single integer 𝑚.

Constraints. 1 ≤ 𝑚 ≤ 103.

Output Format. Output the minimum number of coins with denominations 1, 5, 10 that changes 𝑚.
Sample 1.

Input:
2
Output:
2

2 = 1 + 1.

Sample 2.

Input:
28
Output:
6

28 = 10 + 10 + 5 + 1 + 1 + 1.
'''

''' 
Strategy
--------
Safe Move
The largest coin denomination is 10, so we should fill up the money with as many
10 value coins as possible until adding another 10 coin would be over capacity.

Subproblem:
Iterate through adding 10c coins trying to get up to m.
The last iteration of 10c coin adding will either be at value m or over m.
If it is over m, we would start adding 5c coins until m is reached.
If it is over value on the last iteration of 5c coins, we fill up the rest with
1c coins.

We have an accumulator variable that gets +1 on each new coin added, and it returns at the end.

Formula:
c = coins
m = money
V1 = 10
V2 = 5
V3 = 1

Complexity Analysis:
Time = 5 + (n + 3) + (n + 3) + (n + 2)
     = 3(n + 3) + 5
     = 3n + 9 + 5
     = 3n + 14
     = O(n) Linear Time

'''

def get_change(m):
    # write your code here
    coins = 0 # accumulator
    dime = 10
    nickel = 5
    penny = 1
    current_value = 0

    while current_value < m
    
        if current_value + dime < m:
            current_value += dime
            coin += 1
        elif current_value == m:
            return coins
        else:
            break

    while current_value < m
    
        if current_value + nickel < m:
            current_value += nickel
            coin += 1
        elif current_value == m:
            return coins
        else:
            break

    while current_value < m
        if current_value + penny < m:
            current_value += penny
            coin += 1
        else:
            break      
        
    return coins

if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))