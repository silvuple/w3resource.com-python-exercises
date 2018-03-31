"""
1. Write a Python program to find those numbers which are divisible by 7
and multiple of 5, between 1500 and 2700 (both included).
"""

my_list = []

for i in range(1500, 2701):
    if i%7 == 0 and i%5 == 0:
        my_list.append(i)
print(my_list)

"""
2. Write a Python program to convert temperatures to and from celsius, fahrenheit.
Formula : c/5 = (f-32)/9 [ where c=temp in celsius and f=temp in fahrenheit 
Expected Output : 
60°C is 140 in Fahrenheit
45°F is 7 in Celsius
"""

def celsius_fahrenheit_conversion(temperature, scale_name='F'):
    if scale_name == 'C':
        converted = temperature*9/5+32
    elif scale_name == 'F':
        converted = (temperature-32)*5/9
    return converted

t = float(input('enter temperature '))
s = input('enter F for Fahrenheit or C for Celsius ').upper()

if s == 'F':
    print('%.0f°F is %.0f in Celsius' % (t, celsius_fahrenheit_conversion(t, s)))
elif s == 'C':
    print('%.0f°C is %.0f in Fahrenheit' % (t, celsius_fahrenheit_conversion(t, s)))
    
"""
3. Write a Python program to guess a number between 1 to 9. 
Note : User is prompted to enter a guess. If the user guesses wrong then
the prompt appears again until the guess is correct, on successful guess,
user will get a "Well guessed!" message, and the program will exit.
"""

from random import randint

number = randint(1, 9)
guess = int(input('guess a number between 1 and 9: '))

while guess != number:
    guess = int(input('you guessed wrong, guess again: '))

print('Well guesed!')

"""
4. Write a Python program to construct the following pattern,
using a nested for loop.
* 
* * 
* * * 
* * * * 
* * * * * 
* * * * 
* * * 
* * 
*
"""

width = int(input('choose pattern width '))

# solution with 2 for loops
for i in range(1, width):
    print('*' * i)
for i in range(width, 0, -1):
    print('*' * i)

# solution with for loop and if statement
for row in range(1, width*2):
    if row < width:
        print('*' * row)
    else:
        print('*' * (width*2 - row))

"""
5. Write a Python program that accepts a word from the user and reverse it.
"""

word = input('please eneter a word ')

# solution 1
print(''.join((reversed(word))))

# solution 2
word_list = list(word)
print(''.join(word_list[::-1]))

# solution 3
reversed_word = ''
for i in range(len(word)-1, -1, -1):
    reversed_word += word[i]
print(reversed_word)

"""
6. Write a Python program to count the number of even and odd numbers
from a series of numbers. 
Sample numbers : numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9) 
Expected Output : 
Number of even numbers : 5
Number of odd numbers : 4
"""
    
numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9)
odds_counter = 0
evens_counter = 0
for i in numbers:
    if i%2 == 0:
        evens_counter += 1
    else:
        odds_counter += 1

print('Number of even numbers: %d' % evens_counter)
print('Number of odd numbers: %d' % odds_counter)

"""
7. Write a Python program that prints each item and its corresponding type
from the following list.
Sample List : datalist = [1452, 11.23, 1+2j, True, 'w3resource',
(0, -1), [5, 12], {"class":'V', "section":'A'}]
"""
datalist = [1452, 11.23, 1+2j, True, 'w3resource', (0, -1),
            [5, 12], {"class":'V', "section":'A'}]

for i in datalist:
    print(i, type(i))

"""
8. Write a Python program that prints all the numbers from 0 to 6 except 3 and 6.
Note : Use 'continue' statement. 
Expected Output : 0 1 2 4 5
"""

for i in range(7):
    if i == 3 or i == 6:
        continue
    print(i, end = ' ')

"""
9. Write a Python program to get the Fibonacci series between 0 to 50.
Note : The Fibonacci Sequence is the series of numbers :
0, 1, 1, 2, 3, 5, 8, 13, 21, .... 
Every next number is found by adding up the two numbers before it.
Expected Output : 1 1 2 3 5 8 13 21 34
"""
fib_list = [1, 1]
while fib_list[-1] <= 50:
    fib_list.append(fib_list[-1]+fib_list[-2])
print(fib_list[:-1])

