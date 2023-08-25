def solution(n):
    # Convert the integer to a string
    n_str = str(n)
    
    # Access the individual digits
    first_digit = int(n_str[0])
    second_digit = int(n_str[1])
    
    # Calculate the sum of the digits
    digit_sum = first_digit + second_digit
    
    return digit_sum

# Example usage
n = 29
print(solution(n))  # Output: 11
