"""
1. Write a Python class to convert an integer to a roman numeral.
"""

class RomanNumeral:
    """Roman Numerals class
        Rules:
            I =	1
            V =	5
            X =	10
            L =	50
            C =	100
            D =	500
            M =	1000
        
        1. Repeating a numeral up to three times represents addition of the number.
            For example, III represents 1 + 1 + 1 = 3.
            Only I, X, C, and M can be repeated; V, L, and D cannot be, and there
            is no need to do so.
        
        2. Writing numerals that decrease from left to right represents addition of the numbers.
            For example, LX represents 50 + 10 = 60 and XVI represents 10 + 5 + 1 = 16.
        
        3. Writing a smaller numeral to the left of a larger numeral represents subtraction.
            For example, IV represents 5 - 1 = 4 and IX represents 10 - 1 = 9.
            To avoid ambiguity, the only pairs of numerals that use this subtraction rule are:
            IV	4   = 5 - 1
            IX	9   = 10 - 1
            XL	40  = 50 - 10
            XC	90  = 100 - 10
            CD	400 = 500 - 100
            CM	900 = 1000 - 100
            
        4. To represent larger numbers, a bar over a numeral means to multiply the number by 1000.
            For example, D(bar) represents 1000 x 500 = 500,000 and M(bar) represents 1000 x 1000
            = 1,000,000, one million.***
            
        *** this class only works for integers lower than 4000 (till 3999 including)
    """
    
    def __init__(self, integer):
        self.integer = integer
        self.roman = ''

        roman_numerals = ['I','IV','V','IX','X','XL','L','XC','C','CD', 'D', 'CM', 'M']
        integers =       [1,   4,   5,  9,  10,  40,  50, 90, 100, 400, 500, 900, 1000]

        n = self.integer
        for i,r in sorted(zip(integers, roman_numerals), reverse=True):
            while n//i > 0:
                self.roman += r
                n = n-i

x = int(input("please enter a number from 1 to 3999: "))         
var = RomanNumeral(x)
print("the Roman numeral of your number is:", var.roman)
print("your number in Hindu-Arabic numerals is:", var.integer)
##print(var.__doc__)

"""
2. Write a Python class to convert a roman numeral to an integer.
"""
class HinduArabic:
    """HinduArabic class lets you convert roman numeral to hindu-arabic numeral
        Rules:
            I =	1
            V =	5
            X =	10
            L =	50
            C =	100
            D =	500
            M =	1000
        
        1. Repeating a numeral up to three times represents addition of the number.
            For example, III represents 1 + 1 + 1 = 3.
            Only I, X, C, and M can be repeated; V, L, and D cannot be, and there
            is no need to do so.
        
        2. Writing numerals that decrease from left to right represents addition of the numbers.
            For example, LX represents 50 + 10 = 60 and XVI represents 10 + 5 + 1 = 16.
        
        3. Writing a smaller numeral to the left of a larger numeral represents subtraction.
            For example, IV represents 5 - 1 = 4 and IX represents 10 - 1 = 9.
            To avoid ambiguity, the only pairs of numerals that use this subtraction rule are:
            IV	4   = 5 - 1
            IX	9   = 10 - 1
            XL	40  = 50 - 10
            XC	90  = 100 - 10
            CD	400 = 500 - 100
            CM	900 = 1000 - 100
            
        4. To represent larger numbers, a bar over a numeral means to multiply the number by 1000.
            For example, D(bar) represents 1000 x 500 = 500,000 and M(bar) represents 1000 x 1000
            = 1,000,000, one million.***
            
        *** this class only works for integers lower than 4000 (till 3999 including)
    """
    
    def __init__(self, roman):
        self.integer = int()
        self.roman = roman

        roman_numerals = ['IV','IX','XL','XC','CD','CM','I','V','X','L','C','D','M']
        
        integers       = [  4,   9,  40,  90,  400, 900, 1,  5, 10, 50, 100, 500, 1000]

        n = self.roman
        for i,r in zip(integers, roman_numerals):
            while n.rfind(r) != -1:
                self.integer += i
                n = n.replace(r , '', 1)

x = input("please enter a roman numeral using I, V, X, L, C, D, M letters only: ")        
var = HinduArabic(x)
print("your number in Hindu-Arabic numerals is:", var.integer)
print("the Roman numeral of your number is:", var.roman)
##print(var.__doc__)

"""
3. Write a Python class to find validity of a string of parentheses, '(', ')', '{', '}', '[' and '].
These brackets must be close in the correct order, for example "()" and "()[]{}" and "([]){}"are valid but
"[)", "({[)]" and "{{{" are invalid.
"""

class Parenthesis:
    def __init__(self, par_string):
        self.par_string = par_string
        
# not the most elegant solution, but it works. there is a great solution on w3resource site at 
# https://www.w3resource.com/python-exercises/class-exercises/python-class-exercise-3.php
    def is_valid(self):
        p = self.par_string
        open_par  = ['(', '[', '{']
        close_par = [')', ']', '}']
        wrong_par = ['(]', '(}', '[)', '[}', '{)', '{]']
        
        if len(p)%2 != 0:
            # check if length is not even, the string is invalid, no need to check further
            return False
        elif p[0] in close_par:
            # check if string starts with closing parenthesis, the string is invalid
            return False
        elif p[-1] in open_par:
            # check if string ends with opening parenthesis, the string is invalid
            return False
        else:
            # check if there is a wrong pair of open+close parenthesis from a wrong couples list
            for par in wrong_par:
                if p.find(par) != -1:
                    return False
            # check if all closing parentheses have their opening counterpart before them
            for o, c in zip(open_par, close_par):
                while c in p:
                    i = p.find(c)
                    print(i)
                    j = p.rfind(o, 0, i)
                    print(j)
                    if j == -1:
                        return False
                    else:
                        p = p.replace(o, '', 1)
                        p = p.replace(c, '', 1)
                        print(p)
            if p == '':
                return True
            else:
                return False
                            