"""
10. Write a Python program which iterates the integers from 1 to 50. For multiples of three print "Fizz" instead of the number and for the multiples of five print "Buzz". For numbers which are multiples of both three and five print "FizzBuzz".
Sample Output : 
1
2
fizz
4 
buzz
"""
for i in range(1, 51):
    if i%3 == 0 and i%5 == 0:
        print('fizzbuzz')
    elif i%3 == 0:
        print('fizz')
    elif i%5 == 0:
        print('buzz')
    else:
        print(i)

"""
11. Write a Python program which takes two digits m (row) and n (column)
as input and generates a two-dimensional array. The element value in the i-th
row and j-th column of the array should be i*j. 
Note :
i = 0,1.., m-1 
j = 0,1, n-1.
Test Data : Rows = 3, Columns = 4 
Expected Result : [[0, 0, 0, 0], [0, 1, 2, 3], [0, 2, 4, 6]]
"""

Rows = 3
Columns = 4

my_array = [[column*row for column in range(Columns)] for row in range(Rows)]
print(my_array)

"""
12. Write a Python program that accepts a sequence of lines (blank line to
terminate) as input and prints the lines as output (all characters in lower case).
"""
lines = []
while True:
    line = input()
    if line:
        lines.append(line.upper())
    else:
        break
for line in lines:
    print(line)

"""
13. Write a Python program which accepts a sequence of comma separated
4 digit binary numbers as its input and print the numbers that are divisible
by 5 in a comma separated sequence. 
Sample Data : 0100,0011,1010,1001,1100,1001
Expected Output : 1010
"""

my_bins = input('enter some bins: ')
input_bins = my_bins.split(',')
output_bins = []

for i in input_bins:
    if int(i, base=2)%5 == 0:
        output_bins.append(i)

print(','.join(output_bins))

"""
14. Write a Python program that accepts a string and calculate the number
of digits and letters. 
Sample Data : Python 3.2
Expected Output :
Letters 6 
Digits 2
"""

my_string = input('enter something: ')
count_digits = 0
count_alpha = 0
for i in my_string:
    if i.isdigit():
        count_digits += 1
    if i.isalpha():
        count_alpha += 1

print('%d letters, %d digits' % (count_alpha, count_digits))

"""
15. Write a Python program to check the validity of password input by users.
Validation :

At least 1 letter between [a-z] and 1 letter between [A-Z].
At least 1 number between [0-9].
At least 1 character from [$#@].
Minimum length 6 characters.
Maximum length 16 characters.
"""

password = input('please enter a valid pasword: ')
while True:
    length, digits, lowers, uppers, characters = 0, 0, 0, 0, 0
    if len(password) > 6 and len(password) < 16:
        length = 1
    for i in password:
        if i.isdigit():
            digits = 1
            continue
        if i.islower():
            lowers = 1
            continue
        if i.isupper():
            uppers = 1
            continue
        if i in '$#@':
            characters = 1
            continue
    rules = [length, digits, lowers, uppers, characters]
    if all(rules):
        print('your password is good')
        break
    else:
        print('your password is not good, try again')
        password = input('please enter a valid pasword: ')

"""
16. Write a Python program to find numbers between 100 and 400 (both included)
where each digit of a number is an even number. The numbers obtained should be
printed in a comma-separated sequence.
"""
evens_list = []
for i in range(100, 401):
    number = i
    while number > 0:
        digit = number%10
        if digit%2 == 0:
            number = number//10
            even = True
        else:
            even = False
            break
    if even:
        evens_list.append(i)
print(', '.join(map(str, evens_list)))

"""
17. Write a Python program to print alphabet pattern 'A'. 
Expected Output:
  ***                                                                   
 *   *                                                                  
 *   *                                                                  
 *****                                                                  
 *   *                                                                  
 *   *                                                                  
 *   *
"""

width = 5
height = width + 2
STAR = '*'
space = ' '
for i in range(1, height+1):
    # first row of A
    if i == 1:
        print(space + STAR * (width-2))
    # middle row of A
    elif i == int(height/2+1):
        print(STAR * width)
    # rest of A
    else:
        print(STAR + space * (width-2) + STAR)

"""
18. Write a Python program to print alphabet pattern 'D'.
Expected Output:
 ****                                                                   
 *   *                                                                  
 *   *                                                                  
 *   *                                                                  
 *   *                                                                  
 *   *                                                                  
 ****
"""

width = 5
height = width + 2
STAR = '*'
space = ' '
for i in range(1, height+1):
    # first and last row of D
    if i == 1 or i == height:
        print(STAR * (width-1))
    # rest of D
    else:
        print(STAR + space * (width-2) + STAR)

