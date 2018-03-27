"""
1. Write a Python program to sum all the items in a list.
"""

my_list = [1, 2, 3, 4, 5]

# solution 1
list_sum = 0
for i in my_list:
    list_sum += i
print(list_sum)

# solution 2
list_sum = sum(my_list)
print(list_sum)

"""
2. Write a Python program to multiply all the items in a list.
"""

my_list = [1, 2, 3, 4, 5]

list_prod = 1
for i in my_list:
    list_prod *= i
print(list_prod)

"""
3. Write a Python program to get the largest number from a list.
"""

my_list = [1, 2, 3, 4, 5]

# solution 1
max_num = 0
for i in my_list:
    if i > max_num:
        max_num = i
print(max_num)

# solution 2
max_num = max(my_list)
print(max_num)

"""
4. Write a Python program to get the smallest number from a list.
"""

my_list = [1, 2, 3, 4, 5]

# solution 1
sorted_list = sorted(my_list)
min_num = sorted_list[0]
print(min_num)

# solution 2
min_num = min(my_list)
print(min_num)

# solution 3
min_num = my_list[0]
for i in my_list:
    if i < min_num:
        min_num = i
print(min_num)

"""
5. Write a Python program to count the number of strings where
the string length is 2 or more and the first and last character
are same from a given list of strings. 
Sample List : ['abc', 'xyz', 'aba', '1221']
Expected Result : 2
"""

my_list = ['abc', 'xyz', 'aba', '1221']

counter = 0
for i in my_list:
    if len(i) > 1:
        if i[0] == i[len(i)-1]: # or if i[0] == i[-1]:
            counter += 1
print(counter)

"""
6. Write a Python program to get a list, sorted in increasing order
by the last element in each tuple from a given list of non-empty tuples.
Sample List : [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
Expected Result : [(2, 1), (1, 2), (2, 3), (4, 4), (2, 5)]
"""

# solution 1
my_list = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
sorted_list = sorted(my_list, key=lambda x: x[1])
print(sorted_list)

# solution 2
my_list = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
my_list.sort(key=lambda x: x[1])
print(my_list)

"""
7. Write a Python program to remove duplicates from a list.
"""

my_list = [1, 2, 3, 4, 4, 5, 1, 2, 3, 4, 4, 5, 1, 1]

# solution 1
new_list = list(set(my_list))
print(new_list)

# solution 2
new_list = []
for i in my_list:
    if i not in new_list:
       new_list.append(i)
print(new_list)
        
"""
8. Write a Python program to check a list is empty or not
"""

my_list = []

if my_list:
    print('list is not empty')
else:
    print('list is empty')

"""
10. Write a Python program to find the list of words that are longer
than n from a given list of words.
"""

def is_longer(words, n):
    long_words = []
    for word in words:
        if len(word) > n:
            long_words.append(word)
    return long_words


my_list = ['cat', 'dog', 'apple', 'table', 'bags']

print(is_longer(my_list, 3))

"""
11. Write a Python function that takes two lists and returns True
if they have at least one common member.
"""

list_one = [1, 2, 3, 4, 5]
list_two = [8, 9, 5, 10, 11]

def common_member(li1, li2):
    for i in li1:
        if i in li2:
            return True
    else:
        return False

print(common_member(list_one, list_two))

"""
12. Write a Python program to print a specified list after removing the 0th,
4th and 5th elements.
Sample List : ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
Expected Output : ['Green', 'White', 'Black']
"""

my_list = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']

# solution 1
new_list = []
for index, value in enumerate(my_list):
    if index not in [0, 4, 5]:
        new_list.append(value)
print(new_list)

# solution 2
new_list = [x for i, x in enumerate(my_list) if i not in (0,4,5)]
print(new_list)

"""
13. Write a Python program to generate a 3*4*6 3D array whose each element is *.
"""

my_array = [[['*' for x in range(6)] for x in range(4)] for x in range(3)]
print(my_array)

"""
14. Write a Python program to print the numbers of a specified list
after removing even numbers from it
"""

my_list = [1, 2, 3, 4, 5]

new_list = [x for x in my_list if x%2 != 0]
print(new_list)

