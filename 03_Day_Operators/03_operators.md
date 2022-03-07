<div align="center">
  <h1> 30 Days Of Python: Day 3 - Operators</h1>
  <a class="header-badge" target="_blank" href="https://www.linkedin.com/in/luizfpavanello/">
  <img src="https://img.shields.io/badge/style--5eba00.svg?label=LinkedIn&logo=linkedin&style=social">
  </a>
  <a class="header-badge" target="_blank" href="https://twitter.com/nandovicentin">
  <img alt="Twitter Follow" src="https://img.shields.io/twitter/follow/nandovicentin?style=social">
  </a>

  <sub>Author:
  <a href="https://www.linkedin.com/in/luizfpavanello/" target="_blank">Fernando Vicentin Pavanello</a><br>
  <small> First Edition: March, 2022</small>
  </sub>
</div>

[<< Day 2](../02_Day_Variables_builtin_functions/02_variables_builtin_functions.md) | [Day 4 >>](../04_Day_Strings/04_strings.md)

<div align="center">
<img src="../Images/python_TreviIT.png" alt="30 Days of Python">
</div>

- [📘 Day 3](#-day-3)
  - [Python as a calculator](#python-as-a-calculator)
  - [Operators](#operators)
    - [Assignment Operators](#assignment-operators)
    - [Arithmetic Operators:](#arithmetic-operators)
    - [Comparison Operators](#comparison-operators)
    - [Logical Operators](#logical-operators)
    - [How not to divide](#how-not-to-divide)
    - [Operators and their priorities](#operators-and-their-priorities)
    - [Operators and their bindings](#operators-and-their-bindings)

# 📘 Day 3

## Python as a calculator

YOu already know that the function is able to show you the values of the literals passed to it by arguments, in fact, it can do something more. Take a look at the snippet:

```py
print(2 + 2) # 4
```

## Operators

An *operator* is a symbol of the programming language, which is able to operate on the values. Assignment operators are used to assign values to variables. The table below shows the different types of python assignment operators, taken from [w3school](https://www.w3schools.com/python/python_operators.asp). 

For example, just as in arithmetic, the _+_ sign is the operator which is able to *add* two numbers, giving ht result of the addiction.
Not all Python operators are as obvious as the plus sign, though, so let's go through some of the operators available in Python.

We'll begin with the operators which are associated with the most widely recognizable arithmetic operations:

→ +, -, *, /, //, %, **

The order of their appearance is not accidental. We'll talk more about it once we've gone through them all.

*Remember*: Data and operators when connected together form _expressions_. The simplest expression is a literal itself.

### Assignment Operators

Assignment operators are used to assign values to variables. The table below shows the different types of python assignment operators, taken from [w3school](https://www.w3schools.com/python/python_operators.asp). 

### Arithmetic Operators:

- Addition(+): a + b
- Subtraction(-): a - b
- Multiplication(*): a * b
- Division(/): a / b
- Modulus(%): a % b
- Integer division(//): a // b
- Exponentiation(**): a ** b

### Comparison Operators

In programming we compare values, we use comparison operators to compare two values. We check if a value is greater or less or equal to other value. The following table shows Python comparison operators which was taken from [w3shool](https://www.w3schools.com/python/python_operators.asp).

```py
print(3 > 2)     # True, because 3 is greater than 2
print(3 >= 2)    # True, because 3 is greater than 2
print(3 < 2)     # False,  because 3 is greater than 2
print(2 < 3)     # True, because 2 is less than 3
print(2 <= 3)    # True, because 2 is less than 3
print(3 == 2)    # False, because 3 is not equal to 2
print(3 != 2)    # True, because 3 is not equal to 2
print(len('mango') == len('avocado'))  # False
print(len('mango') != len('avocado'))  # True
print(len('mango') < len('avocado'))   # True
print(len('milk') != len('meat'))      # False
print(len('milk') == len('meat'))      # True
print(len('tomato') == len('potato'))  # True
print(len('python') > len('dragon'))   # False
```
### Logical Operators

Unlike other programming languages python uses keywords _and_, _or_ and _not_ for logical operators. Logical operators are used to combine conditional statements:

```py
print(3 > 2 and 4 > 3) # True - because both statements are true
print(3 > 2 and 4 < 3) # False - because the second statement is false
print(3 < 2 and 4 < 3) # False - because both statements are false
print('True and True: ', True and True)
print(3 > 2 or 4 > 3)  # True - because both statements are true
print(3 > 2 or 4 < 3)  # True - because one of the statements is true
print(3 < 2 or 4 < 3)  # False - because both statements are false
print('True or False:', True or False)
print(not 3 > 2)     # False - because 3 > 2 is true, then not True gives False
print(not True)      # False - Negation, the not operator turns true to false
print(not False)     # True
print(not not True)  # True
print(not not False) # False
```

### How not to divide

As you probably know, division by zero doesn't work.

Do not try to:

  - perform a division by zero;
  - perform an integer division by zero;
  - find a remainder of a division by zero.

### Operators and their priorities

So far, we've treated each operator as if it had no connection with the others. Obviously, such an ideal and simple situation is a rarity in real programming.

Also, you will very often find more than one operator in one expression, and then this presumption is no longer so obvious.

Consider the following expression: 2 + 3 * 5

You probably remember from school that multiplications precede additions.

You surely remember that you should first multiply 3 by 5 and, keeping the 15 in your memory, then add it to 2, thus getting the result of 17.

The phenomenon that causes some operators to act before others is known as the hierarchy of priorities.

Python precisely defines the priorities of all operators, and assumes that operators of a larger (higher) priority perform their operations before the operators of a lower priority.

So, if you know that * has a higher priority than +, the computation of the final result should be obvious.

### Operators and their bindings

The binding of the operator determines the order of computations performed by some operators with equal priority, put side by side in one expression.

Most of Python's operators have left-sided binding, which means that the calculation of the expression is conducted from left to right.

This simple example will show you how it works. Take a look: print(9 % 6 % 2)

There are two possible ways of evaluating this expression:

  - from left to right: first 9 % 6 gives 3, and then 3 % 2 gives 1;
  - from right to left: first 6 % 2 gives 0, and then 9 % 0 causes a fatal error.

Run the example and see what you get.

The result should be 1. This operator has left-sided binding. But there's one interesting exception.

[<< Day 2](../02_Day_Variables_builtin_functions/02_variables_builtin_functions.md) | [Day 4 >>](../04_Day_Strings/04_strings.md)