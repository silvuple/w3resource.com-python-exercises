"""
1. Write a Python program to calculate the length of a string
"""

my_string = input("enter a string ")

# solution 1:
print(len(my_string))

# solution 2:
length = 0
for letter in my_string:
    length += 1

print(length)

"""
2. Write a Python program to count the number of characters
(character frequency) in a string. 
Sample String : 'google.com'
Expected Result : {'o': 3, 'g': 2, '.': 1, 'e': 1, 'l': 1, 'm': 1, 'c': 1}
"""

my_string = input("enter a string ")

# solution 1:
my_dict = {}
for letter in my_string:
    my_dict[letter] = my_string.count(letter)
print(my_dict)

# solution 2:
my_dict = {}
for letter in my_string:
    my_dict[letter] = 0

for letter in my_string:
    my_dict[letter] += 1
print(my_dict)

# solution 3:
my_dict = {}
for letter in my_string:
    if letter in my_dict:
        my_dict[letter] += 1
    else:
        my_dict[letter] = 1
print(my_dict)

"""
3. Write a Python program to get a string made of the first 2
and the last 2 chars from a given string.
If the string length is less than 2, return 'empty string'.
Sample String : 'w3resource'
Expected Result : 'w3ce'
Sample String : 'w3'
Expected Result : 'w3w3'
Sample String : ' w'
Expected Result : Empty String
"""

my_string = input("enter a string ")

# solution 1
if len(my_string) > 1:
    print(my_string[:2]+my_string[-2:])
else:
    print('empty string')

"""
4. Write a Python program to get a string from a given string
where all occurrences of its first char have been changed to '$',
except the first char itself. 
Sample String : 'restart'
Expected Result : 'resta$t'
"""

my_string = input("enter a string ")

# solution 1
new_string = my_string[0]
for i in range(1, len(my_string)):
    if my_string[i] == my_string[0]:
        new_string += '$'
    else:
        new_string += my_string[i]
print(new_string)

# solution 2
new_string = ''
for letter in my_string:
    if letter == my_string[0]:
        new_string += '$'
    else:
        new_string += letter
my_list = list(new_string)
my_list[0] = my_string[0]
new_string = ''.join(my_list)
print(new_string)

# solution 3
first_letter = my_string[0]
helper_string = my_string.replace(first_letter, '$')
new_string = first_letter + helper_string[1:]
print(new_string)

"""
5. Write a Python program to get a single string from two given strings,
separated by a space and swap the first two characters of each string. 
Sample String : 'abc', 'xyz' 
Expected Result : 'xyc abz'
"""

string_one = input("enter first string ")
string_two = input("enter second string ")

# solution 1
new_string = string_two[:2]+string_one[2:]+' '+string_one[:2]+string_two[2:]
print(new_string)

"""
6. Write a Python program to add 'ing' at the end of a given string
(length should be at least 3). If the given string already ends with 'ing'
then add 'ly' instead. If the string length of the given string is less
than 3, leave it unchanged.  
Sample String : 'abc'
Expected Result : 'abcing' 
Sample String : 'string'
Expected Result : 'stringly'
"""

my_string = input("enter a string ")

# solution 1
if len(my_string) < 3:
    new_string = my_string
elif my_string[-3:] == 'ing':
    new_string = my_string + 'ly'
else:
    new_string = my_string + 'ing'
print (new_string)

"""
7. Write a Python program to find the first appearance of the substring
'not' and 'poor' from a given string, if 'poor' follows the 'not', replace
the whole 'not'...'poor' substring with 'good'. Return the resulting string.
Sample String : 'The lyrics is not that poor!'
Expected Result : 'The lyrics is good!'
"""

my_string = input("enter a string ")

# solution 1
not_position = my_string.find('not')
poor_position = my_string.find('poor')

if not_position < poor_position and not_position != -1:
    new_string = my_string[:not_position] + 'good' + my_string[poor_position+4:]
else:
    new_string = my_string

print(new_string)

# solution 2
not_pos = my_string.find('not')
poor_pos = my_string.find('poor')

if not_pos < poor_pos and not_pos != -1:
    new_string = my_string.replace(my_string[not_pos:(poor_pos+4)], 'good')
else:
    new_string = my_string

print(new_string)

"""
8. Write a Python function that takes a list of words and returns
the length of the longest one.
"""

my_words = input("enter a few words ")

# solution 1
my_list = my_words.split()

max_len = 0
for word in my_list:
    if len(word) > max_len:
        max_len = len(word)

print(max_len)

# solution 2
my_list = my_words.split()
len_list = []
for word in my_list:
    len_list.append(len(word))

len_list.sort()
max_len = len_list[-1]
print(max_len)

