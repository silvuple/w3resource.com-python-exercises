"""
4. Write a Python program to reverse a string.
Sample String : "1234abcd"
Expected Output : "dcba4321"
"""

def reverse_string(my_string):
    reversed_string = ''
    for character in my_string[::-1]:
        reversed_string += character
    return reversed_string

my_string = input('please enter a string: ')
print('the reversed string is:', reverse_string(my_string))

"""
5. Write a Python function to calculate the factorial of a number
(a non-negative integer). The function accepts the number as an argument.
"""
# solution 1
def factorial(number):
    fact = 1
    for i in range(1, number+1):
        fact *= i
    return fact

my_number = int(input('please enter a positive integer: '))
print('the factorial of your integer is:', factorial(my_number))

# solution 2
def factorial(number):
    fact = 1
    if number > 1:
        fact = number*(factorial(number-1))
    return fact

my_number = int(input('please enter a positive integer: '))
print('the factorial of your integer is:', factorial(my_number))

"""
6.Write a Python function to check whether a number is in a given range.
"""

def is_in_range(number, n, m):
    if number in range(n,m+1):
        return True
    else:
        return False

num = int(input('please enter a number: '))
n = 0
m = 10
print(num, 'is in range', n, '-', m, is_in_range(num, n, m))

"""
8. Write a Python function that takes a list and returns a new list
with unique elements of the first list. 
Sample List : [1,2,3,3,3,3,4,5]
Unique List : [1, 2, 3, 4, 5]
"""

def uniques(my_list):
    uniques =[]
    for i in my_list:
        if i not in uniques:
            uniques.append(i)
    return uniques

sample_list = [1,2,3,3,3,3,4,5]
print(uniques(sample_list))

"""
9. Write a Python function that takes a number as a parameter and check
the number is prime or not. 
Note : A prime number (or a prime) is a natural number greater than 1
and that has no positive divisors other than 1 and itself.
"""

def is_prime(number):
    if number == 1:
        return True
    for i in range(2, number):
        if number%i == 0:
            return False
    return True

my_number = int(input('please enter a number: '))

if is_prime(my_number):
    print('your number is prime')
else:
    print('your number is not prime')

"""
11. Write a Python function to check whether a number is perfect or not.
According to Wikipedia : In number theory, a perfect number is a positive
integer that is equal to the sum of its proper positive divisors, that is,
the sum of its positive divisors excluding the number itself (also known as
its aliquot sum). Equivalently, a perfect number is a number that is half
the sum of all of its positive divisors (including itself).
Example : The first perfect number is 6, because 1, 2, and 3 are its proper
positive divisors, and 1 + 2 + 3 = 6. Equivalently, the number 6 is equal to
half the sum of all its positive divisors: ( 1 + 2 + 3 + 6 ) / 2 = 6.
The next perfect number is 28 = 1 + 2 + 4 + 7 + 14. This is followed by
the perfect numbers 496 and 8128.
"""

def is_perfect(number):
    divisors_sum = 0
    for i in range(1, int(number/2)+1):
        if number%i == 0:
            divisors_sum += i
    if divisors_sum == number:
        return True
    else:
        return False

print(is_perfect(6))
print(is_perfect(10))
print(is_perfect(28))
print(is_perfect(30))

"""
13. Write a Python function that prints out the first n rows of Pascal's
triangle. 
Note : Pascal's triangle is an arithmetic and geometric figure first imagined
by Blaise Pascal. In Pascal's triangle each number is the two numbers above
it added together
"""
    
def pascals_triangle(n):
    one = [1]
    print(one)
    for i in range(n):
        row = [row[x]+row[x+1] for x in range(i)]
        row = one + row + one
        print(row)
        
pascals_triangle(5)       

"""
14. Write a Python function to check whether a string is a pangram or not.
Note : Pangrams are words or sentences containing every letter of the
alphabet at least once.
For example : "The quick brown fox jumps over the lazy dog"
"""

def is_pangram(your_string):
    alphabet = ''
    for letter in your_string.lower():
        if letter.isalpha() and letter not in alphabet:
            alphabet += letter
    alphabet = ''.join(sorted(alphabet))
    if alphabet == 'abcdefghijklmnopqrstuvwxyz':
        return True
    else:
        return False

print(is_pangram("The quick brown fox jumps over the lazy dog"))

"""
15. Write a Python program that accepts a hyphen-separated sequence of words as input and prints the words in a hyphen-separated sequence after sorting them alphabetically. Go to the editor
Sample Items : green-red-yellow-black-white
Expected Result : black-green-red-white-yellow
"""

def sort_hyphen(your_string):
    your_list = your_string.split('-')
    your_list.sort()
    return '-'.join(your_list)

my_string = 'green-red-yellow-black-white'
print(sort_hyphen(my_string))

"""
17. Write a Python program to make a chain of function decorators
(bold, italic, underline etc.) in Python.
"""

def bold_decorator(func):
    def wrapper(your_string):
        return '<strong>{}<strong>'.format(func(your_string))
    return wrapper

def paragraph_decorator(func):
    def wrapper(your_string):
        return '<p>{}<p>'.format(func(your_string))
    return wrapper

def div_decorator(func):
    def wrapper(your_string):
        return '<div>{}<div>'.format(func(your_string))
    return wrapper

@bold_decorator
@paragraph_decorator
@div_decorator
def s_to_dollarsign(your_string):
    new_string = ''
    for letter in your_string:
        if letter == 's':
            new_string += '$'
        else:
            new_string += letter
    return new_string

print(s_to_dollarsign('Despite their heavy build and awkward gait, \nbears are adept runners, climbers, and swimmers.'))

"""
18. Write a Python program to execute a string containing Python code.
"""

my_string = 'print("this is my string")'
exec(my_string)

def my_function():
    print('this is my function')
my_code_object = my_function.__code__
exec(my_code_object)

"""
19. Write a Python program to access a function inside a function.
"""

def my_function(num):
    print('your number is', num)
    def my_nested_func(s):
        print((s+' ')*num)
    return my_nested_func

my_number = int(input('enter a number from 0 to 10: '))
my_string = input('enter a word: ')
s = my_function(my_number)
s(my_string)

"""
20. Write a Python program to detect the number of local variables
declared in a function. 
"""

def my_function(number):
    a = 4
    b = 'google'
    x = []
    for i in range(number):
        print('{} is awesome and a equals {}'.format(b, a))

my_function(2)
print(my_function.__code__.co_nlocals)
print(my_function.__code__.co_varnames)
