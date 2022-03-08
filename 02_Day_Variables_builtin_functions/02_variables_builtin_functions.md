<div align="center">
  <h1> 30 Days Of Python: Day 2 - Variables, Builtin Functions</h1>
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

[<< Day 1](../readme.md) | [Day 3 >>](../03_Day_Operators/03_operators.md)

<div align="center">
<img src="../Images/python_TreviIT.png" alt="30 Days of Python">
</div>

- [📘 Day 2](#-day-2)
  - [Built in functions](#built-in-functions)
    - [The print() function](#the_print()_function)
      - [The escape and newline characters](#escape_characters)
      - [The keyword arguments](#the_keyword_arguments)
  - [Variables](#variables)
    - [Correct and incorrect variable names](#correct-and-incorrect-variable-names)
    - [Declaring Multiple Variable in a Line](#declaring-multiple-variable-in-a-line)
    - [Assigning a new value to an already existing variable](#assigning-new-value)
  - [Data Types](#data-types)
  - [Checking Data types and Casting](#checking-data-types-and-casting)
  - [Numbers](#numbers)

# 📘 Day 2

## Built in functions

In Python we have lots of built-in functions. Built-in functions are globally available for you to use without importing modules or any extra configuration. Some of the most commonly built-in functions are: _print()_, _len()_, _type()_, _int()_, _float()_, _str()_, _input()_, _list()_, _dict()_, _min()_, _max()_, _sum()_, _sorted()_, _open()_, _file()_, _help()_, and _dir()_. [python documentation](https://docs.python.org/3.9/library/functions.html).

### The print() function

Look at the line of code below

```
print("Hello, World!")
```
The word _print_ that you can see here is a *function name*. That doesn't mean that wherever the word appears it is always a function name. The meaning of the word comes from the context in which the word has been used.

You've probably encountered the term function many times before, during math classes. You can probably also list several names of mathematical functions, like sine or log.
Python functions, however, are more flexible, and can contain more content than their mathematical siblings.

A function (in this context) is a separate part of the computer code able to:

  - _cause some effect_(e.g., send text to the terminal, create a file, draw an image, play a sound, etc.), this is something completely unheard of the world of mathematics;
  - _evaluate a value_(e.g., the square root of a value or the length of a given test) and _return it as the function's result_, this is what makes Python functions the relatives of mathematical concepts.

Moreover, many of Python functions can do the above two things together.

Where do the function come from?

  - They may come _from Python itself_: the print function is one of this kind, such a function is an added value received together with Python and its environment (it is *built-in*), you don't have to do anything special (e.g., ask anyone for anything) if you want to make use of it;
  - they may come from one or more of Python's add-ons named _modules_, some of the modules come with Python, others may require separate installation - whatever the case, they all need to be explicitly connected with your code;
  - you can _write them yourself_, placing as many functions as you want and need inside your program to make it simpler, clearer and more elegant.

The name of the function should be *significant* (the name of the print function is self-evident)

Of course, if you're going to make use of any already existing function, you have no influence on its name, but when you start writing your own functions, you should consider carefully your choice of names.

A Function may have:
  - an _effect_;
  - a _result_

There's also a third, very important function component - the *argument(s)*.

Mathematical functions usually take one argument, e.g., sin(x) takes an x, which is the measure of an angle.

Python functions, on the other hand, are more versatile. Depending in the individual needs, they may accept any number of arguments - as many as necessary to perform their tasks. Note: any number includes zero - some Python functions don't need any argument.

```
print "Hello, World!"
```

In spite of the number of needed/provided arguments, Python functions strongly demand the presence of _a pair of parentheses_ - opening and closing ones, respectively.

If you want to deliver one or more arguments to a function, you place them _inside the parentheses_. If you're going to use a function which doesn't take any argument, you still have to have the parentheses.

Note: to distinguish ordinary words from function names, place _a pair of empty parentheses_ after their names, even if the corresponding function wants one or more arguments. This is a standard convention.

The function we're talking about here is print().

Does the print() function in our example have any arguments?

Of course it does, but what are they?

The only argument delivered to the print() function in this example is a string:

```
print("Hello, World!")
```

As you can see, the *string is delimited with quotes* - in fact, the quotes make the string - they cut out a part of the code and assign a different meaning to it.

You can imagine that the quotes say something like: the text between us is not code. It isn't intended to be executed, and you should take it as is. Almost anything you put inside the quotes will be taken literally, not as code, but as *data*. 

The function name (*print* in this case) along with the parentheses and argument(s), forms the *function invocation*.

```
print("Hello, World!")
```

What happens when Python encounters an invocation like this one below?

```
function_name(argument)
```

→ Let's see:

  - First, Python checks if the name specified is _legal_ (it browses its internal data in order to find an existing function of the name; if this search fails, Python aborts the code);
  - second, Python checks if the function's requirements for the number of arguments _allows you to invoke_ the function in this way (e.g., if a specific function demands exactly two arguments, any invocation delivering only one argument will be considered erroneous, and will abort the code's execution);
  - third, Python _leaves your code for a moment_ and jumps into the function you want to invoke; of course, it takes your argument(s) too and passes it/them to the function;
  - fourth, the function _executes its code_, causes the desired effect (if any), evaluates the desired result(s) (if any) and finishes its task;
  - finally, Python _returns to your code_ (to the place just after the invocation) and resumes its execution.

#### The escape and newline characters

We've modified the code. Look at it carefully.

```
print("The itsy bitsy spider\nclimbed up the waterspout.")
print()
print("Down came the rain\nand washed the spider out.")
```

There are two very subtle changes - we've inserted a strange pair of characters inside the rhyme. They look like this: \n.

Interestingly, while _you can see two characters, Python sees one_.

The backslash [ \ ] has a very special meaning when used inside strings - this is called the *escape character*.

The word escape should be understood specifically - it means that the series of characters in the string escapes for the moment (a very short moment) to introduce a special inclusion.

In other words, the backslash doesn't mean anything in itself, but is only a kind of announcement, that the next character after the backslash has a different meaning too.

The letter [ n ] placed after the backslash comes from the word _newline_.
Both the [ backslash ] and the [ n ] form a special symbol named a *newline character*, which urges the console to start a *new output line*.

Run the code. Your console should now look like this:

```
The itsy bitsy spider
climbed up the waterspout.

Down came the rain
and washed the spider out.
```
As you can see, two newlines appear in the nursery rhyme, in the places where the \n have been used.

#### The keyword arguments

Python offers another mechanism for the passing of arguments, which can be helpful when you want to convince the print() function to change its behavior a bit.

The mechanism is called *keyword arguments*. The name stems from the fact that the meaning of these arguments is taken not from its location (position) but from the special word (keyword) used to identify them.

The print() function has two keyword arguments that you can use for your purposes. The first of them is named [ _end_ ].

```
print("My name is", "Python.", end=" ")
print("Monty Python")
```

The console should now be showing the following text:
→ My name is Python. Monty Python.

In order to use it, it is necessary to know some rules:

  - a keyword argument consists of three elements: a _keyword_ identifying the argument _(end here)_; an _equal sign (=)_; and a _value_ assigned to that argument;
  - any keyword arguments have to be put *after the last positional argument* (this is very important)

#### Key takeaways

1. The print() function is a built-in function. It prints/outputs a specified message to the screen/consol window.

2. Built-in functions, contrary to user-defined functions, are always available and don't have to be imported. Python 3.8 comes with 69 built-in functions. You can find their full list provided in alphabetical order in the Python Standard Library.

3. To call a function (this process is known as function invocation or function call), you need to use the function name followed by parentheses. You can pass arguments into a function by placing them inside the parentheses. You must separate arguments with a comma, e.g., print("Hello,", "world!"). An "empty" print() function outputs an empty line to the screen.

4. Python strings are delimited with quotes, e.g., "I am a string" (double quotes), or 'I am a string, too' (single quotes).

5. Computer programs are collections of instructions. An instruction is a command to perform a specific task when executed, e.g., to print a certain message to the screen.

6. In Python strings the backslash (\) is a special character which announces that the next character has a different meaning, e.g., \n (the newline character) starts a new output line.

7. Positional arguments are the ones whose meaning is dictated by their position, e.g., the second argument is outputted after the first, the third is outputted after the second, etc.

8. Keyword arguments are the ones whose meaning is not dictated by their location, but by a special word (keyword) used to identify them.

9. The end and sep parameters can be used for formatting the output of the print() function. The sep parameter specifies the separator between the outputted arguments (e.g., print("H", "E", "L", "L", "O", sep="-"), whereas the end parameter specifies what to print at the end of the print statement.

## Variables

You already know that you can do some arithmetic operations with these numbers: add, subtract, etc. You'll be doing that many times.

But it's quite a normal question to ask how to _store the results_ of these operations, in order to use them in other operations, and so on.

How do you save the intermediate results, and use them again to produce subsequent ones?

Python will help you with that. It offers special "boxes" (containers) for that purpose, and these boxes are called *variables* - the name itself suggests that the content of these containers can be varied in (almost) any way.

What does every Python variable have?

  - a name;
  - a value (the content of the container)

Let's start with the issues related to a variable's name.

Variables do not appear in a program automatically. As developer, you must decide how many and which variables to use in your programs.

You must also name them. A variable can have a short name, but a more descriptive name is highly recommended.

If you want to _give a name to a variable_, you must follow some strict rules:

  - the name of the variable must be composed of upper-case or lower-case letters, digits, and the character _ (underscore)
  - the name of the variable must begin with a letter;
  - the underscore character is a letter;
  - upper- and lower-case letters are treated as different (a little differently than in the real world - Alice and ALICE are the same first names, but in Python they are two different variable names, and consequently, two different variables);
  - the name of the variable must not be any of Python's reserved words. 

### Correct and incorrect variable names

Note that the same restrictions apply to function names.

Python _does not impose restrictions on the length of variable names_, but that doesn't mean that a long variable name is always better than a short one.

We will use standard Python variable naming style which has been adopted by many Python developers, _snake case_(snake_case) variable naming convention. We use _underscore character_ after each word for a variable containing more than one word(eg. first_name, last_name, engine_rotation_speed).

Here are some correct, but not always convenient variable names:

MyVariable, i, t34, Exchange_Rate, counter, days_to_christmas, TheNameIsSoLongThatYouWillMakeMistakesWithIt, _.

Moreover, Python lets you use not only Latin letters but also characters specific to languages that use other alphabets.

These variable names are also correct:

Adiós_Señora, sûr_la_mer, Einbahnstraße, переменная.

And now for some incorrect names:

10t (does not begin with a letter), Exchange Rate (contains a space)

*NOTE*

The *PEP 8 -- Style Guide for Python Code* recommends the following naming convention for variables and functions in Python:

  - variable names should be lowercase, with words separated by underscores to improve readability (e.g., var, my_variable)
  - function names follow the same convention as variable names (e.g., fun, my_function)
  - it's also possible to use mixed case (e.g., myVariable), but only in contexts where that's already the prevailing style, to retain backwards compatibility with the adopted convention.

### Assigning a new value to an already existing variable

How do you assign a new value to an already created variable? In the same way. You just need to use the equal sign.

The equal sign is in fact an *assignment operator*. Although this may sound strange, the operator has a simple syntax and unambiguous interpretation.

It assigns the value of its right argument to the left, while the right argument may be an arbitrarily complex expression involving literals, operators and already defined variables.

Look at the code below:

```
var = 1
print(var) # 1
var = var + 1
print(var) # 2
```

  - The first line of the snippet creates a new variable named var and assigns 1 to it.
  -  The statement reads: assign a value of 1 to a variable named var.
  - We can say it shorter: assign 1 to var.
  - Some prefer to read such a statement as: var becomes 1.

The third line assigns the same variable with the new value taken from the variable itself, summed with 1. Seeing a record like that, a mathematician would probably protest - no value may be equal to itself plus one. This is a contradiction. But Python treats the sign = not as equal to, but as assign a value.

So how do you read such a record in the program?

Take the current value of the variable var, add 1 to it and store the result in the variable var.

In effect, the value of variable var has been incremented by one, which has nothing to do with comparing the variable with any value.

[<< Day 1](../readme.md) | [Day 3 >>](../03_Day_Operators/03_operators.md)
