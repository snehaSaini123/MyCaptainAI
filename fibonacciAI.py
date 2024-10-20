def fibonacci(n):
    """Generate Fibonacci numbers up to n."""
    fib_sequence = []
    a, b = 0, 1  # Starting values for Fibonacci sequence
    while a <= n:
        fib_sequence.append(a)
        a, b = b, a + b  # Update values for the next Fibonacci number
    return fib_sequence

# Input: Limit for Fibonacci numbers
limit = int(input("Enter the limit for Fibonacci numbers: "))
fib_numbers = fibonacci(limit)

# Output: Display the Fibonacci numbers
print(f"Fibonacci numbers up to {limit}: {fib_numbers}")