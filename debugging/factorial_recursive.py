#!/usr/bin/python3
import sys

# Function description:
#   Computes the factorial of a non-negative integer using recursion.
#
# Parameters:
#   n (int): The number for which the factorial is calculated.
#
# Returns:
#   int: The factorial of the given number.
def factorial(n):
	if n == 0:
		return 1
	else:
		return n * factorial(n - 1)

# Get the command-line argument, convert it to an integer,
# compute its factorial, and print the result
f = factorial(int(sys.argv[1]))
print(f)