"""
15. Write a Python program to shuffle and print a specified list.
"""

from random import shuffle

my_list = [1, 2, 3, 4, 5]
shuffle(my_list)
print(my_list)

"""
16. Write a Python program to generate and print a list of first
and last 5 elements where the values are square of numbers between
1 and 30 (both included).
"""

my_list = [x**2 for x in range(1,31)]
print(my_list[:5],my_list[-5:])

"""
17. Write a Python program to generate and print a list except for the first
5 elements, where the values are square of numbers between 1 and 30 (both included).
"""
my_list = [x**2 for x in range(1,31)]
print(my_list[5:])

"""
18. Write a Python program to generate all permutations of a list in Python.
"""

import itertools

my_list = [1, 2, 3, 4, 5]
print(list(itertools.permutations(my_list)))

"""
19. Write a Python program to get the difference between the two lists.
"""

list_a = [1, 2, 3, 4, 5, 6, 'yellow']
list_b = [1, 2, 3, 4, 5]
diff_list = list(set(list_a) - set(list_b))
print(diff_list)

"""
20. Write a Python program access the index of a list.
"""

my_list = [1, 2, 3, 4, 5]

for index, value in enumerate(my_list):
    print(index)

"""
21. Write a Python program to convert a list of characters into a string.
"""

my_list = ['1', '2', '3', '4', '5']
my_string = ''.join(my_list)
print(my_string)

"""
22. Write a Python program to find the index of an item in a specified list.
"""

my_list = [1, 2, 3, 4, 5]

my_index = my_list.index(3)
print(my_index)

"""
23. Write a Python program to flatten a shallow list.
"""

my_list = [[1, 2], [3, 4], [5]]

# solution 1
new_list = []
for i in my_list:
    for j in i:
        new_list.append(j)
print(new_list)

# solution 2
from itertools import chain

new_list = list(chain.from_iterable(my_list))
print(new_list)

# solution 3
from itertools import chain

new_list = list(chain(*my_list))
print(new_list)

"""
24. Write a Python program to append a list to the second list.
"""

list_a = [1, 2, 3, 4, 5, 6, 'yellow']
list_b = [1, 2, 3, 4, 5]

combi_list = list_a + list_b
print(combi_list)

"""
25. Write a Python program to select an item randomly from a list.
"""

import random

my_list = [1, 2, 3, 4, 5]
rand_element = random.choice(my_list)
print(rand_element)

"""
26. Write a python program to check whether two lists are circularly identical.
"""

list_a = [1, 2, 3, 4, 5]
list_b = [5, 1, 2, 3, 4]
def circularly_identical(list_a, list_b):
    if len(list_a) != len(list_b):
        return print('not circularly identical')  
    double_a = list_a * 2   # double_a = list_a + list_a
    string_b = map(str, list_b)
    string_double_a = map(str, double_a)
    if ' '.join(string_b) in ' '.join(string_double_a):
        return print('circularly identical')
    else:
        return print('not circularly identical')

circularly_identical(list_a, list_b)

"""
27. Write a Python program to find the second smallest number in a list.
"""

my_list = [1, 2, 3, 4, 5]

sorted_list = sorted(my_list)
print(sorted_list[1])

"""
28. Write a Python program to find the second largest number in a list.
"""
my_list = [1, 2, 3, 4, 5]

sorted_list = sorted(my_list)
print(sorted_list[-2])

"""
29. Write a Python program to get unique values from a list.
"""

my_list = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]

print(set(my_list))

"""
30. Write a Python program to get the frequency of the elements in a list.
"""

my_list = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 5, 5, 18, 'yellow']

# solution 1
freq_list = []
for i in set(my_list):
    freq_list.append((i, my_list.count(i)))
print(freq_list)

# soution 2
my_dict = dict(map(lambda x: (x, 0), my_list))
for i in my_dict:
    my_dict[i] = my_list.count(i)
print(my_dict)

"""
31. Write a Python program to count the number of elements in a list
within a specified range.
"""

def count_elements_in_range(my_list, min_range, max_range):
    counter = 0
    for element in my_list:
        if element in range(min_range, max_range+1):
            counter += 1
    return counter

