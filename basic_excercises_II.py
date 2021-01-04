'''
PYTHON BASIC EXCERCISES PART II SOLUTIONS (VIA W3RESOURCE PYTHON)
AUTHORED BY: ATHARVA "HIGHNESS_ATHARVA" SHAH
'''
# 1. function that takes a sequence of numbers and determines whether all the numbers are different from each other
def test_distinct(data):
  if len(data) == len(set(data)):
    return True
  else:
    return False

print(test_distinct([1,5,7,9]))
print(test_distinct([2,4,5,5,7,9]))

# 2. create all possible strings by using 'a', 'e', 'i', 'o', 'u'. Use the characters exactly once
import random
char_list = ['a','e','i','o','u']
random.shuffle(char_list)
print(''.join(char_list))

# 3. remove and print every third number from a list of numbers until the list becomes empty.
def remove_nums(int_list):
  #list starts with 0 index
  position = 3 - 1 
  idx = 0
  len_list = (len(int_list))
  while len_list>0:
    idx = (position+idx)%len_list
    print(int_list.pop(idx))
    len_list -= 1
nums = [10,20,30,40,50,60,70,80,90]
remove_nums(nums)

# 4. (THREE SUM)find unique triplets whose three elements gives the sum of zero from an array of n integers. 
def three_sum(nums):
  result = []
  nums.sort()
  for i in range(len(nums)-2):
    if i> 0 and nums[i] == nums[i-1]:
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
          l+=1
          while l < r and nums[r] == nums[r-1]:
            r -= 1
            l += 1
            r -= 1
          return result

x = [1, -6, 4, 2, -1, 2, 0, -2, 0 ]
print(three_sum(x))

# 5. create the combinations of 3 digit combo.
numbers = []
for num in range(1000):
  num=str(num).zfill(3)
print(num)
numbers.append(num)

# 6. print a long text, convert the string to a list and print all the words and their frequencies
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
print("Pairs (Words and Frequencies:\n {}".format(str(list(zip(word_list, word_freq)))))

# 7. count the number of each character of a given text of a text file
import collections
import pprint
file_input = input('File Name: ')
with open(file_input, 'r') as info:
  count = collections.Counter(info.read().upper())
  value = pprint.pformat(count)
print(value)

# 8. get the top stories from Google news.
import bs4
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen

news_url="https://news.google.com/news/rss"
Client=urlopen(news_url)
xml_page=Client.read()
Client.close()

soup_page=soup(xml_page,"xml")
news_list=soup_page.findAll("item")
# Print news title, url and publish date
for news in news_list:
  print(news.title.text)
  print(news.link.text)
  print(news.pubDate.text)
  print("-"*60)

# 9. get a list of locally installed Python modules.
import pkg_resources
installed_packages = pkg_resources.working_set
installed_packages_list = sorted(["%s==%s" % (i.key, i.version)
     for i in installed_packages])
for m in installed_packages_list:
    print(m)
    
# 10. display some information about the OS where the script is running
import platform as pl

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
    print(key +  ": " + str(getattr(pl, key)()))

# 11. check the sum of three elements (each from an array) from three arrays is equal to a target value. Print all those three-element combinations.
import itertools
from functools import partial
X = [10, 20, 20, 20]
Y = [10, 20, 30, 40]
Z = [10, 30, 40, 20]
T = 70

def check_sum_array(N, *nums):
  if sum(x for x in nums) == N:
    return (True, nums)
  else:
      return (False, nums)
pro = itertools.product(X,Y,Z)
func = partial(check_sum_array, T)
sums = list(itertools.starmap(func, pro))

result = set()
for s in sums:
    if s[0] == True and s[1] not in result:
      result.add(s[1])
      print(result)


# 12. create all possible permutations from a given collection of distinct numbers
def permute(nums):
  result_perms = [[]]
  for n in nums:
    new_perms = []
    for perm in result_perms:
      for i in range(len(perm)+1):
        new_perms.append(perm[:i] + [n] + perm[i:])
        result_perms = new_perms
  return result_perms

