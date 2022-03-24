'''
The Numbers Processor

The third program shows a simple method allowing you to input a line filled with numbers, and to process them easily. Note: the routine input() function, combined together with the int() or float() functions, is unsuitable for this purpose.

The processing will be extremely easy - we want the numbers to be summed.

Look at the code in the editor. Let's analyze it.

Using list comprehension may make the code slimmer. You can do that if you want.

Let's present our version:

    line 03: ask the user to enter a line filled with any number of numbers (the numbers can be floats)
    line 04: split the line receiving a list of substrings;
    line 05: initiate the total sum to zero;
    line 06: as the string-float conversion may raise an exception, it's best to continue with the protection of the try-except block;
    line 07: iterate through the list...
    line 08: ...and try to convert all its elements into float numbers; if it works, increase the sum;
    line 09: everything is good so far, so print the sum;
    line 10: the program ends here in the case of an error;
    line 11: print a diagnostic message showing the user the reason for the failure.

The code has one important weakness - it displays a bogus result when the user enters an empty line. Can you fix it?
'''

# Numbers Processor.

line = input("Enter a line of numbers - separate them with spaces: ")
strings = line.split()
total = 0
try:
    for substr in strings:
        total += float(substr)
    print("The total is:", total)
except:
    print(substr, "is not a number.")