my_list = [1, 2, 3, 4, 5]
print(count_elements_in_range(my_list, 3, 10))

"""
32. Write a Python program to check whether a list contains a sublist.
"""

def is_sublist(main_list, sub_list):
    if ''.join(map(str,sub_list)) in ''.join(map(str,main_list)):
        return True
    else:
        return False

my_list = [1, 2, 3, 4, 5]
my_sublist_one = [2, 3]
my_sublist_two = [3, 2]

print('the list', my_list, 'contains sublist', my_sublist_one, '-',
      is_sublist(my_list, my_sublist_one))
print('the list', my_list, 'contains sublist', my_sublist_two, '-',
      is_sublist(my_list, my_sublist_two))

"""
33. Write a Python program to generate all sublists of a list.
"""
import itertools

my_list = [1, 2, 3, 4, 5]

# solution 1
def sublist_generator(my_list):
    for i in range(0,len(my_list),1):
        for j in range(len(my_list),i,-1):
            yield list(itertools.islice(my_list, i, j))

print(list(sublist_generator(my_list)))

# solution 2
def sublist_generator(my_list):
    sublists = []
    for i in range(len(my_list)):
        j = len(my_list)
        while j > i:
            sublists.append(my_list[i:j])
            j -= 1
    return sublists
print(sublist_generator(my_list))
            
"""
34. Write a Python program using Sieve of Eratosthenes method for computing
primes upto a specified number. 
Note: In mathematics, the sieve of Eratosthenes, one of a number of prime
number sieves, is a simple, ancient algorithm for finding all prime numbers
up to any given limit.
"""

# solution 1

n = int(input('please enter a number ')) + 1
not_primes = []
primes = []
for p in range(2, n):
    if p not in not_primes:
        primes.append(p)
        for j in range(p**2, n, p):   # not_primes.extend(range(p**2, n, p))
            not_primes.append(j)
print(primes)

# solution 2 
def update_list(p, num_list):
    update_list = [x for x in num_list if x%p != 0]
    return update_list

n = int(input('please enter a number ')) + 1
primes = []
num_list = list(range(2, n))
while num_list:
    p = num_list[0]
    primes.append(p)
    num_list = update_list(p, num_list)
print(primes)

"""
35. Write a Python program to create a list by concatenating a given list
which range goes from 1 to n. 
Sample list : ['p', 'q']
n =5
Sample Output : ['p1', 'q1', 'p2', 'q2', 'p3', 'q3', 'p4', 'q4', 'p5', 'q5']
"""

my_list = ['p', 'q']
n = 5

# solution 1
new_list = []
for i in range(1, n+1):
    for element in my_list:
        new_list.append(str(element)+str(i))
print(new_list)

# solution 2
new_list = ['{}{}'.format(x, y) for y in range(1, n+1) for x in my_list]
print(new_list)

"""
37. Write a Python program to find common items from two lists.
"""

list_one = [1, 2, 3, 4, 5, 'red']
list_two = ['yellow', 'red', 'blue', 2, 5]

# solution 1
common_items = []
for i in list_one:
    if i in list_two:
        common_items.append(i)
print('list one is', list_one, ', list two is', list_two,
      'their common items are', common_items)

# solution 2
common_items = list(set(list_one) & set(list_two))     # common_items = list(set(list_one).intersection(set(list_two)))
print('list one is', list_one, ', list two is', list_two,
      'their common items are', common_items)

"""
38. Write a Python program to change the position of every n-th value with
the (n+1)th in a list. 
Sample list: [0,1,2,3,4,5]
Expected Output: [1, 0, 3, 2, 5, 4]
"""

my_list = [0, 1, 2, 3, 4, 5]
n = 2
new_list = []
for i in range(0, len(my_list), n):
    new_list.append(my_list[i+1])
    new_list.append(my_list[i])

print(new_list)

"""
39. Write a Python program to convert a list of multiple integers into
a single integer.
"""

my_list = [0, 1, 2, 3, 4, 5]

if my_list[0] == 0:
    my_list.pop(0)

