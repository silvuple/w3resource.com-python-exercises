"""
1. Write a Python program to create an Enum object and display a member name
and value.
Sample data :
Afghanistan = 93
Albania = 355
Algeria = 213
Andorra = 376
Angola = 244
Antarctica = 672
Expected Output :
Member name: Albania
Member value: 355
"""

from enum import Enum

class Country(Enum):
    Afghanistan = 93
    Albania = 355
    Algeria = 213
    Andorra = 376
    Angola = 244
    Antarctica = 672

##print(Country.Albania)
##print(repr(Country.Albania))
##print(type(Country.Albania))
##print(isinstance(Country.Albania, Country))
##print(Country['Albania'])
##print(Country['Antarctica'].value)
##for country in Country:
##    print(country)
print('Member name:', Country.Albania.name)
print('Member value:', Country.Albania.value)

"""
2. Write a Python program to iterate over an enum class and display individual
member and their value. 
Expected Output:
Afghanistan = 93
Albania = 355
Algeria = 213
Andorra = 376
Angola = 244
Antarctica = 672
"""

from enum import Enum

class Country(Enum):
    Afghanistan = 93
    Albania = 355
    Algeria = 213
    Andorra = 376
    Angola = 244
    Antarctica = 672

for country in Country:
    print('Member name is {:<11}; member value is {}'.format(country.name, country.value))

"""
3. Write a Python program to display all the member name of an enum class
ordered by their values. 
Expected Output:
Country Name ordered by Country Code:
Afghanistan
Algeria
Angola
Albania
Andorra
Antarctica
"""
# solution 1
from enum import Enum

class Country(Enum):
    Afghanistan = 93
    Albania = 355
    Algeria = 213
    Andorra = 376
    Angola = 244
    Antarctica = 672   

print('Country Name ordered by Country Code:')
for country in sorted(Country, key=lambda x: x.value):
    print(country.name)

# solution 2 
from enum import IntEnum

class Country(IntEnum):
    Afghanistan = 93
    Albania = 355
    Algeria = 213
    Andorra = 376
    Angola = 244
    Antarctica = 672   

print('Country Name ordered by Country Code:')
for country in sorted(Country):
    print(country.name)

"""
4. Write a Python program to get all values from an enum class. 
Expected output:
[93, 355, 213, 376, 244, 672]
"""

from enum import Enum

class Country(Enum):
    Afghanistan = 93
    Albania = 355
    Algeria = 213
    Andorra = 376
    Angola = 244
    Antarctica = 672   

output = []
for country in Country:
    output.append(country.value)
print(output)

# alternatively:
output = [country.value for country in Country]
print(output)

"""
5. Write a Python program to count the most common words in a dictionary. 
Expected Output:
[('pink', 6), ('black', 5), ('white', 5), ('red', 4)]
"""

words = ['red', 'green', 'black', 'pink', 'black', 'white', 'black', 'eyes',
         'white', 'black', 'orange', 'pink', 'pink', 'red', 'red', 'white',
         'orange', 'white', 'black', 'pink', 'green', 'green', 'pink', 'green',
         'white', 'orange', "orange", 'red']

# solution 1 withour collections module
counts = set()
for word in words:
    counts.add((word, words.count(word)))

output = sorted(counts, key=lambda x: x[1], reverse=True)
print(output[:4])

# solution 2 with collections
from collections import Counter
print(Counter(words).most_common(4))

"""
6. Write a Python program to find the class wise roll number from a
tuple-of-tuples.
Sample data:
classes = (
('V', 1),
('VI', 1),
('V', 2),
('VI', 2),
('VI', 3),
('VII', 1),
)
Expected Output:
defaultdict(, {'VII': [1], 'V': [1, 2], 'VI': [1, 2, 3]})
"""

classes = (('V', 1),
           ('VI', 1),
           ('V', 2),
           ('VI', 2),
           ('VI', 3),
           ('VII', 1))

my_dict = {}
for a,b in classes:
    my_dict.setdefault(a, []).append(b)
print(my_dict)

"""
7. Write a Python program to count the number of students of individual class.
Sample data:
classes = (
('V', 1),
('VI', 1),
('V', 2),
('VI', 2),
('VI', 3),
('VII', 1),
)
Expected Output:
Counter({'VI': 3, 'V': 2, 'VII': 1})
"""

classes = (('V', 1),
           ('VI', 1),
           ('V', 2),
           ('VI', 2),
           ('VI', 3),
           ('VII', 1))
# solution 1 (if numbers are sequentials and start with 1)
my_dict = {}
for a,b in classes:
    if a in my_dict:
        if b > my_dict[a]:
            my_dict[a] = b
    else:
        my_dict[a] = b

print(my_dict)

# solution 2 (count occurencies of each class)
my_dict = {}
only_classes, roll_numbers = zip(*classes)
for a in only_classes:
    my_dict[a]=only_classes.count(a)

