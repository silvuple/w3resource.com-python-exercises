"""
1. Write a Python script to sort (ascending and descending) a dictionary
by value.
"""

my_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}

print(sorted(my_dict.items(), key=lambda x: x[1]))
print(sorted(my_dict.items(), key=lambda x: x[1], reverse=True))
    
"""
2. Write a Python script to add a key to a dictionary.
"""

my_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}

my_dict['f'] = 6
print(my_dict)

"""
3. Write a Python script to concatenate following dictionaries to create
a new one. 
Sample Dictionary : 
dic1={1:10, 2:20} 
dic2={3:30, 4:40} 
dic3={5:50, 6:60}
Expected Result : {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
"""

dict1={1:10, 2:20} 
dict2={3:30, 4:40} 
dict3={5:50, 6:60}

combined_dict = {k: v for k, v in dict1.items() | dict2.items() | dict3.items()}
print(combined_dict)

"""
4. Write a Python script to check if a given key already exists in a dictionary.
"""

my_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}

print('a' in my_dict)
print('x' in my_dict)

"""
5. Write a Python program to iterate over a dictionary using for loop.
"""

my_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}

for k, v in my_dict.items():
    print(k, v)

"""
6.Write a Python script to generate and print a dictionary that contains
a number (between 1 and n) in the form (x, x*x).
Sample: (n = 5) 
Expected Output: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
"""

n = 5

my_dict = {x: x**2 for x in range(1, n+1)}
print(my_dict)

"""
7. Write a Python script to print a dictionary where the keys are numbers
between 1 and 15 (both included) and the values are square of keys.
Sample Dictionary 
{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100, 11: 121,
12: 144, 13: 169, 14: 196, 15: 225}
"""

my_dict = {x: x**2 for x in range(1, 16)}
print(my_dict)

"""
8. Write a Python script to merge two Python dictionaries.
"""

# solution 1
dict_one = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
dict_two = {'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 0}

for key in dict_two:                 # dict_one.update(dict_two)
    dict_one[key] = dict_two[key]  

print(dict_one)

# soltuion 2
dict_one = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
dict_two = {'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 0}

combined_dict = {}
combined_dict.update(dict_one, **dict_two)
print(combined_dict)

"""
10. Write a Python program to sum all the items in a dictionary.
"""

my_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}

# solution 1
dict_sum = sum(my_dict.values())
print(dict_sum)

# solution 2
dict_sum = 0
for k, v in my_dict.items():
    dict_sum += v
print(dict_sum)

"""
12. Write a Python program to remove a key from a dictionary.
"""

# solution 1
my_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
if my_dict['a']:
    del my_dict['a']
print(my_dict)

# solution 2
my_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
my_dict.pop('a', 0)
print(my_dict)

"""
13. Write a Python program to map two lists into a dictionary.
"""

list_one = ['a', 'b', 'c', 'd']
list_two = [1, 2, 3, 4]

# solution 1
my_dict = {k: v for (k, v) in zip(list_one, list_two)}
print(my_dict)

# solution 2
my_dict = dict(zip(list_one, list_two))
print(my_dict)

"""
14. Write a Python program to sort a dictionary by key.
"""

my_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}

for key in sorted(my_dict.keys()):
    print(key, ":", my_dict[key])

"""
15. Write a Python program to get the maximum and minimum value in a dictionary.
"""

my_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}

dict_min = min(my_dict.values())
dict_max = max(my_dict.values())

print('in dictionary', my_dict, 'max is %d and min is %d' % (dict_max, dict_min))

"""
16.Write a Python program to get a dictionary from an object's fields.
"""

print(dict.__dict__)

"""
17. Write a Python program to remove duplicates from Dictionary.
"""

# solution 1
my_dict = {'a': 1, 'b': 2, 'c': 1, 'd': 2, 'e': 5}

unique_values = []
keys_to_remove = []

for key in my_dict:
    if my_dict[key] in unique_values:
        keys_to_remove.append(key)
    else:
        unique_values.append(my_dict[key])

for key in keys_to_remove:
    del my_dict[key]        # my_dict.pop(key)

print(my_dict)

# solution 2
my_dict = {'a': 1, 'b': 2, 'c': 1, 'd': 2, 'e': 5}

new_dict = {}

for key, value in my_dict.items():
    if value not in new_dict.values():
        new_dict[key] = value

print(new_dict)

"""
18. Write a Python program to check a dictionary is empty or not.
"""

my_dict = {}
my_other_dict = {'a': 1}

if not my_dict:
    print("dicttionary", my_dict, "is empty")
else:
    print("dicttionary", my_dict, "is NOT empty")

if not my_other_dict:
    print("dicttionary", my_other_dict, "is empty")