single_int = int(''.join(map(str,my_list)))
print('from list', my_list, 'to single integer', single_int)

"""
40. Write a Python program to split a list based on first character of word.
"""
import string 
text = input('please enter some text \n')
text_list = text.lower().split()
word_dict = {}
for word in text_list:
    for letter in string.ascii_lowercase:
        if word.startswith(letter):
            if letter in word_dict:
                word_dict[letter].append(word)
            else:
                word_dict[letter] = [word]
print(word_dict)

"""
42. Write a Python program to find missing and additional values in two lists.
Sample data : Missing values in second list: b,a,c
Additional values in second list: g,h
"""

list_one = [1, 2, 3, 4, 'x', 'a', 'b', 'c']
list_two = [1, 2, 3, 'x', 'g', 'h']

print('missing', set(list_one) - set(list_two))
print('additional', set(list_two) - set(list_one))

"""
43. Write a Python program to split a list into different variables.
"""

my_list = [1, 2, 'a']

x, y, z = my_list

print(x)
print(y)
print(z)

"""
44. Write a Python program to generate groups of five consecutive numbers
in a list (list of consecutive numbers grouped in lists of 5).
"""

my_list = [[(5*x + y) for y in range(1,6)] for x in range(10)]
print(my_list)

"""
45. Write a Python program to convert a pair of values into a sorted unique array.
(list of tuples to sorted list of values).
"""

my_list = [(7, 0), (1, 2), (7, 8), (4, 3), (6, 9), (3, 4)]

# solution 1
new_list = []
for x in my_list:
    for y in x:
        new_list.append(y)
new_set = set(new_list)
print(sorted(new_set))

# solution 2 (same as solution 1 only with list comprehension)
new_list = [y for x in my_list for y in x]
new_set = set(new_list)
print(sorted(new_set))

# solution 3
from itertools import chain

new_list = chain(*my_list)
new_set = set(new_list)
print(sorted(new_set))

# solution 4
new_set = set()
new_set = new_set.union(*my_list)
print(sorted(new_set))

"""
46. Write a Python program to select the odd items of a list.
"""

my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8]

new_list = [x for x in my_list if x%2 != 0]
print(new_list)

"""
47. Write a Python program to insert an element before each element of a list.
"""

# solution 1
my_list = [0, 1, 2, 3, 4, 5]
element = 'x'
for i in range(0,len(my_list)*2,2):
    my_list.insert(i, element)
print(my_list)

# solution 2
my_list = [0, 1, 2, 3, 4, 5]
element = 'x'
new_list = [y for x in my_list for y in (element, x)]
print(new_list)

"""
48. Write a Python program to print a nested lists (each list on a new line)
using the print() function.
"""

my_list = [ [7, 0],  [1, 2],  [7, 8],  [4, 3],  [6, 9],  [3, 4]]

for i in my_list:
    print(i)
    
"""
49. Write a Python program to convert list to list of dictionaries.
Sample lists:
["Black", "Red", "Maroon", "Yellow"],
["#000000", "#FF0000", "#800000", "#FFFF00"]
Expected Output:
[{'color_name': 'Black', 'color_code': '#000000'},
{'color_name': 'Red', 'color_code': '#FF0000'},
{'color_name': 'Maroon', 'color_code': '#800000'},
{'color_name': 'Yellow', 'color_code': '#FFFF00'}]
"""

names = ["Black", "Red", "Maroon", "Yellow"]
codes = ["#000000", "#FF0000", "#800000", "#FFFF00"]

colors_list = [dict(color_name=x, color_code=y) for (x,y) in zip(names, codes)]
print(colors_list)

"""
51. Write a Python program to split a list every Nth element.
Sample list:
['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n']
Expected Output:
[['a', 'd', 'g', 'j', 'm'], ['b', 'e', 'h', 'k', 'n'], ['c', 'f', 'i', 'l']]
"""

my_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n']
N = 3
big_list = []
big_list = [[my_list[i] for i in range(n, len(my_list), N)] for n in range(N)]
print(big_list)

