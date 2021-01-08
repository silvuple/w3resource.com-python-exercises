'''
ALL CODE SOLUTIONS BY HIGHNESS_ATHARVA (ATHARVA SHAH) 
'''

# 1. Write a Python program to create a lambda function that adds 15 to a given number passed in as an argument, also create a lambda function that multiplies argument x with argument y and print the result. 
# Sample Output:
# 25
# 48
r = lambda a : a + 15
print(r(10))
r = lambda x, y : x * y
print(r(12, 4))

# 2. Write a Python program to create a function that takes one argument, and that argument will be multiplied with an unknown given number. 
# Sample Output:
# Double the number of 15 = 30
# Triple the number of 15 = 45
# Quadruple the number of 15 = 60
# Quintuple the number 15 = 75
def func_compute(n):
 return lambda x : x * n
result = func_compute(2)
print("Double the number of 15 =", result(15))
result = func_compute(3)
print("Triple the number of 15 =", result(15))
result = func_compute(4)
print("Quadruple the number of 15 =", result(15))
result = func_compute(5)
print("Quintuple the number 15 =", result(15))

# 3. Write a Python program to sort a list of tuples using Lambda.
# Original list of tuples:
# [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]
# Sorting the List of Tuples:
# [('Social sciences', 82), ('English', 88), ('Science', 90), ('Maths', 97)]
subject_marks = [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]
print("Original list of tuples:")
print(subject_marks)
subject_marks.sort(key = lambda x: x[1])
print("\nSorting the List of Tuples:")
print(subject_marks)

# 4. Write a Python program to sort a list of dictionaries using Lambda. 
# Original list of dictionaries :
# [{'make': 'Nokia', 'model': 216, 'color': 'Black'}, {'make': 'Mi Max', 'model': '2', 'color': 'Gold'}, {'make': 'Samsung', 'model': 7, 'color': 'Blue'}]
# Sorting the List of dictionaries :
# [{'make': 'Nokia', 'model': 216, 'color': 'Black'}, {'make': 'Samsung', 'model': 7, 'color': 'Blue'}, {'make': 'Mi Max', 'model': '2', 'color': 'Gold'}]
models = [{'make':'Nokia', 'model':216, 'color':'Black'}, {'make':'Mi Max', 'model':'2', 'color':'Gold'}, {'make':'Samsung', 'model': 7, 'color':'Blue'}]
print("Original list of dictionaries :")
print(models)
sorted_models = sorted(models, key = lambda x: x['color'])
print("\nSorting the List of dictionaries :")
print(sorted_models)

# 5. Write a Python program to filter a list of integers using Lambda. 
# Original list of integers:
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Even numbers from the said list:
# [2, 4, 6, 8, 10]
# Odd numbers from the said list:
# [1, 3, 5, 7, 9]
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("Original list of integers: ", nums)

print("\nEven numbers from the said list:")
even_nums = list(filter(lambda x: x%2 == 0, nums))
print(even_nums)
print("\nOdd numbers from the said list:")
odd_nums = list(filter(lambda x: x%2 != 0, nums))
print(odd_nums)

# 6. Write a Python program to square and cube every number in a given list of integers using Lambda. 
# Original list of integers:
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Square every number of the said list:
# [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
# Cube every number of the said list:
# [1, 8, 27, 64, 125, 216, 343, 512, 729, 1000]
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("Original list of integers:")
print(nums)
print("\nSquare every number of the said list:")
square_nums = list(map(lambda x: x ** 2, nums))
print(square_nums)
print("\nCube every number of the said list:")
cube_nums = list(map(lambda x: x ** 3, nums))
print(cube_nums)

# 7. Write a Python program to find if a given string starts with a given character using Lambda. 
# Sample Output:
# True
# False
starts_with = lambda x: True if x.startswith('P') else False
print(starts_with('Python'))
starts_with = lambda x: True if x.startswith('P') else False
print(starts_with('Java'))

# 8. Write a Python program to extract year, month, date and time using Lambda. 
# Sample Output:
# 2020-01-15 09:03:32.744178
# 2020
# 1
# 15
# 09:03:32.744178
import datetime
now = datetime.datetime.now()
print(now)
year, month, day, t = lambda x: x.year, lambda x: x.month, lambda x: x.day, lambda x: x.time() 
print(year(now))
print(month(now))
print(day(now))
print(t(now))

