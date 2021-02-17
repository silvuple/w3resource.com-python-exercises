from enum import IntEnum
import enum
from enum import Enum
from collections import Counter
from bisect import bisect, bisect_left
from bisect import bisect_right
from bisect import bisect_left
import bisect

NOTE:'''Python Bisect Excercises'''

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
def Binary_Search(l, x):
    i = bisect_left(l, x)
    if i:
        return (i-1)
    else:
        return -1

nums = [1, 2, 3, 4, 8, 8, 10, 12]
x = 5
num_position = Binary_Search(nums, x)
if num_position == -1:
    print("Not found..!")
else:
    print("Largest value smaller than ", x, " is at index ", num_position)

# 6. Write a Python program to find the index position of the last occurrence of a given number in a sorted list using Binary Search(bisect). 
# Expected Output:
# Last occurrence of 8 is present at 5
def BinarySearch(a, x):
    i = bisect_right(a, x)
    if i != len(a)+1 and a[i-1] == x:
        return (i-1)
    else:
        return -1

nums = [1, 2, 3, 4, 8, 8, 10, 12]
x = 8
num_position = BinarySearch(nums, x)
if num_position == -1:
    print("not presetn!")
else:
    print("Last occurrence of", x, "is present at", num_position)

# 7. Write a Python program to find three integers which gives the sum of zero in a given array of integers using Binary Search(bisect). 
# Expected Output:
# [[-40, 0, 40], [-20, -20, 40], [-20, 0, 20]]
# [[-6, 1, 5], [-6, 2, 4]]
class Solution:
    def three_Sum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        triplets = []
        if len(nums) < 3:
            return triplets
        num_freq = Counter(nums)
        nums = sorted(num_freq)  # Sorted unique numbers
        max_num = nums[-1]
        for i, v in enumerate(nums):
            if num_freq[v] >= 2:
                complement = -2 * v
                if complement in num_freq:
                    if complement != v or num_freq[v] >= 3:
                        triplets.append([v] * 2 + [complement])

            # When all 3 numbers are different.
            if v < 0:  # Only when v is the smallest
                two_sum = -v

                # Lower/upper bound of the smaller of remainingtwo.
                lb = bisect_left(nums, two_sum - max_num, i + 1)
                ub = bisect(nums, two_sum // 2, lb)
                for u in nums[lb: ub]:
                    complement = two_sum - u
                    if complement in num_freq and u != complement:
                        triplets.append([v, u, complement])
        return triplets

nums = [-20, 0, 20, 40, -20, -40, 80]
s = Solution()
result = s.three_Sum(nums)
print(result)
nums = [1, 2, 3, 4, 5, -6]
result = s.three_Sum(nums)
print(result)

# 8. Write a Python program to find a triplet in an array such that the sum is closest to a given number. Return the sum of the three integers. 
# Expected Output:
# Array values & target value: [1, 2, 3, 4, 5, -6] & 14
# Sum of the integers closest to target: 12
# Array values & target value: [1, 2, 3, 4, -5, -6] & 5
# Sum of the integers closest to target: 6
#Source: https://bit.ly/2SRefdb
class Solution:
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums = sorted(nums)
        # Let top[i] be the sum of largest i numbers.
        top = [
            0,
            nums[-1],
            nums[-1] + nums[-2]
        ]
        min_diff = float('inf')
        three_sum = 0
        # Find range of the least number in curr_n (0, 1, 2 or 3)
        # numbers that sum up to curr_target, then find range of
        # 2nd least number and so on by recursion.

        def closest(curr_target, curr_n, lo=0):
            if curr_n == 0:
                nonlocal min_diff, three_sum
                if abs(curr_target) < min_diff:
                    min_diff = abs(curr_target)
                    three_sum = target - curr_target
                return

            next_n = curr_n - 1
            max_i = len(nums) - curr_n
            max_i = bisect(
                nums, curr_target // curr_n,
                lo, max_i)
            min_i = bisect_left(
                nums, curr_target - top[next_n],
                lo, max_i) - 1
            min_i = max(min_i, lo)

            for i in range(min_i, max_i + 1):
                if min_diff == 0:
                    return
                if i == min_i or nums[i] != nums[i - 1]:
                    next_target = curr_target - nums[i]
                    closest(next_target, next_n, i + 1)

        closest(target, 3)
        return three_sum

s = Solution()
nums = [1, 2, 3, 4, 5, -6]
target = 14
result = s.threeSumClosest(nums, target)
print("\nArray values & target value:", nums, "&", target)
print("Sum of the integers closest to target:", result)

nums = [1, 2, 3, 4, -5, -6]
target = 5
result = s.threeSumClosest(nums, target)
print("\nArray values & target value:", nums, "&", target)
print("Sum of the integers closest to target:", result)

# 9. Write a Python program to find four elements from a given array of integers whose sum is equal to a given number. The solution set must not contain duplicate quadruplets. 
# Expected Output:
# Array values & target value: [-2, -1, 1, 2, 3, 4, 5, 6] & 10
# Solution Set:
# [[-2, 1, 5, 6], [-2, 2, 4, 6], [-2, 3, 4, 5], [-1, 1, 4, 6],
#     [-1, 2, 3, 6], [-1, 2, 4, 5], [1, 2, 3, 4]]
#Source: https://bit.ly/2SSoyhf
from bisect import bisect_left
class Solution:
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        N = 4
        quadruplets = []
        if len(nums) < N:
            return quadruplets
        nums = sorted(nums)
        quadruplet = []

        # Let top[i] be the sum of largest i numbers.
        top = [0]       
        for i in range(1, N):
            top.append(top[i - 1] + nums[-i])

        # Find range of the least number in curr_n (0,...,N)
        # numbers that sum up to curr_target, then find range
        # of 2nd least number and so on by recursion.
        def sum_(curr_target, curr_n, lo=0):
            if curr_n == 0:
                if curr_target == 0:
                    quadruplets.append(quadruplet[:])
                return

            next_n = curr_n - 1
            max_i = len(nums) - curr_n
            max_i = bisect_left(
                nums, curr_target // curr_n,
                lo, max_i)
            min_i = bisect_left(
                nums, curr_target - top[next_n],
                lo, max_i)

            for i in range(min_i, max_i + 1): 
                if i == min_i or nums[i] != nums[i - 1]:
                    quadruplet.append(nums[i])
                    next_target = curr_target - nums[i]
                    sum_(next_target, next_n, i + 1)
                    quadruplet.pop()

        sum_(target, N)
        return quadruplets

s = Solution()
nums = [-2, -1, 1, 2, 3, 4, 5, 6]
target = 10
result = s.fourSum(nums, target)
print("\nArray values & target value:",nums,"&",target)
print("Solution Set:\n", result)

NOTE: '''Python Enum Excercises'''
# 1. Write a Python program to create an Enum object and display a member name and value. Go to the editor
# Sample data:
# Member name: Albania
# Member value: 355
class Country(Enum):
    Afghanistan = 93
    Albania = 355
    Algeria = 213
    Andorra = 376
    Angola = 244
    Antarctica = 672

print('\nMember name: {}'.format(Country.Albania.name))
print('Member value: {}'.format(Country.Albania.value))

# 2. Write a Python program to iterate over an enum class and display individual member and their value. Go to the editor
# Expected Output:
# Afghanistan = 93
# Albania = 355
# Algeria = 213
# Andorra = 376
# Angola = 244
# Antarctica = 672
class Country(Enum):
    Afghanistan = 93
    Albania = 355
    Algeria = 213
    Andorra = 376
    Angola = 244
    Antarctica = 672

for data in Country:
    print('{:15} = {}'.format(data.name, data.value))


# 3. Write a Python program to display all the member name of an enum class ordered by their values. Go to the editor
# Expected Output:
# Country Name ordered by Country Code:
# Afghanistan
# Algeria
# Angola
# Albania
# Andorra
# Antarctica
class Country(enum.IntEnum):
    Afghanistan = 93
    Albania = 355
    Algeria = 213
    Andorra = 376
    Angola = 244
    Antarctica = 672


print('Country Name ordered by Country Code:')
print('\n'.join('  ' + c.name for c in sorted(Country)))


# 4. Write a Python program to get all values from an enum class. Go to the editor
# Expected output:
# [93, 355, 213, 376, 244, 672]
class Country(IntEnum):
    Afghanistan = 93
    Albania = 355
    Algeria = 213
    Andorra = 376
    Angola = 244
    Antarctica = 672

country_code_list = list(map(int, Country))
print(country_code_list)


# 5.Write a Python program to get the unique enumeration values. Go to the editor
# Expected Output:
# Afghanistan = 93
# Albania = 355
# Algeria = 213
# Andorra = 376
# Angola = 244
import enum
class Countries(enum.Enum):
    Afghanistan = 93
    Albania = 355
    Algeria = 213
    Andorra = 376
    Angola = 244
    India = 355
    USA = 213
for result in Countries:
    print('{:15} = {}'.format(result.name, result.value))
