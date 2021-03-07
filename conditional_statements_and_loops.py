# 1. Write a Python program to find those numbers which are divisible by 7 and multiple of 5, between 1500 and 2700 (both included). 
import random
nl = []
for x in range(1500, 2701):
    if (x % 7 == 0) and (x % 5 == 0):
        nl.append(str(x))
print(','.join(nl))

# 2. Write a Python program to convert temperatures to and from celsius, fahrenheit. 
# [ Formula : c/5 = f-32/9 [ where c = temperature in celsius and f = temperature in fahrenheit ]
# Expected Output :
# 60°C is 140 in Fahrenheit
# 45°F is 7 in Celsius
temp = input(
    "Input the  temperature you like to convert? (e.g., 45F, 102C etc.) : ")
degree = int(temp[:-1])
i_convention = temp[-1]

if i_convention.upper() == "C":
  result = int(round((9 * degree) / 5 + 32))
  o_convention = "Fahrenheit"
elif i_convention.upper() == "F":
  result = int(round((degree - 32) * 5 / 9))
  o_convention = "Celsius"
else:
  print("Input proper convention.")
  quit()
print("The temperature in", o_convention, "is", result, "degrees.")


# 3. Write a Python program to guess a number between 1 to 9. 
# Note : User is prompted to enter a guess. If the user guesses wrong then the prompt appears again until the guess is correct, on successful guess, user will get a "Well guessed!" message, and the program will exit.
target_num, guess_num = random.randint(1, 10), 0
while target_num != guess_num:
    guess_num = int(
        input('Guess a number between 1 and 10 until you get it right : '))
print('Well guessed!')

# 4. Write a Python program to construct the following pattern, using a nested for loop.
n=5;
for i in range(n):
    for j in range(i):
        print ('* ', end="")
    print('')

for i in range(n,0,-1):
    for j in range(i):
        print('* ', end="")
    print('')
# * 
# * * 
# * * * 
# * * * * 
# * * * * * 
# * * * * 
# * * * 
# * * 
# *

# 5. Write a Python program that accepts a word from the user and reverse it. 
word = input("Input a word to reverse: ")
for char in range(len(word) - 1, -1, -1):
  print(word[char], end="")
print("\n")

# 6. Write a Python program to count the number of even and odd numbers from a series of numbers. 
# Sample numbers : numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9) 
# Expected Output :
# Number of even numbers : 5
# Number of odd numbers : 4
numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9)  # Declaring the tuple
count_odd = 0
count_even = 0
for x in numbers:
       if not x % 2:
    	     count_even += 1
       else:
    	     count_odd += 1
print("Number of even numbers :", count_even)
print("Number of odd numbers :", count_odd)

# 7. Write a Python program that prints each item and its corresponding type from the following list.
# Sample List : datalist = [1452, 11.23, 1+2j, True, 'w3resource', (0, -1), [5, 12], {"class":'V', "section":'A'}]
datalist = [1452, 11.23, 1+2j, True, 'w3resource', (0, -1), [5, 12],
            {"class": 'V', "section": 'A'}]
for item in datalist:
   print("Type of ", item, " is ", type(item))

# 8. Write a Python program that prints all the numbers from 0 to 6 except 3 and 6.
# Note : Use 'continue' statement.
# Expected Output : 0 1 2 4 5
for x in range(6):
    if (x == 3 or x == 6):
        continue
    print(x, end=' ')
print("\n")

# 9. Write a Python program to get the Fibonacci series between 0 to 50. 
# Note : The Fibonacci Sequence is the series of numbers :
# 0, 1, 1, 2, 3, 5, 8, 13, 21, ....
# Every next number is found by adding up the two numbers before it.
# Expected Output : 1 1 2 3 5 8 13 21 34
x, y = 0, 1
while y < 50:
    print(y)
    x, y = y, x+y

# 10. Write a Python program which iterates the integers from 1 to 50. For multiples of three print "Fizz" instead of the number and for the multiples of five print "Buzz". For numbers which are multiples of both three and five print "FizzBuzz".
# Sample Output :
# fizzbuzz
# 1
# 2
# fizz
# 4
# buzz
for fizzbuzz in range(51):
    if fizzbuzz % 3 == 0 and fizzbuzz % 5 == 0:
        print("fizzbuzz")
        continue
    elif fizzbuzz % 3 == 0:
        print("fizz")
        continue
    elif fizzbuzz % 5 == 0:
        print("buzz")
        continue
    print(fizzbuzz)

