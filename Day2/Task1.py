"""
Task:
Given an integer n, perform the following conditional actions:

1. If n is odd, print "Weird"
2. If n is even and in the inclusive range of 2 to 5, print "Not Weird"
3. If n is even and in the inclusive range of 6 to 20, print "Weird"
4. If n is even and greater than 20, print "Not Weird"

Input Format:
A single line containing a positive integer n.

Output Format:
Print "Weird" or "Not Weird" based on conditions.
"""

# Read input
n = int(input())

# Conditions
if n % 2 != 0:
    print("Weird")
    
elif 2 <= n <= 5:
    print("Not Weird")
    
elif 6 <= n <= 20:
    print("Weird")
else:
    print("Not Weird")