# 9. Write a Python program to check whether a given string is number or not using Lambda. 
is_num = lambda q: q.replace('.','',1).isdigit()
#Here, we are eliminating . with  '' since it is True in isdigit() checking
print(is_num('26587'))
print(is_num('4.2365'))
print(is_num('-12547'))
print(is_num('00'))
print(is_num('A001'))
print(is_num('001'))
print("\nPrint checking numbers:")
is_num1 = lambda r: is_num(r[1:]) if r[0]=='-' else is_num(r)
print(is_num1('-16.4'))
print(is_num1('-24587.11'))

# 10. Write a Python program to create Fibonacci series upto n using Lambda. 
# Fibonacci series upto 2:
# [0, 1]
# Fibonacci series upto 5:
# [0, 1, 1, 2, 3]
# Fibonacci series upto 6:
# [0, 1, 1, 2, 3, 5]
# Fibonacci series upto 9:
# [0, 1, 1, 2, 3, 5, 8, 13, 21]
from functools import reduce
#A bit complex workaround
fib_series = lambda n: reduce(lambda x, _: x+[x[-1]+x[-2]], range(n-2), [0, 1])
 
print("Fibonacci series upto 2:")
print(fib_series(2))
print("\nFibonacci series upto 5:")
print(fib_series(5))
print("\nFibonacci series upto 6:")
print(fib_series(6))
print("\nFibonacci series upto 9:")
print(fib_series(9))

# 11. Write a Python program to find intersection of two given arrays using Lambda. 
# Original arrays:
# [1, 2, 3, 5, 7, 8, 9, 10]
# [1, 2, 4, 8, 9]
# Intersection of the said arrays: [1, 2, 8, 9]
array_nums1 = [1, 2, 3, 5, 7, 8, 9, 10]
array_nums2 = [1, 2, 4, 8, 9]
print("Original arrays:")
print(array_nums1)
print(array_nums2)
result = list(filter(lambda x: x in array_nums1, array_nums2)) 
print ("\nIntersection of the said arrays: ",result)

# 12. Write a Python program to rearrange positive and negative numbers in a given array using Lambda. 
# Original arrays:
# [-1, 2, -3, 5, 7, 8, 9, -10]
# Rearrange positive and negative numbers of the said array:
# [2, 5, 7, 8, 9, -10, -3, -1]
array_nums = [-1, 2, -3, 5, 7, 8, 9, -10]
print("Original arrays:")
print(array_nums)
result = sorted(array_nums, key = lambda i: 0 if i == 0 else -1 / i)
print("\nRearrange positive and negative numbers of the said array:")
print(result)

# 13. Write a Python program to count the even, odd numbers in a given array of integers using Lambda. 
# Original arrays:
# [1, 2, 3, 5, 7, 8, 9, 10]
# Number of even numbers in the above array: 3
# Number of odd numbers in the above array: 5
array_nums = [1, 2, 3, 5, 7, 8, 9, 10]
print("Original arrays:")
print(array_nums)
odd_ctr = len(list(filter(lambda x: (x%2 != 0) , array_nums)))
even_ctr = len(list(filter(lambda x: (x%2 == 0) , array_nums)))
print("\nNumber of even numbers in the above array: ", even_ctr)
print("\nNumber of odd numbers in the above array: ", odd_ctr)

# 14. Write a Python program to find the values of length six in a given list using Lambda. 
# Sample Output:
# Monday
# Friday
# Sunday
weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
days = filter(lambda day: day if len(day)==6 else '', weekdays)
for d in days:
  print(d)

# 15. Write a Python program to add two given lists using map and lambda. 
# Original list:
# [1, 2, 3]
# [4, 5, 6]
# Result: after adding two list
# [5, 7, 9]
nums1 = [1, 2, 3]
nums2 = [4, 5, 6]
print("Original list:")
print(nums1)
print(nums2)
result = map(lambda x, y: x + y, nums1, nums2)
print("\nResult: after adding two list")
print(list(result))

# 16. Write a Python program to find the second lowest grade of any student(s) from the given names and grades of each student using lists and lambda. Input number of students, names and grades of each student. 
# Input number of students: 5
# Name: S ROY
# Grade: 1
# Name: B BOSE
# Grade: 3
# Name: N KAR
# Grade: 2
# Name: C DUTTA
# Grade: 1
# Name: G GHOSH
# Grade: 1
# Names and Grades of all students:
# [['S ROY', 1.0], ['B BOSE', 3.0], ['N KAR', 2.0], ['C DUTTA', 1.0], ['G GHOSH', 1.0]]
# Second lowest grade: 2.0
# Names:
# N KAR
students = []
sec_name = []
second_low = 0
n = int(input("Input number of students: "))
for _ in range(n):
   s_name = input("Name: ")
   score = float(input("Grade: "))
   students.append([s_name,score])