# 11. Write a Python program which takes two digits m (row) and n (column) as input and generates a two-dimensional array. The element value in the i-th row and j-th column of the array should be i*j. 
# Note :
# i = 0,1.., m-1
# j = 0,1, n-1.
# Test Data : Rows = 3, Columns = 4
# Expected Result : [[0, 0, 0, 0], [0, 1, 2, 3], [0, 2, 4, 6]]
row_num = int(input("Input number of rows: "))
col_num = int(input("Input number of columns: "))
multi_list = [[0 for col in range(col_num)] for row in range(row_num)]
for row in range(row_num):
    for col in range(col_num):
        multi_list[row][col]= row*col

print(multi_list)

# 12. Write a Python program that accepts a sequence of lines (blank line to terminate) as input and prints the lines as output (all characters in lower case). 
lines = []
while True:
    l = input()
    if l:
        lines.append(l.upper())
    else:
        break
for l in lines:
    print(l)

# 13. Write a Python program which accepts a sequence of comma separated 4 digit binary numbers as its input and print the numbers that are divisible by 5 in a comma separated sequence. 
# Sample Data : 0100,0011,1010,1001,1100,1001
# Expected Output : 1010
items = []
num = [x for x in input().split(',')]
for p in num:
    x = int(p, 2)
    if not x % 5:
        items.append(p)
print(','.join(items))

# 14. Write a Python program that accepts a string and calculate the number of digits and letters. 
# Sample Data : Python 3.2
# Expected Output :
# Letters 6
# Digits 2
s = input("Input a string")
d = l = 0
for c in s:
    if c.isdigit():
        d = d+1
    elif c.isalpha():
        l = l+1
    else:
        pass
print("Letters", l)
print("Digits", d)

# 15. Write a Python program to check the validity of password input by users. 
# Validation :
#     At least 1 letter between [a-z] and 1 letter between [A-Z].
#     At least 1 number between [0-9].
#     At least 1 character from [$#@].
#     Minimum length 6 characters.
#     Maximum length 16 characters.
import re
p= input("Input your password")
x = True
while x:  
    if (len(p)<6 or len(p)>12):
        break
    elif not re.search("[a-z]",p):
        break
    elif not re.search("[0-9]",p):
        break
    elif not re.search("[A-Z]",p):
        break
    elif not re.search("[$#@]",p):
        break
    elif re.search("\s",p):
        break
    else:
        print("Valid Password")
        x=False
        break
if x:
    print("Not a Valid Password")


# 16. Write a Python program to find numbers between 100 and 400 (both included) where each digit of a number is an even number. The numbers obtained should be printed in a comma-separated sequence. 
items = []
for i in range(100, 401):
    s = str(i)
    if (int(s[0]) % 2 == 0) and (int(s[1]) % 2 == 0) and (int(s[2]) % 2 == 0):
        items.append(s)
print(",".join(items))

# 17. Write a Python program to print alphabet pattern 'A'. 
# Expected Output:
#   ***                                                                   
#  *   *                                                                  
#  *   *                                                                  
#  *****                                                                  
#  *   *                                                                  
#  *   *                                                                  
#  *   *
result_str = ""
for row in range(0, 7):
    for column in range(0, 7):
        if (((column == 1 or column == 5) and row != 0) or ((row == 0 or row == 3) and (column > 1 and column < 5))):
            result_str = result_str+"*"
        else:
            result_str = result_str+" "
    result_str = result_str+"\n"
print(result_str)

# 18. Write a Python program to print alphabet pattern 'D'. 
# Expected Output:
#  ****                                                                   
#  *   *                                                                  
#  *   *                                                                  
#  *   *                                                                  
#  *   *                                                                  
#  *   *                                                                  
#  **** 
result_str = ""
for row in range(0, 7):
    for column in range(0, 7):
        if (column == 1 or ((row == 0 or row == 6) and (column > 1 and column < 5)) or (column == 5 and row != 0 and row != 6)):
            result_str = result_str+"*"
        else:
            result_str = result_str+" "
    result_str = result_str+"\n"
print(result_str)

