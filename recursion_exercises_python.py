"""
1. Write a Python program to calculate the sum of a list of numbers.
"""

def sum_of_list(my_list):
    if not my_list:
        return 0
    elif len(my_list) == 1:
        return my_list[0]
    else:
        return my_list[0] + sum_of_list(my_list[1:])

print(sum_of_list([1,2,3]))

"""
3. Write a Python program of recursion list sum. 
Test Data: [1, 2, [3,4], [5,6]]
Expected Result: 21
"""

def sum_of_list(my_list):
    if not my_list:
        return 0
    elif isinstance(my_list[0], list):
        return sum_of_list(my_list[0]) + sum_of_list(my_list[1:])
    elif len(my_list) == 1:
        return my_list[0]
    else:
        return my_list[0] + sum_of_list(my_list[1:])
        
print(sum_of_list([1, 2, [3,4], [5,6]]))

"""
4. Write a Python program to get the factorial of a non-negative integer.
"""

def factorial(number):
    if number == 0 or number == 1:
        return 1
    else:
        return number * factorial(number-1)

print(factorial(2))

"""
5. Write a Python program to solve the Fibonacci sequence using recursion.
"""

 solution 1: bad function that will work for a low n but will slow the
 computation drastically as the n increases
def fibonacci(n):
    if n == 1 or n == 2:
        b = 1
    if n > 2:
        b = fibonacci(n-1) + fibonacci(n-2)
    return b

for i in range(1, 21):
    print(fibonacci(i), end = ' ')
print('\n')

# solution 2: with memoization
# explanation to this solution on Socratica youtube channel at https://youtu.be/Qk0zUZW-U_M
fibonacci_cache = {}
def fibonacci(n):
    if n in fibonacci_cache:
        return fibonacci_cache[n]
    if n == 1 or n == 2:
        b = 1
    else:
        b = fibonacci(n-1) + fibonacci(n-2)
    fibonacci_cache[n] = b
    return b

for i in range(1, 21):
    print(fibonacci(i), end = ' ')
print('\n')

# solution 3: with memoize function
# more on this at https://www.python-course.eu/python3_memoization.php
def memoize(func):
    memo_cache = {}
    def helper(n):
        if n not in memo_cache:
            memo_cache[n] = func(n)
        return memo_cache[n]
    return helper

@memoize
def fibonacci(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

for i in range(1, 21):
    print(fibonacci(i), end = ' ')

"""
6. Write a Python program to get the sum of all digits of a non-negative integer. 
Test Data: 
sumDigits(345) -> 12
sumDigits(45) -> 9
"""

def sum_digits(n):
    if n//10 < 1:
        return n
    else:
        return n%10 + sum_digits(n//10)

print(sum_digits(345))

"""
7. Write a Python program to calculate the sum of the positive integers
of n+(n-2)+(n-4)... (until n-x =< 0). Go to the editor
Test Data: 
sum_series(6) -> 12
sum_series(10) -> 30
"""

def sum_series(n):
    if (n-2) <= 0:
        return n
    else:
        return n + sum_series(n-2)

print(sum_series(6))

"""
8. Write a Python program to calculate the harmonic sum of n-1. 
Note: The harmonic sum is the sum of reciprocals of the positive integers. 
"""

def harmonic_sum(n):
    if n == 1:
        return 1
    else:
        return 1/n + harmonic_sum(n-1)

print(harmonic_sum(5))

"""
9. Write a Python program to calculate the geometric sum of n-1.
Note: In mathematics, a geometric series is a series with a constant
ratio between successive terms. 
"""

def geometric_sum(n, a, r):
    # r is a common ratio, a is a start term
    if n == 0:
        return a
    else:
        return a*r**n + geometric_sum(n-1, a, r)
print(geometric_sum(5, 1, 2))

"""
10. Write a Python program to calculate the value of 'a' to the power 'b'. 
Test Data : 
(power(3,4) -> 81
"""

def power(a,b):
    if b == 0:
        return 1
    else:
        return a*power(a, b-1)

print(power(3,4))

"""
11. Write a Python program to find the greatest common divisor (gcd) of two
integers.
"""

# solution 1 (without recursion)
def find_gcd(num1, num2):
    for i in range(min(num1,num2), 0, -1):
        if num1%i==0 and num2%i==0:
            return i
print(find_gcd(12, 500))

# solution 2
# from w3resource at https://www.w3resource.com/python-exercises/data-structures-and-algorithms/python-recursion-exercise-11.php
def gcd(num1, num2):
    low = min(num1, num2)
    high = max(num1, num2)

    if low == 0:
        return high
    elif low == 1:
        return 1
    else:
        return gcd(low, high%low)
print(gcd(12,500))