print("\nNames and Grades of all students:")
print(students)
order =sorted(students, key = lambda x: int(x[1]))
for i in range(n):
   if order[i][1] != order[0][1]:
       second_low = order[i][1]
       break
print("\nSecond lowest grade: ",second_low)
sec_student_name = [x[0] for x in order if x[1] == second_low]
sec_student_name.sort()
print("\nNames:")
for s_name in sec_student_name:
   print(s_name)

# 17. Write a Python program to find numbers divisible by nineteen or thirteen from a list of numbers using Lambda. 
# Orginal list:
# [19, 65, 57, 39, 152, 639, 121, 44, 90, 190]
# Numbers of the above list divisible by nineteen or thirteen:
# [19, 65, 57, 39, 152, 190]
nums = [19, 65, 57, 39, 152, 639, 121, 44, 90, 190]
print("Orginal list:")
print(nums) 
result = list(filter(lambda x: (x % 19 == 0 or x % 13 == 0), nums)) 
print("\nNumbers of the above list divisible by nineteen or thirteen:")
print(result)

# 18. Write a Python program to find palindromes in a given list of strings using Lambda. 
# Orginal list of strings:
# ['php', 'w3r', 'Python', 'abcd', 'Java', 'aaa']
# List of palindromes:
# ['php', 'aaa']
texts = ["php", "w3r", "Python", "abcd", "Java", "aaa"]
print("Orginal list of strings:")
print(texts) 
result = list(filter(lambda x: (x == "".join(reversed(x))), texts)) 
print("\nList of palindromes:")
print(result) 

# 19. Write a Python program to find all anagrams of a string in a given list of strings using lambda. 
# Orginal list of strings:
# ['bcda', 'abce', 'cbda', 'cbea', 'adcb']
# Anagrams of 'abcd' in the above string:
# ['bcda', 'cbda', 'adcb']
from collections import Counter  
texts = ["bcda", "abce", "cbda", "cbea", "adcb"]
str = "abcd"
print("Orginal list of strings:")
print(texts) 
result = list(filter(lambda x: (Counter(str) == Counter(x)), texts)) 
print("\nAnagrams of 'abcd' in the above string: ")
print(result)

# 20. Write a Python program to find the numbers of a given string and store them in a list, display the numbers which are bigger than the length of the list in sorted form. Use lambda function to solve the problem. 
# Original string: sdf 23 safs8 5 sdfsd8 sdfs 56 21sfs 20 5
# Numbers in sorted form:
# 20 23 56
str1 = "sdf 23 safs8 5 sdfsd8 sdfs 56 21sfs 20 5"
print("Original string: ",str1)
str_num=[i for i in str1.split(' ')]
lenght=len(str_num)
numbers=sorted([int(x) for x in str_num if x.isdigit()])
print('Numbers in sorted form:')
for i in ((filter(lambda x:x>lenght,numbers))):
    print(i,end=' ')

# 21. Write a Python program that multiply each number of given list with a given number using lambda function. Print the result. 
# Original list: [2, 4, 6, 9, 11]
# Given number: 2
# Result:
# 4 8 12 18 22
nums = [2, 4, 6, 9 , 11]
n = 2
print("Original list: ", nums)
print("Given number: ", n)
filtered_numbers=list(map(lambda number:number*n,nums))
print("Result:")
print(' '.join(map(str,filtered_numbers)))

# 22. Write a Python program that sum the length of the names of a given list of names after removing the names that starts with an lowercase letter. Use lambda function. 
# Result:
# 16
sample_names = ['sally', 'Dylan', 'rebecca', 'Diana', 'Joanne', 'keith']
sample_names=list(filter(lambda el:el[0].isupper() and el[1:].islower(),sample_names))
print("Result:")
print(len(''.join(sample_names)))

# 23. Write a Python program to calculate the sum of the positive and negative numbers of a given list of numbers using lambda function. 
# Original list: [2, 4, -6, -9, 11, -12, 14, -5, 17]
# Sum of the positive numbers: -32
# Sum of the negative numbers: 48
nums = [2, 4, -6, -9, 11, -12, 14, -5, 17]
print("Original list:",nums)

total_negative_nums = list(filter(lambda nums:nums<0,nums))
total_positive_nums = list(filter(lambda nums:nums>0,nums))

print("Sum of the positive numbers: ",sum(total_negative_nums))
print("Sum of the negative numbers: ",sum(total_positive_nums))

