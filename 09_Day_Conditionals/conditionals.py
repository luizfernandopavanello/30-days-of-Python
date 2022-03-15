'''
1.  Get user input using input(“Enter your age: ”). If user is 18 or older, give feedback: You are old enough to drive. If below 18 give feedback to wait for the missing amount of years. Output:
    ```sh
    Enter your age: 30
    You are old enough to learn to drive.
    Output:
    Enter your age: 15
    You need 3 more years to learn to drive.
    ```
'''
# age = int(input("Enter your age: "))

# def drive():
#     if age >= 18:
#         return("You are old enough to drive.")
#     else:
#         return(f"You need {18 - age} more years to drive.")

# print(drive())

'''
2.  Compare the values of my_age and your_age using if … else. Who is older (me or you)? Use input(“Enter your age: ”) to get the age as input. You can use a nested condition to print 'year' for 1 year difference in age, 'years' for bigger differences, and a custom text if my_age = your_age. Output:
    ```sh
    Enter your age: 30
    You are 5 years older than me.
    ```
'''
# my_age = int(input("Enter my age: "))
# your_age = int(input("Enter your age: "))

# def age():
#     if my_age > your_age:
#         return(f"You are {my_age - your_age} years older than me.")
#     elif my_age < your_age:
#         return(f"I am {your_age - my_age} years older than you.")
#     else:
#         return("Yeah buddy, we have the same age.")

# print(age())

'''
3. Write a code which gives grade to students according to theirs scores:
   
        ```sh
        80-100, A
        70-89, B
        60-69, C
        50-59, D
        0-49, F
        ```
'''
# def grades():
#     score = int(input("Enter your score: "))
#     if score >= 80:
#         return("A")
#     elif score >= 70:
#         return("B")
#     elif score >= 60:
#         return("C")
#     elif score >= 50:
#         return("D")
#     else:
#         return("F")

# print(grades())

'''
4.  The following list contains some fruits:
    ```sh
    fruits = ['banana', 'orange', 'mango', 'lemon']
    ```
    If a fruit doesn't exist in the list add the fruit to the list and print the modified list. If the fruit exists print('That fruit already exist in the list') 
'''
# fruits = ['banana', 'orange', 'mango', 'lemon']

# def list_fruits():
#     fruit = input("Enter a fruit: ")
#     if fruit not in fruits:
#         fruits.append(fruit)
#         return(sorted(fruits))
#     else:
#         return(f"That fruit already exist in the list → {fruits}")
        
# print(list_fruits())

'''
5. Here we have a person dictionary. Feel free to modify it!
   
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

     * Check if the person dictionary has skills key, if so print out the middle skill in the skills list.
     * Check if the person dictionary has skills key, if so check if the person has 'Python' skill and print out the result.
     * If the person is a machine and if he lives in Chiba City Blue, print the information in the following format:

```py
    Case Sprawl lives in Chiba City Blue. He is  not a machine.
```
'''

person = {
    'first_name':'Case',
    'last_name':'Sprawl',
    'age':250,
    'country':'Chiba City Blues',
    'is_machine': False,
    'skills':['Python', 'Linux', 'Cyber Security'],
    'address':{
        'street':'Jules Verne Street',
        'code':'L-5'
    }
}

def middle_skill():
    if 'skills' in person:
        return person['skills']

def has_python():
    if 'skills' in person:
        if 'Python' in person['skills']:
            return True
        else:
            return False


def machine_chiba():
    if person['is_machine'] and person['country'] == 'Chiba City Blues':
        return(f"{person['first_name']} {person['last_name']} lives in {person['country']}. He is a machine.")
    else:
        return(f"{person['first_name']} {person['last_name']} lives in {person['country']}. He is not a machine.")               

   
print(middle_skill())
print(has_python())
print(machine_chiba())