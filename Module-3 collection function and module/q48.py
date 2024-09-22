#(48)Write a Python function to calculate the factorial of a number (anonnegative integer). 

def factorial(n):
    if n < 0:
        return "factorial does not exit for negative number"

    fact = 1

    for i in range(1, n + 1):
        fact *= i
    return fact

print(factorial(5))  # Output: 120