# 24. Write a Python program to find numbers within a given range where every number is divisible by every digit it contains. 
# Sample Output:
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15, 22]
def divisible_by_digits(start_num, end_num):
    return [n for n in range(start_num, end_num+1) \
                if not any(map(lambda x: int(x) == 0 or n%int(x) != 0, str(n)))]
print(divisible_by_digits(1,22))

# 25. Write a Python program to create the next bigger number by rearranging the digits of a given number. 
# Original number: 12
# Next bigger number: 21
# Original number: 10
# Next bigger number: False
# Original number: 201
# Next bigger number: 210
# Original number: 102
# Next bigger number: 120
# Original number: 445
# Next bigger number: 454
def rearrange_bigger(n):
    #Break the number into digits and store in a list
    nums = list(str(n))
    for i in range(len(nums)-2,-1,-1):
        if nums[i] < nums[i+1]:
            z = nums[i:]
            y = min(filter(lambda x: x > z[0], z))
            z.remove(y)
            z.sort()
            nums[i:] = [y] + z
            return int("".join(nums))
    return False
n = 12
print("Original number:",n)
print("Next bigger number:",rearrange_bigger(n))
n = 10
print("\nOriginal number:",n)
print("Next bigger number:",rearrange_bigger(n))
n = 201
print("\nOriginal number:",n)
print("Next bigger number:",rearrange_bigger(n))
n = 102
print("\nOriginal number:",n)
print("Next bigger number:",rearrange_bigger(n))
n = 445
print("\nOriginal number:",n)
print("Next bigger number:",rearrange_bigger(n))

# 26. Write a Python program to find the list with maximum and minimum length using lambda. 
# Original list:
# [[0], [1, 3], [5, 7], [9, 11], [13, 15, 17]]
# List with maximum length of lists:
# (3, [13, 15, 17])
# List with minimum length of lists:
# (1, [0])
def max_length_list(input_list):
    max_length = max(len(x) for x in input_list )   
    max_list = max(input_list, key = lambda i: len(i))    
    return(max_length, max_list)
    
def min_length_list(input_list):
    min_length = min(len(x) for x in input_list )  
    min_list = min(input_list, key = lambda i: len(i))
    return(min_length, min_list)
      
list1 = [[0], [1, 3], [5, 7], [9, 11], [13, 15, 17]]
print("Original list:")
print(list1)
print("\nList with maximum length of lists:")
print(max_length_list(list1))
print("\nList with minimum length of lists:")
print(min_length_list(list1))

# 27. Write a Python program to sort each sublist of strings in a given list of lists using lambda. 
# Original list:
# [['green', 'orange'], ['black', 'white'], ['white', 'black', 'orange']]
# After sorting each sublist of the said list of lists:
# [['green', 'orange'], ['black', 'white'], ['black', 'orange', 'white']]
def sort_sublists(input_list):
    result = [sorted(x, key = lambda x:x[0]) for x in input_list] 
    return result
color1 = [["green", "orange"], ["black", "white"], ["white", "black", "orange"]]
print("\nOriginal list:")
print(color1)  
print("\nAfter sorting each sublist of the said list of lists:")
print(sort_sublists(color1))

# 28. Write a Python program to sort a given list of lists by length and value using lambda. 
# Original list:
# [[2], [0], [1, 3], [0, 7], [9, 11], [13, 15, 17]]
# Sort the list of lists by length and value:
# [[0], [2], [0, 7], [1, 3], [9, 11], [13, 15, 17]]
def sort_sublists(input_list):
    result = sorted(input_list, key=lambda l: (len(l), l))
    return result
list1 = [[2], [0], [1, 3], [0, 7], [9, 11], [13, 15, 17]]
print("Original list:")
print(list1)
print("\nSort the list of lists by length and value:")
print(sort_sublists(list1))

# 29. Write a Python program to find the maximum value in a given heterogeneous list using lambda. 
# Original list:
# ['Python', 3, 2, 4, 5, 'version']
# Maximum values in the said list using lambda:
# 5
def max_val(list_val):
     max_val = max(list_val, key = lambda i: (isinstance(i, int), i))  
     return(max_val)

list_val = ['Python', 3, 2, 4, 5, 'version'] 
print("Original list:")
print(list_val)
print("\nMaximum values in the said list using lambda:")
print(max_val(list_val))

