# Collections module implements specialized container datatypes providing alternatives to Python's general purpose built-in containers, dict, list, set, and tuple.

# 1. Write a Python program that iterate over elements repeating each as many times as its count. 
# Sample Output: ['p', 'p', 'p', 'p', 'q', 'q']
from itertools import chain
import collections as ct
import collections
from collections import Counter, OrderedDict
import re
from collections import Counter
c = Counter(p=4, q=2, r=0, s=-2)
print(list(c.elements()))



# 2. Write a Python program to find the most common elements and their counts of a specified text. 
# Original string: lkseropewdssafsdfafkpwe
# Most common three characters of the said string:
# [('s', 4), ('e', 3), ('f', 3)]
s = 'lkseropewdssafsdfafkpwe'
print("Original string: "+s)
print("Most common three characters of the said string:")
print(Counter(s).most_common(3))


# 3. Write a Python program to create a new deque with three items and iterate over the deque's elements. 
# Sample Output:
# a
# e
# i
# o
# u
from collections import deque
dq = deque('aeiou')
for element in dq:
   print(element)


# 4. Write a Python program to find the occurrences of 10 most common words in a given text. 
# Sample Output:
# [('Python', 6), ('the', 6), ('and', 5), ('We', 2), ('with', 2),
#  ('The', 1), ('Software', 1), ('Foundation', 1), ('PSF', 1), ('is', 1)]
text = """The Python Software Foundation (PSF) is a 501(c)(3) non-profit 
corporation that holds the intellectual property rights behind
the Python programming language. We manage the open source licensing 
for Python version 2.1 and later and own and protect the trademarks 
associated with Python. We also run the North American PyCon conference 
annually, support other Python conferences around the world, and 
fund Python related development with our grants program and by funding 
special projects."""
words = re.findall('\w+', text)
print(Counter(words).most_common(10))


# 5. Write a Python program that accept some words and count the number of distinct words. Print the number of distinct words and number of occurrences for each distinct word according to their appearance. 
# Input number of words: 5
# Input the words:
# Red
# Green
# Blue
# Black
# White
# 5
# 1 1 1 1 1
class OrderedCounter(Counter, OrderedDict):
   pass


word_array = []
n = int(input("Input number of words: "))
print("Input the words: ")
for i in range(n):
   word_array.append(input().strip())
word_ctr = OrderedCounter(word_array)
print(len(word_ctr))
for word in word_ctr:
   print(word_ctr[word], end=' ')


# 6. Write a Python program that accept name of given subject and marks. Input number of subjects in first line and subject name, marks separated by a space in next line. Print subject name and marks in order of its first occurrence. 
# Sample Output:
# Powered by
# Number of subjects: 3
# Input Subject name and marks: Bengali 58
# Input Subject name and marks: English 62
# Input Subject name and marks: Math 68
# Bengali 58
# English 62
# Math 68
n = int(input("Number of subjects: "))
item_order = collections.OrderedDict()
for i in range(n):
   sub_marks_list = re.split(
       r'(\d+)$', input("Input Subject name and marks: ").strip())
   subject_name = sub_marks_list[0]
   item_price = int(sub_marks_list[1])
   if subject_name not in item_order:
       item_order[subject_name] = item_price
   else:
       item_order[subject_name] = item_order[subject_name]+item_price

for i in item_order:
   print(i+str(item_order[i]))


# 7. Write a Python program to create a deque and append few elements to the left and right, then remove some elements from the left, right sides and reverse the deque. 
# Sample Output:
# deque(['Red', 'Green', 'White'])
# Adding to the left:
# deque(['Pink', 'Red', 'Green', 'White'])
# Adding to the right:
# deque(['Pink', 'Red', 'Green', 'White', 'Orange'])
# Removing from the right:
# deque(['Pink', 'Red', 'Green', 'White'])
# Removing from the left:
# deque(['Red', 'Green', 'White'])
# Reversing the deque:
# deque(['White', 'Green', 'Red'])
import collections
# Create a deque
deque_colors = collections.deque(["Red","Green","White"])
print(deque_colors)
# Append to the left
print("\nAdding to the left: ")
deque_colors.appendleft("Pink")
print(deque_colors)
# Append to the right
print("\nAdding to the right: ")
deque_colors.append("Orange")
print(deque_colors)
# Remove from the right
print("\nRemoving from the right: ")
deque_colors.pop()
print(deque_colors)
# Remove from the left
print("\nRemoving from the left: ")
deque_colors.popleft()
print(deque_colors)
# Reverse the dequeue
print("\nReversing the deque: ")
deque_colors.reverse()
print(deque_colors)