"""
19. Write a Python program to print alphabet pattern 'E'.
Expected Output:
 *****                                                                  
 *                                                                      
 *                                                                      
 ****                                                                   
 *                                                                      
 *                                                                      
 *****
"""

width = 5
height = width + 2
STAR = '*'
for i in range(1, height+1):
    # first and last row of E
    if i == 1 or i == height:
        print(STAR * width)
    # middle of E
    elif i == int(height/2+1):
        print(STAR * (width-1))
    # rest of E
    else:
        print(STAR)

"""
20. Write a Python program to print alphabet pattern 'G'.
Expected Output:
  ***                                                                   
 *   *                                                                  
 *                                                                      
 * ***                                                                  
 *   *                                                                  
 *   *                                                                  
  *** 
"""

width = 5
height = width + 2
STAR = '*'
space = ' '
for i in range(1, height+1):
    # first and last row of G
    if i == 1 or i == height:
        print(space + STAR * (width-2))
    # row above middle of G except the second row
    elif i > 2 and i <= int(height/2):
        print(STAR)
    # middle of G
    elif i == int(height/2+1):
        print(STAR + space + STAR * (width-2))
    # rest of G
    else:
        print(STAR + space * (width-2) + STAR)

"""
21. Write a Python program to print alphabet pattern 'L'.
Expected Output:
 *                                                                      
 *                                                                      
 *                                                                      
 *                                                                      
 *                                                                      
 *                                                                      
 *****
"""

width = 5
height = width + 2
STAR = '*'
for i in range(1, height+1):
    # last row of G
    if i == height:
        print(STAR * width)
    # rest of G
    else:
        print(STAR)

"""
22. Write a Python program to print alphabet pattern 'M'. 
Expected Output:
  *       *                                                             
  *       *                                                             
  * *   * *                                                             
  *   *   *                                                             
  *       *                                                             
  *       *                                                             
  *       *
"""

width = 5 # must be an odd number for symmetry
height = width + 2
STAR = '*'
space = ' '
for i in range(1, height+1):
    # middle of M
    if i == int(height/2+1):
        print(STAR + space * int((width-3)/2) + STAR + space * int((width-3)/2) + STAR)
    # row above middle of M
    elif i < int(height/2+1) and i > (int(height/4+1)):
        print(STAR + space * (i-3) + STAR + space * (width-4-2*(i-3)) + STAR + space * (i-3) + STAR)
    # rest of M
    else:
        print(STAR + space * (width-2) + STAR)

"""
23. Write a Python program to print alphabet pattern 'O'. 
Expected Output:
  ***                                                                   
 *   *                                                                  
 *   *                                                                  
 *   *                                                                  
 *   *                                                                  
 *   *                                                                  
  ***
"""

width = 5
height = width + 2
STAR = '*'
space = ' '
for i in range(1, height+1):
    # first and last row of O
    if i == 1 or i == height:
        print(space + STAR * (width-2))
    # rest of D
    else:
        print(STAR + space * (width-2) + STAR)

"""
24. Write a Python program to print alphabet pattern 'P'.
Expected Output:
 ****                                                                   
 *   *                                                                  
 *   *                                                                  
 ****                                                                   
 *                                                                      
 *                                                                      
 *
"""

width = 5
height = width + 2
STAR = '*'
space = ' '
for i in range(1, height+1):
    # first and middle row of P
    if i == 1 or i == int(height/2+1):
        print(STAR * (width-1))
    # rows between first and middle row of P
    elif i > 1 and i < int(height/2+1):
        print(STAR + space * (width-2) + STAR)
    # lower part of P
    else:
        print(STAR)

"""
25. Write a Python program to print alphabet pattern 'R'.
Expected Output:
 ****                                                                   
 *   *                                                                  
 *   *                                                                  
 ****                                                                   
 * *                                                                    
 *  *                                                                   
 *   *
"""

width = 5
height = width + 2
STAR = '*'
space = ' '
for i in range(1, height+1):
    # first and middle row of R
    if i == 1 or i == int(height/2+1):
        print(STAR * (width-1))
    # rows between first and middle row of R
    elif i > 1 and i < int(height/2+1):
        print(STAR + space * (width-2) + STAR)
    # lower part of R
    else:
        print(STAR + space * (i-4) + STAR)

