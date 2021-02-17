# 1. Write a Python program to create an iterator from several iterables in a sequence and display the type and elements of the new iterator. 
from itertools import takewhile
from itertools import combinations
from operator import itemgetter
from itertools import groupby
from more_itertools import windowed
from itertools import permutations
from itertools import product
from itertools import combinations_with_replacement
import itertools
import itertools as it
import operator
from itertools import accumulate
from itertools import chain
def chain_func(l1,l2,l3):
    return chain(l1,l2,l3)    
#List
result = chain_func([1,2,3], ['a','b','c','d'], [4,5,6,7,8,9])
print("Type of the new iterator:")
print(type(result))
print("Elements of the new iterator:")
for i in result:
    print(i)

#Tuple
result = chain_func((10,20,30,40), ('A','B','C','D'), (40,50,60,70,80,90))
print("Type of the new iterator:")
print(type(result))
print("Elements of the new iterator:")
for i in result:
    print(i)

# 2. Write a Python program to generate the running product of the elements of an given iterable.
def running_product(it):
    return accumulate(it, operator.mul)
#List
result = running_product([1, 2, 3, 4, 5, 6, 7])
print("Running product of a list:")
for i in result:
    print(i)
#Tuple
result = running_product((1, 2, 3, 4, 5, 6, 7))
print("Running product of a Tuple:")
for i in result:
    print(i)

# 3. Write a Python program to generate the running maximum, minimum value of the elements of an iterable. 
def running_max_product(iters):
    return accumulate(iters, max)

#List
result = running_max_product([1, 3, 2, 7, 9, 8, 10, 11, 12, 14, 11, 12, 7])
print("Running maximum value of a list:")
for i in result:
    print(i)
#Tuple
result = running_max_product((1, 3, 3, 7, 9, 8, 10, 9, 8, 14, 11, 15, 7))
print("Running maximum value of a Tuple:")
for i in result:
    print(i)


def running_min_product(iters):
    return accumulate(iters, min)

#List
result = running_min_product([3, 2, 7, 9, 8, 10, 11, 12, 1, 14, 11, 12, 7])
print("Running minimum value of a list:")
for i in result:
    print(i)
#Tuple
result = running_min_product((1, 3, 3, 7, 9, 8, 10, 9, 8, 0, 11, 15, 7))
print("Running minimum value of a Tuple:")
for i in result:
    print(i)

# 4. Write a Python program to construct an infinite iterator that returns evenly spaced values starting with a specified number and step.
start = 10
step = 1
print("The starting number is ", start, "and step is ", step)
my_counter = it.count(start, step)
# Following  loop will run for ever
print("The said function print never-ending items:")
for i in my_counter:
    print(i)

# 5. Write a Python program to generate an infinite cycle of elements from an iterable. 
import itertools as it
def cycle_data(iter):
    return it.cycle(iter)
# Following  loops will run for ever    
#List
result = cycle_data(['A','B','C','D'])
print("The said function print never-ending items:")
for i in result:
    print(i)

#String
result = cycle_data('Python itertools')
print("The said function print never-ending items:")
for i in result:
    print(i)

# 6. Write a Python program to make an iterator that drops elements from the iterable as soon as an element is a positive number. 
def drop_while(nums):
    return it.dropwhile(lambda x: x < 0, nums)

nums = [-1, -2, -3, 4, -10, 2, 0, 5, 12]
print("Original list: ", nums)
result = drop_while(nums)
print("Drops elements from the iterable when a positive number arises \n", list(result))
#Alternate solution
def negative_num(x):
    return x < 0

def drop_while(nums):
    return it.dropwhile(negative_num, nums)

nums = [-1, -2, -3, 4, -10, 2, 0, 5, 12]
print("Original list: ", nums)
result = drop_while(nums)
print("Drops elements from the iterable when a positive number arises \n", list(result))

# 7. Write a Python program to make an iterator that drops elements from the iterable as long as the elements are negative
# afterwards, returns every element. 
def drop_while(nums):
    return it.takewhile(lambda x: x < 0, nums)

nums = [-1, -2, -3, 4, -10, 2, 0, 5, 12]
print("Original list: ", nums)
result = drop_while(nums)
print("Drop elements from the said list as long as the elements are negative\n", list(result))
#Alternate solution
def negative_num(x):
    return x < 0

