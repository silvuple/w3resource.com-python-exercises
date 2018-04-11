"""
1. Write a Python program to check that a string contains only a certain set of
characters (in this case a-z, A-Z and 0-9).
"""
import re
my_string = input('enter a string: ')
p = re.compile('[^0-9A-Za-z ]+')
m = p.search(my_string)
if m:
    print('the sting contains', m.group(), 'at place', m.start())
else:
    print('the string contains only digits 0-9 and letters of english alphabet')

"""
2. Write a Python program that matches a string that has an 'a' followed by zero
or more b's.
"""

import re
my_string = input('enter a string ')
p = re.compile('ab*?')
m = p.search(my_string)
if m:
    print('it\'s a match')
else:
    print('no match found')

"""
3. Write a Python program that matches a string that has an 'a' followed by
one or more b's.
"""

import re
my_string = input('enter a string ')
p = re.compile('ab+?')
m = p.search(my_string)
if m:
    print('it\'s a match')
else:
    print('no match found')

"""
4. Write a Python program that matches a string that has an 'a' followed by
zero or one 'b'.
"""

import re
my_string = input('enter a string ')
p = re.compile('ab??')
m = p.search(my_string)
if m:
    print('it\'s a match')
else:
    print('no match found')

"""
5. Write a Python program that matches a string that has an 'a' followed by
three 'b'.
"""

import re
my_string = input('enter a string ')
p = re.compile('ab{3}?')
m = p.search(my_string)
if m:
    print('it\'s a match')
else:
    print('no match found')

"""
6. Write a Python program that matches a string that has an 'a' followed by
two to three 'b'.
"""

import re
my_string = input('enter a string ')
p = re.compile('ab{2,3}?')
m = p.search(my_string)
if m:
    print('it\'s a match')
else:
    print('no match found')

"""
7. Write a Python program to find sequences of lowercase letters joined with
an underscore.
"""

import re
my_string = input('enter a string ')
p = re.compile('[a-z]+_[a-z]+')
m = p.search(my_string)
if m:
    print('it\'s a match')
else:
    print('no match found')

"""
8. Write a Python program to find sequences of one upper case letter followed
by lower case letters.
"""

import re
my_string = input('enter a string ')
p = re.compile('[A-Z]+[a-z]+')
m = p.search(my_string)
if m:
    print('it\'s a match')
else:
    print('no match found')

"""
9. Write a Python program that matches a string that has an 'a' followed by
anything, ending in 'b'.
"""

import re
my_string = input('enter a string ')
p = re.compile('a.*?b$')
m = p.search(my_string)
if m:
    print('it\'s a match')
else:
    print('no match found')

"""
10. Write a Python program that matches a word at the beginning of a string.
"""

import re
my_string = input('enter a string ')
m = re.match('^\w+', my_string)
if m:
    print('it\'s a match')
else:
    print('no match found')

"""
11. Write a Python program that matches a word at end of string, with optional
punctuation.
"""

import re
my_string = input('enter a string ')
m = re.search('\b\w+[.!?,;]*$', my_string)
if m:
    print('it\'s a match')
else:
    print('no match found')

"""
12. Write a Python program that matches a word containing 'z'.
"""

import re
my_string = input('enter a string ')
m = re.search('\w*z\w*', my_string)
if m:
    print('it\'s a match')
else:
    print('no match found')

"""
13. Write a Python program that matches a word containing 'z', not start or
end of the word.
"""

import re
my_string = input('enter a string ')
m = re.search('\w+z\w+', my_string)
if m:
    print('it\'s a match')
else:
    print('no match found')

"""
14. Write a Python program to match a string that contains only upper and
lowercase letters, numbers, and underscores.
"""

import re
my_string = input('enter a string ')
m = re.search('[^0-9A-Za-z_]+', my_string)
if m:
    print('no match found')
else:
    print('it\'s a match')

"""
15. Write a Python program where a string will start with a specific number.
"""

import re
my_string = input('enter a string ')
my_number = input('enter a number ')
m = re.match(my_number, my_string)
if m:
    print('it\'s a match')
else:
    print('no match found')

"""
16. Write a Python program to remove leading zeros from an IP address.
"""

import re
my_IP = input('enter a string ')
my_clean_IP = re.sub('\.0*', '.', my_IP)
print(my_clean_IP)

"""
17. Write a Python program to check for a number at the end of a string.
"""

import re
my_string = input('enter a string ')
my_number = input('enter a number ')
m = re.search(my_number+'$', my_string)
if m:
    print('it\'s a match')
else:
    print('no match found')

"""
18. Write a Python program to search the numbers (0-9) of length between
1 to 3 in a given string.
"""

import re
my_string = input('enter a string ')
m = re.search('[0-9]{1,3}', my_string)
if m:
    print('it\'s a match')
else:
    print('no match found')

"""
19. Write a Python program to search some literals strings in a string. 
Sample text : 'The quick brown fox jumps over the lazy dog.'
Searched words : 'fox', 'dog', 'horse'
"""

import re
my_string = 'The quick brown fox jumps over the lazy dog.'
m = re.search('cat|dog|fox|horse', my_string)
if m:
    print('it\'s a match')
else:
    print('no match found')

"""
20. Write a Python program to search a literals string in a string and also
find the location within the original string where the pattern occurs. 
Sample text : 'The quick brown fox jumps over the lazy dog.'
Searched words : 'fox'
"""

import re
my_string = 'The quick brown fox jumps over the lazy dog.'
m = re.search('\Wfox\W', my_string)
if m:
    print('it\'s a match, starts on', m.start())
else:
    print('no match found')

"""
21. Write a Python program to find the substrings within a string. 
Sample text : 'Python exercises, PHP exercises, C# exercises'
Pattern : 'exercises'
Note: There are two instances of exercises in the input string.
"""

import re
my_string = 'Python exercises, PHP exercises, C# exercises'
my_substring = 'exercises'
m = re.findall(my_substring, my_string)
if m:
    print('it\'s a match', len(m))
else:
    print('no match found')

"""
22. Write a Python program to find the occurrence and position of the
substrings within a string.
"""

import re
my_string = 'Python exercises, PHP exercises, C# exercises'
my_substring = 'exercises'
m = re.finditer(my_substring, my_string)
for match in m:
    print('string \'{}\''.format(my_substring), 'found at position', match.span())

"""
23. Write a Python program to replace whitespaces with an underscore and
vice versa.
"""

import re
my_string = input('enter a sentence: ')
m = re.sub('\s', '_', my_string)
print(m)
m1 = re.sub('_', ' ', m)
print(m1)

"""
25. Write a Python program to convert a date of yyyy-mm-dd format to dd-mm-yyyy
format.
"""

import re
date = '2018-03-31'
m = re.split('-', date)
new_date = '-'.join(m[::-1])
print(new_date)

"""
26. Write a Python program to match if two words from a list of words starting
with letter 'P'.
"""

import re
my_list = ['Python Program', 'hello world', 'python program']
for phrase in my_list:
    if re.match('P\w*\sP\w*', phrase):
        print(phrase)

"""
27. Write a Python program to separate and print the numbers of a given string.
"""
