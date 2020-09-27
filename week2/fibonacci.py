# Uses python3
def calc_fib(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    elif n == 2:
        return 1
    
    f1 = 0
    f2 = 1
    fibArray = [f1, f2] # we will try to grab the last number
    while f2 < n:
        original_f1 = 0 + f1
        f1 = f2
        f2 = original_f1 + f2 # needs to add the previous number
        fibArray.append(f2)
    # print(fibArray)
    
    # return the second to number in the list!
    return fibArray[len(fibArray) - 2]

n = int(input())
print(calc_fib(n))