def drop_while(nums):
    return it.dropwhile(negative_num, nums)

nums = [-1, -2, -3, 4, -10, 2, 0, 5, 12]
print("Original list: ", nums)
result = drop_while(nums)
print("Drop elements from the said list as long as the elements are negative\n", list(result))

# 8. Write a Python program to create an iterator that returns consecutive keys and groups from an iterable. 
import itertools as it
print("Iterate over characters of a string and display\nconsecutive keys and groups from the iterable:")
str1 = 'AAAAJJJJHHHHNWWWEERRRSSSOOIIU'
data_groupby = it.groupby(str1)
for key, group in data_groupby:
    print('Key:', key)
    print('Group:', list(group))    
print("\nIterate over elements of a list and display\nconsecutive keys and groups from the iterable:")
str1 = 'AAAAJJJJHHHHNWWWEERRRSSSOOIIU'    
str1 = [1,2,2,3,4,4,5,5,5,6,6,7,7,7,8]
data_groupby = it.groupby(str1)
for key, group in data_groupby:
    print('Key:', key)
    print('Group:', list(group))

# 9. Write a Python program to split an iterable and generate iterables specified number of times. 
def tee_data(iter, n):
    return it.tee(iter, n)
#List
result = tee_data(['A', 'B', 'C', 'D'], 5)
print("Generate iterables specified number of times:")
for i in result:
    print(list(i))

#String
result = tee_data("Python itertools", 4)
print("\nGenerate iterables specified number of times:")
for i in result:
    print(list(i))

# 10. Write a Python program to create an iterator to get specified number of permutations of elements. 
def permutations_data(iter, length):
    return it.permutations(iter, length)
#List
result = permutations_data(['A', 'B', 'C', 'D'], 3)
print("\nIterator to get specified number of permutations of elements:")
for i in result:
    print(i)

#String
result = permutations_data("Python", 2)
print("\nIterator to get specified number of permutations of elements:")
for i in result:
    print(i)

# 11. Write a Python program to generate combinations of a given length of given iterable. 
def combinations_data(iter, length):
    return it.combinations(iter, length)

#List
result = combinations_data(['A', 'B', 'C', 'D'], 1)
print("\nCombinations of an given iterable of length 1:")
for i in result:
    print(i)

#String
result = combinations_data("Python", 1)
print("\nCombinations of an given iterable of length 1:")
for i in result:
    print(i)

#List
result = combinations_data(['A', 'B', 'C', 'D'], 2)
print("\nCombinations of an given iterable of length 2:")
for i in result:
    print(i)

#String
result = combinations_data("Python", 2)
print("\nCombinations of an given iterable of length 2:")
for i in result:
    print(i)

# 12. Write a Python program to create Cartesian product of two or more given lists using itertools.
def cartesian_product(lists):
    return list(itertools.product(*lists))

ls = [[1, 2], [3, 4]]
print("Original Lists:", ls)
print("Cartesian product of the said lists: ", cartesian_product(ls))
ls = [[1, 2, 3], [3, 4, 5]]
print("\nOriginal Lists:", ls)
print("Cartesian product of the said lists: ", cartesian_product(ls))
ls = [[], [1, 2, 3]]
print("\nOriginal Lists:", ls)
print("Cartesian product of the said lists: ", cartesian_product(ls))
ls = [[1, 2], []]
print("\nOriginal Lists:", ls)
print("Cartesian product of the said lists: ", cartesian_product(ls))


# 13. Write a Python program to chose specified number of colours from three different colours and generate all the combinations with repetitions.
def combinations_colors(l, n):
    return combinations_with_replacement(l, n)


l = ["Red", "Green", "Blue"]
print("Original List: ", l)
n = 1
print("\nn = 1")
print(list(combinations_colors(l, n)))
n = 2
print("\nn = 2")
print(list(combinations_colors(l, n)))
n = 3
print("\nn = 3")
print(list(combinations_colors(l, n)))

# 14. Write a Python program generate permutations of specified elements, drawn from specified values.
def permutations_colors(inp, n):
    for x in product(inp, repeat=n):
        c = ''.join(x)
        print(c, end=', ')