else:
    print("dicttionary", my_other_dict, "is NOT empty")

"""
19. Write a Python program to combine two dictionary adding values
for common keys. 
d1 = {'a': 100, 'b': 200, 'c':400}
d2 = {'a': 300, 'b': 200, 'd':400}
Sample output: Counter({'a': 400, 'b': 400, 'd': 400, 'c': 300})
"""

d1 = {'a': 100, 'b': 200, 'c':400}
d2 = {'a': 300, 'b': 200, 'd':400}
counter = {}
counter = d1.copy()

for key in d2:
    if key in counter:
        counter[key] += d2[key]
    else:
        counter[key] = d2[key]
print(counter)

"""
20. Write a Python program to print all unique values in a dictionary.
Sample Data: [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"},
            {"VI": "S005"}, {"VII": "S005"}, {"V": "S009"}, {"VIII": "S007"}]
Expected Output: Unique Values: {'S005', 'S002', 'S007', 'S001', 'S009'}
"""

my_list = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"},
            {"VI": "S005"}, {"VII": "S005"}, {"V": "S009"}, {"VIII": "S007"}]
# solution 1
my_set = set()
for dictionary in my_list:
    for k, v in dictionary.items():
        my_set.add(v)
print(my_set)

# solution 1 with set comprehension
my_set = {v for d in my_list for k, v in d.items()}
print(my_set)

"""
21. Write a Python program to create and display all combinations of letters,
selecting each letter from a different key in a dictionary. 
Sample data : {'1':['a','b'], '2':['c','d']}
Expected Output: 
ac
ad
bc
bd
"""

my_dict = {'1':['a','b'], '2':['c','d']}

my_list = list(my_dict.values())
print(my_list)
for i in my_list[0]:
    for j in range(1, len(my_list)):
        for x in my_list[j]:
            my_string = i + x
            print(my_string)

"""
22. Write a Python program to find the highest 3 values in a dictionary.
"""

my_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 5, 'x': 2}
sorted_values_list = sorted(set(my_dict.values()))
print("the highest 3 values are", sorted_values_list[-3:])
keys_with_highest_values = []
for key in my_dict:
    if my_dict[key] in sorted_values_list[-3:]:
        keys_with_highest_values.append(key)
print("their keys are (not in order)", keys_with_highest_values)

"""
23. Write a Python program to combine values in python list of dictionaries.
Sample data: [{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount': 300},
{'item': 'item1', 'amount': 750}]
Expected Output: Counter({'item1': 1150, 'item2': 300})
"""

my_list = [{'item': 'item1', 'amount': 400},
           {'item': 'item2', 'amount': 300},
           {'item': 'item1', 'amount': 750}]

new_list = []
for d in my_list:
    new_list.append(tuple(d.values()))
combined_dict = {}
for t in new_list:
    if t[0] in combined_dict:
        combined_dict[t[0]] += t[1]
    else:
        combined_dict[t[0]] = t[1]
print(combined_dict)

"""
24. Write a Python program to create a dictionary from a string. 
Note: Track the count of the letters from the string.
Sample string : 'w3resource'
Expected output: {'3': 1, 's': 1, 'r': 2, 'u': 1, 'w': 1, 'c': 1, 'e': 2, 'o': 1}
"""

my_string = 'w3resource'

my_dict = {letter: my_string.count(letter) for letter in my_string}
print(my_dict)

"""
25. Write a Python program to print a dictionary in table format.
"""

my_dict = {'alice': 11, 'benji': 24, 'cilian': 38, 'david': 42, 'ewan': 56}

for key, value in my_dict.items():
    print('{:<7s}'.format(key), '{:>3d}'.format(value))

"""
26. Write a Python program to count the values associated with key in a dictionary.
Sample data: = [{'id': 1, 'success': True, 'name': 'Lary'}, {'id': 2, 'success': False, 'name': 'Rabi'}, {'id': 3, 'success': True, 'name': 'Alex'}]
Expected result: Count of how many dictionaries have success as True
"""

my_list = [{'id': 1, 'success': True, 'name': 'Lary'},
           {'id': 2, 'success': False, 'name': 'Rabi'},
           {'id': 3, 'success': True, 'name': 'Alex'}]

# solution 1
success_count = 0
for dictionary in my_list:
    if 'success' in dictionary:
        if dictionary['success'] == True:
            success_count += 1
print(success_count)
    
"""
27. Write a Python program to convert a list into a nested dictionary of keys.
"""

my_list = [1, 2, 3, 4, 5]
my_dict = {}

"""
28. Write a Python program to sort a list alphabetically in a dictionary.
"""

