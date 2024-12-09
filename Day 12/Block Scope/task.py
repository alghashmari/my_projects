def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num)):
        if num % i == 0:
            return False
    return True

# Test cases
print(is_prime(73))  # Should print True
print(is_prime(75))  # Should print False