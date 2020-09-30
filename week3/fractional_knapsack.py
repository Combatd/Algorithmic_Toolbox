# Uses python3
import sys

'''
Greedy Algorithm
* While capacity is not full
* Choose item i with maximum vi / wi (volume / weight)
* if item fits into capacity, take all of it
* Otherwise, take enough of the item to fill to total capacity
* Return value and amounts of each item

Amount <-- [0,0,0,0,0], Value <- 0

repeat n times:
    if Weight = 0:
        return (V, A)
    select i with Wi > 0 and max Vi/Wi
    a <- min(Wi, W)
    V <- V + a(Vi/Wi)
    ** Change the value of the variables! **
    Wi <- Wi - a, A[i] <- A[i] + a, W <- V 
return (V, A)

Lemma (Complexity Analysis)
Time Complexity of #get_optimal_value is O(n^2) polynomial

* Selecting the best item on each step is O(n) because of inner looping
* Main loop will be executed n times

But we can continue optimizing this...

** We can ignore iterations we already checked! **
for i from 1 to n: 
    if W = 0:
        return (V,A)
    a <- min(Wi, W)
    V <- V + a(Vi/Wi)
    Wi <- Wi - a, A[i] <- A[i] + a, W <- V - a
return (V, A)

Array A will be filled with amounts of items starting with values 0

* Each iteration is O(1) Constant Time
* If we sort the items first, that takes O(n)
* Sort + Knapsack is O(nlogn) Linear Logarithmic time as it is always less than O(n)
'''

def get_optimal_value(capacity, weights, values):
    value = 0
    # write your code here

    # print(values)
    # print(weights)
    # sorted_weights = sorted(weights)
    # sorted_values = sorted(values)
        
    amounts = []
    idx = 0
    for item in range(0, len(weights) - 1):
        amounts.append([values[idx]])
        idx += 1

    return amounts
    
    W = 0 + capacity
    i = 0
    # while i < len(weights) - 1:
    #     i += 1
    #     if W == 0:
    #         return value
    #     amount = min(values[i]/weights[i]) # round the float
    #     values += amount
    #     W = W - amount

    return value

        



if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))