"""
9. Write a Python program to remove the nth index character
from a nonempty string.
"""

# solution 1
my_string = input("enter a string ")
n = int(input("enter a number "))
new_string = my_string[:n-1] + my_string[n:]
print(new_string)

"""
10. Write a Python program to change a given string to a new string
where the first and last chars have been exchanged.
"""

my_string = input("enter a string ")

# soltuion 1
new_string = my_string[-1] + my_string[1:-1] + my_string[0]
print(new_string)

"""
11. Write a Python program to remove the characters
which have odd index values of a given string.
"""

my_string = input("enter a string ")

# solution 1
my_list = [my_string[x] for x in range(len(my_string)) if x%2 == 0]
new_string = ''.join(my_list)
print(new_string)

# solution 2
new_string = ''
for i in range(len(my_string)):
    if i%2 == 0:
        new_string += my_string[i]
print(new_string)

"""
12. Write a Python program to count the occurrences of each word
in a given sentence.
"""

my_string = input("enter a sentence ")

# solution 1
my_list = my_string.split()
my_set = set(my_list)
my_dict = {}
for word in my_set:
    my_dict[word] = my_string.count(word)
print(my_dict)

# solution 2
my_list = my_string.split()
my_set = set(my_list)
my_dict = {}
for word in my_set:
    my_dict[word] = 0
    for item in my_list:
        if word == item:
            my_dict[word] += 1
print(my_dict)

# solution 3
my_list = my_string.split()
my_dict = {}
for word in my_list:
    if word in my_dict:
        my_dict[word] += 1
    else:
        my_dict[word] = 1
print(my_dict)
    
"""
13. Write a Python script that takes input from the user
and displays that input back in upper and lower cases.
"""

my_string = input("enter something ")

print(my_string.upper())
print(my_string.lower())

"""
14. Write a Python program that accepts a comma separated sequence of words
as input and prints the unique words in sorted form (alphanumerically). 
Sample Words : red, white, black, red, green, black
Expected Result : black, green, red, white,red
"""

my_string = input("enter words ")
my_set = sorted(set(my_string.split(',')))
print(','.join(my_set))

"""
15. Write a Python function to create the HTML string with tags around the word(s).
Sample function and result : 
add_tags('i', 'Python') -> '<i>Python</i>'
add_tags('b', 'Python Tutorial') -> '<b>Python Tutorial </b>'
"""

# solution 1
def add_tags(tag, text):
    return "<"+tag+">"+text+"<"+tag+">"

print(add_tags('i', 'Python'))
print(add_tags('b', 'Python Tutorial'))

# solution 2
def add_tags(tag, text):
    return "<%s>%s<%s>" % (tag, text, tag)

print(add_tags('i', 'Python'))
print(add_tags('b', 'Python Tutorial'))

"""
16. Write a Python function to insert a string in the middle of a string. 
Sample function and result : 
insert_sting_middle('[[]]', 'Python') -> [[Python]]
insert_sting_middle('{{}}', 'PHP') -> {{PHP}}
"""

def insert_sting_middle(main_string, middle_string):
    main_len = len(main_string)
    middle = int(main_len/2)
    return main_string[:middle] + middle_string + main_string[middle:]

print(insert_sting_middle('[[]]', 'Python'))
print(insert_sting_middle('{{}}', 'PHP'))
print(insert_sting_middle('<<>>', 'HTML'))

"""
17. Write a Python function to get a string made of 4 copies of the
last two characters of a specified string (length must be at least 2). 
Sample function and result : 
insert_end('Python') -> onononon
insert_end('Exercises') -> eseseses
"""

def insert_end(my_string):
    return my_string[-2:] * 4

print(insert_end('Python'))
print(insert_end('Exercises'))

"""
18. Write a Python function to get a string made of its first three
characters of a specified string. If the length of the string is less
than 3 then return the original string. 
Sample function and result : 
first_three('ipy') -> ipy
first_three('python') -> pyt
"""

def first_three(my_string):
    if len(my_string) > 2:
        return my_string[:3]
    else:
        return my_string
print(first_three('ipy'))
print(first_three('python'))

"""
19. Write a Python program to get the last part of a string
before a specified character. 
https://www.w3resource.com/python-exercises
https://www.w3resource.com/python
"""

# solution 1
def get_last_part(my_string, char):
    position = my_string.rfind(char)
    return my_string[:position]

print(get_last_part('https://www.w3resource.com/python', "/"))

# solution 2
def get_last_part(my_string, char):
    my_list = my_string.split(char)
    return char.join(my_list[:-1])

print(get_last_part('https://www.w3resource.com/python', "/"))

"""
20. Write a Python function to reverses a string if it's length is a multiple of 4.
"""

