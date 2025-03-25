def large_power(base, exponent):
    
    result = base ** exponent
    
    # Check if the result is greater than 5000
    if result > 5000:
        return True
    else:
        return False

# Example usage
print(large_power(10, 3))  # Should return True, as 10^3 = 1000, which is greater than 5000
print(large_power(5, 4))   # Should return False, as 5^4 = 625, which is less than 5000
