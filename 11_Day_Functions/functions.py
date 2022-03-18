'''
### Exercises: 

1. Declare a function _add_two_numbers_. It takes two parameters and it returns a sum.
'''
from calendar import month


x = int(input("Enter the first number: "))
y = int(input("Enter the second number: "))

def sum(x, y):
    return x + y

print(sum(x, y))

'''
2. Area of a circle is calculated as follows: area = π x r x r. Write a function that calculates _area_of_circle_.
'''
π = 3.14
r = int(input("Enter the radius of the circle: "))

def area_of_circle(r):
    return π * r * r

print(area_of_circle(r))

'''
3. Write a function called add_all_nums which takes arbitrary number of arguments and sums all the arguments. Check if all the list items are number types. If not do give a reasonable feedback.
'''
def add_all_nums(*args):
   total = 0
   for num in args:
       if type(num) == int:
           total += num
       else:
           return "Please enter only numbers"
   return total

print(add_all_nums(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))

'''
4. Temperature in °C can be converted to °F using this formula: °F = (°C x 9/5) + 32. Write a function which converts °C to °F, _convert_celsius_to-fahrenheit_.
'''
c = int(input("Enter the temperature in °C: "))

def convert_celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

print(convert_celsius_to_fahrenheit(c))

'''
5. Write a function called check-season, it takes a month parameter and returns the season: Autumn, Winter, Spring or Summer.
'''
month = int(input("Enter the number of the month: "))

def check_season(month):
    if month == 12 or month == 1 or month == 2:
        return "Winter"
    elif month == 3 or month == 4 or month == 5:
        return "Spring"
    elif month == 6 or month == 7 or month == 8:
        return "Summer"
    elif month == 9 or month == 10 or month == 11:
        return "Autumn"

print(f"The weather at the Northern Hemisphere is {check_season(month)}.")