# 8. Write a Python program to create a deque from an existing iterable object. 
# Sample Output:
# Original tuple:
# (2, 4, 6)
# <class 'tuple' >
# Original deque:
# deque([2, 4, 6])
# New deque from an existing iterable object:
# deque([2, 2, 4, 6, 8, 10, 12])
# <class 'collections.deque' >
import collections
even_nums = (2, 4, 6)
print("Original tuple:")
print(even_nums)
print(type(even_nums))
even_nums_deque = collections.deque(even_nums)
print("\nOriginal deque:")
print(even_nums_deque)
even_nums_deque.append(8)
even_nums_deque.append(10)
even_nums_deque.append(12)
even_nums_deque.appendleft(2)
print("New deque from an existing iterable object:")
print(even_nums_deque)
print(type(even_nums_deque))


# 9. Write a Python program to add more number of elements to a deque object from an iterable object. 
# Sample Output:
# Even numbers:
# deque([2, 4, 6, 8, 10])
# More even numbers:
# deque([2, 4, 6, 8, 10, 12, 14, 16, 18, 20])
even_nums = (2, 4, 6, 8, 10)
even_deque = collections.deque(even_nums)
print("Even numbers:")
print(even_deque)
more_even_nums = (12, 14, 16, 18, 20)
even_deque.extend(more_even_nums)
print("More even numbers:")
print(even_deque)


# 10. Write a Python program to remove all the elements of a given deque object. 
# Sample Output:
# Original Deque object with odd numbers:
# deque([1, 3, 5, 7, 9])
# Deque length: 5
# Deque object after removing all numbers - deque([])
# Deque length: 0
import collections
odd_nums = (1,3,5,7,9)
odd_deque  = collections.deque(odd_nums)
print("Original Deque object with odd numbers:")
print(odd_deque)
print("Deque length: %d"%(len(odd_deque)))
odd_deque.clear()
print("Deque object after removing all numbers-")
print(odd_deque)
print("Deque length:%d"%(len(odd_deque)))


# 11. Write a Python program to copy of a deque object and verify the shallow copying process. 
# Sample Output:
# Content of dq1:
# deque([1, 3, 5, 7, 9])
# dq2 id:
# 140706429557152
# Content of dq2:
# deque([1, 3, 5, 7, 9])
# dq2 id:
# 140706406914152
# Checking the first element of dq1 and dq2 are shallow copies:
# 11065888
# 11065888
import collections
tup1 = (1,3,5,7,9)
dq1 = collections.deque(tup1)
dq2 = dq1.copy()
print("Content of dq1:")
print(dq1)
print("dq2 id:")
print(id(dq1))
print("\nContent of dq2:")
print(dq2)
print("dq2 id:")
print(id(dq2))
print("\nChecking the first element of dq1 and dq2 are shallow copies:")
print(id(dq1[0]))
print(id(dq2[0]))


# 12. Write a Python program to count the number of times a specific element presents in a deque object. 
# Sample Output:
# Number of 2 in the sequence
# 5
# Number of 4 in the sequence
# 4
import collections
nums = (2,9,0,8,2,4,0,9,2,4,8,2,0,4,2,3,4,0)
nums_dq = collections.deque(nums)
print("Number of 2 in the sequence")
print(nums_dq.count(2))
print("Number of 4 in the sequence")
print(nums_dq.count(4))


# 13. Write a Python program to rotate a Deque Object specified number(positive) of times. 
# Sample Output:
# Deque before rotation:
# deque([2, 4, 6, 8, 10])
# Deque after 1 positive rotation:
# deque([10, 2, 4, 6, 8])
# Deque after 2 positive rotations:
# deque([6, 8, 10, 2, 4])
import collections
# declare an empty deque object
dq_object = collections.deque()
# Add elements to the deque - left to right
dq_object.append(2)
dq_object.append(4)
dq_object.append(6)
dq_object.append(8)
dq_object.append(10)
print("Deque before rotation:")
print(dq_object)
# Rotate once in positive direction
dq_object.rotate()
print("\nDeque after 1 positive rotation:")
print(dq_object)
# Rotate twice in positive direction
dq_object.rotate(2)
print("\nDeque after 2 positive rotations:")
print(dq_object)


