'''Exercises:

```py
countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
names = ['Case', 'Moli', 'James', 'Gibson']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
```
'''

for c in countries:
   print(c)

countries_list = list(map(str,countries))
print(countries_list)

def country_long(countries):
    if len(countries) > 6:
        return True
    return False

country_long_name = filter(country_long, countries)
print(list(country_long_name))  


for name in names:
   print(name)

names_list = list(map(str.upper, names))
print(names_list)


for number in numbers:
   print(number)

number_list = list(map(int, numbers))
print(number_list)

from functools import reduce

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

result = reduce(lambda x, y: x + y, numbers)
print(result)

