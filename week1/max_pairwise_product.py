# python3

# Brute Force Solution

# def max_pairwise_product(numbers):
#     n = len(numbers) # the length of the array passed in
#     max_product = 0 # this is our accmulator
#     for first_num in range(n): # first loop
#         for second_num in range(first_num + 1, n): # nested loop
#             max_product = max(max_product,
#                 numbers[first_num] * numbers[second_num])
#         # max returns the highest value
#     return max_product


# Sorted uses hash maps so this should be logarithmic time
def max_pairwise_product(numbers):
    n = len(numbers)
    max_product = 0
    sorted_numbers = sorted(numbers)
    first_num = sorted_numbers[n - 1]
    second_num = sorted_numbers[n - 2]
    max_product = first_num * second_num
    return max_product

    

if __name__ == '__main__':
    input_n = int(input())
    input_numbers = [int(x) for x in input().split()]
    print(max_pairwise_product(input_numbers))
