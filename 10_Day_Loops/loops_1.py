'''
A program that reads a sequence of numbers and counts how many numbers are even and how many are odd.
The program terminates when zero is entered.
'''

odd_numbers = 0
even_numbers = 0

# Read the first number
number = int(input("Enter a number or type 0 to stop: "))

# 0 terminates execution
while number != 0:
    # Check if the number is odd.
    if number % 2 == 0:
        # Increase the odd_numbers counter
        odd_numbers += 1
    else:
        # Increase the even_numbers counter
        even_numbers += 1
    # Read the next number
    number = int(input("Enter a number or type 0 to stop: "))

# Print results.
print("The number of odd numbers is:", odd_numbers)
print("The number of even numbers is:", even_numbers)
