"""
1. Write a Python program to create a set.
"""

my_set = set()
my_second_set = {'a', 'b'}
print(my_set, type(my_set))
print(my_second_set, type(my_second_set))

"""
2. Write a Python program to iterate over sets.
"""

my_set = {'a', 'b'}

for i in my_set:
    print(i)

"""
3. Write a Python program to add member(s) in a set.
"""

my_set = {'a', 'b'}
my_set.add('c')
print(my_set)

"""
4. Write a Python program to remove item(s) from set
"""

my_set = {'a', 'b'}
my_set.discard('a')
print(my_set)

my_set = {'a', 'b'}
my_set.remove('a')
print(my_set)

my_set = {'a', 'b'}
my_set.pop()
print(my_set)

"""
5. Write a Python program to remove an item from a set if it is present in the set.
"""

my_set = {'a', 'b'}
my_set.discard('a')
my_set.discard('c')
print(my_set)

"""
6. Write a Python program to create an intersection of sets.
"""
set_one = {'a', 'b', 'c'}
set_two = {'a', 'x', 'f'}

set_inter1 = set_one.intersection(set_two)
set_inter2 = set_one & set_two

print(set_inter1)
print(set_inter2)

"""
7. Write a Python program to create a union of sets.
"""

set_one = {'a', 'b', 'c'}
set_two = {'a', 'x', 'f'}

set_inter1 = set_one.union(set_two)
set_inter2 = set_one | set_two

print(set_inter1)
print(set_inter2)

"""
8. Write a Python program to create set difference.
"""

set_one = {'a', 'b', 'c'}
set_two = {'a', 'x', 'f'}

set_inter1 = set_one.difference(set_two)
set_inter2 = set_one - set_two

print(set_inter1)
print(set_inter2)

"""
9. Write a Python program to create a symmetric difference.
"""

set_one = {'a', 'b', 'c'}
set_two = {'a', 'x', 'f'}

set_inter1 = set_one.symmetric_difference(set_two)
set_inter2 = set_one ^ set_two

print(set_inter1)
print(set_inter2)

"""
10. Write a Python program to issubset and issuperset.
"""

set_one = {'a', 'b', 'c'}
set_two = {'a', 'b'}

print(set_two.issubset(set_one))
print(set_one.issuperset(set_two))

"""
11. Write a Python program to create a shallow copy of sets. 
Note : Shallow copy is a bit-wise copy of an object. A new object is created
that has an exact copy of the values in the original object.
"""

set_one = {'a', 'b', 'c'}
set_two = set_one.copy()
print(set_one)
print(set_two)

"""
12. Write a Python program to clear a set.
"""

set_one = {'a', 'b', 'c'}
set_one.clear()
print(set_one)

"""
13. Write a Python program to use of frozensets.
"""

set_one = frozenset((1, 2, 3))
set_two = set((1, 2, 3))
list_one = [4, 5, 6]
print (set_one == set_two)
print(set_one.isdisjoint(list_one))

"""
14. Write a Python program to find maximum and the minimum value in a set.
"""

set_one = frozenset((1, 2, 3))
print(max(set_one))
print(min(set_one))

"""
15. Write a Python program to find the length of a set.
"""

set_one = frozenset((1, 2, 3))
print(len(set_one))
length = 0
for i in set_one:
    length += 1
print(length)
