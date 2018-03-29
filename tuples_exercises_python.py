"""
1. Write a Python program to create a tuple.
"""

my_empty_tuple = ()
my_another_empty_tuple = tuple()
my_single_tuple = 'abc',
my_multiple_tuple = 'abc', 'bcd', 'xyz'
my_multiple_tuple_with_braktes = ('abc', 'bcd', 'xyz')
my_list = [1, 2, 3, 3, 4]
my_tuple_from_list = tuple(my_list)


print(my_empty_tuple, type(my_empty_tuple), '\n',
      my_another_empty_tuple, type(my_another_empty_tuple), '\n',
      my_single_tuple, type(my_single_tuple), '\n',
      my_multiple_tuple, type(my_multiple_tuple), '\n',
      my_multiple_tuple_with_braktes, type(my_multiple_tuple_with_braktes), '\n',
      my_tuple_from_list, type(my_tuple_from_list))

"""
2. Write a Python program to create a tuple with different data types.
"""

my_tuple = ('abc', 1, 4.56, ['a', 'b', 'c'], True)
print(my_tuple)

for i in my_tuple:
    print(i, 'type is', type(i))

"""
3. Write a Python program to create a tuple with numbers and print one item.
"""
from random import randint
my_tuple = (1, 2, 3, 3, 4)
print(my_tuple[randint(0, len(my_tuple)-1)])

"""
4. Write a Python program to unpack a tuple in several variables.
"""
my_tuple = ('a', 'b')
var1, var2 = my_tuple
print(var1, var2)

"""
5. Write a Python program to add an item in a tuple.
"""

my_tuple = ('a', 'b')
my_new_tuple = my_tuple + ('c',)

print(my_new_tuple)

"""
6. Write a Python program to convert a tuple to a string.
"""
my_tuple = ('a', 'b')
my_string = ''.join(my_tuple)
print(my_string)

"""
7. Write a Python program to get the 4th element
and 4th element from last of a tuple.
"""

my_tuple = tuple('abcdefgh')
print(my_tuple)
print('4th element is', my_tuple[3])
print('4th to last element is', my_tuple[-4]) 

"""
8. Write a Python program to create the colon of a tuple.
"""

my_tuple = (':',)
my_colon, = my_tuple
print(my_colon)

"""
9. Write a Python program to find the repeated items of a tuple.
"""

my_tuple = (1, 1, 2, 3, 4, 4, 5)

repeated_items = []
for i in my_tuple:
    if my_tuple.count(i) > 1:
        repeated_items.append(i)
print(set(repeated_items))

"""
10. Write a Python program to check whether an element exists within a tuple.
"""

my_tuple = (1, 2, 3, 4, 5)

if 2 in my_tuple:
    print('2 is in', my_tuple)
else:
    print('2 is NOT in', my_tuple)

if 6 in my_tuple:
    print('6 is in', my_tuple)
else:
    print('6 is NOT in', my_tuple)

"""
11. Write a Python program to convert a list to a tuple.
"""

my_list = [1, 2, 3, 4, 5]
my_tuple = tuple(my_list)
print(my_tuple)

"""
12. Write a Python program to remove an item from a tuple.
"""

my_tuple = (1, 2, 3, 4, 5)
# to remove number 3
my_new_tuple = my_tuple[:my_tuple.index(3)] + my_tuple[my_tuple.index(3)+1:]
print(my_new_tuple)

"""
13. Write a Python program to slice a tuple.
"""

my_tuple = tuple('axbxcx')

print(my_tuple[::2])

"""
14. Write a Python program to find the index of an item of a tuple.
"""

my_tuple = ('a', 'b')
print(my_tuple.index('a'))

"""
15. Write a Python program to find the length of a tuple.
"""

my_tuple = ('a', 'b')
print(len(my_tuple))

"""
16. Write a Python program to convert a tuple to a dictionary.
"""

my_tuple = ('a', 1, 'b', 2)

my_dict = {}
for i in range(0, len(my_tuple), 2):
    my_dict[my_tuple[i]] = my_tuple[i+1]
print(my_dict)

"""
17. Write a Python program to unzip a list of tuples into individual lists.
"""

my_list = [(1, 2), ('a', 'b'), (True, False)]
new_list = []
for i in my_list:
    new_list.append(list(i))
print(*new_list)

"""
18. Write a Python program to reverse a tuple.
"""
my_tuple = (1, 2, 3, 4)
reversed_tuple = my_tuple[::-1]
print(reversed_tuple)

"""
19. Write a Python program to convert a list of tuples into a dictionary.
"""

# solution 1 for unique keys
my_list = [('a', 1), ('b', 2)]
my_dict = {i[0]:i[1] for i in my_list}
print(my_dict)

# solution 2 for same key appearing in several tuples
my_list = [('a', 1), ('b', 2), ('a', 5)]
my_dict = {}
for i in my_list:
    my_dict.setdefault(i[0],[]).append(i[1])
print(my_dict)

"""
20. Write a Python program to print a tuple with string formatting.
Sample tuple : (100, 200, 300)
Output : This is a tuple (100, 200, 300)
"""

my_tuple = (100, 200, 300)
print('This is a tuple {}'.format(my_tuple))

"""
21. Write a Python program to replace last value of tuples in a list.
Sample list: [(10, 20, 40), (40, 50, 60), (70, 80, 90)]
Expected Output: [(10, 20, 100), (40, 50, 100), (70, 80, 100)]
"""

my_list = [(10, 20, 40), (40, 50, 60), (70, 80, 90)]

new_list = [i[:len(i)-1]+(100,) for i in my_list]
print(new_list)

"""
22. Write a Python program to remove an empty tuple(s) from a list of tuples.
Sample data: [(), (), ('',), ('a', 'b'), ('a', 'b', 'c'), ('d')]
Expected output: [('',), ('a', 'b'), ('a', 'b', 'c'), 'd']
"""


my_list = [(), (), ('',), ('a', 'b'), ('a', 'b', 'c'), ('d')]

new_list = [i for i in my_list if i]
print(new_list)

"""
23. Write a Python program to sort a listof tuples by the float element.
Sample data: [('item1', '12.20'), ('item2', '15.10'), ('item3', '24.5')]
Expected Output: [('item3', '24.5'), ('item2', '15.10'), ('item1', '12.20')]
"""

my_list = [('item1', '12.20'), ('item2', '15.10'), ('item3', '24.5')]

my_list.sort(key=lambda x: x[1], reverse=True)
print(my_list)

"""
24. Write a Python program to count the elements in a list until an element is a tuple.
"""

my_list = [1, 2, 3, (4,), 5, 6]

counter = 0
for i in my_list:
    if not isinstance(i, tuple):
        counter += 1
    else:
        break
print(counter)