# 19. Write a Python program to print alphabet pattern 'E'. 
# Expected Output:
#  *****                                                                  
#  *                                                                      
#  *                                                                      
#  ****                                                                   
#  *                                                                      
#  *                                                                      
#  *****
result_str = ""
for row in range(0, 7):
    for column in range(0, 7):
        if (column == 1 or ((row == 0 or row == 6) and (column > 1 and column < 6)) or (row == 3 and column > 1 and column < 5)):
            result_str = result_str+"*"
        else:
            result_str = result_str+" "
    result_str = result_str+"\n"
print(result_str)

# 20. Write a Python program to print alphabet pattern 'G'. 
# Expected Output:
#   ***                                                                   
#  *   *                                                                  
#  *                                                                      
#  * ***                                                                  
#  *   *                                                                  
#  *   *                                                                  
#   *** 
result_str = ""
for row in range(0, 7):
    for column in range(0, 7):
        if ((column == 1 and row != 0 and row != 6) or ((row == 0 or row == 6) and column > 1 and column < 5) or (row == 3 and column > 2 and column < 6) or (column == 5 and row != 0 and row != 2 and row != 6)):
            result_str = result_str+"*"
        else:
            result_str = result_str+" "
    result_str = result_str+"\n"
print(result_str)

# 21. Write a Python program to print alphabet pattern 'L'. 
# Expected Output:
#  *                                                                      
#  *                                                                      
#  *                                                                      
#  *                                                                      
#  *                                                                      
#  *                                                                      
#  *****
result_str = ""
for row in range(0, 7):
    for column in range(0, 7):
        if (column == 1 or (row == 6 and column != 0 and column < 6)):
            result_str = result_str+"*"
        else:
            result_str = result_str+" "
    result_str = result_str+"\n"
print(result_str)

# 22. Write a Python program to print alphabet pattern 'M'. 
# Expected Output:
#   *       *                                                             
#   *       *                                                             
#   * *   * *                                                             
#   *   *   *                                                             
#   *       *                                                             
#   *       *                                                             
#   *       *
result_str="";    
for row in range(0,7):    
    for column in range(0,7):     
        if (column == 1 or column == 5 or (row == 2 and (column == 2 or column == 4)) or (row == 3 and column == 3)):  
            result_str=result_str+"* "    
        else:      
            result_str=result_str+"  "    
    result_str=result_str+"\n"    
print(result_str);

# 23. Write a Python program to print alphabet pattern 'O'. 
# Expected Output:
#   ***                                                                   
#  *   *                                                                  
#  *   *                                                                  
#  *   *                                                                  
#  *   *                                                                  
#  *   *                                                                  
#   *** 
result_str="";    
for row in range(0,7):    
    for column in range(0,7):     
        if (((column == 1 or column == 5) and row != 0 and row != 6) or ((row == 0 or row == 6) and column > 1 and column < 5)):  
            result_str=result_str+"*"    
        else:      
            result_str=result_str+" "    
    result_str=result_str+"\n"    
print(result_str);

# 24. Write a Python program to print alphabet pattern 'P'. 
# Expected Output:
#  ****                                                                   
#  *   *                                                                  
#  *   *                                                                  
#  ****                                                                   
#  *                                                                      
#  *                                                                      
#  *  
result_str = ""
for row in range(0, 7):
    for column in range(0, 7):
        if (column == 1 or ((row == 0 or row == 3) and column > 0 and column < 5) or ((column == 5 or column == 1) and (row == 1 or row == 2))):
            result_str = result_str+"*"
        else:
            result_str = result_str+" "
    result_str = result_str+"\n"
print(result_str)

# 25. Write a Python program to print alphabet pattern 'R'. 
# Expected Output:
#  ****                                                                   
#  *   *                                                                  
#  *   *                                                                  
#  ****                                                                   
#  * *                                                                    
#  *  *                                                                   
#  *   *
result_str = ""
for row in range(0, 7):
    for column in range(0, 7):
        if (column == 1 or ((row == 0 or row == 3) and column > 1 and column < 5) or (column == 5 and row != 0 and row < 3) or (column == row - 1 and row > 2)):
            result_str = result_str+"*"
        else:
            result_str = result_str+" "
    result_str = result_str+"\n"
print(result_str)