"""
26. Write a Python program to print the following patterns. 
Expected Output:
  ****                                                                  
 *                                                                      
 *                                                                      
  ***                                                                   
     *                                                                  
     *                                                                  
 ****

ooooooooooooooooo                                                       
ooooooooooooooooo                                                       
ooooooooooooooooo                                                       
oooo                                                                    
oooo                                                                    
oooo                                                                    
ooooooooooooooooo                                                       
ooooooooooooooooo                                                       
ooooooooooooooooo                                                       
             oooo                                                       
             oooo                                                       
             oooo                                                       
ooooooooooooooooo                                                       
ooooooooooooooooo                                                       
ooooooooooooooooo 
"""

width = 5
height = width + 2
STAR = '*'
space = ' '
for i in range(1, height+1):
    # first row of S
    if i == 1:
        print(space + STAR * (width-1))
    # middle row of S
    elif i == int(height/2+1):
        print(space + STAR * (width-2) + space)
    # last row of S
    elif i == height:
        print(STAR * (width-1) + space)
    # rows above middle row of S (exept first row)
    elif i > 1 and i < int(height/2+1):
        print(STAR)
    else:
        print(space * (width-1) + STAR)

width = 4
height = width + 1
STAR = 'ooo'
space = ' '
for i in range(1, height+1):
    # first, last and middle row of S
    if i == 1 or i == height or i == int(height/2+1):
        for j in range(3):
            print(STAR * width)
    # rows between first and middle row of S
    elif i > 1 and i < int(height/2+1):
        for j in range(3):
            print(STAR)
    # rows below middle of S
    else:
        for j in range(3):
            print(space * (width-1)*3 + STAR)

"""
27. Write a Python program to print alphabet pattern 'T'. 
Expected Output:
 *****                                                                  
   *                                                                    
   *                                                                    
   *                                                                    
   *                                                                    
   *                                                                    
   *  
"""

width = 5
height = width + 2
STAR = '*'
space = ' '
for i in range(1, height+1):
    # first row of T
    if i == 1:
        print(STAR * width)
    # rest of T
    else:
        print(space * int((width-1)/2) + STAR + space * int((width-1)/2))

"""
28. Write a Python program to print alphabet pattern 'U'. 
Expected Output:
 *   *                                                                  
 *   *                                                                  
 *   *                                                                  
 *   *                                                                  
 *   *                                                                  
 *   *                                                                  
  *** 
"""

width = 5
height = width + 2
STAR = '*'
space = ' '
for i in range(1, height+1):
    # last row of U
    if i == height:
        print(space + STAR * (width-2) + space)
    else:
        print(STAR + space * (width-2) + STAR)

"""
29. Write a Python program to print alphabet pattern 'X'.
Expected Output:
 *   *                                                                  
 *   *
  * *                                                                   
   *                                                                    
  * *                                                                   
 *   *                                                                  
 *   *
"""

width = 13  # must be an odd number for symmetry
height = width + 2
STAR = '*'
space = ' '
for i in range(1, height+1):
    # middle of X
    if i == int(height/2+1):
        print(space * int((width-1)/2) + STAR + space * int((width-1)/2))
        
    # row above middle of X
    elif i < int(height/2+1) and i > int(height/4):
        print(space * (i-2) + STAR + space * (width-2-2*(i-2)) + STAR + space * (i-2))
        
    # row below middle of X
    elif i > int(height/2+1) and i <= int(height*3/4+1):
        print(space * (width-i+1) + STAR + space * (width-2-2*(width-i+1))+ STAR + space * (width-i+1))
        
    # rest of M (first rows and last rows)
    else:
        print(STAR + space * (width-2) + STAR)

"""
30. Write a Python program to print alphabet pattern 'Z'. 
Expected Output:
*******                                                                 
     *                                                                  
    *                                                                   
   *                                                                    
  *                                                                     
 *                                                                      
*******
"""

width = 7
height = width
STAR = '*'
space = ' '
for i in range(1, height+1):
    # first and last row of Z
    if i == 1 or i == height:
        print(STAR * width)
    # rest of Z
    else:
        print(space * (width-i) + STAR + space * (i-1))

"""
31. Write a Python program to calculate a dog's age in dog's years. 
Note: For the first two years, a dog year is equal to 10.5 human years.
After that, each dog year equals 4 human years.
Expected Output:

Input a dog's age in human years: 15                                    
The dog's age in dog's years is 73
"""
dog_age = float(input("Input a dog's age in human years: "))
dogs_years = float()
if dog_age <= 2:
    dogs_years = dog_age*10.5
