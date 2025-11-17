def caching_fibonacci():
    """
    Returns a fibonacci function that uses a cache (closure)
    to speed up repeated Fibonacci number calculations.
    """
    cache = {}

    def fibonacci(n):
        # Base cases
        if n <= 0:
            return 0
        if n == 1:
            return 1

        # Return from cache if exists
        if n in cache:
            return cache[n]

        # Recursive calculation with caching
        cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
        return cache[n]

    return fibonacci


# Example usage:
fib = caching_fibonacci()
print(fib(10))  # 55
print(fib(15))  # 610