# 26. Write a Python program to print the following patterns. 
# Expected Output:
#   ****                                                                  
#  *                                                                      
#  *                                                                      
#   ***                                                                   
#      *                                                                  
#      *                                                                  
#  **** 
result_str = ""
for row in range(0, 7):
    for column in range(0, 7):
        if (((row == 0 or row == 3 or row == 6) and column > 1 and column < 5) or (column == 1 and (row == 1 or row == 2 or row == 6)) or (column == 5 and (row == 0 or row == 4 or row == 5))):
            result_str = result_str+"*"
        else:
            result_str = result_str+" "
    result_str = result_str+"\n"
print(result_str)

row = 15
col = 18
result_str = ""
for i in range(1, row+1):
    if((i <= 3) or (i >= 7 and i <= 9) or (i >= 13 and i <= 15)):
        for j in range(1, col):
            result_str = result_str+"o"
        result_str = result_str+"\n"
    elif(i >= 4 and i <= 6):
        for j in range(1, 5):
            result_str = result_str+"o"
        result_str = result_str+"\n"
    else:
        for j in range(1, 14):
            result_str = result_str+" "
        for j in range(1, 5):
            result_str = result_str+"o"
        result_str = result_str+"\n"
print(result_str)

# 27. Write a Python program to print alphabet pattern 'T'. 
# Expected Output:
#  *****                                                                  
#    *                                                                    
#    *                                                                    
#    *                                                                    
#    *                                                                    
#    *                                                                    
#    *  
result_str = ""
for row in range(0, 7):
    for column in range(0, 7):
        if (column == 3 or (row == 0 and column > 0 and column < 6)):
            result_str = result_str+"*"
        else:
            result_str = result_str+" "
    result_str = result_str+"\n"
print(result_str)

# 28. Write a Python program to print alphabet pattern 'U'. 
# Expected Output:
#  *   *                                                                  
#  *   *                                                                  
#  *   *                                                                  
#  *   *                                                                  
#  *   *                                                                  
#  *   *                                                                  
#   *** 
result_str = ""
for row in range(0, 7):
    for column in range(0, 7):
        if (((column == 1 or column == 5) and row != 6) or (row == 6 and column > 1 and column < 5)):
            result_str = result_str+"*"
        else:
            result_str = result_str+" "
    result_str = result_str+"\n"
print(result_str)

# 29. Write a Python program to print alphabet pattern 'X'. 
# Expected Output:
#  *   *                                                                  
#  *   *                                                                  
#   * *                                                                   
#    *                                                                    
#   * *                                                                   
#  *   *                                                                  
#  *   *
result_str = ""
for row in range(0, 7):
    for column in range(0, 7):
        if (((column == 1 or column == 5) and (row > 4 or row < 2)) or row == column and column > 0 and column < 6 or (column == 2 and row == 4) or (column == 4 and row == 2)):
            result_str = result_str+"*"
        else:
            result_str = result_str+" "
    result_str = result_str+"\n"
print(result_str)

# 30. Write a Python program to print alphabet pattern 'Z'. 
# Expected Output:
# *******                                                                 
#      *                                                                  
#     *                                                                   
#    *                                                                    
#   *                                                                     
#  *                                                                      
# *******
result_str = ""
for row in range(0, 7):
    for column in range(0, 7):
        if (((row == 0 or row == 6) and column >= 0 and column <= 6) or row+column == 6):
            result_str = result_str+"*"
        else:
            result_str = result_str+" "
    result_str = result_str+"\n"
print(result_str)

# 31. Write a Python program to calculate a dog's age in dog's years. 
# Note: For the first two years, a dog year is equal to 10.5 human years. After that, each dog year equals 4 human years.
# Expected Output:
# Input a dog's age in human years: 15                                    
# The dog's age in dog's years is 73
h_age = int(input("Input a dog's age in human years: "))
if h_age < 0:
	print("Age must be positive number.")
	exit()
elif h_age <= 2:
	d_age = h_age * 10.5
else:
	d_age = 21 + (h_age - 2)*4

print("The dog's age in dog's years is", d_age)

# 32. Write a Python program to check whether an alphabet is a vowel or consonant. 
# Expected Output:
# Input a letter of the alphabet: k                                       
# k is a consonant.
l = input("Input a letter of the alphabet: ")

if l in ('a', 'e', 'i', 'o', 'u'):
	print("%s is a vowel." % l)
elif l == 'y':
	print("Sometimes letter y stand for vowel, sometimes stand for consonant.")