str1 = "Red"
print("Original String: ", str1)
print("Permutations of specified elements, drawn from specified values:")
n = 1
print("\nn = 1")
permutations_colors(str1, n)
n = 2
print("\nn = 2")
permutations_colors(str1, n)
n = 3
print("\nn = 3")
permutations_colors(str1, n)

lst1 = ["Red", "Green", "Black"]
print("\n\nOriginal list: ", lst1)
print("Permutations of specified elements, drawn from specified values:")
n = 1
print("\nn = 1")
permutations_colors(lst1, n)
n = 2
print("\nn = 2")
permutations_colors(lst1, n)
n = 3
print("\nn = 3")
permutations_colors(lst1, n)

# 15. Write a Python program to generate all possible permutations of n different objects. 
import itertools
def permutations_all(l):
    for values in itertools.permutations(l):
        print(values)
permutations_all([1])
print("\n")
permutations_all([1,2])
print("\n")
permutations_all([1,2,3])

# 16. Write a Python program find the sorted sequence from a set of permutations of a given input.
def is_seq_sorted(lst):
  print(lst)
  return all(
      x <= y
      for x, y in windowed(lst, 2)
  )

def permutation_sort(lst):
  return next(
      permutation_seq
      for permutation_seq in permutations(lst)
      if is_seq_sorted(permutation_seq)
  )

print("All the sequences:")
print("\nSorted sequence: ", permutation_sort([12, 10, 9]))

print("\n\nAll the sequences:")
print("\nSorted sequence: ", permutation_sort([2, 3, 1, 0]))


# 17. Write a Python program to read a given string character by character and compress repeated character by storing the length of those character(s).
def encode_str(input_str):
    return [(len(list(n)), m) for m, n in groupby(input_str)]

str1 = "AAASSSSKKIOOOORRRREEETTTTAAAABBBBBBDDDDD"
print("Original string:")
print(str1)
print("Result:")
print(encode_str(str1))

str1 = "jjjjiiiiooooosssnssiiiiwwwweeeaaaabbbddddkkkklll"
print("\nOriginal string:")
print(str1)
print("Result:")
print(encode_str(str1))

# 18. Write a Python program to generate permutations of n items in which successive permutations differ from each other by the swapping of any two items.
DEBUG = False  # like the built-in __debug__
def spermutations(n):
    """permutations by swapping. Yields: perm, sign"""
    sign = 1
    p = [[i, 0 if i == 0 else -1]  # [num, direction]
         for i in range(n)]

    if DEBUG:
        print(' #', p)
    yield tuple(pp[0] for pp in p), sign

    while any(pp[1] for pp in p):  # moving
        i1, (n1, d1) = max(((i, pp) for i, pp in enumerate(p) if pp[1]),
                           key=itemgetter(1))
        sign *= -1
        if d1 == -1:
            # Swap down
            i2 = i1 - 1
            p[i1], p[i2] = p[i2], p[i1]
            # If this causes the chosen element to reach the First or last
            # position within the permutation, or if the next element in the
            # same direction is larger than the chosen element:
            if i2 == 0 or p[i2 - 1][0] > n1:
                # The direction of the chosen element is set to zero
                p[i2][1] = 0
        elif d1 == 1:
            # Swap up
            i2 = i1 + 1
            p[i1], p[i2] = p[i2], p[i1]
            # If this causes the chosen element to reach the first or Last
            # position within the permutation, or if the next element in the
            # same direction is larger than the chosen element:
            if i2 == n - 1 or p[i2 + 1][0] > n1:
                # The direction of the chosen element is set to zero
                p[i2][1] = 0
        if DEBUG:
            print(' #', p)
        yield tuple(pp[0] for pp in p), sign

        for i3, pp in enumerate(p):
            n3, d3 = pp
            if n3 > n1:
                pp[1] = 1 if i3 < i2 else -1
                if DEBUG:
                    print(' # Set Moving')


if __name__ == '__main__':
    from itertools import permutations

    for n in (3, 4):
        print('\nPermutations and sign of %i items' % n)
        sp = set()
        for i in spermutations(n):
            sp.add(i[0])
            print('Permutation: %r Sign: %2i' % i)
            #if DEBUG: raw_input('?')
        # Test
        p = set(permutations(range(n)))
        assert sp == p, 'Two methods of generating permutations do not agree'