# 14. Write a Python program to rotate a Deque Object specified number(negative) of times. 
# Sample Output:
# Deque before rotation:
# deque([2, 4, 6, 8, 10])
# Deque after 1 negative rotation:
# deque([4, 6, 8, 10, 2])
# Deque after 2 negative rotations:
# deque([8, 10, 2, 4, 6])
# declare an empty deque object
dq_object = collections.deque()
# Add elements to the deque - left to right
dq_object.append(2)
dq_object.append(4)
dq_object.append(6)
dq_object.append(8)
dq_object.append(10)
print("Deque before rotation:")
print(dq_object)
# Rotate once in negative direction
dq_object.rotate(-1)
print("\nDeque after 1 negative rotation:")
print(dq_object)
# Rotate twice in negative direction
dq_object.rotate(-2)
print("\nDeque after 2 negative rotations:")
print(dq_object)


# 15. Write a Python program to find the most common element of a given list. 
# Sample Output:
# Original list:
# ['PHP', 'PHP', 'Python', 'PHP', 'Python', 'JS', 'Python', 'Python', 'PHP', 'Python']
# Most common element of the said list:
# Python
language = ['PHP', 'PHP', 'Python', 'PHP', 'Python',
            'JS', 'Python', 'Python', 'PHP', 'Python']
print("Original list:")
print(language)
cnt = Counter(language)
print("\nMost common element of the said list:")
print(cnt.most_common(1)[0][0])


# 16. Write a Python program to perform Counter arithmetic and set operations for aggregating results. 
# Sample Output:
# C1: Counter({1: 1, 2: 1, 3: 1, 4: 1, 5: 1})
# C2: Counter({4: 1, 5: 1, 6: 1, 7: 1, 8: 1})
# Combined counts:
# Counter({4: 2, 5: 2, 1: 1, 2: 1, 3: 1, 6: 1, 7: 1, 8: 1})
# Subtraction:
# Counter({1: 1, 2: 1, 3: 1})
# Intersection(taking positive minimums):
# Counter({4: 1, 5: 1})
# Union(taking maximums):
# Counter({1: 1, 2: 1, 3: 1, 4: 1, 5: 1, 6: 1, 7: 1, 8: 1})
import collections
c1 = collections.Counter([1, 2, 3, 4, 5])
c2 = collections.Counter([4, 5, 6, 7, 8])
print('C1:', c1)
print('C2:', c2)
print('\nCombined counts:')
print(c1 + c2)
print('\nSubtraction:')
print(c1 - c2)
print('\nIntersection (taking positive minimums):')
print(c1 & c2)
print('\nUnion (taking maximums):')
print(c1 | c2)