"""
52. Write a Python program to compute the similarity between two lists.
Sample data:
["red", "orange", "green", "blue", "white"],
["black", "yellow", "green", "blue"]
Expected Output: 
Color1-Color2: ['white', 'orange', 'red']
Color2-Color1: ['black', 'yellow']
"""

list_one = ["red", "orange", "green", "blue", "white"]
list_two = ["black", "yellow", "green", "blue"]

print('Color1-Color2', list(set(list_one) - set(list_two)))
print('Color2-Color1', list(set(list_two) - set(list_one)))

"""
54. Write a Python program to concatenate elements of a list. 
"""

my_list = [1, 2, 3, 4, 5, 'a']

my_string = ''.join(map(str, my_list))
print(my_string)

"""
55. Write a Python program to remove key values pairs from a list of dictionaries.
"""

# solution 1
my_list = [{'x': 1, 'y': 2},
           {'x': 3, 'y': 4},
           {'x': 5, 'y': 6}]

for i in my_list:
    del(i['x'])
print(my_list)

# solution 2
my_list = [{'x': 1, 'y': 2},
           {'x': 3, 'y': 4},
           {'x': 5, 'y': 6}]

new_list = [{k: v for k, v in x.items() if k != 'x'} for x in my_list]
print(new_list)

"""
56. Write a Python program to convert a string to a list.
"""

my_string = 'abracadabra'

# list of letters
my_list = list(my_string)
print(my_list)
# list of words
my_list = my_string.split()
print(my_list)

# convert a "string" list example color ="['Red', 'Green', 'White']" to real list
my_string = "['Red', 'Green', 'White']"
print(my_string)
my_string = my_string.strip('[]')
my_string = my_string.replace(',', ' ')
my_string = my_string.replace("'", ' ')
my_list = my_string.split()
print(my_list)

"""
57. Write a Python program to check if all items of a list is equal
to a given string.
"""

my_list = ['a', 'a', 'a', 'a']
control_list = ['a', 'a', 'a', 'b']
my_string = 'a'

# long solution
def items_equal(my_list, my_string):
    counter = 0
    for i in my_list:
        if i == my_string:
            counter += 1
    if counter == len(my_list):
        return True
    else:
        return False

if items_equal(my_list, my_string):
    print('all items in list', my_list, 'are equal to', my_string)
else:
    print('NOT all items in list', my_list, 'are equal to', my_string)   

if items_equal(control_list, my_string):
    print('all items in list', control_list, 'are equal to', my_string)
else:
    print('NOT all items in list', control_list, 'are equal to', my_string) 

# short solution
if all(i == my_string for i in my_list):
    print('all items in list', my_list, 'are equal to', my_string)
else:
    print('NOT all items in list', my_list, 'are equal to', my_string)  

if all(i == my_string for i in control_list):
    print('all items in list', control_list, 'are equal to', my_string)
else:
    print('NOT all items in list', control_list, 'are equal to', my_string) 

"""
58. Write a Python program to replace the last element in a list with
another list. 
Sample data : [1, 3, 5, 7, 9, 10], [2, 4, 6, 8]
Expected Output: [1, 3, 5, 7, 9, 2, 4, 6, 8]
"""

list_one = [1, 3, 5, 7, 9, 10]
list_two = [2, 4, 6, 8]
list_one[len(list_one)-1:] = list_two  # list_one[-1:] = list_two
print(list_one)

"""
59. Write a Python program to check if the n-th element exists in a given list.
"""

my_list = [1, 3, 5, 7, 9, 10]
n = 6

# solution 1
if len(my_list) > n:
    print("there is {}-th element in list".format(n), my_list)
else:
    print("no {}-th element in list".format(n), my_list)
    

# solution 2
try:
    my_list[n]
    print("there is {}-th element in list".format(n), my_list)    
except:
    print("no {}-th element in list".format(n), my_list)

"""
60. Write a Python program to find a tuple with the smallest 'second
index' value from a list of tuples.
"""

my_list = [(1, 2), (9, 6), (3, 5), (3, 1), (6, 3)]
print(my_list)

# solution 1
my_list.sort(key=lambda x: x[1])
print('tuple with the smallest second value is', my_list[0])

