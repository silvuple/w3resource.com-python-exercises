# 1. Write a Python program to find the three largest integers from a given list of numbers using Heap queue algorithm. 
import queue
from heapq import merge
from io import StringIO
import math
from collections import Counter
from pprint import pprint
import heapq
import heapq as hq
nums_list = [25, 35, 22, 85, 14, 65, 75, 22, 58]
print("Original list:")
print(nums_list)
# Find three largest values
largest_nums = hq.nlargest(3, nums_list)
print("\nThree largest numbers are:", largest_nums)

# 2. Write a Python program to find the three smallest integers from a given list of numbers using Heap queue algorithm. 
nums_list = [25, 35, 22, 85, 14, 65, 75, 22, 58]
print("Original list:")
print(nums_list)
# Find three smallest values
largest_nums = hq.nsmallest(3, nums_list)
print("\nThree smallest numbers are:", largest_nums)

# 3. Write a Python program to implement a heapsort by pushing all values onto a heap and then popping off the smallest values one at a time. 
import heapq as hq
def heapsort(iterable):
    h = []
    for value in iterable:
        hq.heappush(h, value)
    return [hq.heappop(h) for i in range(len(h))]
print(heapsort([1, 3, 5, 7, 9, 2, 4, 6, 8, 0]))

# 4. Write a Python function which accepts an arbitrary list and converts it to a heap using Heap queue algorithm. 
import heapq as hq
raw_heap = [25, 44, 68, 21, 39, 23, 89]
print("Raw Heap: ", raw_heap)
hq.heapify(raw_heap)
print("\nHeapify(heap): ", raw_heap)

# 5. Write a Python program to delete the smallest element from the given Heap and then inserts a new item. 
heap = [25, 44, 68, 21, 39, 23, 89]
hq.heapify(heap)
print("heap: ", heap)
hq.heapreplace(heap, 21)
print("heapreplace(heap, 21): ", heap)
hq.heapreplace(heap, 110)
print("heapreplace(heap, 110): ", heap)

# 6. Write a Python program to sort a given list of elements in ascending order using Heap queue algorithm. 
import heapq as hq
nums_list = [18, 14, 10, 9, 8, 7, 9, 3, 2, 4, 1]
print("Original list:")
print(nums_list)
hq.heapify(nums_list)
s_result = [hq.heappop(nums_list) for i in range(len(nums_list))]
print("\nSorted list:")
print(s_result)

# 7. Write a Python program to find the kth(1 <= k <= array's length) largest element in an unsorted array using Heap queue algorithm.
class Solution(object):
    def find_Kth_Largest(self, nums, k):
        """
        :type nums: List[int]
        :type of k: int
        :return value type: int
        """
        h = []
        for e in nums:
            heapq.heappush(h, (-e, e))
        for i in range(k):
            w, e = heapq.heappop(h)
            if i == k - 1:
                return e
arr_nums = [12, 14, 9, 50, 61, 41]
s = Solution()
result = s.find_Kth_Largest(arr_nums, 3)
print("Third largest element:", result)
result = s.find_Kth_Largest(arr_nums, 2)
print("\nSecond largest element:", result)
result = s.find_Kth_Largest(arr_nums, 5)
print("\nFifth largest element:", result)

# 8. Write a Python program to compute maximum product of three numbers of a given array of integers using Heap queue algorithm. 
def maximumProduct(nums):
    import heapq
    a, b = heapq.nlargest(3, nums), heapq.nsmallest(2, nums)
    return max(a[0] * a[1] * a[2], a[0] * b[0] * b[1])
arr_nums = [12, 74, 9, 50, 61, 41]
print("Original array elements:")
print(arr_nums)
print("Maximum product of three numbers of the said array:")
print(maximumProduct(arr_nums))

# 9. Write a Python program to find the top k integers that occur the most frequently from a given lists of sorted and distinct integers using Heap queue algorithm. 
def func(nums, k):
    import collections
    d = collections.defaultdict(int)
    for row in nums:
        for i in row:
            d[i] += 1
    temp = []
    import heapq
    for key, v in d.items():
        if len(temp) < k:
            temp.append((v, key))
            if len(temp) == k:
                heapq.heapify(temp)
        else:
            if v > temp[0][0]:
                heapq.heappop(temp)
                heapq.heappush(temp, (v, key))
    result = []
    while temp:
        v, key = heapq.heappop(temp)
        result.append(key)
    return result
nums = [
      [1, 2, 6],
      [1, 3, 4, 5, 7, 8],
      [1, 3, 5, 6, 8, 9],
      [2, 5, 7, 11],
      [1, 4, 7, 8, 12]
    ]  
k = 3
print("Original lists:")
print(nums)
print("\nTop 3 integers that occur the most frequently in the said lists:")
print(func(nums, k))