print(Parenthesis("{}{{}}{{").is_valid())

"""
4. Write a Python class to get all possible unique subsets from a set of distinct integers.
Input : [4, 5, 6]
Output : [[], [6], [5], [5, 6], [4], [4, 6], [4, 5], [4, 5, 6]]
"""

class Subsets:

    def all_subsets(self, my_set):
        output = [[]]
        for i in range(len(my_set)):
            output.append([my_set[i]])
            k = len(my_set)
            while k>=i:
                for j in range(i+1, k):
                    output.append([my_set[i]]+my_set[j:k])
                k = k - 1
        return sorted(output)


print(Subsets().all_subsets([4, 5, 6]))

        
"""
5. Write a Python class to find a pair of elements (indices of the two numbers) from a
given array whose sum equals a specific target number. 
Input: numbers= [10,20,10,40,50,60,70], target=50
Output: 3, 4
"""

# solution 1 (finds first pair only)
class EqualsTarget:
    def find_pair(self, iterable, target):
        for i in iterable:
            for j in iterable[iterable.index(i)+1:]:
                if i+j == target:
                    return iterable.index(i), iterable.index(j)
        return -1, -1

print(EqualsTarget().find_pair([10,20,10,40,50,60,70], 50))

# solution 2 (finds all pairs)
class EqualsTarget:
    def find_pair(self, iterable, target):
        pairs = []
        for i,n in enumerate(iterable):
            for j,m in enumerate(iterable[i+1:]):
                if n+m == target:
                    pairs.append((i, j+i+1))
        return pairs

print(EqualsTarget().find_pair([-10,10,20,10,40,50,60,70,0,-20], 50))

"""
6. Write a Python class to find the three elements that sum to zero from a set
of n real numbers. 
Input array : [-25, -10, -7, -3, 2, 4, 8, 10]
Output : [[-10, 2, 8], [-7, -3, 10]]
"""

class SumZero:
    def three_sum_zero(self, iterable):
        triples = []
        for i, n in enumerate(iterable):
            for j, m in enumerate(iterable[i+1:]):
                for x, y in enumerate(iterable[i+1+j+1:]):
                    if n+m+y == 0:
                        triples.append([n, m, y])
        return triples


print(SumZero().three_sum_zero([-25, -10, -7, -3, 2, 4, 8, 10]))


"""
7. Write a Python class to implement pow(x, n).
"""

class ImplementPow:
    def imp_pow(self, x, n):
        return x ** n

print(ImplementPow().imp_pow(3, 4))

"""
8. Write a Python class to reverse a string word by word. - Go to the editor
Input string : 'hello .py'
Expected Output : '.py hello'
"""

# solution 1
class ReverseString:
    def reversed(self, astring):
        split_string = astring.split()
        reversed_string = ''
        for word in split_string[::-1]:
            reversed_string += word+' '
        return reversed_string

print(ReverseString().reversed('hello .py nice to meet you'))

# solution 2
class ReverseString:
    def reversed(self, astring):
        split_string = astring.split()
        reversed_string = ' '.join(reversed(split_string))
        return reversed_string

print(ReverseString().reversed('hello .py nice to meet you'))
        
"""
9. Write a Python class which has two methods get_String and print_String.
get_String accepts a string from the user and print_String prints the string in upper case.
"""

class MyString:
    def __init__(self):
        self.string = ''
        
    def get_String(self):
        s = input('input your string: ')
        self.string = s

    def print_String(self):
        print(self.string.upper())

var = MyString()
var.get_String()
var.print_String()
print(var.string)

"""
10. Write a Python class named Rectangle constructed by a length and width and
a method which will compute the area of a rectangle.
"""

class Rectangle:
    def __init__(self, l, w):
        self.length = l
        self.width = w
        
    def area(self):
        a = self.length * self.width
        return a

X = Rectangle(4,5)
print(X.area())

"""
11. Write a Python class named Circle constructed by a radius and two methods which
will compute the area and the perimeter of a circle.
"""
from math import pi

class Circle:
    def __init__(self, r):
        self.radius = r

    def area(self):
        return round(pi * self.radius * self.radius, 2)
    
    def perimeter(self):
        return round(2 * pi * self.radius, 2)

X = Circle(8)
print(X.area())
print(X.perimeter())
print(X.radius)

"""
12. Write a Python program to get the class name of an instance in Python.
"""
"""
instance.__class__
The class to which a class instance belongs.
definition.__name__
The name of the class, function, method, descriptor, or generator instance.
"""
class Circle:
    """ construct a circle """
    def __init__(self, r):
        self.radius = r
    def area(self):
        return round(3.1415 * self.radius * self.radius, 2)
    
    def perimeter(self):
        return round(2 * 3.1415 * self.radius, 2)

X = Circle(8)
print(X.__class__)
print(type(X).__name__)
##print(type(X).__bases__)
##print(type(X).__dict__)
