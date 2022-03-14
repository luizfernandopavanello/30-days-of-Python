<div align="center">
  <h1> 30 Days Of Python: Day 8 - Dictionaries</h1>
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

[<< Day 7 ](../07_Day_Sets/07_sets.md) | [Day 9 >>](../09_Day_Conditionals/09_conditionals.md)

<img src="../Images/python_TreviIT.png" alt="30 Days of Python">
</div>

- [📘 Day 8](#-day-8)
  - [Dictionaries](#dictionaries)
    - [Creating a Dictionary](#creating-a-dictionary)
    - [Dictionary Length](#dictionary-length)
    - [Accessing Dictionary Items](#accessing-dictionary-items)
    - [Adding Items to a Dictionary](#adding-items-to-a-dictionary)
    - [Modifying Items in a Dictionary](#modifying-items-in-a-dictionary)
    - [Checking Keys in a Dictionary](#checking-keys-in-a-dictionary)
    - [Removing Key and Value Pairs from a Dictionary](#removing-key-and-value-pairs-from-a-dictionary)
    - [Changing Dictionary to a List of Items](#changing-dictionary-to-a-list-of-items)
    - [Clearing a Dictionary](#clearing-a-dictionary)
    - [Deleting a Dictionary](#deleting-a-dictionary)
    - [Copy a Dictionary](#copy-a-dictionary)
    - [Getting Dictionary Keys as a List](#getting-dictionary-keys-as-a-list)
    - [Getting Dictionary Values as a List](#getting-dictionary-values-as-a-list)
    
# 📘 Day 8

## Dictionaries

A dictionary is a collection of unordered, modifiable(mutable) paired (key: value) data type. It's _not a sequence_ type, but can be easily adapted to sequence processing.

To explain what the Python dictionary actually is, it is important to understand it is literally a dictionary.

The Python dictionary works in the same way as a bilingual dictionary. For example, you have an English word (e.g., dog) and need its Portuguese equivalent. You browse the dictionary in order to find the word and eventually you get it ( use your technique to do that - it doesn't matter, really). Next, you check the Portuguese counterpart and it is (most probably) the word "cachorro".

In Python's world, the word you _look for_ is named a *key*. The word you _get_ from the dictionary is called a *value*.

This means that a dictionary is a set of _key-value_ pairs. Note:

  - each *key* must be *unique* - it's not possible to have more than one key of the same value;
  - a key may be _any immutable type of object_: it can be a number (integer or float), or even a string, but not a list;
  - a dictionary is not a list - a list contains a set of numbered values, while a _dictionary holds pairs of values_;
  - the _len()_ function works for dictionaries, too - it returns the numbers of key-value elements in the dictionary;
  - a dictionary is a _one-way tool_ - if you have an English-Portuguese dictionary, you can look for Portuguese equivalents of English terms, but not vice versa.

### Creating a Dictionary

To create a dictionary we use curly brackets, {} or the *dict()* built-in function.

```py
# syntax
empty_dict = {}
# Dictionary with data values
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
```

**Example:**

```py
person = {
    'first_name':'Case',
    'last_name':'Sprawl',
    'age':250,
    'country':'Chiba City Blues',
    'is_machine':False,
    'skills':['Python', 'Linux', 'Cyber Security'],
    'address':{
        'street':'Jules Verne Street',
        'code':'L-5'
    }
}
```

The dictionary above shows that a value could be any data types:string, boolean, list, tuple, set or a dictionary.

### Dictionary Length

It checks the number of 'key: value' pairs in the dictionary.

```py
# syntax
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
print(len(dct)) # 4
```

**Example:**

```py
person = {
    'first_name':'Case',
    'last_name':'Sprawl',
    'age':250,
    'country':'Chiba City Blues',
    'is_machine':False,
    'skills':['Python', 'Linux', 'Cyber Security'],
    'address':{
        'street':'Jules Verne Street',
        'code':'L-5'
    }
}
print(len(person)) # 7
```

### Accessing Dictionary Items

We can access Dictionary items by referring to its key name.

```py
# syntax
dct = {'key1':'value1', 'key2': 'value2', 'key3':'value3', 'key4': 'value4'}
print(dct['key3']) # value3
print(dct['key2']) # value2
```

**Example:**

```py
person = {
    'first_name':'Case',
    'last_name':'Sprawl',
    'age':40,
    'country':'Chiba City Blues',
    'is_machine':False,
    'skills':['Python', 'Linux', 'Cyber Security'],
    'address':{
        'street':'Jules Verne Street',
        'code':'L-5'
    }
}

print(person['first_name']) # Case
print(person['last_name']) # Sprawl 
print(person['age']) # 40
print(person['skills']) # ['Python', 'Linux', 'Cyber Security']
print(person['skills'][0]) # Python
print(person['city']) # Error
```

Accessing an item by key name raises an error if the key does not exist. To avoid this error first we have to check if a key exist or we can use the _get_ method. The get method returns None, which is a NoneType object data type, if the key does not exist.

```py
person = {
    'first_name':'Case',
    'last_name':'Sprawl',
    'age':40,
    'country':'Chiba City Blues',
    'is_machine':False,
    'skills':['Python', 'Linux', 'Cyber Security'],
    'address':{
        'street':'Jules Verne Street',
        'code':'L-5'
    }
}

print(person.get['first_name']) # Case
print(person.get['last_name']) # Sprawl 
print(person.get['age']) # 40
print(person.get['skills']) # ['Python', 'Linux', 'Cyber Security']
print(person.get['skills'][0]) # Python
print(person.get['city']) # None
```

### Adding Items to a Dictionary

We can add new key and value pairs to a dictionary

```py
# syntax
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
dct['key5'] = 'value5'
```

**Example:**

```py
person = {
    'first_name':'Case',
    'last_name':'Sprawl',
    'age':250,
    'country':'Chiba City Blues',
    'is_machine':False,
    'skills':['Python', 'Linux', 'Cyber Security'],
    'address':{
        'street':'Jules Verne Street',
        'code':'L-5'
    }
}

person['job_title'] = 'Linux Administrator'
person['skills'].append('JavaScript')
print(person)
```

### Modifying Items in a Dictionary

We can modify itens in a dictionary. Just remember, we can only have *one* key, is unique.

```py
# syntax
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
dct['key1'] = 'value-one'

print(dct['key1']) # value-one
```

### Checking Keys in a Dictionary

We use the _in_ operator to check if a key exist in a dictionary

```py
# syntax
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
print('key2' in dct) # True
print('key5' in dct) # False
```

### Removing Key and Value Pairs from a Dictionary

- _pop(key)_: removes the item with the specified key name:
- _popitem()_: removes the last item
- _del_: removes an item with specified key name

```py
# syntax
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
dct.pop('key1') # removes key1 item
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
dct.popitem() # removes the last item
del dct['key2'] # removes key2 item
```

### Changing Dictionary to a List of Items

The _items()_ method changes dictionary to a list of tuples.

```py
# syntax
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
print(dct.items()) # dict_items([('key1', 'value1'), ('key2', 'value2'), ('key3', 'value3'), ('key4', 'value4')])
```

### Clearing a Dictionary

If we don't want the items in a dictionary we can clear them using _clear()_ method

```py
# syntax
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
print(dct.clear()) # None
```

### Deleting a Dictionary

If we do not use the dictionary we can delete it completely

```py
# syntax
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
del dct
```

### Copy a Dictionary

We can copy a dictionary using a _copy()_ method. Using copy we can avoid mutation of the original dictionary.

```py
# syntax
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
dct_copy = dct.copy() # {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
```

### Getting Dictionary Keys as a List

The _keys()_ method gives us all the keys of a a dictionary as a list.

```py
# syntax
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
keys = dct.keys()
print(keys)     # dict_keys(['key1', 'key2', 'key3', 'key4'])
```

### Getting Dictionary Values as a List

The _values_ method gives us all the values of a a dictionary as a list.

```py
# syntax
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
values = dct.values()
print(values)     # dict_values(['value1', 'value2', 'value3', 'value4'])
```

[<< Day 7 ](../07_Day_Sets/07_sets.md) | [Day 9 >>](../09_Day_Conditionals/09_conditionals.md)