my_dict = {'a': [2, 3, 5],
           'b': [1, 8, 4],
           'c': [9, 0, 1]}

for li in my_dict.values():
    li.sort()
print(my_dict)

"""
29. Write a Python program to remove spaces from dictionary keys.
"""

my_dict = {'a b c': [2, 3, 5],
           'b d e': [1, 8, 4],
           'c f g': [9, 0, 1]}

for key in my_dict:
    new_key = key.replace(' ', '')
    my_dict[new_key] = my_dict.pop(key)
print(my_dict)

"""
30. Write a Python program to get the top three items in a shop.
Sample data: {'item1': 45.50, 'item2':35, 'item3': 41.30,
'item4':55, 'item5': 24}
Expected Output: 
item4 55
item1 45.5
item3 41.3
"""

items_dict = {'item1': 45.50, 'item2':35, 'item3': 41.30, 'item4':55, 'item5': 24}

my_list = [(k, v) for k,v in items_dict.items()]
my_list.sort(key=lambda x: x[1], reverse=True)
for i in my_list[:3]:
    print('{:<5s}'.format(i[0]), '{:<5.2f}'.format(i[1]))

"""
31. Write a Python program to get the key, value and item in a dictionary.
"""

my_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 5, 'x': 2}

for k, v in my_dict.items():
    print('key:', k, 'value:', v, 'item:', (k, v))

"""
32. Write a Python program to print a dictionary line by line.
"""

my_dict = {'alice': 11, 'benji': 24, 'cilian': 38, 'david': 42, 'ewan': 56}

for k,v in my_dict.items():
    print(k)
    print(v)

"""
33. Write a Python program to check multiple keys exists in a dictionary.
"""

my_dict = {'a': 1}
my_other_dict = {'a': 1, 'b': 2}
my_empty_dict = {}

if len(my_dict.keys()) > 1:
    print('dictionary', my_dict, 'has multiple keys')
else:
    print('dictionary', my_dict, 'does not have multiple keys')

if len(my_other_dict.keys()) > 1:
    print('dictionary', my_other_dict, 'has multiple keys')
else:
    print('dictionary', my_other_dict, 'does not have multiple keys')

if len(my_empty_dict.keys()) > 1:
    print('dictionary', my_empty_dict, 'has multiple keys')
else:
    print('dictionary', my_empty_dict, 'does not have multiple keys')

"""
34. Write a Python program to count number of items in a dictionary value
that is a list.
"""

my_dict = {'a': [2, 3, 5],
           'b': [1, 8, 4],
           'c': [9, 0, 1],
           'd': 3}

for k, v in my_dict.items():
    if isinstance(v, list):
        print('key=', k, 'value lenth=', len(v))
    else:
        print('key=', k, 'value is not a list')

"""
35. Write a Python program to sort Counter by value. 
Sample data : {'Math':81, 'Physics':83, 'Chemistry':87}
Expected data: [('Chemistry', 87), ('Physics', 83), ('Math', 81)]
"""

my_dict = {'Math':81, 'Physics':83, 'Chemistry':87}
my_list = list(my_dict.items())
my_list.sort(key=lambda x: x[1], reverse= True)
print(my_list)

"""
36. Write a Python program to create a dictionary from two lists
without losing duplicate values. 
Sample lists: ['Class-V', 'Class-VI', 'Class-VII', 'Class-VIII'], [1, 2, 2, 3]
Expected Output: defaultdict(<class 'set'>, {'Class-VII': {2}, 'Class-VI': {2},
'Class-VIII': {3}, 'Class-V': {1}})
"""

list_one = ['Class-V', 'Class-VI', 'Class-VII', 'Class-VIII']
list_two = [1, 2, 2, 3]

my_dict = {k: v for (k, v) in zip(list_one, list_two)}
print(my_dict)

"""
37. Write a Python program to replace dictionary values with their sum.
"""

my_dict = {'a': [2, 3, 5],
           'b': [1, 8, 4],
           'c': [9, 0, 1]}

my_new_dict = {k: sum(v) for k, v in my_dict.items()}
print(my_new_dict)

"""
38. Write a Python program to match key values in two dictionaries. 
Sample dictionary: {'key1': 1, 'key2': 3, 'key3': 2}, {'key1': 1, 'key2': 2}
Expected output: key1: 1 is present in both x and y
"""

dict_one = {'key1': 1, 'key2': 3, 'key3': 2}
dict_two = {'key1': 1, 'key2': 2}

for key in (dict_one.keys() & dict_two.keys()):
    print(key, 'key is present in both lists')

for (key, value) in (dict_one.items() & dict_two.items()):
    print('{:s}:'.format(key), value, 'is present in both lists')