# solution 1
def reverse_string(my_string):
    if len(my_string)%4 == 0:
        my_list = list(my_string)
        my_list.reverse()
        return ''.join(my_list)
    else:
        return my_string

my_string = input("enter a string ")
print(reverse_string(my_string))

# solution 2
def reverse_string(my_string):
    if len(my_string)%4 == 0:
        return ''.join(reversed(my_string))
    else:
        return my_string

my_string = input("enter a string ")
print(reverse_string(my_string))

"""
21. Write a Python function to convert a given string to all uppercase
if it contains at least 2 uppercase characters in the first 4 characters.
"""

def to_upper(my_string):
    counter = 0
    for i in my_string[:4]:
        if i.isupper():
            counter += 1
    if counter > 1:
        return my_string.upper()
    else:
        return my_string

my_string = input("enter a string ")
print(to_upper(my_string))

"""
22.Write a Python program to sort a string lexicographically.
"""

my_string = input("enter a string ")
print(''.join(sorted(my_string, key=str.lower)))

"""
24. Write a Python program to check whether a string starts with specified characters.
"""

def starts_with(my_string, char):
    if my_string.startswith(char):
        return True
    else:
        return False

my_string = input("enter a string ")
my_char = input("enter a character ")

print("does the string '%s' starts with the character '%s'?" % (my_string, my_char))
print(starts_with(my_string, my_char))

"""
25. Write a Python program to create a Caesar encryption. 
Note : In cryptography, a Caesar cipher, also known as Caesar's cipher,
the shift cipher, Caesar's code or Caesar shift, is one of the simplest
and most widely known encryption techniques. It is a type of substitution
cipher in which each letter in the plaintext is replaced by a letter some
fixed number of positions down the alphabet. For example, with a left shift of 3,
D would be replaced by A, E would become B, and so on. The method is named
after Julius Caesar, who used it in his private correspondence.
"""

def Caesar_encryption(my_string, my_shift, my_side):
    # for decription need to use negative shift(step) or same shift opposite side
    step = my_shift
    shift_side = my_side
    new_string = ''
    for letter in my_string:
        letter_ord = ord(letter)
        if letter.islower():
            if shift_side == 'left':
                if (letter_ord-step) < ord('a'):
                    letter_ord += 26
                new_string += chr(letter_ord-step)
            elif shift_side == 'right':
                if (letter_ord+step) > ord('z'):
                    letter_ord -= 26
                new_string += chr(letter_ord+step)
        if letter.isupper():
            if shift_side == 'left':
                if (letter_ord-step) < ord('A'):
                    letter_ord += 26
                new_string += chr(letter_ord-step)
            elif shift_side == 'right':
                if (letter_ord+step) > ord('Z'):
                    letter_ord -= 26
                new_string += chr(letter_ord+step)
    return new_string

my_string = input("enter a string ")
my_shift = int(input("enter shift number "))
my_side = input("enter 'left' for left shift or 'right' for right shift ")
print("encrepted string is", Caesar_encryption(my_string, my_shift, my_side))

"""
30. Write a Python program to print the following floating numbers
upto 2 decimal places.
"""

my_float = float(input("enter a float number "))

# solution 1
print("this is a float number %.2f" % my_float)

# solution 2
print("this is a float number {:.2f}".format(my_float))

"""
31. Write a Python program to print the following floating numbers
upto 2 decimal places with a sign.
"""

my_float = float(input("enter a float number "))

# solution 1
print("this is a float number %+.2f" % my_float)

# solution 2
print("this is a float number {:+.2f}".format(my_float))

"""
32. Write a Python program to print the following floating numbers
with no decimal places.
"""

my_float = float(input("enter a float number "))

# solution 1
print("this is a float number %.0f" % my_float)

# solution 2
print("this is a float number {:.0f}".format(my_float))

"""
33. Write a Python program to print the following integers with zeros
on the left of specified width.
"""

my_string = input("enter an integer ")

# solution 1
print(my_string.zfill(5))

# solution 2
print('{:0>5s}'.format(my_string))

"""
34. Write a Python program to print the following integers with '*'
on the right of specified width.
"""

my_string = input("enter an integer ")

print('{:*<5s}'.format(my_string))

"""
35. Write a Python program to display a number with a comma separator.
"""

my_int = int(input("enter a number "))

print('{:,}'.format(my_int))

"""
36. Write a Python program to format a number with a percentage
"""

my_num = float(input("enter a number "))

print('{:.2%}'.format(my_num))

"""
37. Write a Python program to display a number in left,
right and center aligned of width 10.
"""

my_num = float(input("enter a number "))

print('{:<10}'.format(my_num))
print('{:>10}'.format(my_num))
print('{:^10}'.format(my_num))