# 17. Write a Python program to find the majority element from a given array of size n using Collections module. 
# Sample Output:
# 10
import collections
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :return type: int
        """
        count_ele=collections.Counter(nums)
        return count_ele.most_common()[0][0]

result = Solution().majorityElement([10,10,20,30,40,10,20,10])
print(result)


# 18. Write a Python program to merge more than one dictionary in a single expression. 
# Sample Output:
# Original dictionaries:
# {'R': 'Red', 'B': 'Black', 'P': 'Pink'} {'G': 'Green', 'W': 'White'}
# Merged dictionary:
# {'B': 'Black', 'R': 'Red', 'P': 'Pink', 'G': 'Green', 'W': 'White'}
# Original dictionaries:
# {'R': 'Red', 'B': 'Black', 'P': 'Pink'} {'G': 'Green', 'W': 'White'} {'O': 'Orange', 'W': 'White', 'B': 'Black'}
# Merged dictionary:
# {'B': 'Black', 'R': 'Red', 'P': 'Pink', 'G': 'Green', 'W': 'White', 'O': 'Orange'}
def merge_dictionaries(color1, color2):
    merged_dict = dict(ct.ChainMap({}, color1, color2))
    return merged_dict


color1 = {"R": "Red", "B": "Black", "P": "Pink"}
color2 = {"G": "Green", "W": "White"}
print("Original dictionaries:")
print(color1, ' ', color2)
print("\nMerged dictionary:")
print(merge_dictionaries(color1, color2))


def merge_dictionaries(color1, color2, color3):
    merged_dict = dict(ct.ChainMap({}, color1, color2, color3))
    return merged_dict


color1 = {"R": "Red", "B": "Black", "P": "Pink"}
color2 = {"G": "Green", "W": "White"}
color3 = {"O": "Orange", "W": "White", "B": "Black"}

print("\nOriginal dictionaries:")
print(color1, ' ', color2, color3)
print("\nMerged dictionary:")
# Duplicate colours have automatically removed.
print(merge_dictionaries(color1, color2, color3))


# 19. Write a Python program to break a given list of integers into sets of a given positive number. Return true or false. 
# Sample Output:
# Original list: [1, 2, 3, 4, 5, 6, 7, 8]
# Number to devide the said list: 4
# True
# Original list: [1, 2, 3, 4, 5, 6, 7, 8]
# Number to devide the said list: 3
# False
import collections as clt
def check_break_list(nums, n):
    coll_data = clt.Counter(nums)
    for x in sorted(coll_data.keys()):
        for index in range(1, n):
            coll_data[x+index] = coll_data[x+index]  - coll_data[x]
            if coll_data[x+index] < 0:
                return False
    return True

nums = [1,2,3,4,5,6,7,8]
n = 4
print("Original list:",nums)
print("Number to devide the said list:",n)
print(check_break_list(nums, n))
nums = [1,2,3,4,5,6,7,8]
n = 3
print("\nOriginal list:",nums)
print("Number to devide the said list:",n)
print(check_break_list(nums, n))


# 20. Write a Python program to find the item with maximum frequency in a given list. 
# Sample Output:
# Original list:
# [2, 3, 8, 4, 7, 9, 8, 2, 6, 5, 1, 6, 1, 2, 3, 2, 4, 6, 9, 1, 2]
# Item with maximum frequency of the said list:
# (2, 5)
from collections import defaultdict
def max_occurrences(nums):
    dict = defaultdict(int)
    for i in nums:
        dict[i] += 1
    result = max(dict.items(), key=lambda x: x[1]) 
    return result
nums = [2,3,8,4,7,9,8,2,6,5,1,6,1,2,3,2,4,6,9,1,2]
print ("Original list:")
print(nums)
print("\nItem with maximum frequency of the said list:")
print(max_occurrences(nums))


# 21. Write a Python program to count most and least common characters in a given string. 
# Sample Output:
# Original string:
# hello world
# Most common character of the said string: l
# Least common character of the said string: h


def max_least_char(str1):
    temp = Counter(str1)
    max_char = max(temp, key=temp.get)
    min_char = min(temp, key=temp.get)
    return (max_char, min_char)


str1 = "hello world"
print("Original string: ")
print(str1)
result = max_least_char(str1)
print("\nMost common character of the said string:", result[0])
print("Least common character of the said string:", result[1])


# 22. Write a Python program to insert an element at the beginning of a given OrderedDictionary. 
# Sample Output:
# Original OrderedDict:
# OrderedDict([('color1', 'Red'), ('color2', 'Green'), ('color3', 'Blue')])
# Insert an element at the beginning of the said OrderedDict:
# Updated OrderedDict:
# OrderedDict([('color4', 'Orange'), ('color1', 'Red'),
#              ('color2', 'Green'), ('color3', 'Blue')])
from collections import OrderedDict
color_orderdict = OrderedDict([('color1', 'Red'), ('color2', 'Green'), ('color3', 'Blue')]) 
print("Original OrderedDict:")
print(color_orderdict)
print("Insert an element at the beginning of the said OrderedDict:")
color_orderdict.update({'color4':'Orange'})
color_orderdict.move_to_end('color4', last = False)
print("\nUpdated OrderedDict:")
print(color_orderdict)


# 23. Write a Python program to get the frequency of the tuples in a given list. 
# Sample Output:
# Original list of tuples:
# [(['1', '4'], ['4', '1'], ['3', '4'], ['2', '7'], [
#   '6', '8'], ['5', '8'], ['6', '8'], ['5', '7'], ['2', '7'])]
# Tuples frequency
# ('1', '4') 2
# ('3', '4') 1
# ('2', '7') 2
# ('6', '8') 2
# ('5', '8') 1
# ('5', '7') 1
from collections import Counter
nums = [(['1', '4'], ['4', '1'], ['3', '4'], ['2', '7'], ['6', '8'], ['5','8'], ['6','8'], ['5','7'], ['2','7'])]
print("Original list of tuples:")
print(nums)
result = Counter(tuple(sorted(i)) for i in nums[0])
print("\nTuples","    ","frequency")
for key,val in result.items():
    print(key," ", val)


# 24. Write a Python program to calculate the maximum aggregate from the list of tuples(pairs). 
# Sample Output:
# Original list:
# [('Juan Whelan', 90), ('Sabah Colley', 88), ('Peter Nichols', 7),
#  ('Juan Whelan', 122), ('Sabah Colley', 84)]
# Maximum aggregate value of the said list of tuple pair:
# ('Juan Whelan', 212)
from collections import defaultdict
def max_aggregate(st_data):
    temp = defaultdict(int)
    for name, marks in st_data:
        temp[name] += marks
    return max(temp.items(), key=lambda x: x[1])


students = [('Juan Whelan',90),('Sabah Colley',88),('Peter Nichols',7),('Juan Whelan',122),('Sabah Colley',84)]
print("Original list:")
print(students)
print("\nMaximum aggregate value of the said list of tuple pair:")
print(max_aggregate(students))


# 25. Write a Python program to find the characters in a list of strings which occur more than and less than a given number. 
# Sample Output:
# Original list:
# ['abcd', 'iabhef', 'dsalsdf', 'sdfsas', 'jlkdfgd']
# Characters of the said list of strings which occur more than: 3
# ['a', 'd', 'f']
# Characters of the said list of strings which occur less than: 3
# ['c', 'b', 'h', 'e', 'i', 's', 'l', 'k', 'j', 'g']


def max_aggregate(list_str, N):
    temp = (set(sub) for sub in list_str)
    counts = Counter(chain.from_iterable(temp))
    gt_N = [chr for chr, count in counts.items() if count > N]
    lt_N = [chr for chr, count in counts.items() if count < N]
    return gt_N, lt_N


list_str = ['abcd', 'iabhef', 'dsalsdf', 'sdfsas', 'jlkdfgd']
print("Original list:")
print(list_str)
N = 3
result = max_aggregate(list_str, N)
print("\nCharacters of the said list of strings which occur more than:", N)
print(result[0])
print("\nCharacters of the said list of strings which occur less than:", N)
print(result[1])


# 26. Write a Python program to find the difference between two list including duplicate elements. Use collections module. 
# Sample Output:
# Original lists:
# [3, 3, 4, 7]
from collections import Counter
l1 = [1,1,2,3,3,4,4,5,6,7]
l2 = [1,1,2,4,5,6]
print("Original lists:")
c1 = Counter(l1)
c2 = Counter(l2)
diff = c1-c2
print(list(diff.elements()))


# 27. Write a Python program to remove duplicate words from a given string use collections module. 
# Sample Output:
# Original String:
# Python Exercises Practice Solution Exercises
# After removing duplicate words from the said string:
# Python Exercises Practice Solution
from collections import OrderedDict
text_str = "Python Exercises Practice Solution Exercises"
print("Original String:")
print(text_str)
print("\nAfter removing duplicate words from the said string:")
result = ' '.join(OrderedDict((w,w) for w in text_str.split()).keys())
print(result)


# 28. Write a Python program to create a dictionary grouping a sequence of key-value pairs into a dictionary of lists. Use collections module. 
# Sample Output:
# Original list:
# [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
# Grouping a sequence of key-value pairs into a dictionary of lists:
# defaultdict( < class 'list' > , {'yellow': [1, 3], 'blue': [2, 4], 'red': [1]})
from collections import defaultdict
def grouping_dictionary(l):
    d = defaultdict(list)
    for k, v in l:
        d[k].append(v)
    return d
colors = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
print("Original list:")
print(colors)
print("\nGrouping a sequence of key-value pairs into a dictionary of lists:")
print(grouping_dictionary(colors))


# 29. Write a Python program to get the frequency of the elements in a given list of lists. Use collections module. 
# Sample Output:
# Original list of lists:
# [[1, 2, 3, 2], [4, 5, 6, 2], [7, 1, 9, 5]]
# Frequency of the elements in the said list of lists:
# Counter({2: 3, 1: 2, 5: 2, 3: 1, 4: 1, 6: 1, 7: 1, 9: 1})
from collections import Counter
from itertools import chain
nums = [
        [1,2,3,2],
        [4,5,6,2],
        [7,1,9,5],
       ]
    
print("Original list of lists:")
print(nums)
print("\nFrequency of the elements in the said list of lists:")
result = Counter(chain.from_iterable(nums))
print(result)


# 30. Write a Python program to count the occurrence of each element of a given list. 
# Sample Output:
# Original List:
# ['Green', 'Red', 'Blue', 'Red', 'Orange', 'Black', 'Black', 'White', 'Orange']
# Count the occurrence of each element of the said list:
# Counter({'Red': 2, 'Orange': 2, 'Black': 2, 'Green': 1, 'Blue': 1, 'White': 1})
# Original List:
# [3, 5, 0, 3, 9, 5, 8, 0, 3, 8, 5, 8, 3, 5, 8, 1, 0, 2]
# Count the occurrence of each element of the said list:
# Counter({3: 4, 5: 4, 8: 4, 0: 3, 9: 1, 1: 1, 2: 1})
colors = ['Green', 'Red', 'Blue', 'Red',
          'Orange', 'Black', 'Black', 'White', 'Orange']
print("Original List:")
print(colors)
print("Count the occurrence of each element of the said list:")
result = Counter(colors)
print(result)
nums = [3, 5, 0, 3, 9, 5, 8, 0, 3, 8, 5, 8, 3, 5, 8, 1, 0, 2]
print("\nOriginal List:")
print(nums)
print("Count the occurrence of each element of the said list:")
result = Counter(nums)
print(result)


# 31. Write a Python program to count the most common words in a dictionary. 
# Sample Output:
# [('pink', 6), ('black', 5), ('white', 5), ('red', 4)]
words = [
   'red', 'green', 'black', 'pink', 'black', 'white', 'black', 'eyes',
   'white', 'black', 'orange', 'pink', 'pink', 'red', 'red', 'white', 'orange',
   'white', "black", 'pink', 'green', 'green', 'pink', 'green', 'pink',
   'white', 'orange', "orange", 'red'
]
from collections import Counter
word_counts = Counter(words)
top_four = word_counts.most_common(4)
print(top_four)


# 32. Write a Python program to find the class wise roll number from a tuple-of-tuples. 
# Sample Output:
# defaultdict( < class 'list' > , {'V': [1, 2], 'VI': [1, 2, 3], 'VII': [1]})
from collections import defaultdict
classes = (
    ('V', 1),
    ('VI', 1),
    ('V', 2),
    ('VI', 2),
    ('VI', 3),
    ('VII', 1),
)

class_rollno = defaultdict(list)

for class_name, roll_id in classes:
    class_rollno[class_name].append(roll_id)

print(class_rollno)


# 33. Write a Python program to count the number of students of individual class. 
# Sample Output:
# Counter({'VI': 3, 'V': 2, 'VII': 1})
from collections import Counter
classes = (
    ('V', 1),
    ('VI', 1),
    ('V', 2),
    ('VI', 2),
    ('VI', 3),
    ('VII', 1),
)
students = Counter(class_name for class_name, no_students in classes)
print(students)


# 34. Write a Python program to create an instance of an OrderedDict using a given dictionary. Sort the dictionary during the creation and print the members of the dictionary in reverse order. 
# Sample Output:
# Afghanistan 93
# Albania 355
# Algeria 213
# Andorra 376
# Angola 244
# In reverse order:
# Angola 244
# Andorra 376
# Algeria 213
# Albania 355
# Afghanistan 93
from collections import OrderedDict
dict = {'Afghanistan': 93, 'Albania': 355, 'Algeria': 213, 'Andorra': 376, 'Angola': 244}
new_dict = OrderedDict(dict.items())
for key in new_dict:
    print (key, new_dict[key])

print("\nIn reverse order:")
for key in reversed(new_dict):
    print (key, new_dict[key])


# 35. Write a Python program to group a sequence of key-value pairs into a dictionary of lists. 
# Sample Output:
# [('v', [1, 3]), ('vi', [2, 4]), ('vii', [1])]
from collections import defaultdict
class_roll = [('v', 1), ('vi', 2), ('v', 3), ('vi', 4), ('vii', 1)]
d = defaultdict(list)
for k, v in class_roll:
    d[k].append(v)
print(sorted(d.items()))


# 36. Write a Python program to compare two unordered lists(not sets). 
# Sample Output:
# False
def compare_lists(x, y):
    return Counter(x) == Counter(y)
n1 = [20, 10, 30, 10, 20, 30]
n2 = [30, 20, 10, 30, 20, 50]
print(compare_lists(n1, n2))
