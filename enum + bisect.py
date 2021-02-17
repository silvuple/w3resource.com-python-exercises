import bisect
NOTE:'''Python Bisect'''

# 1. Write a Python program to locate the left insertion point for a specified value in sorted order. 
# Expected Output: 4 2
def index(a, x):
    i = bisect.bisect_left(a, x)
    return i
a = [1, 2, 4, 5]
print(index(a, 6))
print(index(a, 3))

# 2. Write a Python program to locate the right insertion point for a specified value in sorted order. 
# Expected Output: 3 2
def index(a, x):
    i = bisect.bisect_right(a, x)
    return i
a = [1, 2, 4, 7]
print(index(a, 6))
print(index(a, 3))

# 3. Write a Python program to insert items into a list in sorted order. 
# Expected Output:
# Original List:
# [25, 45, 36, 47, 69, 48, 68, 78, 14, 36]
# Sorted List:
# [14, 25, 36, 36, 45, 47, 48, 68, 69, 78]
import bisect
# Sample list
my_list = [25, 45, 36, 47, 69, 48, 68, 78, 14, 36]
print("Original List:")
print(my_list)
sorted_list = []
for i in my_list:
    position = bisect.bisect(sorted_list, i)
    bisect.insort(sorted_list, i)
print("Sorted List:")
print(sorted_list)

# 4. Write a Python program to find the first occurrence of a given number in a sorted list using Binary Search(bisect). 
# Expected Output:
# First occurrence of 8 is present at index 4
from bisect import bisect_left   
def Binary_Search(a, x): 
    i = bisect_left(a, x) 
    if i != len(a) and a[i] == x: 
        return i 
    else: 
        return -1

nums = [1, 2, 3, 4, 8, 8, 10, 12] 
x = 8 
num_position = Binary_Search(nums, x) 
if num_position == -1: 
    print(x, "is not present.") 
else: 
    print("First occurrence of", x, "is present at index", num_position)

# 5. Write a Python program to find the index position of the largest value smaller than a given number in a sorted list using Binary Search(bisect). 
# Expected Output:
# Largest value smaller than 5 is at index 3
from bisect import bisect_left  
def Binary_Search(l, x): 
    i = bisect_left(l, x) 
    if i: 
        return (i-1) 
    else: 
        return -1  
nums = [1, 2, 3, 4, 8, 8, 10, 12] 
x = 5 
num_position  = Binary_Search(nums, x) 
if num_position  == -1: 
    print("Not found..!") 
else: 
    print("Largest value smaller than ", x, " is at index ", num_position )


# 6. Write a Python program to find the index position of the last occurrence of a given number in a sorted list using Binary Search(bisect). 
# Expected Output:
# Last occurrence of 8 is present at 5


# 7. Write a Python program to find three integers which gives the sum of zero in a given array of integers using Binary Search(bisect). 
# Expected Output:
# [[-40, 0, 40], [-20, -20, 40], [-20, 0, 20]]
# [[-6, 1, 5], [-6, 2, 4]]


# 8. Write a Python program to find a triplet in an array such that the sum is closest to a given number. Return the sum of the three integers. 
# Expected Output:
# Array values & target value: [1, 2, 3, 4, 5, -6] & 14
# Sum of the integers closest to target: 12
# Array values & target value: [1, 2, 3, 4, -5, -6] & 5
# Sum of the integers closest to target: 6


# 9. Write a Python program to find four elements from a given array of integers whose sum is equal to a given number. The solution set must not contain duplicate quadruplets. 
# Expected Output:
# Array values & target value: [-2, -1, 1, 2, 3, 4, 5, 6] & 10
# Solution Set:
# [[-2, 1, 5, 6], [-2, 2, 4, 6], [-2, 3, 4, 5], [-1, 1, 4, 6],
#     [-1, 2, 3, 6], [-1, 2, 4, 5], [1, 2, 3, 4]]