# 19. Write a Python program which iterates the integers from 1 to a given number and print "Fizz" for multiples of three, print "Buzz" for multiples of five, print "FizzBuzz" for multiples of both three and five using itertools module. 
#Source:https://bit.ly/30PS62m
import itertools as it
def fizz_buzz(n):
    fizzes = it.cycle([""] * 2 + ["Fizz"])
    buzzes = it.cycle([""] * 4 + ["Buzz"])
    fizzes_buzzes = (fizz + buzz for fizz, buzz in zip(fizzes, buzzes))
    result = (word or n for word, n in zip(fizzes_buzzes, it.count(1)))
    for i in it.islice(result, 100):
        print(i)
n = 50
fizz_buzz(n)

# 20. Write a Python program to find the factorial of a number using itertools module. 
import itertools as it
import operator as op

def factorials_nums(n):
    result = list(it.accumulate(it.chain([1], range(1, 1 + n)), op.mul))
    return result
    
print("Factorials of 5 :", factorials_nums(5))
print("Factorials of 9 :", factorials_nums(9))

# 21. Write a Python program to find the years where 25th of December be a Sunday between 2000 and 2150. 
'''Days of the week'''
# Source:https://bit.ly/30NoXF8
from datetime import date
from itertools import islice
 
# xmasIsSunday :: Int -> Bool
def xmasIsSunday(y):
    '''True if Dec 25 in the given year is a Sunday.'''
    return 6 == date(y, 12, 25).weekday()
 
# main :: IO ()
def main():
    '''Years between 2000 and 2150 with 25 December on a Sunday''' 
    xs = list(filter(
        xmasIsSunday,
        enumFromTo(2000)(2150)
    ))
    total = len(xs)
    print(
        fTable(main.__doc__ + ':\n\n' + '(Total ' + str(total) + ')\n')(
            lambda i: str(1 + i)
        )(str)(index(xs))(
            enumFromTo(0)(total - 1)
        )
    )
# GENERIC -------------------------------------------------
 
# enumFromTo :: (Int, Int) -> [Int]
def enumFromTo(m):
    '''Integer enumeration from m to n.'''
    return lambda n: list(range(m, 1 + n))
# index (!!) :: [a] -> Int -> a
def index(xs):
    '''Item at given (zero-based) index.'''
    return lambda n: None if 0 > n else (
        xs[n] if (
            hasattr(xs, "__getitem__")
        ) else next(islice(xs, n, None))
    )
 
 # unlines :: [String] -> String
def unlines(xs):
    '''A single string formed by the intercalation
       of a list of strings with the newline character.
    '''
    return '\n'.join(xs)
 
#  FORMATTING ---------------------------------------------
# fTable :: String -> (a -> String) ->
#                     (b -> String) -> (a -> b) -> [a] -> String
def fTable(s):
    '''Heading -> x display function -> fx display function ->
                     f -> xs -> tabular string.
    '''
    def go(xShow, fxShow, f, xs):
        ys = [xShow(x) for x in xs]
        w = max(map(len, ys))
        return s + '\n' + '\n'.join(map(
            lambda x, y: y.rjust(w, ' ') + ' -> ' + fxShow(f(x)),
            xs, ys
        ))
    return lambda xShow: lambda fxShow: lambda f: lambda xs: go(
        xShow, fxShow, f, xs
    ) 
 # MAIN --
if __name__ == '__main__':
    main()

# 22. Write a Python program to create a 24-hour time format(HH: MM) using 4 given digits. Display the latest time and do not use any digit more than once. 
import itertools
def max_time(nums):
    for i in range(len(nums)):
        nums[i] *= -1
    nums.sort()
    for hr1, hr2, m1, m2 in itertools.permutations(nums):
        hrs = -(10*hr1 + hr2)
        mins = -(10*m1 + m2)
        if 60> mins >=0 and 24 > hrs >=0:
            result = "{:02}:{:02}".format(hrs, mins)
            break
    return result

nums = [1,2,3,4]
print("Original array:",nums)
print("Latest time: ",max_time(nums))

nums = [1,2,4,5]
print("\nOriginal array:",nums)
print("Latest time: ",max_time(nums))

nums = [2,2,4,5]
print("\nOriginal array:",nums)
print("Latest time: ",max_time(nums))

