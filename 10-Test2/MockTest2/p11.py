def decimal_to_binary(n):
    """Convert a natural number to binary using a stack."""
    if n < 0:
        raise ValueError("Only natural numbers (>= 0) are allowed")
    
    if n == 0:
        return "0"

    stack = []

    while n > 0:
        stack.append(str(n % 2))
        n //= 2

    return ''.join(reversed(stack))


# Example usage
print(decimal_to_binary(515))
