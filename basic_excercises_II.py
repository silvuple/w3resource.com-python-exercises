'''
PYTHON BASIC EXCERCISES PART II SOLUTIONS (VIA W3RESOURCE PYTHON)
AUTHORED BY: ATHARVA "HIGHNESS_ATHARVA" SHAH
'''
import os
from multiprocessing import Process
import requests
import string
from collections import Counter
from itertools import chain, compress
from bisect import bisect_right
import sys
from datetime import date
import math
import re
from collections import deque
from functools import partial
import itertools
import platform as pl
import pkg_resources
from urllib.request import urlopen
from bs4 import BeautifulSoup as soup
import bs4
import pprint
import collections
import random

# 1. function that takes a sequence of numbers and determines whether all the numbers are different from each other
```


def test_distinct(data):
    if len(data) == len(set(data)):
        return True
    else:
        return False


print(test_distinct([1, 5, 7, 9]))
print(test_distinct([2, 4, 5, 5, 7, 9]))
```
# 2. create all possible strings by using 'a', 'e', 'i', 'o', 'u'. Use the characters exactly once
```
char_list = ['a', 'e', 'i', 'o', 'u']
random.shuffle(char_list)
print(''.join(char_list))
```
# 3. remove and print every third number from a list of numbers until the list becomes empty.

```


def remove_nums(int_list):
    # list starts with 0 index
    position = 3 - 1
    idx = 0
    len_list = (len(int_list))
    while len_list > 0:
        idx = (position+idx) % len_list
        print(int_list.pop(idx))
        len_list -= 1


nums = [10, 20, 30, 40, 50, 60, 70, 80, 90]
remove_nums(nums)
```
# 4. (THREE SUM)find unique triplets whose three elements gives the sum of zero from an array of n integers.

```


def three_sum(nums):
    result = []
    nums.sort()
    for i in range(len(nums)-2):
        if i > 0 and nums[i] == nums[i-1]:
            continue
        l, r = i+1, len(nums)-1
        while l < r:
            s = nums[i] + nums[l] + nums[r]
            if s > 0:
                r -= 1
            elif s < 0:
                l += 1
            else:
                # found three sum
                result.append((nums[i], nums[l], nums[r]))
                # remove duplicates
                while l < r and nums[l] == nums[l+1]:
                    l += 1
                    while l < r and nums[r] == nums[r-1]:
                        r -= 1
                        l += 1
                        r -= 1
                    return result


x = [1, -6, 4, 2, -1, 2, 0, -2, 0]
print(three_sum(x))
```

# 5. create the combinations of 3 digit combo.
```
numbers = []
for num in range(1000):
    num = str(num).zfill(3)
print(num)
numbers.append(num)
```

# 6. print a long text, convert the string to a list and print all the words and their frequencies
```
string_words = '''United States Declaration of Independence
From Wikipedia, the free encyclopedia
The United States Declaration of Independence is the statement
adopted by the Second Continental Congress meeting at the Pennsylvania State
House (Independence Hall) in Philadelphia on July 4, 1776, which announced
that the thirteen American colonies, then at war with the Kingdom of Great
Britain, regarded themselves as thirteen independent sovereign states, no longer
under British rule. These states would found a new nation – the United States of
America. John Adams was a leader in pushing for independence, which was passed
on July 2 with no opposing vote cast. A committee of five had already drafted the
formal declaration, to be ready when Congress voted on independence.
'''
word_list = string_words.split()
word_freq = [word_list.count(n) for n in word_list]

print("String:\n {} \n".format(string_words))
print("List:\n {} \n".format(str(word_list)))
print("Pairs (Words and Frequencies:\n {}".format(
    str(list(zip(word_list, word_freq)))))
```
# 7. count the number of each character of a given text of a text file
```
file_input = input('File Name: ')
with open(file_input, 'r') as info:
    count = collections.Counter(info.read().upper())
    value = pprint.pformat(count)
print(value)
```

# 8. get the top stories from Google news.
```
news_url = "https://news.google.com/news/rss"
Client = urlopen(news_url)
xml_page = Client.read()
Client.close()

soup_page = soup(xml_page, "xml")
news_list = soup_page.findAll("item")
# Print news title, url and publish date
for news in news_list:
    print(news.title.text)
    print(news.link.text)
    print(news.pubDate.text)
    print("-"*60)
```

# 9. get a list of locally installed Python modules.
```
installed_packages = pkg_resources.working_set
installed_packages_list = sorted(["%s==%s" % (i.key, i.version)
                                  for i in installed_packages])
for m in installed_packages_list:
    print(m)
```

# 10. display some information about the OS where the script is running
```
os_profile = [
    'architecture',
    'linux_distribution',
    'mac_ver',
    'machine',
    'node',
    'platform',
    'processor',
    'python_build',
    'python_compiler',
    'python_version',
    'release',
    'system',
    'uname',
    'version',
]
for key in os_profile:
    if hasattr(pl, key):
        print(key + ": " + str(getattr(pl, key)()))
```
# 11. check the sum of three elements (each from an array) from three arrays is equal to a target value. Print all those three-element combinations.
```
X = [10, 20, 20, 20]
Y = [10, 20, 30, 40]
Z = [10, 30, 40, 20]
T = 70
   
   
def check_sum_array(N, *nums):
    if sum(x for x in nums) == N:
        return (True, nums)
    else:
        return (False, nums)


pro = itertools.product(X, Y, Z)
func = partial(check_sum_array, T)
sums = list(itertools.starmap(func, pro))

result = set()
for s in sums:
    if s[0] == True and s[1] not in result:
        result.add(s[1])
        print(result)

```
# 12. create all possible permutations from a given collection of distinct numbers
```


def permute(nums):
    result_perms = [[]]
    for n in nums:
        new_perms = []
        for perm in result_perms:
            for i in range(len(perm)+1):
                new_perms.append(perm[:i] + [n] + perm[i:])
                result_perms = new_perms
    return result_perms


my_nums = [1, 2, 3]
print("Original Cofllection: ", my_nums)
print("Collection of distinct numbers:\n", permute(my_nums))
```
# 13. get all possible two digit letter combinations from a digit (1 to 9) string.
```


def letter_combinations(digits):
    if digits == "":
        return []
    string_maps = {
        "1": "abc",
        "2": "def",
        "3": "ghi",
        "4": "jkl",
        "5": "mno",
        "6": "pqrs",
        "7": "tuv",
        "8": "wxy",
        "9": "z"
    }
    result = [""]
    for num in digits:
        temp = []
        for an in result:
            for char in string_maps[num]:
                temp.append(an + char)
        result = temp
    return result


digit_string = "47"
print(letter_combinations(digit_string))
digit_string = "29"
print(letter_combinations(digit_string))
```
# 14. add two positive integers without using the '+' operator. Go to the editor
# Note: Use bit wise operations to add two numbers.
```


def add_without_plus_operator(a, b):
    while b != 0:
        data = a & b
        a = a ^ b
        b = data << 1
    return a


print(add_without_plus_operator(2, 10))
print(add_without_plus_operator(-20, 10))
print(add_without_plus_operator(-10, -20))
```
# 15. check the priority of the four operators (+, -, *, /).
```
__operators__ = "+-/*"
__parenthesis__ = "()"
__priority__ = {
    '+': 0,
    '-': 0,
    '*': 1,
    '/': 1,
}


def test_higher_priority(operator1, operator2):
    return __priority__[operator1] >= __priority__[operator2]


print(test_higher_priority('*', '-'))
print(test_higher_priority('+', '-'))
print(test_higher_priority('+', '*'))
print(test_higher_priority('+', '/'))
print(test_higher_priority('*', '/'))
```
# 16. get the third side of right angled triangle from two given sides.
```


def pythagoras(opposite_side, adjacent_side, hypotenuse):
    if opposite_side == str("x"):
        return ("Opposite = " + str(((hypotenuse**2) - (adjacent_side**2))**0.5))
    elif adjacent_side == str("x"):
        return ("Adjacent = " + str(((hypotenuse**2) - (opposite_side**2))**0.5))
    elif hypotenuse == str("x"):
        return ("Hypotenuse = " + str(((opposite_side**2) + (adjacent_side**2))**0.5))
    else:
        return "You know the answer!"


print(pythagoras(3, 4, 'x'))
print(pythagoras(3, 'x', 5))
print(pythagoras('x', 4, 5))
print(pythagoras(3, 4, 5))
```
# 17. get all strobogrammatic numbers that are of length n. Go to the editor
# A strobogrammatic number is a number whose numeral is rotationally symmetric, so that it appears the same when rotated 180 degrees. In other words, the numeral looks the same right-side up and upside down (e.g., 69, 96, 1001).
# For example,
# Given n = 2, return ["11", "69", "88", "96"].
# Given n = 3, return ['818', '111', '916', '619', '808', '101', '906', '609', '888', '181', '986', '689']
```


def gen_strobogrammatic(n):
    """
    :type n: int
    :rtype: List[str]
    """
    result = helper(n, n)
    return result


def helper(n, length):
    if n == 0:
        return [""]
    if n == 1:
        return ["1", "0", "8"]
    middles = helper(n-2, length)
    result = []
    for middle in middles:
        if n != length:
            result.append("0" + middle + "0")
        result.append("8" + middle + "8")
        result.append("1" + middle + "1")
        result.append("9" + middle + "6")
        result.append("6" + middle + "9")
    return result


print("n = 2: \n", gen_strobogrammatic(2))
print("n = 3: \n", gen_strobogrammatic(3))
print("n = 4: \n", gen_strobogrammatic(4))
```
# 18. Find the mean, median, mode of N Numbers without using Stats module
```
'''
MEAN
'''
n_num = [1, 2, 3, 4, 5]
n = len(n_num)
get_sum = sum(n_num)
mean = get_sum / n
print("Mean / Average is: " + str(mean))

'''
MODE
'''
# list of elements to calculate mode
n_num = [1, 2, 3, 4, 5, 5]
n = len(n_num)

data = Counter(n_num)
get_mode = dict(data)
mode = [k for k, v in get_mode.items() if v == max(list(data.values()))]

if len(mode) == n:
    get_mode = "No mode found"
else:
    get_mode = "Mode is / are: " + ', '.join(map(str, mode))
print(get_mode)

'''
MEDIAN
'''
n_num = [1, 2, 3, 4, 5]
n = len(n_num)
n_num.sort()

if n % 2 == 0:
    median1 = n_num[n//2]
    median2 = n_num[n//2 - 1]
    median = (median1 + median2)/2
else:
    median = n_num[n//2]
print("Median is: " + str(median))
```

