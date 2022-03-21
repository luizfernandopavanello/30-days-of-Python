'''
### Exercises

1. Writ a function which generates a six digit/character random_user_id.
   ```py
     print(random_user_id());
     '1ee33d'
   ```
'''
import random

def random_user_id():
    return ''.join(random.choices('0123456789abcdef', k=6))
# The choices() method returns a list with the randomly selected element from the specified sequence.
# k 	Optional. An integer defining the length of the returned list

print(random_user_id()) 

'''
2. Modify the previous task. Declare a function named user_id_gen_by_user. It doesn’t take any parameters but it takes two inputs using input(). One of the inputs is the number of characters and the second input is the number of IDs which are supposed to be generated.
   
```py
print(user_id_gen_by_user()) # user input: 5 5
#output:
#kcsy2
#SMFYb
#bWmeq
#ZXOYh
#2Rgxf
   
print(user_id_gen_by_user()) # 16 5
#1GCSgPLMaBAVQZ26
#YD7eFwNQKNs7qXaT
#ycArC5yrRupyG00S
#UbGxOFI7UXSWAyKN
#dIV0SSUTgAdKwStr
```
'''
def user_id_user():
    num_char = int(input('Enter number of characters: '))
    num_id = int(input('Enter number of IDs: '))
    for i in range(num_id):
        print(''.join(random.choices('0123456789abcdef', k=num_char)))

'''
3. Write a function named rgb_color_gen. It will generate rgb colors (3 values ranging from 0 to 255 each).
   
```py
print(rgb_color_gen())
# rgb(125,244,255) - the output should be in this form
```
'''
def rgb_color_gen():
    return f'rgb({random.randint(0,255)},{random.randint(0,255)},{random.randint(0,255)})'

'''
4. Write a function list_of_hexa_colors which returns any number of hexadecimal colors in an array (six hexadecimal numbers written after #. Hexadecimal numeral system is made out of 16 symbols, 0-9 and first 6 letters of the alphabet, a-f. Check the task 6 for output examples).
1. Write a function list_of_rgb_colors which returns any number of RGB colors in an array.
1. Write a function generate_colors which can generate any number of hexa or rgb colors.

```py
   generate_colors('hexa', 3) # ['#a3e12f','#03ed55','#eb3d2b'] 
   generate_colors('hexa', 1) # ['#b334ef']
   generate_colors('rgb', 3)  # ['rgb(5, 55, 175','rgb(50, 105, 100','rgb(15, 26, 80'] 
   generate_colors('rgb', 1)  # ['rgb(33,79, 176)']
   ```
'''
def list_of_hexa_colors(num_colors):
    return [f'#{random.choices("0123456789abcdef", k=6)}' for i in range(num_colors)]

def list_of_rgb_colors(num_colors):
    return [f'rgb({random.randint(0,255)},{random.randint(0,255)},{random.randint(0,255)})' for i in range(num_colors)]

def generate_colors():
    num_colors = int(input('Enter number of colors: '))
    color_type = input('Enter color type (hexa or rgb): ')
    if color_type == 'hexa':
        return list_of_hexa_colors(num_colors)
    elif color_type == 'rgb':
        return list_of_rgb_colors(num_colors)
    else:
        print('Invalid color type')