my_nums = [1,2,3]
print("Original Cofllection: ",my_nums)
print("Collection of distinct numbers:\n",permute(my_nums))

# 13. get all possible two digit letter combinations from a digit (1 to 9) string.
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

# 14. add two positive integers without using the '+' operator. Go to the editor
      # Note: Use bit wise operations to add two numbers.
def add_without_plus_operator(a, b):
    while b != 0:
        data = a & b
        a = a ^ b
        b = data << 1
    return a
print(add_without_plus_operator(2, 10))
print(add_without_plus_operator(-20, 10))
print(add_without_plus_operator(-10, -20))

# 15. check the priority of the four operators (+, -, *, /). 
from collections import deque
import re
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

print(test_higher_priority('*','-'))
print(test_higher_priority('+','-'))
print(test_higher_priority('+','*'))
print(test_higher_priority('+','/'))
print(test_higher_priority('*','/'))

# 16. get the third side of right angled triangle from two given sides.
def pythagoras(opposite_side,adjacent_side,hypotenuse):
        if opposite_side == str("x"):
            return ("Opposite = " + str(((hypotenuse**2) - (adjacent_side**2))**0.5))
        elif adjacent_side == str("x"):
            return ("Adjacent = " + str(((hypotenuse**2) - (opposite_side**2))**0.5))
        elif hypotenuse == str("x"):
            return ("Hypotenuse = " + str(((opposite_side**2) + (adjacent_side**2))**0.5))
        else:
            return "You know the answer!"
    
print(pythagoras(3,4,'x'))
print(pythagoras(3,'x',5))
print(pythagoras('x',4,5))
print(pythagoras(3,4,5))

# 17. get all strobogrammatic numbers that are of length n. Go to the editor
    # A strobogrammatic number is a number whose numeral is rotationally symmetric, so that it appears the same when rotated 180 degrees. In other words, the numeral looks the same right-side up and upside down (e.g., 69, 96, 1001).
    # For example,
    # Given n = 2, return ["11", "69", "88", "96"].
    # Given n = 3, return ['818', '111', '916', '619', '808', '101', '906', '609', '888', '181', '986', '689']
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

print("n = 2: \n",gen_strobogrammatic(2))
print("n = 3: \n",gen_strobogrammatic(3))
print("n = 4: \n",gen_strobogrammatic(4))

# 18. Find the mean, median, mode of N Numbers without using Stats module 
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
from collections import Counter 
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

# 19. find the value of n where n degrees of number 2 are written sequentially in a line without spaces
def ndegrees(num):
  ans = True
  n, tempn, i = 2, 2, 2
  while ans:
    if str(tempn) in num:
      i += 1
      tempn = pow(n, i)
    else:
      ans = False
  return i-1;
print(ndegrees("2481632"))
print(ndegrees("248163264"))

# 20. find the number of zeros at the end of a factorial of a given positive number. 
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

# 21. find the number of notes (Sample of notes: 10, 20, 50, 100, 200 and 500 ) against a given amount
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

# 22. create a sequence where the first four members of the sequence are equal to one, and each successive term of the sequence is equal to the sum of the four previous ones. Find the Nth member of the sequence
def new_seq(n):
    if n==1 or n==2 or n==3 or n==4:
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
    result=0
    i=0
    while i<len(arr):
        result+=i*arr[i]-(len(arr)-i-1)*arr[i]
        i+=1
    return result
# 3-1=2, 2-1=1, 3-2=1 so 2+1+1=4 which is absolute difference.     
print(dist_sum([1,2,3]))
# 5-1=4, 4-1=3, 5-4=1 so 4+3+1=8 which is absolute difference.
print(dist_sum([1,4,5]))

# 27.  Find the type of the progression and the next successive member of a given three successive members of a sequence
       #For this solution we do not include HP, only AP and GP
def ap_gp_sequence(arr):
  if arr[0]==arr[1]==arr[2]==0:
    return "Wrong Numbers"
  else:
    if arr[1]-arr[0]==arr[2]-arr[1]:
      n=2*arr[2]-arr[1]
      return "AP sequence, "+'Next number of the sequence: '+str(n)
    else:
      n=arr[2]**2/arr[1]
      return "GP sequence, " + 'Next number of the sequence:  '+str(n)

