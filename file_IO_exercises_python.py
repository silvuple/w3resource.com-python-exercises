"""
1. Write a Python program to read an entire text file.
"""
# It is good practice to use the with keyword when dealing with file objects.
# The advantage is that the file is properly closed after its suite finishes,
# even if an exception is raised at some point. 
with open('exercises.txt') as f:
    read_data = f.read()
    print(read_data)
print(f.closed)

# If you’re not using the with keyword, then you should call f.close() to close
# the file and immediately free up any system resources used by it.
f = open('exercises.txt')
read_data = f.read()
print(read_data)
print(f.closed)
f.close()
print(f.closed)

"""
2. Write a Python program to read first n lines of a file.
"""

# solution 1
n = 5
f = open('exercises.txt')
for i in range(n):
    print(f.readline())
f.close()

# solution 2
n = 5
with open('exercises.txt') as f:
    lines = list(f)
    for line in lines[:n]:
        print(line)

# solution 3
n = 5
with open('exercises.txt') as f:
    lines = f.readlines()
    for line in lines[:n]:
        print(line)
    
# solution 4
from itertools import islice
n = 5
with open('exercises.txt') as f:
    for line in islice(f, n):
        print(line)
        
"""
3. Write a Python program to append text to a file and display the text.
"""

f = open('exercises.txt', 'a')
f.write('\nappending a line at the end of the file')
f.close()
f = open('exercises.txt', 'r')
print(f.read())
f.close()

"""
4. Write a Python program to read last n lines of a file.
"""

n = 6
f = open('exercises.txt')
lines = list(f)
for line in lines[-n:]:
    print(line)
f.close()

"""
5. Write a Python program to read a file line by line and store it into a list.
"""

with open('exercises.txt') as f:
    lines = list(f)
    print(lines)

"""
6. Write a Python program to read a file line by line store it into a variable.
"""

with open('exercises.txt') as f:
    for line in f:
        my_string = line
        print(my_string)

"""
8. Write a python program to find the longest words.
"""

# solution 1 (finds 1 longest word)
with open('exercises.txt') as f:
    lines = list(f)
    longest = ''
    for line in lines:
        for word in line.split():
            if len(longest) < len(word):
                longest = word
    print(longest)
    
# solution 2 (finds 1 longest word)
with open('exercises.txt') as f:
    words = f.read().split()
    longest = max(words, key=len)
    print(longest)
    
# solution 3 (finds all words with greatest length)
with open('exercises.txt') as f:
    words = f.read().split()
    max_length = len(max(words, key=len))
    all_longest = []
    for word in words:
        if len(word) == max_length:
            all_longest.append(word)
    print(set(all_longest))

"""
9. Write a Python program to count the number of lines in a text file.
"""

# solution 1
with open('exercises.txt') as f:
    print(len(list(f)))

# solution 2
with open('exercises.txt') as f:
    counter = 0
    for line in f:
        counter += 1
    print(counter)

"""
10. Write a Python program to count the frequency of words in a file.
"""

# solution 1
import string

with open('exercises.txt') as f:
    # remove punctuation marks from the text 
    intab = string.punctuation
    outtab = " "*len(string.punctuation)
    trans_table = str.maketrans(intab, outtab)
    text = f.read().translate(trans_table)

    # create list of words (all words lowercased)
    words = text.lower().split()

    # create dictionary and populate it with count for each word
    words_freq = {}
    for word in words:
        if word in words_freq:
            words_freq[word] += 1
        else:
           words_freq[word] = 1
           
print(words_freq)

# solution 2
from collections import Counter
import string

with open('exercises.txt') as f:
    # remove punctuation marks from the text
    intab = string.punctuation
    outtab = " "*len(string.punctuation)
    trans_table = str.maketrans(intab, outtab)
    text = f.read().translate(trans_table)

    # split text to list of words (all lowercased)
    words = text.lower().split()

    # create a Counter object
    words_freq = Counter(words)

print(words_freq)
        
"""
11. Write a Python program to get the file size of a plain file.
"""
from os import stat

# os.stat() - Get the status of a file or a file descriptor.
# st_size - Size of the file in bytes
statinfo = stat('exercises.txt')
print(statinfo.st_size)

"""
12. Write a Python program to write a list to a file.
"""
my_list = [1, 2, 3, 4]
with open('list-to-file.txt', 'w+') as f:
    f.write(' '.join(map(str, my_list)))

"""
13. Write a Python program to copy the contents of a file to another file.
"""

# solution 1 (copy without deleting existing data)
f = open('list-to-file.txt')
f1 = open('exercises.txt', 'a')
f1.write(f.read())
f.close()
f1.close()

# solution 2 (copy with deleting all previous data in target file)
import shutil
shutil.copyfile('list-to-file.txt', 'exercises.txt')

"""
14. Write a Python program to combine each line from first file with the
corresponding line in second file.
"""

f1 = open('fruits.txt')
f2 = open('vegetables.txt')
for line1, line2 in zip(f1, f2):
    print(line1.strip('\n'), line2.strip('\n'))
f1.close()
f2.close()
    
"""
15. Write a Python program to read a random line from a file.
"""

import random
with open('fruits.txt') as f:
    print(random.choice(f.readlines()))
    
"""
16. Write a Python program to assess if a file is closed or not.
"""
f = open('fruits.txt')
print(f.closed)
f.close()
print(f.closed)

"""
17. Write a Python program to remove newline characters from a file.
"""

with open('fruits.txt') as f:
    my_string = ' '.join(map(lambda x: x.strip('\n'), f.readlines()))
    print(my_string)

    f.seek(0)
    print(f.read())