else:
    dogs_years += 21 + (dog_age-2)*4
print("The dog's age in dog's years is %.1f" % dogs_years)
                
"""
32. Write a Python program to check whether an alphabet is
a vowel or consonant. 
Expected Output:
Input a letter of the alphabet: k                                       
k is a consonant.
"""

letter = input("Input a letter of the alphabet: ").lower()
while not letter.isalpha():
    print("the character you have entered is not an english leter, try again")
    letter = input("Input a letter of the alphabet: ").lower()
if letter in 'aeiouy':      # i include y in vowels
    print(letter, 'is a vowel')
else:
    print(letter, 'is a consonant')

"""
33. Write a Python program to convert month name to a number of days. 
Expected Output:
List of months: January, February, March, April, May, June, July, August
, September, October, November, December                                
Input the name of Month: February                                       
No. of days: 28/29 days
"""

months = ['January', 'February', 'March', 'April', 'May', 'June', 'July',
          'August', 'September', 'October', 'November', 'December']
month = input('please enter a month ').title()
if month in months:
    if month == 'February':
        print('No. of days: 28/29 days')
    elif month in ('April', 'June', 'September', 'November'):
        print('No. of days: 30 days')
    else:
        print('No. of days: 31 days')
else:
    print('you enter a wrong month name')

"""
34. Write a Python program to sum of two given integers.
However, if the sum is between 15 to 20 it will return 20.
"""

int1 = int(input('integer 1: '))
int2 = int(input('integer 2: '))
def sum_of_integers(i, j):
    sum_of_int = i+j
    if sum_of_int in range(15, 21):
        return 20
    else:
        return sum_of_int
print(sum_of_integers(int1, int2))

"""
35. Write a Python program to check a string represent an integer or not.
Expected Output:
Input a string: Python                                                  
The string is not an integer.
"""

my_string = input('Input a string: ')
try:
    int(my_string)
    print('The string is an integer')
except:
    print('The string is not an integer')

"""
36. Write a Python program to check a triangle is equilateral,
isosceles or scalene. 
Note:
An equilateral triangle is a triangle in which all three sides are equal.
A scalene triangle is a triangle that has three unequal sides.
An isosceles triangle is a triangle with (at least) two equal sides.
Expected Output:
Input lengths of the triangle sides:                                    
x: 6                                                                    
y: 8                                                                    
z: 12                                                                   
Scalene triangle
"""

x = int(input('x: '))
y = int(input('y: '))
z = int(input('z: '))

if x == y == z:
    print('equilateral')
elif x != y != z:
    print('scalene')
else:
    print('isosceles')

"""
40. Write a Python program to find the median of three values.
Expected Output:
Input first number: 15                                                  
Input second number: 26                                                 
Input third number: 29                                                  
The median is 26.0
"""

x = int(input('Input first number: '))
y = int(input('Input second number: '))
z = int(input('Input third number: '))

if (x>=y and x<=z) or (x>=z and x<=y):
    median = x
elif (y>=x and y<=z) or (y>=z and y<=x):
    median = y
else:
    median = z
print('The median is', median)

"""
42. Write a Python program to calculate the sum and average of n integer
numbers (input from the user). Input 0 to finish. 
"""

number = int(input('input integer: '))
sum_integers = number
n = 1

while number != 0:
    number = int(input('input integer: '))
    sum_integers += number
    n += 1

average = sum_integers/(n-1)
print('sum is ', sum_integers)
print('average is ', average)

"""
43. Write a Python program to create the multiplication table
(from 1 to 10) of a number. 
Expected Output:
Input a number: 6                                                       
6 x 1 = 6                                                               
6 x 2 = 12                                                              
6 x 3 = 18                                                              
6 x 4 = 24                                                              
6 x 5 = 30                                                              
6 x 6 = 36                                                              
6 x 7 = 42                                                              
6 x 8 = 48                                                              
6 x 9 = 54                                                              
6 x 10 = 60
"""

number = int(input('Input a number: '))

for i in range(1, 11):
    print('%d x %d = %d' % (number, i, number*i))

"""
44. Write a Python program to construct the following pattern,
using a nested loop number. 
Expected Output:
1
22
333
4444
55555
666666
7777777
88888888
999999999
"""

n = int(input('type a number: '))
for i in range(1,n+1):
    print(str(i)*i)