# 30. Write a Python program to sort a given matrix in ascending order according to the sum of its rows using lambda. 
# Original Matrix:
# [[1, 2, 3], [2, 4, 5], [1, 1, 1]]
# Sort the said matrix in ascending order according to the sum of its rows
# [[1, 1, 1], [1, 2, 3], [2, 4, 5]]
# Original Matrix:
# [[1, 2, 3], [-2, 4, -5], [1, -1, 1]]
# Sort the said matrix in ascending order according to the sum of its rows
# [[-2, 4, -5], [1, -1, 1], [1, 2, 3]]
def sort_matrix(M):
    result = sorted(M, key=lambda matrix_row: sum(matrix_row)) 
    return result

matrix1 = [[1, 2, 3], [2, 4, 5], [1, 1, 1]]
matrix2 = [[1, 2, 3], [-2, 4, -5], [1, -1, 1]]

print("Original Matrix:")
print(matrix1)
print("\nSort the said matrix in ascending order according to the sum of its rows") 
print(sort_matrix(matrix1))
print("\nOriginal Matrix:")
print(matrix2) 
print("\nSort the said matrix in ascending order according to the sum of its rows") 
print(sort_matrix(matrix2))


# 31. Write a Python program to extract specified size of strings from a give list of string values using lambda. 
# Original list:
# ['Python', 'list', 'exercises', 'practice', 'solution']
# length of the string to extract:
# 8
# After extracting strings of specified length from the said list:
# ['practice', 'solution']
def extract_string(str_list1, l):
    result = list(filter(lambda e: len(e) == l, str_list1))
    return result

str_list1 = ['Python', 'list', 'exercises', 'practice', 'solution'] 
print("Original list:")
print(str_list1)
l = 8
print("\nlength of the string to extract:")
print(l)
print("\nAfter extracting strings of specified length from the said list:")
print(extract_string(str_list1 , l))

# 32. Write a Python program to count float number in a given mixed list using lambda. 
# Original list:
# [1, 'abcd', 3.12, 1.2, 4, 'xyz', 5, 'pqr', 7, -5, -12.22]
# Number of floats in the said mixed list:
# 3
def count_integer(list1):
    ert = list(map(lambda i: isinstance(i, float), list1)) 
    result = len([e for e in ert if e])         
    return result
list1 = [1, 'abcd', 3.12, 1.2, 4, 'xyz', 5, 'pqr', 7, -5, -12.22]
print("Original list:")
print(list1)
print("\nNumber of floats in the said mixed list:")
print(count_integer(list1))

# 33. Write a Python program to check whether a given string contains a capital letter, a lower case letter, a number and a minimum length using lambda. 
# Input the string: W3resource
# ['Valid string.']
def check_string(str1):
    messg = [
    lambda str1: any(x.isupper() for x in str1) or 'String must have 1 upper case character.',
    lambda str1: any(x.islower() for x in str1) or 'String must have 1 lower case character.',
    lambda str1: any(x.isdigit() for x in str1) or 'String must have 1 number.',
    lambda str1: len(str1) >= 7                 or 'String length should be atleast 8.',]
    result = [x for x in [i(str1) for i in messg] if x != True]
    if not result:
        result.append('Valid string.')
    return result    
s = input("Input the string: ")
print(check_string(s))

# 34. Write a Python program to filter the height and width of students, which are stored in a dictionary using lambda. 
# Original Dictionary:
# {'Cierra Vega': (6.2, 70), 'Alden Cantrell': (5.9, 65), 'Kierra Gentry': (6.0, 68), 'Pierre Cox': (5.8, 66)}
# Height> 6ft and Weight> 70kg:
# {'Cierra Vega': (6.2, 70)}
def filter_data(students):
    result = dict(filter(lambda x: (x[1][0], x[1][1]) > (6.0, 70), students.items()))
    return result  
students = {'Cierra Vega': (6.2, 70), 'Alden Cantrell': (5.9, 65), 'Kierra Gentry': (6.0, 68), 'Pierre Cox': (5.8, 66)}
print("Original Dictionary:")
print(students)
print("\nHeight> 6ft and Weight> 70kg:")
print(filter_data(students))

# 35. Write a Python program to check whether a specified list is sorted or not using lambda. 
# Original list:
# [1, 2, 4, 6, 8, 10, 12, 14, 16, 17]
# Is the said list is sorted!
# True
# Original list:
# [1, 2, 4, 6, 8, 10, 12, 14, 16, 17]
# Is the said list is sorted!
# False
def is_sort_list(nums, key=lambda x: x):
    for i, e in enumerate(nums[1:]):
        if key(e) < key(nums[i]): 
            return False
    return True