else:
	print("%s is a consonant." % l)

# 33. Write a Python program to convert month name to a number of days. 
# Expected Output:
# List of months: January, February, March, April, May, June, July, August
# , September, October, November, December                                
# Input the name of Month: February                                       
# No. of days: 28/29 days 
print("List of months: January, February, March, April, May, June, July, August, September, October, November, December")
month_name = input("Input the name of Month: ")

if month_name == "February":
	print("No. of days: 28/29 days")
elif month_name in ("April", "June", "September", "November"):
	print("No. of days: 30 days")
elif month_name in ("January", "March", "May", "July", "August", "October", "December"):
	print("No. of days: 31 day")
else:
	print("Wrong month name")

# 34. Write a Python program to sum of two given integers. However, if the sum is between 15 to 20 it will return 20. 
def sum(x, y):
    sum = x + y
    if sum in range(15, 20):
        return 20
    else:
        return sum
print(sum(10, 6))
print(sum(10, 2))
print(sum(10, 12))

# 35. Write a Python program to check a string represent an integer or not. 
# Expected Output:
# Input a string: Python                                                  
# The string is not an integer.  
text = input("Input a string: ")
text = text.strip()
if len(text) < 1:
    print("Input a valid text")
else:
    if all(text[i] in "0123456789" for i in range(len(text))):
        print("The string is an integer.")
    elif (text[0] in "+-") and \
            all(text[i] in "0123456789" for i in range(1, len(text))):
        print("The string is an integer.")
    else:
        print("The string is not an integer.")

# 36. Write a Python program to check a triangle is equilateral, isosceles or scalene. 
# Note :
# An equilateral triangle is a triangle in which all three sides are equal.
# A scalene triangle is a triangle that has three unequal sides.
# An isosceles triangle is a triangle with (at least) two equal sides.
# Expected Output:
# Input lengths of the triangle sides:                                    
# x: 6                                                                    
# y: 8                                                                    
# z: 12                                                                   
# Scalene triangle  
print("Input lengths of the triangle sides: ")
x = int(input("x: "))
y = int(input("y: "))
z = int(input("z: "))

if x == y == z:
	print("Equilateral triangle")
elif x == y or y == z or z == x:
	print("isosceles triangle")
else:
	print("Scalene triangle")

# 37. Write a Python program that reads two integers representing a month and day and prints the season for that month and day. 
# Expected Output:
# Input the month (e.g. January, February etc.): july                     
# Input the day: 31                                                       
# Season is autumn  
month = input("Input the month (e.g. January, February etc.): ")
day = int(input("Input the day: "))

if month in ('January', 'February', 'March'):
	season = 'winter'
elif month in ('April', 'May', 'June'):
	season = 'spring'
elif month in ('July', 'August', 'September'):
	season = 'summer'
else:
	season = 'autumn'

if (month == 'March') and (day > 19):
	season = 'spring'
elif (month == 'June') and (day > 20):
	season = 'summer'
elif (month == 'September') and (day > 21):
	season = 'autumn'
elif (month == 'December') and (day > 20):
	season = 'winter'
print("Season is", season)

# 38. Write a Python program to display astrological sign for given date of birth. 
# Expected Output:
# Input birthday: 15                                                      
# Input month of birth (e.g. march, july etc): may                        
# Your Astrological sign is : Taurus 
day = int(input("Input birthday: "))
month = input("Input month of birth (e.g. march, july etc): ")
if month == 'december':
	astro_sign = 'Sagittarius' if (day < 22) else 'capricorn'
elif month == 'january':
	astro_sign = 'Capricorn' if (day < 20) else 'aquarius'
elif month == 'february':
	astro_sign = 'Aquarius' if (day < 19) else 'pisces'
elif month == 'march':
	astro_sign = 'Pisces' if (day < 21) else 'aries'
elif month == 'april':
	astro_sign = 'Aries' if (day < 20) else 'taurus'
elif month == 'may':
	astro_sign = 'Taurus' if (day < 21) else 'gemini'
elif month == 'june':
	astro_sign = 'Gemini' if (day < 21) else 'cancer'
elif month == 'july':
	astro_sign = 'Cancer' if (day < 23) else 'leo'
elif month == 'august':
	astro_sign = 'Leo' if (day < 23) else 'virgo'