# solution 2
my_list = [(1, 2), (9, 6), (3, 5), (3, 1), (6, 3)]
print('tuple with the smallest second value is', min(my_list, key=lambda x: x[1]))

"""
61. Write a Python program to create a list of empty dictionaries.
"""

my_list = [{} for i in range(5)]
print(my_list)

"""
62. Write a Python program to print a list of space-separated elements.
"""

my_list = [1, 2, 3, 4, 5]

# solution 1
print(' '.join(map(str, my_list)))

# solution 2
print(*my_list)

"""
63. Write a Python program to insert a given string at the beginning of all
items in a list.
Sample list : [1,2,3,4], string : emp
Expected output : ['emp1', 'emp2', 'emp3', 'emp4']
"""

my_list = [1,2,3,4]
my_string = 'emp'

# solution 1
new_list = [my_string+str(x) for x in my_list]
print(new_list)

"""
64. Write a Python program to iterate over two lists simultaneously.
"""

list_one = [1, 2, 3, 4, 5]
list_two = [11, 22, 33, 44, 55]

for x, y in zip(list_one, list_two):
    my_tuple = (x, y)
    print(my_tuple)

"""
65. Write a Python program to access dictionary keys element by index.
"""

my_list = {'john': 15, 'dave': 12, 'jack': 10}
list_of_keys = list(my_list)
for i in range(len(list_of_keys)):
    print('the key', list_of_keys[i], 'has index', i)

"""
66. Write a Python program to find the list in a list of lists whose
sum of elements is the highest. 
Sample lists: [1,2,3], [4,5,6], [10,11,12], [7,8,9]
Expected Output: [10, 11, 12]
"""

my_list = [[1,2,3], [4,5,6], [10,11,12], [7,8,9]]

print(max(my_list, key=lambda x: sum(x)))  # print(max(my_list, key=sum))

"""
67. Write a Python program to find all the values in a list that are greater
than a specified number.
"""

my_list = [1, 2, 3, 4, 5]
num = 3
new_list = [x for x in my_list if x > num]
print(new_list)

"""
67. Write a Python program to find if all the values in a list are greater
than a specified number.
"""

my_list = [1, 2, 3, 4, 5]
num = 3
print(all(x > num for x in my_list))
num = 0
print(all(x > num for x in my_list))

"""
68. Write a Python program to extend a list without append.
Sample data: [10, 20, 30] [40, 50, 60]
Expected output : [40, 50, 60, 10, 20, 30]
"""

# solution 1
list_one = [10, 20, 30]
list_two = [40, 50, 60]
list_two.extend(list_one)
print(list_two)

# solution 2
list_one = [10, 20, 30]
list_two = [40, 50, 60]
list_two[len(list_two):] = list_one
print(list_two)

"""
69. Write a Python program to remove duplicates from a list of lists.
Sample list : [[10, 20], [40], [30, 56, 25], [10, 20], [33], [40]]
New List : [[10, 20], [30, 56, 25], [33], [40]]
"""

my_list = [[10, 20], [40], [30, 56, 25], [10, 20], [33], [40]]
print(my_list)

sorted_list = sorted(my_list)
unique_list = []
for i in my_list:
    if i in unique_list:
        continue
    else:
        unique_list.append(i)
print(unique_list)

"""
70. Write a Python program to get the depth of a dictionary.
"""


my_dict = {'a1': 2, 'a2': {'b': {'c': {'x': {'z': 1}}}}}

def dict_depth(my_dict):
    depth = 0
    if isinstance(my_dict, dict):
        depth += 1
        for key in my_dict:
            depth += dict_depth(my_dict[key])
    return depth
print(dict_depth(my_dict))


"""
71. Write a Python program to check if all dictionaries in a list
are empty or not. 
Sample list : [{},{},{}]
Return value : True
Sample list : [{1,2},{},{}]
Return value : False
"""

# solution 1
def is_empty(my_list):
    for i in my_list:
        if i:
            return False
    return True

print(is_empty([{},{},{}]))
print(is_empty([{1,2},{},{}]))

# solution 2
print(all(not x for x in [{},{},{}]))
print(all(not x for x in [{1,2},{},{}]))
