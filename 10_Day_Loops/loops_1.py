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


'''
1. Iterate 0 to 10 using for loop, do the same using while loop.
'''
for number in range(11):
    print(number)

count = 0
while count <= 10:
    print(count)
    count += 1

'''
2. Iterate 10 to 0 using for loop, do the same using while loop.
'''
for number in range(10, -1, -1):
    print(number)

count = 10
while count >= 0:
    print(count)
    count -= 1

'''
3. Write a loop that makes seven calls to print(), so we get on 
the output the following triangle:

   ```py
     #
     ##
     ###
     ####
     #####
     ######
     #######
   ```
'''
calls = int(input("Enter the number of calls: "))

for number in range(calls):
    print('#' * (number + 1))

'''
4. Use nested loops to create the following:

   ```sh
   # # # # # # # #
   # # # # # # # #
   # # # # # # # #
   # # # # # # # #
   # # # # # # # #
   # # # # # # # #
   # # # # # # # #
   # # # # # # # #
   ```
'''
rows = int(input("Enter the number of rows: "))
columns = int(input("Enter the number of columns: "))

for row in range(rows):
    for column in range(columns):
        print("#", end='')
    print()

'''
5. Print the following pattern:

   ```sh
   0 x 0 = 0
   1 x 1 = 1
   2 x 2 = 4
   3 x 3 = 9
   4 x 4 = 16
   5 x 5 = 25
   6 x 6 = 36
   7 x 7 = 49
   8 x 8 = 64
   9 x 9 = 81
   10 x 10 = 100
   ```
'''
num = int(input("Which table's number: "))
for number in range(11):
    print(f"{number} x {num} = {number * num}")

'''
6. Iterate through the list, ['Python', 'Numpy','Pandas','Django', 'Flask'] using a for loop and print out the items.
'''
list = ['Python', 'Numpy','Pandas','Django', 'Flask']
for item in list:
    print(item)

'''
7. Use for loop to iterate from 0 to 100 and print only even numbers
'''
for number in range(101):
    if number % 2 == 0:
        print(number)

'''
8. Use for loop to iterate from 0 to 100 and print only odd numbers
'''
for number in range(101):
    if number % 2 != 0:
        print(number)

'''
9.  Use for loop to iterate from 0 to 100 and print the sum of all numbers.

   ```sh
   The sum of all numbers is 5050.
   ```
'''
num = int(input("Enter the number: "))
sum = 0
for value in range(1, num + 1):
    sum += value

print(sum)

'''
10. Use for loop to iterate from 0 to 100 and print the sum of all evens and the sum of all odds.

    ```sh
    The sum of all evens is 2550. And the sum of all odds is 2500.
    ```
'''
num = int(input("Enter the number: "))
sum_even = 0
sum_odd = 0
for value in range(1, num + 1):
    if value % 2 == 0:
        sum_even += value
    else:
        sum_odd += value

print(f"The sum of all evens is {sum_even}. And the sum of all odds is {sum_odd}.")