nums = [2,2,4,3]
print("\nOriginal array:",nums)
print("Latest time: ",max_time(nums))

nums = [0,2,4,3]
print("\nOriginal array:",nums)
print("Latest time: ",max_time(nums))

# 23. Write a Python program to find the shortest distance from a specified character in a given string. Return the shortest distances through a list and use itertools module to solve the problem. 
def char_shortest_distancer(str1, char1):
    result = [len(str1)] * len(str1)
    prev_char = -len(str1)
    for i in it.chain(range(len(str1)), reversed(range(len(str1)))):
        if str1[i] == char1:
            prev_char = i
        result[i] = min(result[i], abs(i-prev_char))
    return result


str1 = "w3resource"
chr1 = 'r'
print("Original string:", str1, ": Specified character:", chr1)
print(char_shortest_distancer(str1, chr1))

str1 = "python exercises"
chr1 = 'e'
print("\nOriginal string:", str1, ": Specified character:", chr1)
print(char_shortest_distancer(str1, chr1))

str1 = "JavaScript"
chr1 = 'S'
print("\nOriginal string:", str1, ": Specified character:", chr1)
print(char_shortest_distancer(str1, chr1))


# 24. Write a Python program to find the maximum length of a substring in a given string where all the characters of the substring are same. Use itertools module to solve the problem. 
def max_sub_string(str1):
    return max(len(list(x)) for _, x in itertools.groupby(str1))
str1 = "aaabbccddeeeee"

print("Original string:", str1)
print("Maximum length of a substring with unique characters of the said string:")
print(max_sub_string(str1))

str1 = "c++ exercises"
print("\nOriginal string:", str1)
print("Maximum length of a substring with unique characters of the said string:")
print(max_sub_string(str1))


# 25. Write a Python program to find the first two elements of a given list whose sum is equal to a given value. Use itertools module to solve the problem. 
import itertools as it
def sum_pairs_list(nums, n):
    for num2, num1 in list(it.combinations(nums[::-1], 2))[::-1]:
        if num2 + num1 == n:
            return [num1, num2]

nums = [1,2,3,4,5,6,7]     
n = 10
print("Original list:",nums,": Given value:",n)   
print("Sum of pair equal to ",n,"=",sum_pairs_list(nums,n))

nums = [1,2,-3,-4,-5,6,-7]     
n = -6
print("Original list:",nums,": Given value:",n)   
print("Sum of pair equal to ",n,"=",sum_pairs_list(nums,n))

# 26. Write a Python program to find the nth Hamming number. User itertools module. 
import itertools
from heapq import merge
def nth_hamming_number(n):
    def num_recur():
        last = 1
        yield last
        x, y, z = itertools.tee(num_recur(), 3)
        for n in merge((2 * i for i in x), (3 * i for i in y), (5 * i for i in z)):
            if n != last:
                yield n
                last = n
    result =  itertools.islice(num_recur(), n)
    return list(result)[-1]

print(nth_hamming_number(8))
print(nth_hamming_number(14))
print(nth_hamming_number(17))

# 27. Write a Python program to chose specified number of colours from three different colours and generate the unique combinations.
def unique_combinations_colors(list_data, n):
    return [" and ".join(items) for items in combinations(list_data, r=n)]

colors = ["Red", "Green", "Blue"]
print("Original List: ", colors)
n = 1
print("\nn = 1")
print(list(unique_combinations_colors(colors, n)))
n = 2
print("\nn = 2")
print(list(unique_combinations_colors(colors, n)))
n = 3
print("\nn = 3")
print(list(unique_combinations_colors(colors, n)))


# 28. Write a Python program to find the maximum, minimum aggregation pair in given list of integers. 
def max_aggregate(l_data):
    max_pair = max(combinations(l_data, 2), key=lambda pair: pair[0] + pair[1])
    min_pair = min(combinations(l_data, 2), key=lambda pair: pair[0] + pair[1])
    return max_pair, min_pair

nums = [1, 3, 4, 5, 4, 7, 9, 11, 10, 9]
print("Original list:")
print(nums)
result = max_aggregate(nums)
print("\nMaximum aggregation pair of the said list of tuple pair:")
print(result[0])
print("\nMinimum aggregation pair of the said list of tuple pair:")
print(result[1])