"""
38. Write a Python program to count occurrences of a substring in a string.
"""

my_string = input("enter a string ")
my_substring = input("enter a substring ")

print("'%s' occures in '%s' %d times" % (my_substring, my_string, my_string.count(my_substring)))

"""
39. Write a Python program to reverse a string.
"""

my_string = input("enter a string ")

# solution 1
my_list = list(my_string)
my_list.reverse()
print(''.join(my_list))

# solution 2
print(''.join(reversed(my_string)))

"""
40. Write a Python program to reverse words order in a string.
"""

my_sentence = input("enter a sentence ")

my_list = my_sentence.split()
print(' '.join(my_list[::-1]))

"""
41. Write a Python program to strip a set of characters from a string.
"""

my_string = input("enter a website domain ")

# solution 1
print(my_string.strip('wcom.'))

# solution 2
my_list = [x for x in my_string if x not in 'wcom.']
##print(''.join(my_list))

"""
42. Write apython program to count repeated characters in a string. 
Sample string: 'thequickbrownfoxjumpsoverthelazydog'
Expected output :
o 4
e 3
u 2
h 2
r 2
t 2
"""

my_string = input("enter a string ")

# solution 1
my_list = []
for letter in my_string:
    my_list.append((letter, my_string.count(letter)))
my_unique_list = list(set(my_list))
for i in my_unique_list:
    print(i[0], i[1])

print('*' * 10)

# solution 2
my_dict = {}
for letter in my_string:
    if letter in my_dict:
        my_dict[letter] += 1
    else:
        my_dict[letter] = 1
for key, value in my_dict.items():
    print(key, value)

"""
43. Write a Python program to print the square and cube symbol
in the area of a rectangle and volume of a cylinder. 
Sample output: 
The area of the rectangle is 1256.66cm2
The volume of the cylinder is 1254.725cm3
"""

from math import pi

def rectangle_area(length, width):
    return length*width

def cylinder_volume(r, height):
    return pi*r*r*height

# solution 1 using unicode superscript
print('The area of the rectangle is %.2f cm\u00B2' % rectangle_area(5.5, 7))
print('The volume of the cylinder is %.2f cm\u00B3' % cylinder_volume(5.5, 7))

"""
44. Write a Python program to print the index of the character in a string. 
Sample string: w3resource
Expected output:
Current character w position at 0
Current character 3 position at 1
Current character r position at 2
- - - - - - - - - - - - - - - - - - - - - - - - -
Current character c position at 8
Current character e position at 9
"""

my_string = 'w3resource'

for i, v in enumerate(my_string):
    print("Current character %s position at %d" % (v,i))

"""
45. Write a Python program to check if a string contains all letters
of the alphabet.
"""
import string
my_string = input("enter a string ")

# solution 1
alphabet = 'abcdefghijklmnopqrstuvwxyz'
counter = 0
for letter in alphabet:
    if letter in my_string.lower():
        counter += 1
    else:
        break
if counter == 26:
    print('the string contains all the letters of the alphabet')
else:
    print('the string DOES NOT contain all the letters of the alphabet')

# solution 2
string_letters = ''.join(sorted(set(my_string.lower())))
print(string_letters)
if string.ascii_lowercase == string_letters:
    print('the string contains all the letters of the alphabet')
else:
    print('the string DOES NOT contain all the letters of the alphabet')
    
"""
47. Write a Python program to lowercase first n characters in a string.
"""

my_string = input('enter a string ')
n = 3
print(my_string[:n].lower()+my_string[n:])

"""
48. Write a Python program to swap comma and dot in a string. Go to the editor
Sample string: "32.054,23"
Expected Output: "32,054.23"
"""

# solution 1
my_string = '32.054,23'
print(my_string)
my_list = my_string.split('.')
new_list = []
for i in my_list:
    new_list.append(i.replace(',','.'))
new_string = ','.join(new_list)
print(new_string)

# solution 2
my_string = '32.054,23'
print(my_string)
swap = str.maketrans(',.', '.,')
new_string = my_string.translate(swap)
print(new_string)

"""
49. Write a Python program to count and display the vowels of a given text.
"""

my_string = input("enter a text ")

# solution 1
vowels = 'aeiouy'
my_dict = {}
for i in vowels:
    my_dict[i] = 0
for i in my_string.lower():
    if i in vowels:
        my_dict[i] += 1
print(my_dict)

# solution 2
vowels = 'aeiouy'
my_string = my_string.lower()
my_list = [(x, my_string.count(x)) for x in my_string if x in vowels]
print(set(my_list))

"""
50. Write a Python program to split a string on the last occurrence
of the delimiter.
"""

my_string = 'this is some text with space as a delimeter'
print(my_string.rsplit(maxsplit=1))