print(ap_gp_sequence([1,2,3]))
print(ap_gp_sequence([2,6,18]))
print(ap_gp_sequence([0,0,0]))

# 28.  print the length of the series and the series from the given 3rd term, 3rd last term and the sum of a series.
tn = int(input("Input third term of the series:"))
tltn = int(input("Input 3rd last term:"))
s_sum = int(input("Sum of the series:"))
n = int(2*s_sum/(tn+tltn))
print("Length of the series: ",n)


if n-5==0:
  d = (s_sum-3*tn)//6
else:
  d = (tltn-tn)/(n-5)

a = tn-2*d
j = 0
print("Series:")
for j in range(n-1):
  print(int(a),end=" ")
  a+=d
print(int(a),end=" ")

# 29. Find common divisors between two numbers in a given pair.
def ngcd(x, y):
    i=1
    while(i<=x and i<=y):
        if(x%i==0 and y%i == 0):
            gcd=i;
        i+=1
    return gcd;
def num_comm_div(x, y):
  n = ngcd(x, y)
  result = 0
  z = int(n**0.5)
  i = 1
  while( i <= z ):
    if(n % i == 0):
      result += 2 
      if(i == n/i):
        result-=1
    i+=1
  return result

print("Number of common divisors: ",num_comm_div(2, 4))
print("Number of common divisors: ",num_comm_div(2, 8))
print("Number of common divisors: ",num_comm_div(12, 24))

# 30. reverse the digits of a given number and add it to the original, If the sum is not a palindrome repeat this procedure. 
  #Note: A palindrome is a word, number, or other sequence of characters which reads the same backward as forward, such as madam or racecar.
  #P.S: Master solutio provided by Website is incorrect. I have offered a much cleaner and efficient solution. 
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
      z = x%10 + y%10 + z
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
a,b = map(int,input().split(" "))
print("Number of digit of a and b.:")
print(len(str(a+b)))

# 34. check whether three given lengths (integers) of three sides form a right triangle. Print "Yes" if the given sides form a right triangle otherwise print "No"
print("Input three integers(sides of a triangle)")
int_num = list(map(int,input().split()))
x,y,z = sorted(int_num)
if x**2+y**2==z**2:
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
import math
#Interest is fixed @5% PA
x=int(input("Amount? "))
period=int(input("Period? "))
for i in range(period):
  x=math.trunc(x*.05+x)
  if x%1000==0:
    x=x
  else:
    x=(1000-(x%1000))+x
print("Amount of Debt: ", x)

# 37. program which reads an integer n and find the number of combinations of a,b,c and d (0 <= a,b,c,d <= 9) where (a + b + c + d) will be equal to n.
import itertools
print("Input the number(n):")
n=int(input())
result=0
for (i,j,k) in itertools.product(range(10),range(10),range(10)):
    result+=(0<=n-(i+j+k)<=9)
print("Number of combinations:",result)

# 38. print the number of prime numbers which are less than or equal to a given integer.
def is_prime(n):
  for i in range(2, int(n//2)+1):
    if n%i == 0:
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
print("{:>.3f}".format(px),"{:>.3f}".format(py))

# 40. check whether a point (x,y) is in a triangle or not. There is a triangle formed by three points
print("Input x1,y1,x2,y2,x3,y3,xp,yp:")
x1,y1,x2,y2,x3,y3,xp,yp = map(float, input().split())
c1 = (x2-x1)*(yp-y1)-(y2-y1)*(xp-x1)
c2 = (x3-x2)*(yp-y2)-(y3-y2)*(xp-x2)
c3 = (x1-x3)*(yp-y3)-(y1-y3)*(xp-x3)
if (c1<0 and c2<0 and c3<0) or (c1>0 and c2>0 and c3>0):
    print("The point is in the triangle.")
else:
    print("The point is outside the triangle.")
