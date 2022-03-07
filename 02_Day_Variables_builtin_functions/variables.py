# Variable in Python

from platform import python_version_tuple


first_name = 'Case'
last_name = 'Sprawl'
country = 'Sendai'
city = 'Chiba City Blues'
age = 43
is_machine = False
skills = ['Python', 'Linux', 'ETH']
person_info = {
    'firstname': 'Case',
    'lastname': 'Sprawl',
    'country': 'Sendai',
    'city': 'Chiba City Blues',
    'age': 43,
    'is_machine': False,
    'skills': ['Python', 'Linux', 'ETH']
    }

# Printing the values store in the variables

print('First name:', first_name)
print('First name length:', len(first_name))
print('Last name: ', last_name)
print('Last name length: ', len(last_name))
print('Country: ', country)
print('City: ', city)
print('Age: ', age)
print('Machine: ', is_machine)
print('Skills: ', skills)
print('Person information: ', person_info)

# Declaring multiple variables in one line

first_name, last_name, country, age, is_machine = 'Case', 'Sprawl', 'Sendai', 43, False

print(first_name, last_name, country, age, is_machine)
print('First name:', first_name)
print('Last name: ', last_name)
print('Country: ', country)
print('Age: ', age)
print('Machine: ', is_machine)