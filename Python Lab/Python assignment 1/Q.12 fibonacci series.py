def fibonacci_series(n):
    # initialize the first two terms
    fib_series = [0, 1]
    
    # generate the Fibonacci series
    for i in range(2, n):
        next_term = fib_series[-1] + fib_series[-2]
        fib_series.append(next_term)
    
    return fib_series

# Function to print Fibonacci series up to n terms
def print_fibonacci(n):
    fib_series = fibonacci_series(n)
    print("Fibonacci Series up to {} terms:".format(n))
    for num in fib_series:
        print(num, end=" ")

# Taking input from the user for the number of terms
num_terms = int(input("Enter the number of terms: "))

# Printing Fibonacci series
print_fibonacci(num_terms)

# Example of fibonacci series
# 0 1 1 2 3 5 8 13 21 34 55 89