# 10. Write a Python program to get the n expensive and cheap price items from a given dataset using Heap queue algorithm.
items = [
    {'name': 'Item-1', 'price': 101.1},
    {'name': 'Item-2', 'price': 555.22},
    {'name': 'Item-3', 'price': 45.09},
    {'name': 'Item-4', 'price': 22.75},
    {'name': 'Item-5', 'price': 16.30},
    {'name': 'Item-6', 'price': 110.65}
]

cheap = heapq.nsmallest(3, items, key=lambda s: s['price'])
expensive = heapq.nlargest(3, items, key=lambda s: s['price'])
print("Original datasets:")
pprint(items)
print("\nFirst 3 expensive items:")
pprint(expensive)
print("\nFirst 3 cheap items:")
pprint(cheap)

# 11. Write a Python program to merge multiple sorted inputs into a single sorted iterator(over the sorted values) using Heap queue algorithm. 
num1 = [25, 24, 15, 4, 5, 29, 110]
num2 = [19, 20, 11, 56, 25, 233, 154]
num3 = [24, 26, 54, 48]
num1 = sorted(num1)
num2 = sorted(num2)
num3 = sorted(num3)
result = heapq.merge(num1, num2, num3)
print(list(result))

# 12. Given a n x n matrix where each of the rows and columns are sorted in ascending order, write a Python program to find the kth smallest element in the matrix. 
class Solution(object):
    def find_Kth_Smallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        m, n = len(matrix), len(matrix[0])
        temp = [[False] * n for _ in range(m)]
        q = [(matrix[0][0], 0, 0)]
        ans = None
        temp[0][0] = True
        for _ in range(k):
            ans, i, j = heapq.heappop(q)
            if i + 1 < m and not temp[i + 1][j]:
                temp[i + 1][j] = True
                heapq.heappush(q, (matrix[i + 1][j], i + 1, j))
            if j + 1 < n and not temp[i][j + 1]:
                temp[i][j + 1] = True
                heapq.heappush(q, (matrix[i][j + 1], i, j + 1))
        return ans
matrix = [
    [0, 5, 9],
    [11, 12, 13],
    [15, 17, 19]
]
k = 1
s = Solution()
result = s.find_Kth_Smallest(matrix, k)
print("First smallest element:", result)
k = 2
s = Solution()
result = s.find_Kth_Smallest(matrix, k)
print("\nSecond smallest element:", result)
k = 3
s = Solution()
result = s.find_Kth_Smallest(matrix, k)
print("\nThird smallest element:", result)

# 13. Write a Python program to find the nth super ugly number from a given prime list of size k using Heap queue algorithm. 
#Ref.: https://bit.ly/32c9P3A
def nth_Super_Ugly_Number(n, primes):
    uglies = [1]

    def gen(prime):
        for ugly in uglies:
            yield ugly * prime

    merged = heapq.merge(*map(gen, primes))
    while len(uglies) < n:
        ugly = next(merged)
        if ugly != uglies[-1]:
            uglies.append(ugly)
    return uglies[-1]
n = 12
primes = [2, 7, 13, 19]
print(nth_Super_Ugly_Number(n, primes))

