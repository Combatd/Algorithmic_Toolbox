# python3
import sys

'''
You are going to travel to another city that is located 𝑑 miles away from your home city. 
Your car can travel at most 𝑚 miles on a full tank and you start with a full tank. Along your way, there are gas stations at
distances stop1, stop2, . . . , stop𝑛 from your home city. What is the minimum number of refills needed?

Problem Description
Input Format. The first line contains an integer 𝑑. 
The second line contains an integer 𝑚. 
The third line
specifies an integer 𝑛. Finally, the last line contains integers stop1, stop2, . . . , stop𝑛.


Output Format. Assuming that the distance between the cities is 𝑑 miles, a car can travel at most 𝑚 miles
on a full tank, and there are gas stations at distances stop1, stop2, . . . , stop𝑛 along the way, output the
minimum number of refills needed. Assume that the car starts with a full tank. If it is not possible to
reach the destination, output −1.
'''

# distance integer
# tank integer
# stops list/array

def compute_min_refills(distance, tank, stops):
    # write your code here
    number_of_refills = 0
    current_refill = 0
    last_refill = 0
    n = len(stops) # number of stops
    # We need the destination as the final stop, and a 0 at the starting point
    stops.insert(0,0)
    stops.append(distance)

    print(stops)

    if distance <= tank:
        return 0 # we will never need refills
    
    while current_refill <= n:
        last_refill = current_refill
    
        while current_refill <= n and stops[current_refill + 1] - stops[last_refill] <= tank:
            current_refill += 1
            print(stops[current_refill + 1] - stops[last_refill])

            if current_refill == number_of_refills:
                break

        if current_refill == last_refill:
            return -1 
        
        if current_refill <= n:
            number_of_refills += 1
            
    
    return number_of_refills

if __name__ == '__main__':
    d, m, _, *stops = map(int, sys.stdin.read().split())
    print(compute_min_refills(d, m, stops))
