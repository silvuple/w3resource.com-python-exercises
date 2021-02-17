# Collections module implements specialized container datatypes providing alternatives to Python's general purpose built-in containers, dict, list, set, and tuple.

# 1. Write a Python program that iterate over elements repeating each as many times as its count. 
# Sample Output: ['p', 'p', 'p', 'p', 'q', 'q']



# 2. Write a Python program to find the most common elements and their counts of a specified text. 
# Original string: lkseropewdssafsdfafkpwe
# Most common three characters of the said string:
# [('s', 4), ('e', 3), ('f', 3)]


# 3. Write a Python program to create a new deque with three items and iterate over the deque's elements. 
# Sample Output:
# a
# e
# i
# o
# u


# 4. Write a Python program to find the occurrences of 10 most common words in a given text. 
# Sample Output:
# [('Python', 6), ('the', 6), ('and', 5), ('We', 2), ('with', 2),
#  ('The', 1), ('Software', 1), ('Foundation', 1), ('PSF', 1), ('is', 1)]


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


# 9. Write a Python program to add more number of elements to a deque object from an iterable object. 
# Sample Output:
# Even numbers:
# deque([2, 4, 6, 8, 10])
# More even numbers:
# deque([2, 4, 6, 8, 10, 12, 14, 16, 18, 20])


# 10. Write a Python program to remove all the elements of a given deque object. 
# Sample Output:
# Original Deque object with odd numbers:
# deque([1, 3, 5, 7, 9])
# Deque length: 5
# Deque object after removing all numbers - deque([])
# Deque length: 0


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


# 12. Write a Python program to count the number of times a specific element presents in a deque object. 
# Sample Output:
# Number of 2 in the sequence
# 5
# Number of 4 in the sequence
# 4


# 13. Write a Python program to rotate a Deque Object specified number(positive) of times. 
# Sample Output:
# Deque before rotation:
# deque([2, 4, 6, 8, 10])
# Deque after 1 positive rotation:
# deque([10, 2, 4, 6, 8])
# Deque after 2 positive rotations:
# deque([6, 8, 10, 2, 4])


# 14. Write a Python program to rotate a Deque Object specified number(negative) of times. 
# Sample Output:
# Deque before rotation:
# deque([2, 4, 6, 8, 10])
# Deque after 1 negative rotation:
# deque([4, 6, 8, 10, 2])
# Deque after 2 negative rotations:
# deque([8, 10, 2, 4, 6])


# 15. Write a Python program to find the most common element of a given list. 
# Sample Output:
# Original list:
# ['PHP', 'PHP', 'Python', 'PHP', 'Python', 'JS', 'Python', 'Python', 'PHP', 'Python']
# Most common element of the said list:
# Python


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


# 17. Write a Python program to find the majority element from a given array of size n using Collections module. 
# Sample Output:
# 10


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


# 19. Write a Python program to break a given list of integers into sets of a given positive number. Return true or false. 
# Sample Output:
# Original list: [1, 2, 3, 4, 5, 6, 7, 8]
# Number to devide the said list: 4
# True
# Original list: [1, 2, 3, 4, 5, 6, 7, 8]
# Number to devide the said list: 3
# False


# 20. Write a Python program to find the item with maximum frequency in a given list. 
# Sample Output:
# Original list:
# [2, 3, 8, 4, 7, 9, 8, 2, 6, 5, 1, 6, 1, 2, 3, 2, 4, 6, 9, 1, 2]
# Item with maximum frequency of the said list:
# (2, 5)


# 21. Write a Python program to count most and least common characters in a given string. 
# Sample Output:
# Original string:
# hello world
# Most common character of the said string: l
# Least common character of the said string: h


# 22. Write a Python program to insert an element at the beginning of a given OrderedDictionary. 
# Sample Output:
# Original OrderedDict:
# OrderedDict([('color1', 'Red'), ('color2', 'Green'), ('color3', 'Blue')])
# Insert an element at the beginning of the said OrderedDict:
# Updated OrderedDict:
# OrderedDict([('color4', 'Orange'), ('color1', 'Red'),
#              ('color2', 'Green'), ('color3', 'Blue')])


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


# 24. Write a Python program to calculate the maximum aggregate from the list of tuples(pairs). 
# Sample Output:
# Original list:
# [('Juan Whelan', 90), ('Sabah Colley', 88), ('Peter Nichols', 7),
#  ('Juan Whelan', 122), ('Sabah Colley', 84)]
# Maximum aggregate value of the said list of tuple pair:
# ('Juan Whelan', 212)


# 25. Write a Python program to find the characters in a list of strings which occur more than and less than a given number. 
# Sample Output:
# Original list:
# ['abcd', 'iabhef', 'dsalsdf', 'sdfsas', 'jlkdfgd']
# Characters of the said list of strings which occur more than: 3
# ['a', 'd', 'f']
# Characters of the said list of strings which occur less than: 3
# ['c', 'b', 'h', 'e', 'i', 's', 'l', 'k', 'j', 'g']


# 26. Write a Python program to find the difference between two list including duplicate elements. Use collections module. 
# Sample Output:
# Original lists:
# [3, 3, 4, 7]


# 27. Write a Python program to remove duplicate words from a given string use collections module. 
# Sample Output:
# Original String:
# Python Exercises Practice Solution Exercises
# After removing duplicate words from the said string:
# Python Exercises Practice Solution


# 28. Write a Python program to create a dictionary grouping a sequence of key-value pairs into a dictionary of lists. Use collections module. 
# Sample Output:
# Original list:
# [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
# Grouping a sequence of key-value pairs into a dictionary of lists:
# defaultdict( < class 'list' > , {'yellow': [1, 3], 'blue': [2, 4], 'red': [1]})


# 29. Write a Python program to get the frequency of the elements in a given list of lists. Use collections module. 
# Sample Output:
# Original list of lists:
# [[1, 2, 3, 2], [4, 5, 6, 2], [7, 1, 9, 5]]
# Frequency of the elements in the said list of lists:
# Counter({2: 3, 1: 2, 5: 2, 3: 1, 4: 1, 6: 1, 7: 1, 9: 1})


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


# 31. Write a Python program to count the most common words in a dictionary. 
# Sample Output:
# [('pink', 6), ('black', 5), ('white', 5), ('red', 4)]


# 32. Write a Python program to find the class wise roll number from a tuple-of-tuples. 
# Sample Output:
# defaultdict( < class 'list' > , {'V': [1, 2], 'VI': [1, 2, 3], 'VII': [1]})


# 33. Write a Python program to count the number of students of individual class. 
# Sample Output:
# Counter({'VI': 3, 'V': 2, 'VII': 1})


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


# 35. Write a Python program to group a sequence of key-value pairs into a dictionary of lists. 
# Sample Output:
# [('v', [1, 3]), ('vi', [2, 4]), ('vii', [1])]


# 36. Write a Python program to compare two unordered lists(not sets). 
# Sample Output:
# False