# 29. Write a Python program to interleave multiple lists of the same length. Use itertools module. 
def interleave_multiple_lists(list1, list2, list3):
    result = list(itertools.chain(*zip(list1, list2, list3)))
    return result

list1 = [100, 200, 300, 400, 500, 600, 700]
list2 = [10, 20, 30, 40, 50, 60, 70]
list3 = [1, 2, 3, 4, 5, 6, 7]
print("Original list:")
print("list1:", list1)
print("list2:", list2)
print("list3:", list3)
print("\nInterleave multiple lists:")
print(interleave_multiple_lists(list1, list2, list3))


# 30. Write a Python program to create non-repeated combinations of Cartesian product of four given list of numbers. 
mums1 = [1, 2, 3, 4]
mums2 = [5, 6, 7, 8]
mums3 = [9, 10, 11, 12]
mums4 = [13, 14, 15, 16]
print("Original lists:")
print(mums1)
print(mums2)
print(mums3)
print(mums4)
print("\nSum of the specified range:")
for i in it.product([tuple(mums1)], it.permutations(mums2), it.permutations(mums3), it.permutations(mums4)):
    print(i)

# 31. Write a Python program to count the frequency of consecutive duplicate elements in a given list of numbers. Use itertools module. 
from itertools import groupby
def count_same_pair(nums):
    result = [sum(1 for _ in group) for _, group in groupby(nums)]
    return result

nums = [1,1,2,2,2,4,4,4,5,5,5,5]
print("Original lists:")
print(nums)
print("\nFrequency of the consecutive duplicate elements:")
print(count_same_pair(nums))

# 32. Write a Python program to count the frequency of the elements of a given unordered list. 
from itertools import groupby
uno_list = [2,1,3,8,5,1,4,2,3,4,0,8,2,0,8,4,2,3,4,2]
print("Original list:")
print(uno_list)
uno_list.sort()
print(uno_list)
print("\nSort the said unordered list:")
print(uno_list)
print("\nFrequency of the elements of the said unordered list:")
result = [len(list(group)) for key, group in groupby(uno_list)]
print(result)

# 33. Write a Python program to find the pairs of maximum and minimum product from a given list. Use itertools module. 
import itertools as it
def list_max_min_pair(nums):
    result_max = max(it.combinations(nums, 2), key = lambda sub: sub[0] * sub[1])
    result_min = min(it.combinations(nums, 2), key = lambda sub: sub[0] * sub[1])
    return result_max, result_min

nums = [2,5,8,7,4,3,1,9,10,1]   
print("The original list: ") 
print(nums)
print("\nPairs of maximum and minimum product from the said list:")
print(list_max_min_pair(nums))

# 34. Write a Python program to compute the sum of digits of each number of a given list of positive integers. 
from itertools import chain
def sum_of_digits(nums):
    return sum(int(y) for y in (chain(*[str(x) for x in nums])))

nums = [10,2,56]
print("Original tuple: ") 
print(nums)
print("Sum of digits of each number of the said list of integers:")
print(sum_of_digits(nums))

nums = [10,20,4,5,70]
print("\nOriginal tuple: ") 
print(nums)
print("Sum of digits of each number of the said list of integers:")
print(sum_of_digits(nums))

# 35. Write a Python program to get all possible combinations of the elements of a given list using itertools module. 
def combinations_list(list1):
    temp = []
    for i in range(0, len(list1)+1):
        temp.append(list(itertools.combinations(list1, i)))
    return temp

colors = ['orange', 'red', 'green', 'blue']
print("Original list:")
print(colors)
print("\nAll possible combinations of the said list’s elements:")
print(combinations_list(colors))

# 36. Write a Python program to add two given lists of different lengths, start from right, using itertools module. 
from itertools import zip_longest
def elementswise_right_join(l1, l2):
    result = [a + b for a,b in zip_longest(reversed(l1), reversed(l2), fillvalue=0)][::-1]
    return result

nums1 = [2, 4, 7, 0, 5, 8]
nums2 = [3, 3, -1, 7]
print("\nOriginal lists:")
print(nums1)
print(nums2)
print("\nAdd said two lists from right:")
print(elementswise_right_join(nums1, nums2))

nums3 = [1, 2, 3, 4, 5, 6]
nums4 = [2, 4, -3]
print("\nOriginal lists:")
print(nums3)
print(nums4)
print("\nAdd said two lists from right:")
print(elementswise_right_join(nums3, nums4))

