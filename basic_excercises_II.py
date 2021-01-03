'''
PYTHON BASIC EXCERCISES PART II SOLUTIONS (VIA W3RESOURCE PYTHON)
AUTHORED BY: ATHARVA SHAH
'''

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