elif month == 'september':
	astro_sign = 'Virgo' if (day < 23) else 'libra'
elif month == 'october':
	astro_sign = 'Libra' if (day < 23) else 'scorpio'
elif month == 'november':
	astro_sign = 'scorpio' if (day < 22) else 'sagittarius'
print("Your Astrological sign is :", astro_sign)

# 39. Write a Python program to display the sign of the Chinese Zodiac for given year in which you were born. 
# Expected Output:
# Input your birth year: 1973                                             
# Your Zodiac sign : Ox  
year = int(input("Input your birth year: "))
if (year - 2000) % 12 == 0:
    sign = 'Dragon'
elif (year - 2000) % 12 == 1:
    sign = 'Snake'
elif (year - 2000) % 12 == 2:
    sign = 'Horse'
elif (year - 2000) % 12 == 3:
    sign = 'sheep'
elif (year - 2000) % 12 == 4:
    sign = 'Monkey'
elif (year - 2000) % 12 == 5:
    sign = 'Rooster'
elif (year - 2000) % 12 == 6:
    sign = 'Dog'
elif (year - 2000) % 12 == 7:
    sign = 'Pig'
elif (year - 2000) % 12 == 8:
    sign = 'Rat'
elif (year - 2000) % 12 == 9:
    sign = 'Ox'
elif (year - 2000) % 12 == 10:
    sign = 'Tiger'
else:
    sign = 'Hare'
print("Your Zodiac sign :",sign)


# 40. Write a Python program to find the median of three values. 
# Expected Output:
# Input first number: 15                                                  
# Input second number: 26                                                 
# Input third number: 29                                                  
# The median is 26.0   
a = float(input("Input first number: "))
b = float(input("Input second number: "))
c = float(input("Input third number: "))
if a > b:
    if a < c:
        median = a
    elif b > c:
        median = b
    else:
        median = c
else:
    if a > c:
        median = a
    elif b < c:
        median = b
    else:
        median = c
print("The median is", median)

# 41. Write a Python program to get next day of a given date. 
# Expected Output:
# Input a year: 2016                                                      
# Input a month [1-12]: 08                                                
# Input a day [1-31]: 23                                                  
# The next date is [yyyy-mm-dd] 2016-8-24   
year = int(input("Input a year: "))

if (year % 400 == 0):
    leap_year = True
elif (year % 100 == 0):
    leap_year = False
elif (year % 4 == 0):
    leap_year = True
else:
    leap_year = False

month = int(input("Input a month [1-12]: "))

if month in (1, 3, 5, 7, 8, 10, 12):
    month_length = 31
elif month == 2:
    if leap_year:
        month_length = 29
    else:
        month_length = 28
else:
    month_length = 30
day = int(input("Input a day [1-31]: "))
if day < month_length:
    day += 1
else:
    day = 1
    if month == 12:
        month = 1
        year += 1
    else:
        month += 1
print("The next date is [yyyy-mm-dd] %d-%d-%d." % (year, month, day))

# 42. Write a Python program to calculate the sum and average of n integer numbers (input from the user). Input 0 to finish. 
print("Input some integers to calculate their sum and average. Input 0 to exit.")
count = 0
sum = 0.0
number = 1
while number != 0:
	number = int(input(""))
	sum = sum + number
	count += 1
if count == 0:
	print("Input some numbers")
else:
	print("Average and Sum of the above numbers are: ", sum / (count-1), sum)

# 43. Write a Python program to create the multiplication table (from 1 to 10) of a number. 
# Expected Output:
# Input a number: 6                                                       
# 6 x 1 = 6                                                               
# 6 x 2 = 12                                                              
# 6 x 3 = 18                                                              
# 6 x 4 = 24                                                              
# 6 x 5 = 30                                                              
# 6 x 6 = 36                                                              
# 6 x 7 = 42                                                              
# 6 x 8 = 48                                                              
# 6 x 9 = 54                                                              
# 6 x 10 = 60 
n = int(input("Input a number: "))
# use for loop to iterate 10 times
for i in range(1,11):
   print(n,'x',i,'=',n*i)

# 44. Write a Python program to construct the following pattern, using a nested loop number. 
# Expected Output:
# 1
# 22
# 333
# 4444
# 55555
# 666666
# 7777777
# 88888888
# 999999999
for i in range(10):
    print(str(i) * i)