nums1 = [1,2,4,6,8,10,12,14,16,17]
print ("Original list:")
print(nums1)
print("\nIs the said list is sorted!")
print(is_sort_list(nums1)) 
nums2 = [2,3,8,4,7,9,8,2,6,5,1,6,1,2,3,4,6,9,1,2]
print ("\nOriginal list:")
print(nums1)
print("\nIs the said list is sorted!")
print(is_sort_list(nums2))

# 36. Write a Python program to extract the nth element from a given list of tuples using lambda. 
# Original list:
# [('Greyson Fulton', 98, 99), ('Brady Kent', 97, 96), ('Wyatt Knott', 91, 94), ('Beau Turnbull', 94, 98)]
# Extract nth element ( n = 0 ) from the said list of tuples:
# ['Greyson Fulton', 'Brady Kent', 'Wyatt Knott', 'Beau Turnbull']
# Extract nth element ( n = 2 ) from the said list of tuples:
# [99, 96, 94, 98]
def extract_nth_element(test_list, n):
    result = list(map (lambda x:(x[n]), test_list))
    return result
students = [('Greyson Fulton', 98, 99), ('Brady Kent', 97, 96), ('Wyatt Knott', 91, 94), ('Beau Turnbull', 94, 98)] 
print ("Original list:")
print(students)
n = 0
print("\nExtract nth element ( n =",n,") from the said list of tuples:")
print(extract_nth_element(students, n))
n = 2
print("\nExtract nth element ( n =",n,") from the said list of tuples:")
print(extract_nth_element(students, n))

# 37. Write a Python program to sort a list of lists by a given index of the inner list using lambda. 
# Original list:
# [('Greyson Fulton', 98, 99), ('Brady Kent', 97, 96), ('Wyatt Knott', 91, 94), ('Beau Turnbull', 94, 98)]
# Sort the said list of lists by a given index ( Index = 0 ) of the inner list
# [('Beau Turnbull', 94, 98), ('Brady Kent', 97, 96), ('Greyson Fulton', 98, 99), ('Wyatt Knott', 91, 94)]
# Sort the said list of lists by a given index ( Index = 2 ) of the inner list
# [('Wyatt Knott', 91, 94), ('Brady Kent', 97, 96), ('Beau Turnbull', 94, 98), ('Greyson Fulton', 98, 99)]
def index_on_inner_list(list_data, index_no):
    result = sorted(list_data, key=lambda x: x[index_no])
    return result
students = [('Greyson Fulton', 98, 99), ('Brady Kent', 97, 96), ('Wyatt Knott', 91, 94), ('Beau Turnbull', 94, 98)] 
print ("Original list:")
print(students)
index_no = 0
print("\nSort the said list of lists by a given index","( Index = ",index_no,") of the inner list")
print(index_on_inner_list(students, index_no))
index_no = 2
print("\nSort the said list of lists by a given index","( Index = ",index_no,") of the inner list")
print(index_on_inner_list(students, index_no))

# 38. Write a Python program to remove all elements from a given list present in another list using lambda. 
# Original lists:
# list1: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# list2: [2, 4, 6, 8]
# Remove all elements from 'list1' present in 'list2:
# [1, 3, 5, 7, 9, 10]
def index_on_inner_list(list1, list2):
    result = list(filter(lambda x: x not in list2, list1))
    return result
list1 = [1,2,3,4,5,6,7,8,9,10]
list2 = [2,4,6,8]
print("Original lists:")
print("list1:", list1)
print("list2:", list2)
print("\nRemove all elements from 'list1' present in 'list2:")
print(index_on_inner_list(list1, list2))


# 39. Write a Python program to find the elements of a given list of strings that contain specific substring using lambda. 
# Original list:
# ['red', 'black', 'white', 'green', 'orange']
# Substring to search:
# ack
# Elements of the said list that contain specific substring:
# ['black']
# Substring to search:
# abc
# Elements of the said list that contain specific substring:
# []
def find_substring(str1, sub_str):
    result = list(filter(lambda x: sub_str in x, str1))
    return result
colors = ["red", "black", "white", "green", "orange"]
print("Original list:")
print(colors)

sub_str = "ack"
print("\nSubstring to search:")
print(sub_str)
print("Elements of the said list that contain specific substring:")
print(find_substring(colors, sub_str))
sub_str = "abc"
print("\nSubstring to search:")
print(sub_str)
print("Elements of the said list that contain specific substring:")
print(find_substring(colors, sub_str))

