'''
Exercises: 

1. Filter only negative and zero in the list using list comprehension
   ```py
   numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
   ```
'''
filter_list = [x for x in numbers if x <= 0]

'''
2. Flatten the following list of lists of lists to a one dimensional list :

   ```py
   list_of_lists =[[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]

   output
   [1, 2, 3, 4, 5, 6, 7, 8, 9]
   ```
'''
flatten = [item for sublist in list_of_lists for item in sublist]

'''
3. Using list comprehension create the following list of tuples:
   ```py
   [(0, 1, 0, 0, 0, 0, 0),
   (1, 1, 1, 1, 1, 1, 1),
   (2, 1, 2, 4, 8, 16, 32),
   (3, 1, 3, 9, 27, 81, 243),
   (4, 1, 4, 16, 64, 256, 1024),
   (5, 1, 5, 25, 125, 625, 3125),
   (6, 1, 6, 36, 216, 1296, 7776),
   (7, 1, 7, 49, 343, 2401, 16807),
   (8, 1, 8, 64, 512, 4096, 32768),
   (9, 1, 9, 81, 729, 6561, 59049),
   (10, 1, 10, 100, 1000, 10000, 100000)]
   ```
'''
list_of_tuples = [(x, x ** 0, x ** 1, x ** 2, x ** 3, x ** 4, x ** 5) for x in range(11)]

'''   
4. Flatten the following list to a new list:
   ```py
   countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
   output:
   [['FINLAND','FIN', 'HELSINKI'], ['SWEDEN', 'SWE', 'STOCKHOLM'], ['NORWAY', 'NOR', 'OSLO']]
   ```
'''
new_list = [country[0][0].upper() + country[0][1].upper() for country in countries]

'''
5. Change the following list to a list of dictionaries:
   ```py
   countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
   output:
   [{'country': 'FINLAND', 'city': 'HELSINKI'},
   {'country': 'SWEDEN', 'city': 'STOCKHOLM'},
   {'country': 'NORWAY', 'city': 'OSLO'}]
   ```
'''
'''
6. Change the following list of lists to a list of concatenated strings:
   ```py
   names = [[('Case', 'Sprawl')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
   output
   ['Case Sprawl', 'David Smith', 'Donald Trump', 'Bill Gates']
   ```
'''
new_list_names = [name[0][0] + ' '+ name[0][1] for name in names]