# 19. find the value of n where n degrees of number 2 are written sequentially in a line without spaces
```


def ndegrees(num):
    ans = True
    n, tempn, i = 2, 2, 2
    while ans:
        if str(tempn) in num:
            i += 1
            tempn = pow(n, i)
        else:
            ans = False
    return i-1


print(ndegrees("2481632"))
print(ndegrees("248163264"))

# 20. find the number of zeros at the end of a factorial of a given positive number.
```


def factendzero(n):
    x = n // 5
    y = x
    while x > 0:
        x /= 5
        y += int(x)
    return y


print(factendzero(5))
print(factendzero(12))
print(factendzero(100))
```
# 21. find the number of notes (Sample of notes: 10, 20, 50, 100, 200 and 500 ) against a given amount
```


def no_notes(a):
    Q = [500, 200, 100, 50, 20, 10]
    x = 0
    for i in range(6):
        q = Q[i]
        x += int(a / q)
        a = int(a % q)
    if a > 0:
        x = -1
    return x


print(no_notes(880))
print(no_notes(1000))
```
# 22. create a sequence where the first four members of the sequence are equal to one, and each successive term of the sequence is equal to the sum of the four previous ones. Find the Nth member of the sequence


def new_seq(n):
    if n == 1 or n == 2 or n == 3 or n == 4:
        return 1
    return new_seq(n-1) + new_seq(n-2) + new_seq(n-3) + new_seq(n-4)


print(new_seq(5))
print(new_seq(6))
print(new_seq(7))

# 23. Accept a positive number and subtract from this number the sum of its digits
num = int(input('Please enter a multi-digit number: '))
if num > 0:
    num = num - sum([int(x) for x in str(num)])
    print(num)


# 24. Find the number of divisors of a given integer is even or odd
def divisor(n):
    for i in range(n):
        x = len([i for i in range(1, n+1) if not n % i])
    return x


print(divisor(15))
print(divisor(12))
print(divisor(9))
print(divisor(6))
print(divisor(3))

# 25.  Find the digits which are absent in a given mobile number


def absent_digits(n):
    all_nums = set([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
    n = set([int(i) for i in n])
    n = n.symmetric_difference(all_nums)
    n = sorted(n)
    return n


print(absent_digits([9, 8, 3, 2, 2, 0, 9, 7, 6, 3]))

# 26. Compute the summation of the absolute difference of all distinct pairs in an given array


def dist_sum(arr):
    result = 0
    i = 0
    while i < len(arr):
        result += i*arr[i]-(len(arr)-i-1)*arr[i]
        i += 1
    return result


# 3-1=2, 2-1=1, 3-2=1 so 2+1+1=4 which is absolute difference.
print(dist_sum([1, 2, 3]))
# 5-1=4, 4-1=3, 5-4=1 so 4+3+1=8 which is absolute difference.
print(dist_sum([1, 4, 5]))

# 27.  Find the type of the progression and the next successive member of a given three successive members of a sequence
# For this solution we do not include HP, only AP and GP


def ap_gp_sequence(arr):
    if arr[0] == arr[1] == arr[2] == 0:
        return "Wrong Numbers"
    else:
        if arr[1]-arr[0] == arr[2]-arr[1]:
            n = 2*arr[2]-arr[1]
            return "AP sequence, "+'Next number of the sequence: '+str(n)
        else:
            n = arr[2]**2/arr[1]
            return "GP sequence, " + 'Next number of the sequence:  '+str(n)


print(ap_gp_sequence([1, 2, 3]))
print(ap_gp_sequence([2, 6, 18]))
print(ap_gp_sequence([0, 0, 0]))

# 28.  print the length of the series and the series from the given 3rd term, 3rd last term and the sum of a series.
tn = int(input("Input third term of the series:"))
tltn = int(input("Input 3rd last term:"))
s_sum = int(input("Sum of the series:"))
n = int(2*s_sum/(tn+tltn))
print("Length of the series: ", n)


if n-5 == 0:
    d = (s_sum-3*tn)//6
else:
    d = (tltn-tn)/(n-5)

a = tn-2*d
j = 0
print("Series:")
for j in range(n-1):
    print(int(a), end=" ")
    a += d
print(int(a), end=" ")

# 29. Find common divisors between two numbers in a given pair.


def ngcd(x, y):
    i = 1
    while(i <= x and i <= y):
        if(x % i == 0 and y % i == 0):
            gcd = i
        i += 1
    return gcd


def num_comm_div(x, y):
    n = ngcd(x, y)
    result = 0
    z = int(n**0.5)
    i = 1
    while(i <= z):
        if(n % i == 0):
            result += 2
            if(i == n/i):
                result -= 1
        i += 1
    return result


print("Number of common divisors: ", num_comm_div(2, 4))
print("Number of common divisors: ", num_comm_div(2, 8))
print("Number of common divisors: ", num_comm_div(12, 24))

# 30. reverse the digits of a given number and add it to the original, If the sum is not a palindrome repeat this procedure.
# Note: A palindrome is a word, number, or other sequence of characters which reads the same backward as forward, such as madam or racecar.
# P.S: Master solutio provided by Website is incorrect. I have offered a much cleaner and efficient solution.


def revadder(n):
    number = str(n)
    number = list(number)
    number.sort(reverse=True)
    return int(''.join(number)) + n


print(revadder(45))

# 31.  count the number of carry operations for each of a set of addition problems


def carry_number(x, y):
    ctr = 0
    if(x == 0 and y == 0):
        return 0
    z = 0
    for i in reversed(range(10)):
        z = x % 10 + y % 10 + z
        if z > 9:
            z = 1
        else:
            z = 0
        ctr += z
        x //= 10
        y //= 10

    if ctr == 0:
        return "No carry operation."
    elif ctr == 1:
        return ctr
    else:
        return ctr


print(carry_number(786, 457))
print(carry_number(5, 6))

# 32. python program to find heights of the top three building in descending order from eight given buildings
print("Input the heights of eight buildings:")
l = [int(input()) for i in range(8)]
print("Heights of the top three buildings:")
l.sort(reverse=True)
print(l[:3], end='\n')

# 33.  compute the digit number of sum of two given integers
print("Input two integers(a b): ")
a, b = map(int, input().split(" "))
print("Number of digit of a and b.:")
print(len(str(a+b)))

# 34. check whether three given lengths (integers) of three sides form a right triangle. Print "Yes" if the given sides form a right triangle otherwise print "No"
print("Input three integers(sides of a triangle)")
int_num = list(map(int, input().split()))
x, y, z = sorted(int_num)
if x**2+y**2 == z**2:
    print('Yes')
else:
    print('No')

# 35. program which solve the equation: Go to the editor
    # ax+by=c
    # dx+ey=f
    # Print the values of x, y where a, b, c, d, e and f are given.
print("Input the value of a, b, c, d, e, f:")
a, b, c, d, e, f = map(float, input().split())
n = a*e - b*d
print("Values of x and y:")
if n != 0:
    x = (c*e - b*f) / n
    y = (a*f - c*d) / n
    print('{:.3f} {:.3f}'.format(x+0, y+0))

# 36. compute the amount of the debt in n months. The borrowing amount is $100,000 and the loan adds 5% interest of the debt and rounds it to the nearest 1,000 above month by month.
#Interest is fixed @5% PA
x = int(input("Amount? "))
period = int(input("Period? "))
for i in range(period):
    x = math.trunc(x*.05+x)
    if x % 1000 == 0:
        x = x
    else:
        x = (1000-(x % 1000))+x
print("Amount of Debt: ", x)

# 37. program which reads an integer n and find the number of combinations of a,b,c and d (0 <= a,b,c,d <= 9) where (a + b + c + d) will be equal to n.
print("Input the number(n):")
n = int(input())
result = 0
for (i, j, k) in itertools.product(range(10), range(10), range(10)):
    result += (0 <= n-(i+j+k) <= 9)
print("Number of combinations:", result)

# 38. print the number of prime numbers which are less than or equal to a given integer.


def is_prime(n):
    for i in range(2, int(n//2)+1):
        if n % i == 0:
            return False
        return True


n = int(input('Input an integer: '))
list_primes = []
for j in range(2, n+1):
    if is_prime(j):
        list_primes.append(j)
print("Number of prime numbers which are less than or equal to n.:",
      len(list_primes))

# 39. compute the radius and the central coordinate (x, y) of a circle which is constructed by three given points on the plane surface.
print("Input three coordinate of the circle:")
x1, y1, x2, y2, x3, y3 = map(float, input().split())
c = (x1-x2)**2 + (y1-y2)**2
a = (x2-x3)**2 + (y2-y3)**2
b = (x3-x1)**2 + (y3-y1)**2
s = 2*(a*b + b*c + c*a) - (a*a + b*b + c*c)
px = (a*(b+c-a)*x1 + b*(c+a-b)*x2 + c*(a+b-c)*x3) / s
py = (a*(b+c-a)*y1 + b*(c+a-b)*y2 + c*(a+b-c)*y3) / s
ar = a**0.5
br = b**0.5
cr = c**0.5
r = ar*br*cr / ((ar+br+cr)*(-ar+br+cr)*(ar-br+cr)*(ar+br-cr))**0.5
print("Radius of the said circle:")
print("{:>.3f}".format(r))
print("Central coordinate (x, y) of the circle:")
print("{:>.3f}".format(px), "{:>.3f}".format(py))

# 40. check whether a point (x,y) is in a triangle or not. There is a triangle formed by three points
print("Input x1,y1,x2,y2,x3,y3,xp,yp:")
x1, y1, x2, y2, x3, y3, xp, yp = map(float, input().split())
c1 = (x2-x1)*(yp-y1)-(y2-y1)*(xp-x1)
c2 = (x3-x2)*(yp-y2)-(y3-y2)*(xp-x2)
c3 = (x1-x3)*(yp-y3)-(y1-y3)*(xp-x3)
if (c1 < 0 and c2 < 0 and c3 < 0) or (c1 > 0 and c2 > 0 and c3 > 0):
    print("The point is in the triangle.")
else:
    print("The point is outside the triangle.")

# 41. compute and print sum of two given integers (more than or equal to zero). If given integers or the sum have more than 80 digits, print "overflow"
print("Input first integer:")
x = int(input())
print("Input second integer:")
y = int(input())
if x >= 10 ** 80 or y >= 10 ** 80 or x + y >= 10 ** 80:
    print("Overflow!")
else:
    print("Sum of the two integers: ", x + y)

# 42. program that accepts six numbers as input and sorts them in descending order
print("Input six integers:")
nums = list(map(int, input().split()))
nums.sort()
nums.reverse()
print("After sorting the said ntegers:")
print(*nums)

# 43.  test whether two lines PQ and RS are parallel. The four points are P(x1, y1), Q(x2, y2), R(x3, y3), S(x4, y4).
print("Input x1,y1,x2,y2,x3,y3,xp,yp:")
x1, y1, x2, y2, x3, y3, x4, y4 = map(float, input().split())
print('PQ and RS are parallel.' if abs((x2 - x1)*(y4 - y3) -
                                       (x4 - x3)*(y2 - y1)) < 1e-10 else 'PQ and RS are not parallel')

# 44. find the maximum sum of a contiguous subsequence from a given sequence of numbers a1, a2, a3, ... an. A subsequence of one element is also a continuous subsequence. Go to the editor
# Input:
# You can assume that 1 <= n <= 5000 and -100000 <= ai <= 100000.
# Input numbers are separated by a space.
# Input 0 to exit.
# Input number of sequence of numbers you want to input (0 to exit):
# 3
# Input numbers:
# 2
# 4
# 6
# Maximum sum of the said contiguous subsequence: 12
# Input number of sequence of numbers you want to input (0 to exit):
# 0
numlist = [-2, -3, 4, -1, -2, 1, 5, -3]
print(numlist)
sumlst = []

for i in range(0, len(numlist)):
    for j in range(2, len(numlist)+1):
        x = sum(numlist[i:j])
        sumlst.append(x)

print("Maximum sum is : ", max(sumlst))

# 45. There are two circles C1 with radius r1, central coordinate (x1, y1) and C2 with radius r2 and central coordinate (x2, y2).
# Write a Python program to test the followings -

#     "C2 is in C1" if C2 is in C1
#     "C1 is in C2" if C1 is in C2
#     "Circumference of C1 and C2 intersect" if circumference of C1 and C2 intersect, and
#     "C1 and C2 do not overlap" if C1 and C2 do not overlap.
print("Input x1, y1, r1, x2, y2, r2:")
x1, y1, r1, x2, y2, r2 = [float(i) for i in input().split()]
d = math.sqrt((x1-x2)**2 + (y1-y2)**2)
if d < r1-r2:
    print("C2  is in C1")
elif d < r2-r1:
    print("C1  is in C2")
elif d > r1+r2:
    print("Circumference of C1  and C2  intersect")
else:
    print("C1 and C2  do not overlap")

# 46. Write a Python program to that reads a date (from 2016/1/1 to 2016/12/31) and prints the day of the date. Jan. 1, 2016, is Friday. Note that 2016 is a leap year. Go to the editor
    # Input:
    # Two integers m and d separated by a single space in a line, m ,d represent the month and the day.
    # Input month and date (separated by a single space):
    # 5 15
    # Name of the date: Sunday
print("Input month and date (separated by a single space):")
m, d = map(int, input().split())
weeks = {1: 'Monday', 2: 'Tuesday', 3: 'Wednesday',
         4: 'Thursday', 5: 'Friday', 6: 'Saturday', 7: 'Sunday'}
w = date.isoweekday(date(2016, m, d))
print("Name of the date: ", weeks[w])

# 47. program which reads a text (only alphabetical characters and spaces.) and prints two words. The first one is the word which is arise most frequently in the text. The second one is the word which has the maximum number of letters.
# Input:
# A text is given in a line with following condition:
# a. The number of letters in the text is less than or equal to 1000.
# b. The number of letters in a word is less than or equal to 32.
# c. There is only one word which is arise most frequently in given text.
# d. There is only one word which has the maximum number of letters in given text.
# Input text: Thank you for your comment and your participation.
# Output: your participation.
print("Input a text in a line.")
text_list = list(map(str, input().split()))
sc = collections.Counter(text_list)
common_word = sc.most_common()[0][0]
max_char = ""
for s in text_list:
    if len(max_char) < len(s):
        max_char = s
print("\nMost frequent text and the word which has the maximum number of letters.")
print(common_word, max_char)

# 48. program that reads n digits (given) chosen from 0 to 9 and prints the number of combinations where the sum of the digits equals to another given number (s). Do not use the same digits in a combination
# Two integers as number of combinations and their sum by a single space in a line. Input 0 0 to exit.
# Input number of combinations and sum, input 0 0 to exit:
# 5 6
# 2 4
# 0 0
# 2
print("Input number of combinations and sum, input 0 0 to exit:")
while True:
    x, y = map(int, input(). split())
    if x == 0 and y == 0:
        break
    s = list(itertools.combinations(range(10), x))
    ctr = 0
    for i in s:
        if sum(i) == y:
            ctr += 1

print(ctr)

# 49.  program which reads the two adjoined sides and the diagonal of a parallelogram and check whether the parallelogram is a rectangle or a rhombus.
print("Input two adjoined sides and the diagonal of a parallelogram (comma separated):")
a, b, c = map(int, input().split(","))
# Using Pythagoras Thm,
if c**2 == a**2+b**2:
    print("This is a rectangle.")
# Since all four sides of rhombus are equal in length.
if a == b:
    print("This is a rhombus.")

# 50. program to replace a string "Python" with "Java" and "Java" with "Python" in a given string.
n = input('Input a text with two words "Python" and "Java"')
new = n.split()
for i in new:
    if i == 'Python':
        new[new.index(i)] = 'Java'
    elif i == 'Java':
        new[new.index(i)] = 'Python'
result = ' '.join(new)
print(result)

# 51.  find the difference between the largest integer and the smallest integer which are created by 8 numbers from 0 to 9. The number that can be rearranged shall start with 0 as in 00135668
print("Input an integer created by 8 numbers from 0 to 9.:")
num = list(input())
print("Difference between the largest and the smallest integer from the given integer:")
print(int("".join(sorted(num, reverse=True))) - int("".join(sorted(num))))

# 52. compute the sum of first n given prime numbers
MAX = 105000
print("Input a number (n≤10000) to compute the sum:(0 to exit)")
is_prime = [True for _ in range(MAX)]
is_prime[0] = is_prime[1] = False
for i in range(2, int(MAX ** (1 / 2)) + 1):
    if is_prime[i]:
        for j in range(i ** 2, MAX, i):
            is_prime[j] = False
primes = [i for i in range(MAX) if is_prime[i]]
while True:
    n = int(input())
    if not n:
        break
    print("Sum of first", n, "prime numbers:")
    print(sum(primes[:n]))

# 53. program that accept an even number (>=4, Goldbach number) from the user and create a combinations that express the given number as a sum of two prime numbers. Print the number of combinations
print("Input an even number (0 to exit):")
ub = 50000
is_prime = [0, 0, 1, 1] + [0]*(ub-3)
is_prime[5::6] = is_prime[7::6] = [1]*int(ub/6)
primes = [2, 3]
append = primes.append

for n in chain(range(5, ub, 6), range(7, ub, 6)):
    if is_prime[n]:
        append(n)
        is_prime[n*3::n*2] = [0]*((ub-n)//(n*2))
primes.sort()

for n in map(int, sys.stdin):
    if not n:
        break
    if n % 2:
        print("Number of combinations:")
        print(is_prime[n-2])
    else:
        print("Number of combinations:")
        print(len([1 for p in primes[:bisect_right(primes, n/2)] if is_prime[n-p]]))

# 54. if you draw a straight line on a plane, the plane is divided into two regions. For example, if you pull two straight lines in parallel, you get three areas, and if you draw vertically one to the other you get 4 areas.
    # Write a Python program to create maximum number of regions obtained by drawing n given straight lines
while True:
    print("Input number of straight lines (o to exit): ")
    n = int(input())
    if n <= 0:
        break
    print("Number of regions:")
    print((n*n+n+2)//2)

# 55. There are four different points on a plane, P(xp,yp), Q(xq, yq), R(xr, yr) and S(xs, ys). Write a Python program to test AB and CD are orthogonal or not.
while True:
    try:
        print("Input xp, yp, xq, yq, xr, yr, xs, ys:")
        x_p, y_p, x_q, y_q, x_r, y_r, x_s, y_s = map(float, input().split())
        pq_x, pq_y = x_q - x_p, y_q - y_p
        rs_x, rs_y = x_s - x_r, y_s - y_r
        rs = pq_x*rs_x + pq_y*rs_y
        if abs(rs) > 1e-10:
            print("AB and CD are not orthogonal!")
        else:
            print("AB and CD are orthogonal!")
    except:
        break

# 56. sum of all numerical values (positive integers) embedded in a sentence.
    # Write a Python program to create maximum number of regions obtained by drawing n given straight lines
    # CONTAINS REGEX IMPLEMENTATION!!!


def test(stri):
    print("Input some text and numeric values (<ctrl-d> to exit):")
    print("Sum of the numeric values: ", sum(
        [sum(map(int, re.findall(r"[0-9]{1,5}", stri)))]))


print(test("sd1fdsfs23 dssd56"))
print(test("15apple2banana"))
print(test("flowers5fruit5"))


# 57. There are 10 vertical and horizontal squares on a plane. Each square is painted blue and green. Blue represents the sea, and green represents the land. When two green squares are in contact with the top and bottom, or right and left, they are said to be ground. The area created by only one green square is called "island". For example, there are five islands in the figure below.
# Write a Python program to read the mass data and find the number of islands.
c = 0


def f(x, y, z):
    if 0 <= y < 10 and 0 <= z < 10 and x[z][y] == '1':
        x[z][y] = '0'
        for dy, dz in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
            f(x, y+dy, z+dz)


print("Input 10 rows of 10 numbers representing green squares (island) as 1 and blue squares (sea) as zeros")
while 1:
    try:
        if c:
            input()
    except:
        break
    x = [list(input()) for _ in [0]*10]
    c = 1
    b = 0
    for i in range(10):
        for j in range(10):
            if x[j][i] == '1':
                b += 1
                f(x, i, j)
    print("Number of islands:")
    print(b)

# 58. When character are consecutive in a string , it is possible to shorten the character string by replacing the character with a certain rule. For example, in the case of the character string YYYYY, if it is expressed as # 5 Y, it is compressed by one character.
    # Write a Python program to restore the original string by entering the compressed string with this rule. However, the # character does not appear in the restored character string. Go to the editor
    # Note: The original sentences are uppercase letters, lowercase letters, numbers, symbols, less than 100 letters, and consecutive letters are not more than 9 letters.


def restore_original_str(a1):
    result = ""
    ind = 0
    end = len(a1)
    while ind < end:
        if a1[ind] == "#":
            result += a1[ind + 2] * int(a1[ind + 1])
            ind += 3
        else:
            result += a1[ind]
            ind += 1
    return result


print("Original text:", "XY#6Z1#4023")
print(restore_original_str("XY#6Z1#4023"))
print("Original text:", "#39+1=1#30")
print(restore_original_str("#39+1=1#30"))

# 59. A convex polygon is a simple polygon in which no line segment between two points on the boundary ever goes outside the polygon. Equivalently, it is a simple polygon whose interior is a convex set. In a convex polygon, all interior angles are less than or equal to 180 degrees, while in a strictly convex polygon all interior angles are strictly less than 180 degrees.
# Write a Python program that compute the area of the polygon . The vertices have the names vertex 1, vertex 2, vertex 3, ... vertex n according to the order of edge connections Go to the editor
# Note: The original sentences are uppercase letters, lowercase letters, numbers, symbols, less than 100 letters, and consecutive letters are not more than 9 letters.


def poly_area(c):
    add = []
    for i in range(0, (len(c) - 2), 2):
        add.append(c[i] * c[i + 3] - c[i + 1] * c[i + 2])
        add.append(c[len(c) - 2] * c[1] - c[len(c) - 1] * c[0])
        return abs(sum(add) / 2)


print(poly_area([1, 0, 0, 0, 1, 1, 2, 0, -1, 1]))

# 60. Internet search engine giant, such as Google accepts web pages around the world and classify them, creating a huge database. The search engines also analyze the search keywords entered by the user and create inquiries for database search. In both cases, complicated processing is carried out in order to realize efficient retrieval, but basics are all cutting out words from sentences.
# Write a Python program to cut out words of 3 to 6 characters length from a given sentence not more than 1024 characters

print("Input a sentence (1024 characters. max.)")
yy = input()
yy = yy.replace(",", " ")
yy = yy.replace(".", " ")
print("3 to 6 characters length of words:")
print(*[y for y in yy.split() if 3 <= len(y) <= 6])

#####EXTRA PROBLEM#####
'''LCM and GCD'''


def gcd(x, y):
    gcd = 1
    # Assign z the highest value, either x or y
    if x % y == 0:
        return y
    # Iterate in reverse manner, make sure to typecast y/2 as int
    for z in range(int(y / 2), 0, -1):
        if x % z == 0 and y % z == 0:
            gcd = z
            break

    return gcd


def lcm(x, y):
    z = x if x > y else y
    while (True):
        if (z % x == 0 and z % y == 0):
            lcm = z
            break
        z += 1

    return lcm


print(gcd(14, 42))
print(lcm(12, 17))

# 61. Arrange integers (0 to 99) as narrow hilltop, as illustrated in Figure 1. Reading such data representing huge, when starting from the top and proceeding according to the next rule to the bottom. Write a Python program that compute the maximum value of the sum of the passing integers
print("Input the numbers (ctrl+d to exit):")
nums = [list(map(int, l.split(","))) for l in sys.stdin]
mvv = nums[0]

for i in range(1, (len(nums)+1)//2):
    rvv = [0]*(i+1)
    for j in range(i):
        rvv[j] = max(rvv[j], mvv[j]+nums[i][j])
        rvv[j+1] = max(rvv[j+1], mvv[j]+nums[i][j+1])
    mvv = rvv

for i in range((len(nums)+1)//2, len(nums)):
    rvv = [0]*(len(mvv)-1)
    for j in range(len(rvv)):
        rvv[j] = max(mvv[j], mvv[j+1]) + nums[i][j]
    mvv = rvv
print("Maximum value of the sum of integers passing according to the rule on one line.")
print(mvv[0])


# 62. program to find the number of combinations that satisfy p + q + r + s = n where n is a given number <= 4000 and p, q, r, s in the range of 0 to 1000.
print("Input a positive integer: (ctrl+d to exit)")
pair_dict = Counter()
for i in range(2001):
    pair_dict[i] = min(i, 2000 - i) + 1

while True:
    try:
        n = int(input())
        ans = 0
        for i in range(n + 1):
            ans += pair_dict[i] * pair_dict[n - i]
        print("Number of combinations of a,b,c,d:", ans)
    except EOFError:
        break

# 63.  program which adds up columns and rows of given table as shown in the specified figure.
while True:
    print("Input number of rows/columns (0 to exit)")
    n = int(input())
    if n == 0:
        break
    print("Input cell value:")
    x = []
    for i in range(n):
        x.append([int(num) for num in input().split()])

    for i in range(n):
        sum = 0
        for j in range(n):
            sum += x[i][j]
        x[i].append(sum)

    x.append([])
    for i in range(n + 1):
        sum = 0
        for j in range(n):
            sum += x[j][i]
        x[n].append(sum)
    print("Result:")
    for i in range(n + 1):
        for j in range(n + 1):
            print('{0:>5}'.format(x[i][j]), end="")
        print()


# 64.  Given a list of numbers and a number k, write a Python program to check whether the sum of any two numbers from the list is equal to k or not
def check_sum(nums, k):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == k:
                return True
    return False


print(check_sum([12, 5, 0, 5], 10))
print(check_sum([20, 20, 4, 5], 40))
print(check_sum([1, -1], 0))
print(check_sum([1, 1, 0], 0))

# 65. In mathematics, a subsequence is a sequence that can be derived from another sequence by deleting some or no elements without changing the order of the remaining elements. For example, the sequence (A,B,D) is a subsequence of (A,B,C,D,E,F) obtained after removal of elements C, E, and F. The relation of one sequence being the subsequence of another is a preorder.
# The subsequence should not be confused with substring (A,B,C,D) which can be derived from the above string (A,B,C,D,E,F) by deleting substring (E,F). The substring is a refinement of the subsequence.
# The list of all subsequences for the word "apple" would be "a", "ap", "al", "ae", "app", "apl", "ape", "ale", "appl", "appe", "aple", "apple", "p", "pp", "pl", "pe", "ppl", "ppe", "ple", "pple", "l", "le", "e", "".
# Write a Python program to find the longest word in set of words which is a subsequence of a given string.


def longest_word_sequence(s, d):
    long_word = ""

    for word in d:
        temp_word = ''
        j = 0
        for letter in word:

            for i in range(j, len(s)):

                if letter == s[i]:
                    temp_word += letter
                    j = i
                    break
                else:
                    continue

        if (temp_word) == word and len(long_word) < len(temp_word):
            long_word = temp_word

        else:
            continue
    return long_word


print(longest_word_sequence("Green", {"Gn", "Gren", "ree", "en"}))
print(longest_word_sequence("pythonexercises", {"py", "ex", "exercises"}))


# 66. A happy number is defined by the following process:
# Starting with any positive integer, replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. Those numbers for which this process ends in 1 are happy numbers, while those that do not end in 1 are unhappy numbers.
# Write a Python program to check whether a number is "happy" or not.
def is_Happy_num(n):
    past = set()
    while n != 1:
        n = sum(int(i)**2 for i in str(n))
        if n in past:
            return False
        past.add(n)
    return True


print(is_Happy_num(7))
print(is_Happy_num(932))
print(is_Happy_num(6))


# 67. program to find and print the first 10 happy numbers
def happy_numbers(n):
    past = set()
    while n != 1:
        n = sum(int(i)**2 for i in str(n))
        if n in past:
            return False
        past.add(n)
    return True


print([x for x in range(500) if happy_numbers(x)][:10])


# 68. program to count the number of prime numbers less than a given non-negative number
def count_Primes_nums(n):
    ctr = 0

    for num in range(n):
        if num <= 1:
            continue
        for i in range(2, num):
            if (num % i) == 0:
                break
        else:
            ctr += 1

    return ctr


print(count_Primes_nums(10))
print(count_Primes_nums(100))


# # 69. In abstract algebra, a group isomorphism is a function between two groups that sets up a one-to-one correspondence between the elements of the groups in a way that respects the given group operations. If there exists an isomorphism between two groups, then the groups are called isomorphic.
# Two strings are isomorphic if the characters in string A can be replaced to get string B
# Given "foo", "bar", return false.
# Given "paper", "title", return true.
# Write a Python program to check if two given strings are isomorphic to each other or not
# Write a Python program to find the longest common prefix string amongst a given array of strings. Return false If there is no common prefix.
# For Example, longest common prefix of "abcdefgh" and "abcefgh" is "abc"
def isIsomorphic(str1, str2):
    dict_str1 = {}
    dict_str2 = {}

    for i, value in enumerate(str1):
        dict_str1[value] = dict_str1.get(value, []) + [i]

    for j, value in enumerate(str2):
        dict_str2[value] = dict_str2.get(value, []) + [j]

    if sorted(dict_str1.values()) == sorted(dict_str2.values()):
        return True
    else:
        return False


print(isIsomorphic("foo", "bar"))
print(isIsomorphic("bar", "foo"))
print(isIsomorphic("paper", "title"))
print(isIsomorphic("title", "paper"))
print(isIsomorphic("apple", "orange"))
print(isIsomorphic("aa", "ab"))
print(isIsomorphic("ab", "aa"))

# 70. program to find the longest common prefix string amongst a given array of strings. Return false If there is no common prefix.
# For Example, longest common prefix of "abcdefgh" and "abcefgh" is "abc"


def longest_Common_Prefix(str1):
    if not str1:
        return ""
    short_str = min(str1, key=len)
    for i, char in enumerate(short_str):
        for other in str1:
            if other[i] != char:
                return short_str[:i]
    return short_str


print(longest_Common_Prefix(["abcdefgh", "abcefgh"]))
print(longest_Common_Prefix(["w3r", "w3resource"]))
print(longest_Common_Prefix(["Python", "PHP", "Perl"]))
print(longest_Common_Prefix(["Python", "PHP", "Java"]))

# 71. program to reverse only the vowels of a given string


def reverse_vowels(str1):
    vowels = ""
    for char in str1:
        if char in "aeiouAEIOU":
            vowels += char
    result_string = ""
    for char in str1:
        if char in "aeiouAEIOU":
            result_string += vowels[-1]
            vowels = vowels[:-1]
        else:
            result_string += char
    return result_string


print(reverse_vowels("w3resource"))
print(reverse_vowels("Python"))
print(reverse_vowels("Perl"))
print(reverse_vowels("USA"))

# 72. program to check whether a given integer is a palindrome or not.


def is_Palindrome(n):
    return str(n) == str(n)[::-1]


print(is_Palindrome(100))
print(is_Palindrome(252))
print(is_Palindrome(-838))

# 73. program to remove the duplicate elements of a given array of numbers such that each element appear only once and return the new length of the given array.


def remove_duplicates(nums):
    for i in range(len(nums)-1, 0, -1):
        if nums[i] == nums[i-1]:
            del nums[i-1]
    return len(nums)


print(remove_duplicates([0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 4]))
print(remove_duplicates([1, 2, 2, 3, 4, 4]))

# 74. program to calculate the maximum profit from selling and buying values of stock. An array of numbers represent the stock prices in chronological order. For example, given [8, 10, 7, 5, 7, 15], the function will return 10, since the buying value of the stock is 5 dollars and sell value is 15 dollars.


def buy_and_sell(stock_price):
    max_profit_val, current_max_val = 0, 0
    for price in reversed(stock_price):
        current_max_val = max(current_max_val, price)
        potential_profit = current_max_val - price
        max_profit_val = max(potential_profit, max_profit_val)
    return max_profit_val


print(buy_and_sell([8, 10, 7, 5, 7, 15]))
print(buy_and_sell([1, 2, 8, 1]))
print(buy_and_sell([]))

# 75. program to remove all instances of a given value from a given array of integers and find the length of the new array.


def remove_element(array_nums, val):
    i = 0
    while i < len(array_nums):
        if array_nums[i] == val:
            array_nums.remove(array_nums[i])
        else:
            i += 1
    return len(array_nums)


print(remove_element([1, 2, 3, 4, 5, 6, 7, 5], 5))
print(remove_element([10, 10, 10, 10, 10], 10))
print(remove_element([10, 10, 10, 10, 10], 20))
print(remove_element([], 1))

# 76.  program to find the starting and ending position of a given value in a given array of integers, sorted in ascending order


def search_Range(array_nums, target_val):
    result_arra = []
    start_pos = 0
    end_pos = 0
    for i in range(len(array_nums)):
        if target_val == array_nums[i] and start_pos == -1:
            start_pos = i
            end_pos = i
        elif target_val == array_nums[i] and start_pos != -1:
            end_pos = i
    result_arra.append(start_pos)
    result_arra.append(end_pos)
    return result_arra


print(search_Range([5, 7, 7, 8, 8, 8], 8))
print(search_Range([1, 3, 6, 9, 13, 14], 4))
print(search_Range([5, 7, 7, 8, 10], 8))

# 77.
'''SOLUTION ALREADY COVERED UNDER Q. 74'''


# 78. program to print a given N by M matrix of numbers line by line in forward > backwards > forward >... order.
def print_matrix(nums):
    flag = True

    for line in nums:

        if flag == True:
            i = 0
            while i < len(line):
                print(line[i])
                i += 1
            flag = False

        else:
            i = -1
            while i > -1 * len(line) - 1:
                print(line[i])
                i = i - 1
            flag = True


print_matrix([[1, 2, 3, 4],
              [5, 6, 7, 8],
              [0, 6, 2, 8],
              [2, 3, 0, 2]])

# 79. program to compute the largest product of three integers from a given list of integers.


def largest_product_of_three(nums):
    max_val = nums[1]
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            for k in range(j+1, len(nums)):
                max_val = max(nums[i] * nums[j] * nums[k], max_val)
    return max_val


print(largest_product_of_three([-10, -20, 20, 1]))
print(largest_product_of_three([-1, -1, 4, 2, 1]))
print(largest_product_of_three([1, 2, 3, 4, 5, 6]))

# 80.  program to find the first missing positive integer that does not exist in a given list


def first_missing_number(nums):
    if len(nums) == 0:
        return 1
    nums.sort()
    smallest_int_num = 0
    for i in range(len(nums) - 1):
        if nums[i] <= 0 or nums[i] == nums[i + 1]:
            continue
        else:
            if nums[i + 1] - nums[i] != 1:
                smallest_int_num = nums[i] + 1
                return smallest_int_num
    if smallest_int_num == 0:
        smallest_int_num = nums[-1] + 1
    return smallest_int_num


print(first_missing_number([2, 3, 7, 6, 8, -1, -10, 15, 16]))
print(first_missing_number([1, 2, 4, -7, 6, 8, 1, -10, 15]))
print(first_missing_number([1, 2, 3, 4, 5, 6, 7]))
print(first_missing_number([-2, -3, -1, 1, 2, 3]))

# 81. randomly generate a list with 10 even numbers between 1 and 100 inclusive
print(random.sample([i for i in range(1, 100) if i % 2 == 0], 10))

# 82.
'''ALREADY COVERED PREVIOUSLY'''

# 83. test whether a given number is symmetrical or not.


def is_symmetrical_num(n):
    return str(n) == str(n)[::-1]


print(is_symmetrical_num(121))
print(is_symmetrical_num(0))
print(is_symmetrical_num(122))
print(is_symmetrical_num(990099))
# Basically, a palindorme program.

# 84. accept a list of numbers and create a list to store the count of negative number in first element and store the sum of positive numbers in second element.


def count_sum(nums):
    if not nums:
        return []
    return [len([n for n in nums if n < 0]), sum(n for n in nums if n > 0)]


print(count_sum([1, 2, 3, 4, 5]))
print(count_sum([-1, -2, -3, -4, -5]))
print(count_sum([1, 2, 3, -4, -5]))
print(count_sum([1, 2, -3, -4, -5]))

# 85. An isogram (also known as a "nonpattern word") is a logological term for a word or phrase without a repeating letter. It is also used by some people to mean a word or phrase in which each letter appears the same number of times, not necessarily just once. Conveniently, the word itself is an isogram in both senses of the word, making it autological.
# Write a Python program to check whether a given string is an "isogram" or not


def check_isogram(str1):
    return len(str1) == len(set(str1.lower()))


print(check_isogram("w3resource"))
print(check_isogram("w3r"))
print(check_isogram("Python"))
print(check_isogram("Java"))

# 86. count the number of equal numbers from three given integers


def test_three_equal(x, y, z):
    result = set([x, y, z])
    if len(result) == 3:
        return 0
    else:
        return (4 - len(result))


print(test_three_equal(1, 1, 1))
print(test_three_equal(1, 2, 2))
print(test_three_equal(-1, -2, -3))
print(test_three_equal(-1, -1, -1))

# 87. check whether a given employee code is exactly 8 digits or 12 digits. Return True if the employee code is valid and False if it's not.


def is_valid_emp_code(emp_code):
    return len(emp_code) in [8, 12] and emp_code.isdigit()


print(is_valid_emp_code('12345678'))
print(is_valid_emp_code('1234567j'))
print(is_valid_emp_code('12345678j'))
print(is_valid_emp_code('123456789123'))
print(is_valid_emp_code('123456abcdef'))

# 88. accept two strings and test if the letters in the second string are present in the first string


def string_letter_check(list_data):
    return all([char in list_data[0].lower() for char in list_data[1].lower()])


print(string_letter_check(["python", "ypth"]))
print(string_letter_check(["python", "ypths"]))
print(string_letter_check(["python", "ypthon"]))
print(string_letter_check(["123456", "01234"]))
print(string_letter_check(["123456", "1234"]))

# 89. compute the sum of the three lowest positive numbers from a given list of numbers


def sum_three_smallest_nums(lst):
    return sum(sorted([x for x in lst if x > 0])[:3])


print(sum_three_smallest_nums([10, 20, 30, 40, 50, 60, 7]))
print(sum_three_smallest_nums([1, 2, 3, 4, 5]))
print(sum_three_smallest_nums([0, 1, 2, 3, 4, 5]))


# 90. replace all but the last five characters of a given string into "*" and returns the new masked string.
def mask_string(str1):
    return '*'*(len(str1)-5) + str1[-5:]


print(mask_string("kdi39323swe"))
print(mask_string("12345abcdef"))
print(mask_string("12345"))

# 91. count the number of arguments in a given function.


def num_of_args(*args):
    return(len(args))


print(num_of_args())
print(num_of_args(1))
print(num_of_args(1, 2))
print(num_of_args(1, 2, 3))
print(num_of_args(1, 2, 3, 4))
print(num_of_args([1, 2, 3, 4]))


# 92.  compute cumulative sum of numbers of a given list.
# Note: Cumulative sum = sum of itself + all previous numbers in the said list
def nums_cumulative_sum(nums_list):
    return [sum(nums_list[:i+1]) for i in range(len(nums_list))]


print(nums_cumulative_sum([10, 20, 30, 40, 50, 60, 7]))
print(nums_cumulative_sum([1, 2, 3, 4, 5]))
print(nums_cumulative_sum([0, 1, 2, 3, 4, 5]))

# 93.  find the middle character(s) of a given string. If the length of the string is odd return the middle character and return the middle two characters if the string length is even


def middle_char(txt):
    return txt[(len(txt)-1)//2:(len(txt)+2)//2]


print(middle_char("Python"))
print(middle_char("PHP"))
print(middle_char("Java"))

# 94. find the largest product of the pair of adjacent elements from a given list of integers.


def adjacent_num_product(list_nums):
    return max(a*b for a, b in zip(list_nums, list_nums[1:]))


print(adjacent_num_product([1, 2, 3, 4, 5, 6]))
print(adjacent_num_product([1, 2, 3, 4, 5]))
print(adjacent_num_product([2, 3]))

# 95. check whether every even index contains an even number and every odd index contains odd number of a given list.


def odd_even_position(nums):
    return all(nums[i] % 2 == i % 2 for i in range(len(nums)))


print(odd_even_position([2, 1, 4, 3, 6, 7, 6, 3]))
print(odd_even_position([2, 1, 4, 3, 6, 7, 6, 4]))
print(odd_even_position([4, 1, 2]))

# 96. check whether a given number is a narcissistic number or not.


def is_narcissistic_num(num):
    return num == sum([int(x) ** len(str(num)) for x in str(num)])


print(is_narcissistic_num(153))
print(is_narcissistic_num(370))
print(is_narcissistic_num(407))
print(is_narcissistic_num(409))
print(is_narcissistic_num(1634))
print(is_narcissistic_num(8208))
print(is_narcissistic_num(9474))
print(is_narcissistic_num(9475))

# 97. find the highest and lowest number from a given string of space separated integers


def highest_lowest_num(str1):
    num_list = list(map(int, str1.split()))
    return max(num_list), min(num_list)


print(highest_lowest_num("1 4 5 77 9 0"))
print(highest_lowest_num("-1 -4 -5 -77 -9 0"))
print(highest_lowest_num("0 0"))


# 98. check whether a sequence of numbers has an increasing trend or not.
def increasing_trend(nums):
    if (sorted(nums) == nums):
        return True
    else:
        return False


print(increasing_trend([1, 2, 3, 4]))
print(increasing_trend([1, 2, 5, 3, 4]))
print(increasing_trend([-1, -2, -3, -4]))
print(increasing_trend([-4, -3, -2, -1]))
print(increasing_trend([1, 2, 3, 4, 0]))

# 99. program to find the position of the second occurrence of a given string in another given string. If there is no such string return -1


def find_string(txt, str1):
    return txt.find(str1, txt.find(str1)+1)


print(find_string("The quick brown fox jumps over the lazy dog", "the"))
print(find_string("the quick brown fox jumps over the lazy dog", "the"))

# 100. compute the sum of all items of a given array of integers where each integer is multiplied by its index. Return 0 if there is no number


def sum_index_multiplier(nums):
    return sum(j*i for i, j in enumerate(nums))


print(sum_index_multiplier([1, 2, 3, 4]))
print(sum_index_multiplier([-1, -2, -3, -4]))
print(sum_index_multiplier([]))

# 101. find the name of the oldest student from a given dictionary containing the names and ages of a group of students.


def oldest_student(students):
    return max(students, key=students.get)


print(oldest_student({"Bernita Ahner": 12, "Kristie Marsico": 11,
                      "Sara Pardee": 14, "Fallon Fabiano": 11,
                      "Nidia Dominique": 15}))
print(oldest_student({"Nilda Woodside": 12, "Jackelyn Pineda": 12.2,
                      "Sofia Park": 12.4, "Joannie Archibald": 12.6,
                      "Becki Saunder": 12.7}))

# 102. create a new string with no duplicate consecutive letters from a given string.


def no_consecutive_letters(txt):
    return txt[0] + ''.join(txt[i] for i in range(1, len(txt)) if txt[i] != txt[i-1])


print(no_consecutive_letters("PPYYYTTHON"))
print(no_consecutive_letters("PPyyythonnn"))
print(no_consecutive_letters("Java"))
print(no_consecutive_letters("PPPHHHPPP"))

# 103. check whether two given lines are parallel or not.


def parallel_lines(line1, line2):
    return line1[0]/line1[1] == line2[0]/line2[1]


# 2x + 3y = 4, 2x + 3y = 8
print(parallel_lines([2, 3, 4], [2, 3, 8]))
# 2x + 3y = 4, 4x - 3y = 8
print(parallel_lines([2, 3, 4], [4, -3, 8]))

# 104.  find the lucky number(s) in a given matrix.
# Lucky number in a Matrix: Maximum in its column and minimum in its row.


def lucky_Numbers(matrix):
    result = set(map(min, matrix)) & set(map(max, zip(*matrix)))
    return list(result)


m1 = [[1, 2], [2, 3]]
print("Original matrix:", m1)
print("Lucky number(s) in the said matrix: ", lucky_Numbers(m1))

m1 = [[1, 2, 3], [3, 4, 5]]
print("\nOriginal matrix:", m1)
print("Lucky number(s) in the said matrix: ", lucky_Numbers(m1))

m1 = [[7, 5, 6], [3, 4, 4], [6, 5, 7]]
print("\nOriginal matrix:", m1)
print("Lucky number(s) in the said matrix: ", lucky_Numbers(m1))

# 105. check whether a given sequence is linear, quadratic or cubic.


def Seq_Linear_Quadratic_Cubic(seq_nums):
    seq_nums = [seq_nums[x] - seq_nums[x-1] for x in range(1, len(seq_nums))]
    if len(set(seq_nums)) == 1:
        return "Linear Sequence"
    seq_nums = [seq_nums[x] - seq_nums[x-1] for x in range(1, len(seq_nums))]
    if len(set(seq_nums)) == 1:
        return "Quadratic Sequence"
    seq_nums = [seq_nums[x] - seq_nums[x-1] for x in range(1, len(seq_nums))]
    if len(set(seq_nums)) == 1:
        return "Cubic Sequence"


print(Seq_Linear_Quadratic_Cubic([0, 2, 4, 6, 8, 10]))
print(Seq_Linear_Quadratic_Cubic([1, 4, 9, 16, 25]))
print(Seq_Linear_Quadratic_Cubic([0, 12, 10, 0, -12, -20]))
print(Seq_Linear_Quadratic_Cubic([1, 2, 3, 4, 5]))

# 106. test whether a given integer is pandigital number or not.


def is_pandigital_num(n):
    return len(set(str(n))) == 10


print(is_pandigital_num(1023456897))
print(is_pandigital_num(1023456798))
print(is_pandigital_num(1023457689))
print(is_pandigital_num(1023456789))
print(is_pandigital_num(102345679))

# 107. check whether a given number is Oddish or Evenish.


def oddish_evenish_num(n):
    return 'Oddish' if sum(map(int, str(n))) % 2 else 'Evenish'


print(oddish_evenish_num(120))
print(oddish_evenish_num(321))
print(oddish_evenish_num(43))
print(oddish_evenish_num(4433))
print(oddish_evenish_num(373))

# 108. rogram that takes three integers and check whether the last digit of first number * the last digit of second number = the last digit of third number.


def check_last_digit(x, y, z):
    return str(x*y)[-1] == str(z)[-1]


print(check_last_digit(12, 22, 44))
print(check_last_digit(145, 122, 1010))
print(check_last_digit(0, 22, 40))
print(check_last_digit(1, 22, 40))
print(check_last_digit(145, 122, 101))


# 109. program find the indices of all occurrences of a given item in a given list.
def indices_in_list(nums_list, n):
    return [idx for idx, i in enumerate(nums_list) if i == n]


print(indices_in_list([1, 2, 3, 4, 5, 2], 2))
print(indices_in_list([3, 1, 2, 3, 4, 5, 6, 3, 3], 3))
print(indices_in_list([1, 2, 3, -4, 5, 2, -4], -4))

# 110. program to remove two duplicate numbers from a given number of list.


def two_unique_nums(nums):
    return [i for i in nums if nums.count(i) == 1]


print(two_unique_nums([1, 2, 3, 2, 3, 4, 5]))
print(two_unique_nums([1, 2, 3, 2, 4, 5]))
print(two_unique_nums([1, 2, 3, 4, 5]))

# 111. check whether two given circles (given center (x,y) and radius) are intersecting. Return true for intersecting otherwise false.


def is_circle_collision(circle1, circle2):
    x1, y1, r1 = circle1
    x2, y2, r2 = circle2
    distance = ((x1-x2)**2 + (y1-y2)**2)**0.5
    return distance <= r1 + r2


print(is_circle_collision([1, 2, 4], [1, 2, 8]))
print(is_circle_collision([0, 0, 2], [10, 10, 5]))

# 112. compute the digit distance between two integers.


def digit_distance_nums(n1, n2):
    return sum(map(int, str(abs(n1-n2))))


print(digit_distance_nums(123, 256))
print(digit_distance_nums(23, 56))
print(digit_distance_nums(1, 2))
print(digit_distance_nums(24232, 45645))

# 113. to reverse all the words which have even length.


def reverse_even(txt):
    return ' '.join(i[::-1] if not len(i) % 2 else i for i in txt.split())


print(reverse_even("The quick brown fox jumps over the lazy dog"))
print(reverse_even("Python Exercises"))

# 114. to print letters from the English alphabet from a-z and A-Z
print("Alphabet from a-z:")
for letter in string.ascii_lowercase:
    print(letter, end=" ")
print("\nAlphabet from A-Z:")
for letter in string.ascii_uppercase:
    print(letter, end=" ")

# 115. generate and prints a list of numbers from 1 to 10.
nums = range(1, 10)
print(list(nums))
print(list(map(str, nums)))

# 116. identify nonprime numbers between 1 to 100 (integers). Print the nonprime numbers.


def is_not_prime(n):
    ans = False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            ans = True
    return ans


print("Nonprime numbers between 1 to 100:")
for x in filter(is_not_prime, range(1, 101)):
    print(x)

# 117. make a request to a web page, and test the status code, also display the html code of the specified web page.
url = 'http://www.example.com/'
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh) Gecko/20100101 Firefox/38.0'}
request = requests.get(url, headers=headers)
print("Web page status: ", request)
print("\nHTML code of the above web page:")
if request.ok:
    print(request.text)

# 118. In multiprocessing, processes are spawned by creating a Process object. Write a Python program to show the individual process IDs (parent process, process id etc.) involved


def info(title):
    print(title)
    print('module name:', __name__)
    print('parent process:', os.getppid())
    print('process id:', os.getpid())


def f(name):
    info('function f')
    print('hello', name)


if __name__ == '__main__':
    info('Main line')
    p = Process(target=f, args=('bob',))
    p.start()
    p.join()

# 119. to check if two given numbers are coprime or not. Return True if two numbers are coprime otherwise return false.


def gcd(p, q):
    # Create the gcd of two positive integers.
    while q != 0:
        p, q = q, p % q
    return p


def is_coprime(x, y):
    return gcd(x, y) == 1


print(is_coprime(17, 13))
print(is_coprime(17, 21))
print(is_coprime(15, 21))
print(is_coprime(25, 45))

# 120. calculate Euclid's totient function of a given integer. Use a primitive method to calculate Euclid's totient function.


def gcd(p, q):
    # Create the gcd of two positive integers.
    while q != 0:
        p, q = q, p % q
    return p


def is_coprime(x, y):
    return gcd(x, y) == 1


def phi_func(x):
    if x == 1:
        return 1
    else:
        n = [y for y in range(1, x) if is_coprime(x, y)]
        return len(n)


print(phi_func(10))
print(phi_func(15))
print(phi_func(33))