# 40. Write a Python program to find the nested lists elements, which are present in another list using lambda. 
# Original lists: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
# [[12, 18, 23, 25, 45], [7, 11, 19, 24, 28], [1, 5, 8, 18, 15, 16]]
# Intersection of said nested lists:
# [[12], [7, 11], [1, 5, 8]]
def intersection_nested_lists(l1, l2):
    result = [list(filter(lambda x: x in l1, sublist)) for sublist in l2]
    return result
nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
nums2 = [[12, 18, 23, 25, 45], [7, 11, 19, 24, 28], [1, 5, 8, 18, 15, 16]]
print("\nOriginal lists:")
print(nums1)
print(nums2)
print("\nIntersection of said nested lists:")
print(intersection_nested_lists(nums1, nums2))

# 41. Write a Python program to reverse strings in a given list of string values using lambda. 
# Original lists:
# ['Red', 'Green', 'Blue', 'White', 'Black']
# Reverse strings of the said given list:
# ['deR', 'neerG', 'eulB', 'etihW', 'kcalB']
def reverse_strings_list(string_list):
    result = list(map(lambda x: "".join(reversed(x)), string_list))
    return result

colors_list = ["Red", "Green", "Blue", "White", "Black"]
print("\nOriginal lists:")
print(colors_list)
print("\nReverse strings of the said given list:")
print(reverse_strings_list(colors_list))

# 42. Write a Python program to calculate the product of a given list of numbers using lambda. 
# list1: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Product of the said list numbers:
# 3628800
# list2: [2.2, 4.12, 6.6, 8.1, 8.3]
# Product of the said list numbers:
# 4021.8599520000007
import functools 
#NOTE: reduce function is a part of functools modules. DO NOT FORGET TO INCLUDE!
def remove_duplicates(nums):
    result = functools.reduce(lambda x, y: x * y, nums, 1)
    return result
nums1 = [1,2,3,4,5,6,7,8,9,10]
nums2 = [2.2,4.12,6.6,8.1,8.3]
print("list1:", nums1)
print("Product of the said list numbers:")
print(remove_duplicates(nums1))
print("\nlist2:", nums2)
print("Product of the said list numbers:")
print(remove_duplicates(nums2))

# 43. Write a Python program to multiply all the numbers in a given list using lambda. 
'''SAME AS THE PROGRAM ABOVE'''


# 44. Write a Python program to calculate the average value of the numbers in a given tuple of tuples using lambda. 
# Original Tuple:
# ((10, 10, 10), (30, 45, 56), (81, 80, 39), (1, 2, 3))
# Average value of the numbers of the said tuple of tuples:
# (30.5, 34.25, 27.0)
# Original Tuple:
# ((1, 1, -5), (30, -15, 56), (81, -60, -39), (-10, 2, 3))
# Average value of the numbers of the said tuple of tuples:
# (25.5, -18.0, 3.75)
def average_tuple(nums):
    result = tuple(map(lambda x: sum(x) / float(len(x)), zip(*nums)))
    return result

nums = ((10, 10, 10), (30, 45, 56), (81, 80, 39), (1, 2, 3))
print ("Original Tuple: ")
print(nums)
print("\nAverage value of the numbers of the said tuple of tuples:\n",average_tuple(nums))
nums = ((1, 1, -5), (30, -15, 56), (81, -60, -39), (-10, 2, 3))
print ("\nOriginal Tuple: ")
print(nums)
print("\nAverage value of the numbers of the said tuple of tuples:\n",average_tuple(nums))

# 45. Write a Python program to convert string element to integer inside a given tuple using lambda. 
# Original tuple values:
# (('233', 'ABCD', '33'), ('1416', 'EFGH', '55'), ('2345', 'WERT', '34'))
# New tuple values:
# ((233, 33), (1416, 55), (2345, 34))
def tuple_int_str(tuple_str):
    result = tuple(map(lambda x: (int(x[0]), int(x[2])), tuple_str))
    return result     
tuple_str =  (('233', 'ABCD', '33'), ('1416', 'EFGH', '55'), ('2345', 'WERT', '34'))
print("Original tuple values:")
print(tuple_str)
print("\nNew tuple values:")
print(tuple_int_str(tuple_str))

# 46. Write a Python program to find index position and value of the maximum and minimum values in a given list of numbers using lambda. 
# Original list:
# [12, 33, 23, 10.11, 67, 89, 45, 66.7, 23, 12, 11, 10.25, 54]
# Index position and value of the maximum value of the said list:
# (5, 89)
# Index position and value of the minimum value of the said list:
# (3, 10.11)
def position_max_min(nums):
    max_result = max(enumerate(nums), key=(lambda x: x[1]))
    min_result = min(enumerate(nums), key=(lambda x: x[1]))
    return max_result,min_result

