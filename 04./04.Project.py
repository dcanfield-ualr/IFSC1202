"""
Create a program that displays a list or prime number in a specified range.
A prime number is a natural number greater than 1 that has no positive divisors other than 1 and itself.
Hint: For a given value N, Loop from 2 to (half of N) + 1 and check to see if any number evenly divides into N.
"""
start = int(input("Enter Start of Range: "))
end = int(input("Enter End of Range: "))

for n in  range(start, end)


def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, (number // 2) + 1):
        if number % i == 0:
            return False
    return True

def display_primes_in_range(start, end):
    prime_numbers = [num for num in range(start, end+1) if is_prime(num)]
    return prime_numbers

# Get user input for the range
start_range = int(input("Enter the start of the range: "))
end_range = int(input("Enter the end of the range: "))

# Display prime numbers in the specified range
prime_list = display_primes_in_range(start_range, end_range)
print(f"Prime numbers in the range {start_range} to {end_range}: {prime_list}")