print(my_dict)

"""
8.Write a Python program to get the unique enumeration values. 
Expected Output:
Afghanistan = 93
Albania = 355
Algeria = 213
Andorra = 376
Angola = 244
"""

from enum import Enum, unique

@unique
class Country(Enum):
    
    Afghanistan = 93
    Albania = 355
    Algeria = 213
    Andorra = 376
    Angola = 244

for c in Country:
    print(c.name, c.value)

"""
9. Write a Python program to create an instance of an OrderedDict using a given
dictionary. Sort the dictionary during the creation and print the members of
the dictionary in reverse order. 
Expected Output: 
Angola 244
Andorra 376
Algeria 213
Afghanistan 93
Albania 355
In reverse order:
Albania 355
Afghanistan 93
Algeria 213
Andorra 376
Angola 244
"""

from collections import OrderedDict

my_dict = dict(Afghanistan = 93,
               Albania = 355,
               Algeria = 213,
               Andorra = 376,
               Angola = 244)
# OrderedDict sorted by values in ascending order
my_ordered_dict = OrderedDict(sorted(my_dict.items(), key = lambda x: x[1]))
for k,v in my_ordered_dict.items():
    print(k, v)

# OrderedDict sorted by values in descending (reverse) order
print("In reverse order:")
reversed_dict = OrderedDict(sorted(my_dict.items(), key=lambda x: x[1], reverse=True))
for k,v in reversed_dict.items():
    print(k, v)
    
# or alternatively reversing without creating additional OrderedDict
print("In reverse order:")
for k in reversed(my_ordered_dict):
    print(k, my_ordered_dict[k])


"""
10. Write a Python program to group a sequence of key-value pairs into a
dictionary of lists.
Example:
[('v', 1), ('vi', 2), ('v', 3), ('vi', 4), ('vii', 1)]
Expected output:
[('v', [1, 3]), ('vi', [2, 4]), ('vii', [1])]
"""

classes = [('v', 1), ('vi', 2), ('v', 3), ('vi', 4), ('vii', 1)]

my_dict = {}
for k,v in classes:
    my_dict.setdefault(k, []).append(v)
print(my_dict)

"""
11. Write a Python program to compare two unordered lists (not sets).
Expected Output: False
"""
from collections import Counter

list_a = [1, 2, 5, 3, 4, 1, 2, 3]
list_b = [1, 3, 5, 2, 4, 3, 1, 2]

print(Counter(list_a) == Counter(list_b))

"""
12. Write a Python program to create an array contains six integers.
Also print all the members of the array. 
Expected Output:
10
20
30
40
50
"""

import array

my_arr = array.array('i', [1, 2, 3, 4, 5, 6])
print(my_arr)

for i in my_arr:
    print(i)

"""
13. Write a Python program to get the array size of types unsigned integer
and float. 
Expected Output:
4 
4
"""

import array

my_arr = array.array('I', [4, 4])
print(my_arr.itemsize)
my_arr = array.array('f', [4, 4])
print(my_arr.itemsize)

"""
14. Write a Python program to get an array buffer information. 
Expected Output:
Array buffer start address in memory and number of elements.
(25855056, 2)
"""

import array

my_arr = array.array('I', [4, 4, 4])
print(my_arr.buffer_info())

"""
15. Write a Python program to get the length of an array. 
Expected Output:
Length of the array is: 
5
"""

import array

my_arr = array.array('I', [4, 4, 4, 5])

# solution 1
print(my_arr.buffer_info()[1])

# solution 2
print(len(my_arr))

"""
16. Write a Python program to convert an array to an ordinary list with the
same items. 
Expected Output:
Original array:
array('b', [1, 2, 3, 4])
Array to list:
[1, 2, 3, 4] 
"""

import array

my_arr = array.array('b', [1, 2, 3, 4])

# solution 1
my_list = list(my_arr)
print(my_list, type(my_list))

# solution 2
my_list1 = my_arr.tolist()
print(my_list1, type(my_list1))

"""
17. Write a Python program to convert an array to an array of machine values
and return the bytes representation. 
Expected Output:
Original array: 
A1: array('i', [1, 2, 3, 4, 5, 6])
Array of bytes: b'010000000200000003000000040000000500000006000000'
"""

import array
import binascii

A1 = array.array('i', [1, 2, 3, 4, 5, 6])
print(binascii.b2a_hex(A1.tobytes()))

"""
18. Write a Python program to read a string and interpreting the string as
an array of machine values. 
Expected Output:
array1: array('i', [7, 8, 9, 10])
Bytes: b'0700000008000000090000000a000000' 
array2: array('i', [7, 8, 9, 10])
"""

import array

A1 = array.array('i', [1, 2, 3, 4, 5, 6])
A2 = array.array('i')
A2.frombytes(A1.tobytes())
print(A2)