# 37. Write a Python program to add two given lists of different lengths, start from left, using itertools module. 


def elementswise_left_join(l1, l2):
    result = [a + b for a, b in zip_longest(l1, l2, fillvalue=0)][::1]
    return result

nums1 = [2, 4, 7, 0, 5, 8]
nums2 = [3, 3, -1, 7]
print("\nOriginal lists:")
print(nums1)
print(nums2)
print("\nAdd said two lists from left:")
print(elementswise_left_join(nums1, nums2))

nums3 = [1, 2, 3, 4, 5, 6]
nums4 = [2, 4, -3]
print("\nOriginal lists:")
print(nums3)
print(nums4)
print("\nAdd said two lists from left:")
print(elementswise_left_join(nums3, nums4))


# 38. Write a Python program to interleave multiple given lists of different lengths using itertools module. 
from itertools import chain, zip_longest
def interleave_diff_len_lists(list1, list2, list3, list4):
    return [x for x in chain(*zip_longest(list1, list2, list3, list4)) if x is not None]    
    
nums1 = [2, 4, 7, 0, 5, 8]
nums2 = [2, 5, 8]
nums3 = [0, 1]
nums4 = [3, 3, -1, 7]

print("\nOriginal lists:")
print(nums1)
print(nums2)
print(nums3)
print(nums4)
print("\nInterleave said lists of different lengths:")
print(interleave_diff_len_lists(nums1, nums2, nums3, nums4))

# 39. Write a Python program to get the index of the first element, which is greater than a specified element using itertools module.


def first_index(l1, n):
    return len(list(takewhile(lambda x: x[1] <= n, enumerate(l1))))


nums = [12, 45, 23, 67, 78, 90, 100, 76, 38, 62, 73, 29, 83]
print("Original list:")
print(nums)
n = 73
print("\nIndex of the first element which is greater than", n, "in the said list:")
print(first_index(nums, n))
n = 21
print("\nIndex of the first element which is greater than", n, "in the said list:")
print(first_index(nums, n))
n = 80
print("\nIndex of the first element which is greater than", n, "in the said list:")
print(first_index(nums, n))
n = 55
print("\nIndex of the first element which is greater than", n, "in the said list:")
print(first_index(nums, n))

# 40. Write a Python program to split a given list into specified sized chunks using itertools module. 


def split_list(lst, n):
    lst = iter(lst)
    result = iter(lambda: tuple(islice(lst, n)), ())
    return list(result)


nums = [12, 45, 23, 67, 78, 90, 45, 32, 100, 76, 38, 62, 73, 29, 83]
print("Original list:")
print(nums)
n = 3
print("\nSplit the said list into equal size", n)
print(split_list(nums, n))
n = 4
print("\nSplit the said list into equal size", n)
print(split_list(nums, n))
n = 5
print("\nSplit the said list into equal size", n)
print(split_list(nums, n))

# 41. Write a Python program to find all lower and upper mixed case combinations of a given string. 
import itertools
def combination(str1):
    result = map(''.join, itertools.product(*((c.lower(), c.upper()) for c in str1)))
    return list(result)
st ="abc"
print("Original string:")
print(st)
print("All lower and upper mixed case combinations of the said string:")
print(combination(st))
st ="w3r"
print("\nOriginal string:")
print(st)
print("All lower and upper mixed case combinations of the said string:")
print(combination(st))
st ="Python"
print("\nOriginal string:")
print(st)
print("All lower and upper mixed case combinations of the said string:")
print(combination(st))

# 42. Write a Python program to create group of similar items of a given list. 


def group_similar_items(seq):
    result = [list(el) for _, el in it.groupby(seq, lambda x: x.split('_')[0])]
    return result


colors = ['red_1', 'red_2', 'green_1',
          'green_2', 'green_3', 'orange_1', 'orange_2']
print("Original list:")
print(colors)
print("\nGroup similar items of the said list:")
print(group_similar_items(colors))

colors = ['red_1', 'green-1', 'green_2', 'green_3', 'orange-1', 'orange_2']
print("\nOriginal list:")
print(colors)
print("\nGroup similar items of the said list:")
print(group_similar_items(colors))