# 14. Write a Python program to get the k most frequent elements from a given non-empty list of words using Heap queue algorithm.
class Solution:
    def top_K_Frequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :return type: List[str]
        """
        ctr = Counter(words)
        heap = [(-ctr[word], word) for word in ctr]
        heapq.heapify(heap)
        return [heapq.heappop(heap)[1] for _ in range(k)]
if __name__ == '__main__':
    words = ["a", "abc", "abcdef", "a", "abcd", "abcd", "abc", "abcdefg"]
    k = 3
    s = Solution()
    print("3 most frequent elements:")
    print(s.top_K_Frequent(words, k))

# 15. Write a Python program to check if the letters of a given string can be rearranged so that two characters that are adjacent to each other are different using Heap queue algorithm. 
import heapq
from collections import Counter
def reorganizeString(S):
    ctr = Counter(S)
    heap = [(-value, key) for key, value in ctr.items()]
    heapq.heapify(heap)
    if (-heap[0][0]) * 2 > len(S) + 1: 
        return ""
    ans = []
    while len(heap) >= 2:
        nct1, char1 = heapq.heappop(heap)
        nct2, char2 = heapq.heappop(heap)
        ans.extend([char1, char2])
        if nct1 + 1: heapq.heappush(heap, (nct1 + 1, char1))
        if nct2 + 1: heapq.heappush(heap, (nct2 + 1, char2))
    return "".join(ans) + (heap[0][1] if heap else "")

print(reorganizeString("aab"))
print(reorganizeString("abc"))
print(reorganizeString("aabb"))
print(reorganizeString("abccdd"))

# 16. Write a Python program which add integer numbers from the data stream to a heapq and compute the median of all elements. Use Heap queue algorithm. 
import heapq
class Median_Finder:
    
    def __init__(self):
        #initialize data structure
        self.max_heap = []
        self.min_heap = []
        

    def add_Number(self, num):
        #type num: int, rtype: void
        if not self.max_heap and not self.min_heap:
            heapq.heappush(self.min_heap, num)
            return 
        if not self.max_heap:
            if num > self.min_heap[0]:
                heapq.heappush(self.max_heap, -heapq.heappop(self.min_heap))
                heapq.heappush(self.min_heap, num)
            else:
                heapq.heappush(self.max_heap, -num)
            return
        if len(self.max_heap) == len(self.min_heap):
            if num < -self.max_heap[0]:
                heapq.heappush(self.max_heap, -num)
            else:
                heapq.heappush(self.min_heap, num)
        elif len(self.max_heap) > len(self.min_heap):
            if num < -self.max_heap[0]:
                heapq.heappush(self.min_heap, -heapq.heappop(self.max_heap))
                heapq.heappush(self.max_heap, -num)
            else:
                heapq.heappush(self.min_heap, num)
        else:
            if num > self.min_heap[0]:
                heapq.heappush(self.max_heap, -heapq.heappop(self.min_heap))
                heapq.heappush(self.min_heap, num)
            else:
                heapq.heappush(self.max_heap, -num)
        

    def find_Median(self):
        #rtype: float
        if len(self.max_heap) == len(self.min_heap):
            return (-self.max_heap[0] + self.min_heap[0]) / 2
        elif len(self.max_heap) > len(self.min_heap):
            return -self.max_heap[0]
        else:
            return self.min_heap[0] 
S = Median_Finder()
S.add_Number(1)
S.add_Number(2)
result = S.find_Median()
print(result)
S.add_Number(3)
result = S.find_Median()
print(result)
S.add_Number(4)
S.add_Number(5)
result = S.find_Median()
print(result)

# 17. You are given two integer arrays sorted in ascending order and an integer k. Write a Python program to find k number of pairs(u, v) which consists of one element from the first array and one element from the second array using Heap queue algorithm. 


def k_Smallest_Pairs(nums1, nums2, k):
   queue = []

   def push(i, j):
       if i < len(nums1) and j < len(nums2):
           heapq.heappush(queue, [nums1[i] + nums2[j], i, j])
   push(0, 0)
   pairs = []
   while queue and len(pairs) < k:
       _, i, j = heapq.heappop(queue)
       pairs.append([nums1[i], nums2[j]])
       push(i, j + 1)
       if j == 0:
           push(i + 1, 0)
   return pairs


nums1 = [1, 3, 7]
nums2 = [2, 4, 6]
k = 2
result = k_Smallest_Pairs(nums1, nums2, k)
print(result)

# 18. Write a Python program to find the nth ugly number using Heap queue algorithm. 


class Solution(object):
    #:type n: integer
    #:return type: integer
   def nth_Ugly_Number(self, n):
       ugly_num = 0
       heap = []
       heapq.heappush(heap, 1)
       for _ in range(n):
           ugly_num = heapq.heappop(heap)
           if ugly_num % 2 == 0:
               heapq.heappush(heap, ugly_num * 2)
           elif ugly_num % 3 == 0:
               heapq.heappush(heap, ugly_num * 2)
               heapq.heappush(heap, ugly_num * 3)
           else:
               heapq.heappush(heap, ugly_num * 2)
               heapq.heappush(heap, ugly_num * 3)
               heapq.heappush(heap, ugly_num * 5)
               return ugly_num
n = 7
S = Solution()
result = S.nth_Ugly_Number(n)
print("7th Ugly number:")
print(result)
n = 10
result = S.nth_Ugly_Number(n)
print("\n10th Ugly number:")
print(result)

# 19. Write a Python program to print a heap as a tree-like data structure.
#source https://bit.ly/38HXSoU
def show_tree(tree, total_width=60, fill=' '):
    """Pretty-print a tree.
    total_width depends on your input size"""
    output = StringIO()
    last_row = -1
    for i, n in enumerate(tree):
        if i:
            row = int(math.floor(math.log(i+1, 2)))
        else:
            row = 0
        if row != last_row:
            output.write('\n')
        columns = 2**row
        col_width = int(math.floor((total_width * 1.0) / columns))
        output.write(str(n).center(col_width, fill))
        last_row = row
    print(output.getvalue())
    print('-' * total_width)
    return
#test
heap = []
heapq.heappush(heap, 1)
heapq.heappush(heap, 2)
heapq.heappush(heap, 3)
heapq.heappush(heap, 4)
heapq.heappush(heap, 7)
heapq.heappush(heap, 9)
heapq.heappush(heap, 10)
heapq.heappush(heap, 8)
heapq.heappush(heap, 16)
heapq.heappush(heap, 14)
show_tree(heap)

# 20. Write a Python program to combine two given sorted lists using heapq module. 
# Sample Output:
# Original sorted lists:
# [1, 3, 5, 7, 9, 11]
# [0, 2, 4, 6, 8, 10]
# After merging the said two sorted lists:
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
nums1 = [1, 3, 5, 7, 9, 11]
nums2 = [0, 2, 4, 6, 8, 10]
print("Original sorted lists:")
print(nums1)
print(nums2)
print("\nAfter merging the said two sorted lists:")
print(list(merge(nums1, nums2)))

# 21. Write a Python program to push three items into the heap and print the items from the heap. 
# Sample Output:
# ('V', 1)
# ('V', 2)
# ('V', 3)
import heapq
heap = []
heapq.heappush(heap, ('V', 1))
heapq.heappush(heap, ('V', 2))
heapq.heappush(heap, ('V', 3))
for a in heap:
	print(a)

# 22. Write a Python program to push three items into a heap and return the smallest item from the heap. Also Pop and return the smallest item from the heap. 
# Sample Output:
# Items in the heap:
# ('V', 1)
# ('V', 3)
# ('V', 2)
# ----------------------
# The smallest item in the heap:
# ('V', 1)
# ----------------------
# Pop the smallest item in the heap:
# ('V', 2)
# ('V', 3)
heap = []
heapq.heappush(heap, ('V', 3))
heapq.heappush(heap, ('V', 2))
heapq.heappush(heap, ('V', 1))
print("Items in the heap:")
for a in heap:
	print(a)
print("----------------------")
print("The smallest item in the heap:")
print(heap[0])
print("----------------------")
print("Pop the smallest item in the heap:")
heapq.heappop(heap)
for a in heap:
	print(a)

# 23. Write a Python program to push an item on the heap, then pop and return the smallest item from the heap. 
# Sample Output:
# Items in the heap:
# ('V', 1)
# ('V', 3)
# ('V', 2)
# ----------------------
# Using heappushpop push item on the heap and return the smallest item.
# ('V', 2)
# ('V', 3)
# ('V', 6)
heap = []
heapq.heappush(heap, ('V', 3))
heapq.heappush(heap, ('V', 2))
heapq.heappush(heap, ('V', 1))
print("Items in the heap:")
for a in heap:
	print(a)
print("----------------------")
print("Using heappushpop push item on the heap and return the smallest item.")
heapq.heappushpop(heap, ('V', 6))
for a in heap:
	print(a)

# 24. Write a Python program to create a heapsort, pushing all values onto a heap and then popping off the smallest values one at a time. 
# Sample Output:
# [10, 20, 20, 40, 50, 50, 60, 70, 80, 90, 100]
import heapq
def heapsort(h):
    heap = []
    for value in h:
        heapq.heappush(heap, value)
    return [heapq.heappop(heap) for i in range(len(heap))]
print(heapsort([10, 20, 50, 70, 90, 20, 50, 40, 60, 80, 100]))

# 25. Write a Python program to get the two largest and three smallest items from a dataset. 
# Sample Output:
# [100, 90][10, 20, 20]
import heapq
h = [10, 20, 50, 70, 90, 20, 50, 40, 60, 80, 100]
print(heapq.nlargest(2,h))
print(heapq.nsmallest(3,h))

# 26. Write a Python program to create a queue and display all the members and size of the queue. 
# Sample Output:
# Members of the queue:
# 0 1 2 3
# Size of the queue:
# 4
q = queue.Queue()
for x in range(4):
    q.put(x)
print("Members of the queue:")
y = z = q.qsize()

for n in list(q.queue):
    print(n, end=" ")
print("\nSize of the queue:")
print(q.qsize())

# 27. Write a Python program to find whether a queue is empty or not. 
# Sample Output:
# True
# False
p = queue.Queue()
q = queue.Queue()
for x in range(4):
    q.put(x)
print(p.empty())
print(q.empty())

# 28. Write a Python program to create a FIFO queue. 
# Sample Output:
# 0 1 2 3
q = queue.Queue()
#insert items at the end of the queue
for x in range(4):
    q.put(str(x))
#remove items from the head of the queue
while not q.empty():
    print(q.get(), end=" ")
print("\n")

# 29. Write a Python program to create a LIFO queue. 
# Sample Output:
# 3 2 1 0
import queue
q = queue.LifoQueue()
#insert items at the head of the queue 
for x in range(4):
    q.put(str(x))
#remove items from the head of the queue 
while not q.empty():
    print(q.get(), end=" ")
print()
