<div align="center">
  <h1> 30 Days Of Python: Day 17 - Exception Handling</h1>
  <a class="header-badge" target="_blank" href="https://www.linkedin.com/in/fernandovicentinpavanello/">
  <img src="https://img.shields.io/badge/style--5eba00.svg?label=LinkedIn&logo=linkedin&style=social">
  </a>
  <a class="header-badge" target="_blank" href="https://twitter.com/nandovicentin">
  <img alt="Twitter Follow" src="https://img.shields.io/twitter/follow/nandovicentin?style=social">
  </a>

  <sub>Author:
  <a href="https://www.linkedin.com/in/fernandovicentinpavanello/" target="_blank">Fernando Vicentin Pavanello</a><br>
  <small> First Edition: March, 2022</small>
  </sub>
</div>

[<< Day 16](../16_Day_Python_date_time/16_python_datetime.md) | [Day 18 >>](../18_Day_Regular_expressions/18_regular_expressions.md)

<img src="../Images/python_TreviIT.png" alt="30 Days of Python">
</div>

- [📘 Day 17](#-day-17)
  - [Exception Handling](#exception-handling)
  - [Packing and Unpacking Arguments in Python](#packing-and-unpacking-arguments-in-python)
    - [Unpacking](#unpacking)
      - [Unpacking Lists](#unpacking-lists)
      - [Unpacking Dictionaries](#unpacking-dictionaries)
    - [Packing](#packing)
    - [Packing Lists](#packing-lists)
      - [Packing Dictionaries](#packing-dictionaries)
  - [Spreading in Python](#spreading-in-python)
  - [Enumerate](#enumerate)
  - [Zip](#zip)

  # 📘 Day 17

  ## Exception Handling

Python uses _try_ and _except_ to handle errors gracefully. A graceful exit (or graceful handling) of errors is a simple programming idiom - a program detects a serious error condition and "exits gracefully", in a controlled manner as a result. Often the program prints a descriptive error message to a terminal or log as part of the graceful exit, this makes our application more robust. The cause of an exception is often external to the program itself. An example of exceptions could be an incorrect input, wrong file name, unable to find a file, a malfunctioning IO device. Graceful handling of errors prevents our applications from crashing.

We have covered the different Python _error_ types in the previous section. If we use _try_ and _except_ in our program, then it will not raise errors in those blocks.

```py
try:
    code in this block if things go well
except:
    code in this block run if things go wrong
```

**Example:**

```py
try:
    print(10 + '5') # TypeError: unsupported operand type(s) for +: 'int' and 'str'
except:
    print('Something went wrong') 
```

In the example above the second operand is a string. We could change it to float or int to add it with the number to make it work. But without any changes, the second block, _except_, will be executed.

**Example:**

```py
try:
    name = input('Enter your name:')
    year_born = input('Year you were born:')
    age = 2022 - year_born
    print(f'You are {name}. And your age is {age}.')
except:
    print('Something went wrong')
```

```sh
Something went wrong
```

In the above example, the exception block will run and we do not know exactly the problem. To analyze the problem, we can use the different error types with except.

In the following example, it will handle the error and will also tell us the kind of error raised.

```py
try:
    name = input('Enter your name: ')
    year_born = input('Year you were born: ')
    age = 2022 - year_born
    print(f'You are {name}. And your age is {age}.')
except TypeError:
    print('Type error occurred.')
except ValueError:
    print('Value error occurred.')
except ZeroDivisionError:
    print('zero division error occurred.')
```

```sh
Enter your name: Case
Year you born: 1940
Type error occurred.
```

In the code above the output is going to be _TypeError_. (TypeError: unsupported operand type(s) for +: 'int' and 'str')
Now, let's add an additional block:

```py
try:
    name = input('Enter your name: ')
    year_born = input('Year you born: ')
    age = 2022 - int(year_born)
    print('You are {name}. And your age is {age}.')
except TypeError:
    print('Type error occur.')
except ValueError:
    print('Value error occur.')
except ZeroDivisionError:
    print('zero division error occur.')
else:
    print('I usually run with the try block.')
finally:
    print('I always run.')
```

```sh
Enter your name: Case
Year you born: 1940
You are Case. And your age is 82.
I usually run with the try block
I always run.
```

It is also shorten the above code as follows:
```py
try:
    name = input('Enter your name: ')
    year_born = input('Year you born: ')
    age = 2022 - int(year_born)
    print('You are {name}. And your age is {age}.')
except Exception as e:
    print(e)

```

## Packing and Unpacking Arguments in Python

We use two operators:

- \* for tuples
- \*\* for dictionaries

Let us take as an example below. It takes only arguments but we have list. We can unpack the list and changes to argument.

### Unpacking

#### Unpacking Lists

```py
def sum_of_five_nums(a, b, c, d, e):
    return a + b + c + d + e

lst = [1, 2, 3, 4, 5]
print(sum_of_five_nums(lst)) # TypeError: sum_of_five_nums() missing 4 required positional arguments: 'b', 'c', 'd', and 'e'
```

When we run the this code, it raises an error, because this function takes numbers (not a list) as arguments. Let us unpack/destructure the list.

```py
def sum_of_five_nums(a, b, c, d, e):
    return a + b + c + d + e

lst = [1, 2, 3, 4, 5]
print(sum_of_five_nums(*lst))  # 15
```

We can also use unpacking in the range built-in function that expects a start and an end.

```py
numbers = range(2, 7)  # normal call with separate arguments
print(list(numbers)) # [2, 3, 4, 5, 6]
args = [2, 7]
numbers = range(*args)  # call with arguments unpacked from a list
print(numbers)      # [2, 3, 4, 5, 6]

```

A list or a tuple can also be unpacked like this:

```py
countries = ['Finland', 'Sweden', 'Norway', 'Denmark', 'Iceland']
fin, sw, nor, *rest = countries
print(fin, sw, nor, rest)   # Finland Sweden Norway ['Denmark', 'Iceland']
numbers = [1, 2, 3, 4, 5, 6, 7]
one, *middle, last = numbers
print(one, middle, last)      #  1 [2, 3, 4, 5, 6] 7
```

#### Unpacking Dictionaries

```py
def unpacking_person_info(name, country, city, age):
    return f'{name} lives in {country}, {city}. He is {age} year old.'
dct = {'name':'Case', 'country':'Chiba City Blue', 'city':'Turing', 'age':240}
print(unpacking_person_info(**dct)) # Case lives in Chiba City Blue, Turing. He is 240 years old.
```

### Packing

Sometimes we never know how many arguments need to be passed to a python function. We can use the packing method to allow our function to take unlimited number or arbitrary number of arguments.

### Packing Lists

```py
def sum_all(*args):
    s = 0
    for i in args:
        s += i
    return s
print(sum_all(1, 2, 3))             # 6
print(sum_all(1, 2, 3, 4, 5, 6, 7)) # 28
```

#### Packing Dictionaries

```py
def packing_person_info(**kwargs):
    # check the type of kwargs and it is a dict type
    # print(type(kwargs))
	# Printing dictionary items
    for key in kwargs:
        print("{key} = {kwargs[key]}")
    return kwargs

print(packing_person_info(name="Case",
      country="Chiba City Blue", city="Turing", age=250))
```

```sh
name = Case
country = Chiba City Blue
city = Turing
age = 250
{'name': 'Case', 'country': 'Chiba City Blue', 'city': 'Turing', 'age': 250}
```

## Spreading in Python

Like in JavaScript, spreading is possible in Python. Let us check it in an example below:

```py
lst_one = [1, 2, 3]
lst_two = [4, 5, 6, 7]
lst = [0, *list_one, *list_two]
print(lst)          # [0, 1, 2, 3, 4, 5, 6, 7]
country_lst_one = ['Finland', 'Sweden', 'Norway']
country_lst_two = ['Denmark', 'Iceland']
nordic_countries = [*country_lst_one, *country_lst_two]
print(nordic_countries)  # ['Finland', 'Sweden', 'Norway', 'Denmark', 'Iceland']
```

## Enumerate

If we are interested in an index of a list, we use *enumerate* built-in function to get the index of each item in the list.

```py
for index, item in enumerate([20, 30, 40]):
    print(index, item)
```

```py
countries = ['Finland', 'Sweden', 'Norway', 'Denmark', 'Iceland']
for index, i in enumerate(countries):
    if i == 'Finland':
        print(f'The country {i} has been found at index {index}.')
    else:
        print(f'hi, {i} at index {index}.')
```

```sh
The country Finland has been found at index 0.
hi, Sweden at index 1.
hi, Norway at index 2.
hi, Denmark at index 3.
hi, Iceland at index 4.
```

## Zip

Sometimes we would like to combine lists when looping through them. See the example below:

```py
fruits = ['banana', 'orange', 'mango', 'lemon', 'lime']                    
vegetables = ['Tomato', 'Potato', 'Cabbage','Onion', 'Carrot']
fruits_and_veges = []
for f, v in zip(fruits, vegetables):
    fruits_and_veges.append({'fruit':f, 'veg':v})

print(fruits_and_veges)
```

```sh
[{'fruit': 'banana', 'veg': 'Tomato'}, {'fruit': 'orange', 'veg': 'Potato'}, {'fruit': 'mango', 'veg': 'Cabbage'}, {'fruit': 'lemon', 'veg': 'Onion'}, {'fruit': 'lime', 'veg': 'Carrot'}]
```

[<< Day 16](../16_Day_Python_date_time/16_python_datetime.md) | [Day 18 >>](../18_Day_Regular_expressions/18_regular_expressions.md)