nums = [12,33,23,10.11,67,89,45,66.7,23,12,11,10.25,54]
print("Original list:")
print(nums)
result = position_max_min(nums)
print("\nIndex position and value of the maximum value of the said list:")
print(result[0])
print("\nIndex position and value of the minimum value of the said list:")
print(result[1])

# 47. Write a Python program to sort a given mixed list of integers and strings using lambda. Numbers must be sorted before strings. 
# Original list:
# [19, 'red', 12, 'green', 'blue', 10, 'white', 'green', 1]
# Sort the said mixed list of integers and strings:
# [1, 10, 12, 19, 'blue', 'green', 'green', 'red', 'white']
def sort_mixed_list(mixed_list):
    mixed_list.sort(key=lambda e: (isinstance(e, str), e))
    return mixed_list
mixed_list = [19,'red',12,'green','blue', 10,'white','green',1]
print("Original list:")
print(mixed_list)
print("\nSort the said  mixed list of integers and strings:")
print(sort_mixed_list(mixed_list))

# 48. Write a Python program to sort a given list of strings(numbers) numerically using lambda. 
# Original list:
# ['4', '12', '45', '7', '0', '100', '200', '-12', '-500']
# Sort the said list of strings(numbers) numerically:
# ['-500', '-12', '0', '4', '7', '12', '45', '100', '200']
def sort_numeric_strings(nums_str):
    result = sorted(nums_str, key=lambda el: int(el))
    return result
nums_str = ['4','12','45','7','0','100','200','-12','-500']
print("Original list:")
print(nums_str)
print("\nSort the said list of strings(numbers) numerically:")
print(sort_numeric_strings(nums_str))

# 49. Write a Python program to count the occurrences of the items in a given list using lambda. 
# Original list:
# [3, 4, 5, 8, 0, 3, 8, 5, 0, 3, 1, 5, 2, 3, 4, 2]
# Count the occurrences of the items in the said list:
# {3: 4, 4: 2, 5: 3, 8: 2, 0: 2, 1: 1, 2: 2}
def count_occurrences(nums):
    result = dict(map(lambda el  : (el, list(nums).count(el)), nums))
    return result
nums = [3,4,5,8,0,3,8,5,0,3,1,5,2,3,4,2]
print("Original list:")
print(nums)
print("\nCount the occurrences of the items in the said list:")
print(count_occurrences(nums))

# 50. Write a Python program to remove specific words from a given list using lambda. 
# Original list:
# ['orange', 'red', 'green', 'blue', 'white', 'black']
# Remove words:
# ['orange', 'black']
# After removing the specified words from the said list:
# ['red', 'green', 'blue', 'white']
def remove_words(list1, remove_words):
    result = list(filter(lambda word: word not in remove_words, list1))
    return result
        
colors = ['orange', 'red', 'green', 'blue', 'white', 'black']
remove_colors = ['orange','black']
print("Original list:")
print(colors)
print("\nRemove words:")
print(remove_colors)
print("\nAfter removing the specified words from the said list:")
print(remove_words(colors, remove_colors))

# 51. Write a Python program to find the maximum and minimum values in a given list of tuples using lambda function. 
# Original list with tuples:
# [('V', 62), ('VI', 68), ('VII', 72), ('VIII', 70), ('IX', 74), ('X', 65)]
# Maximum and minimum values of the said list of tuples:
# (74, 62)
def max_min_list_tuples(class_students):
    return_max = max(class_students,key=lambda item:item[1])[1]
    return_min = min(class_students,key=lambda item:item[1])[1]
    return return_max, return_min
    
class_students = [('V', 62), ('VI', 68), ('VII', 72), ('VIII', 70), ('IX', 74), ('X', 65)]
print("Original list with tuples:")
print(class_students)
print("\nMaximum and minimum values of the said list of tuples:")
print(max_min_list_tuples(class_students))

# 52. Write a Python program to remove None value from a given list using lambda function. 
# Original list:
# [12, 0, None, 23, None, -55, 234, 89, None, 0, 6, -12]
# Remove None value from the said list:
# [12, 0, 23, -55, 234, 89, 0, 6, -12]
def remove_none(nums):
    result = filter(lambda v: v is not None, nums)
    return list(result)

nums = [12, 0, None, 23, None, -55, 234, 89, None, 0, 6, -12]
print("Original list:")
print(nums)
print("\nRemove None value from the said list:")
print(remove_none(nums))