"""
19. Write a Python program to push three items into the heap and print
the items from the heap. 
Expected Output:
('V', 1)
('V', 2)
('V', 3)
"""
import heapq

my_heap = []
heapq.heappush(my_heap, ('V', 1))
heapq.heappush(my_heap, ('V', 2))
heapq.heappush(my_heap, ('V', 3))

for i in my_heap:
    print(i)

"""
20. Write a Python program to push three items into a heap and return the
smallest item from the heap. Also Pop and return the smallest item from the heap.
Expected Output:
Items in the heap:
('V', 1)
('V', 3)
('V', 2) 
---------------------- 
The smallest item in the heap:
('V', 1) 
----------------------
Pop the smallest item in the heap:
('V', 2) 
('V', 3)
"""

import heapq

my_heap = []
heapq.heappush(my_heap, ('V', 0))
heapq.heappush(my_heap, ('V', 1))
heapq.heappush(my_heap, ('V', 1))

print("Items in the heap")
for i in my_heap:
    print(i)

print("The smallest item in the heap:")
print(*heapq.nsmallest(1, my_heap, key=lambda x: x[1]))
# also like this:
print(my_heap[0])

print("The smallest item in the heap:")
print(heapq.heappop(my_heap))

"""
21. Write a Python program to push an item on the heap, then pop and return
the smallest item from the heap. 
Expected Output:
Items in the heap:
('V', 1) 
('V', 3) 
('V', 2) 
----------------------
Using heappushpop push item on the heap and return the smallest item.
('V', 2) 
('V', 3) 
('V', 6)
"""

import heapq
my_heap = [('V', 1), ('V', 1)]

print(heapq.heappushpop(my_heap, ('V', 1)))
print(heapq.heappushpop(my_heap, ('V', 2)))
print(heapq.heappushpop(my_heap, ('V', 3)))

"""
22. Write a Python program to create a heapsort, pushing all values onto
a heap and then popping off the smallest values one at a time. 
Expected Output:
[10, 20, 20, 40, 50, 50, 60, 70, 80, 90, 100]
"""

import heapq

my_unsorted_list = [20, 10, 50, 70, 30, 10, 40, 80, 20, 60]
my_sorted_list = []
my_heap = []
for item in my_unsorted_list:
    heapq.heappush(my_heap, item)
    
for x in range(len(my_heap)):
    my_sorted_list.append(heapq.heappop(my_heap))

print(my_sorted_list)

"""
23. Write a Python program to get the two largest and three smallest items
from a dataset.
Expected Output:
[100, 90]
[10, 20, 20]
"""

import heapq

my_list = [20, 10, 50, 70, 30, 10, 40, 80, 20, 60]

print(heapq.nlargest(2, my_list))
print(heapq.nsmallest(3, my_list))

"""
24. Write a Python program to locate the left insertion point for a specified
value in sorted order. 
"""
import bisect

my_list = [10, 10, 20, 20, 30, 50, 40, 80, 70, 60]
print(bisect.bisect_left(my_list, 25))

"""
25. Write a Python program to locate the right insertion point for a specified
value in sorted order.
"""

import bisect

my_list = [10, 10, 20, 20, 30, 50, 40, 80, 70, 60]
print(bisect.bisect_right(my_list, 20))

"""
26. Write a Python program to insert items into a list in sorted order. 
Expected Output:
Original List: 
[25, 45, 36, 47, 69, 48, 68, 78, 14, 36] 
Sorted List: 
[14, 25, 36, 36, 45, 47, 48, 68, 69, 78]
"""

import bisect
 
my_list = [25, 45, 36, 47, 69, 48, 68, 78, 14, 36]
my_sorted_list = []
for i in my_list:
    bisect.insort_left(my_sorted_list, i)
print(my_sorted_list)

"""
27. Write a Python program to create a queue and display all the members and
size of the queue. 
Expected Output:
Members of the queue:
0 1 2 3 
Size of the queue:
4
"""

import queue

q = queue.Queue()

for i in range(4):
    q.put(i)

print("Members of the queue:")    
for elem in list(q.queue):
    print(elem, end=' ')
print("\nSize of the queue:")
print(q.qsize())

"""
28. Write a Python program to find whether a queue is empty or not. Go to the editor
Expected Output:
True 
False
"""

import queue

q = queue.Queue()

if q.empty():
    print(True)
else:
    print(False)

"""
29. Write a Python program to create a FIFO queue. 
Expected Output:
0 1 2 3 
"""

import queue

q = queue.Queue()

for i in range(4):
    q.put(i)
while not q.empty():
    print(q.get(), end=' ')
print('\n')

"""
30. Write a Python program to create a LIFO queue. 
Expected Output:
3 2 1 0
"""

import queue

p = queue.LifoQueue()

for i in range(4):
    p.put(i)
while not p.empty():
    print(p.get(), end=' ')
print('\n')
