import io
import glob
import time
import sys
import os
from os import stat_info

# 1. Write a Python program to get the name of the operating system(Platform independent), information of current operating system, current working directory, print files and directories in the current directory and raises error in the case of invalid or inaccessible file names and paths. 
print("Operating System:", os.name)
print("\nInformation of current operating system: ", os.uname())
print("\nCurrent Working Directory: ", os.getcwd())
print("\nList of files and directories in the current directory:")
print(os.listdir('.'))
print("\nTest if a specified file exis or not:")
try:
   filename = 'abc.txt'
   f = open(filename, 'r')
   text = f.read()
   f.close()
except IOError:
   print('Not accessed or problem in reading: ' + filename)

# 2. Write a Python program to list only directories, files and all directories, files in a specified path. 
path = 'g:\\testpath\\'
print("Only directories:")
print([name for name in os.listdir(path)
       if os.path.isdir(os.path.join(path, name))])
print("\nOnly files:")
print([name for name in os.listdir(path)
       if not os.path.isdir(os.path.join(path, name))])
print("\nAll directories and files :")
print([name for name in os.listdir(path)])

# 3. Write a Python program to scan a specified directory and identify the sub directories and files.
root = 'g:\\testpath\\'
for entry in os.scandir(root):
   if entry.is_dir():
       typ = 'dir'
   elif entry.is_file():
       typ = 'file'
   elif entry.is_symlink():
       typ = 'link'
   else:
       typ = 'unknown'
   print('{name} {typ}'.format(
       name=entry.name,
       typ=typ,
   ))

# 4. Write a Python program to check for access to a specified path. Test the existence, readability, writability and executability of the specified path. 
print('Exist:', os.access('c:\\Users\\Public\\C programming library.docx', os.F_OK))
print('Readable:', os.access(
    'c:\\Users\\Public\\C programming library.docx', os.R_OK))
print('Writable:', os.access(
    'c:\\Users\\Public\\C programming library.docx', os.W_OK))
print('Executable:', os.access(
    'c:\\Users\\Public\\C programming library.docx', os.X_OK))

# 5. Write a Python program to get the size, permissions, owner, device, created, last modified and last accessed date time of a specified path.
path = 'g:\\testpath\\'
print('Path Name ({}):'.format(path))
print('Size:', stat_info.st_size)
print('Permissions:', oct(stat_info.st_mode))
print('Owner:', stat_info.st_uid)
print('Device:', stat_info.st_dev)
print('Created     :', time.ctime(stat_info.st_ctime))
print('Last modified:', time.ctime(stat_info.st_mtime))
print('Last accessed:', time.ctime(stat_info.st_atime))

# 6. Write a Python program to create a symbolic link and read it to decide the original file pointed by the link. 
path = '/tmp/' + os.path.basename(__file__)
print('Creating link {} -> {}'.format(path, __file__))
os.symlink(__file__, path)
stat_info = os.lstat(path)
print('\nFile Permissions:', oct(stat_info.st_mode))
print('\nPoints to:', os.readlink(path))
#removes the file path
os.unlink(path)

# 7. Write a Python program to create a file and write some text and rename the file name.
with open('a.txt', 'w') as f:
   f.write('Python program to create a symbolic link and read it to decide the original file pointed by the link.')
print('\nInitial file/dir name:', os.listdir())
with open('a.txt', 'r') as f:
   print('\nContents of a.txt:', repr(f.read()))
os.rename('a.txt', 'b.txt')
print('\nAfter renaming initial file/dir name:', os.listdir())
with open('b.txt', 'r') as f:
   print('\nContents of b.txt:', repr(f.read()))

# 8. Write a Python program to find the parent's process id, real user ID of the current process and change real user ID. 
print("Parent’s process id:", os.getppid())
uid = os.getuid()
print("\nUser ID of the current process:", uid)
uid = 1400
os.setuid(uid)
print("\nUser ID changed")
print("User ID of the current process:", os.getuid())

# 9. Write a Python program to retrieve the current working directory and change the dir(moving up one). 
print('Current dir:', os.getcwd())
print('\nChange the dir (moving up one):', os.pardir)
os.chdir(os.pardir)
print('Current dir:', os.getcwd())
print('\nChange the dir (moving up one):', os.pardir)
os.chdir(os.pardir)
print('Current dir:', os.getcwd())

# 10. Write a python program to access environment variables and value of the environment variable. 
import os
print("Access all environment variables:")
print('*----------------------------------*')
print(os.environ)
print('*----------------------------------*')
print("Access a particular environment variable:")
print(os.environ['HOME'])
print('*----------------------------------*')
print(os.environ['PATH'])
print('*----------------------------------*')
print('Value of the environment variable key:')
print(os.getenv('JAVA_HOME'))
print(os.getenv('PYTHONPATH'))

# 11. Write a Python program to iterate over a root level path and print all its sub-directories and files, also loop over specified dirs and files. 
print('Iterate over a root level path:')
path = '/tmp/'
for root, dirs, files in os.walk(path):
 print(root)

# 12. Write a Python program to test whether a given path exists or not. If the path exist find the filename and directory portion of the said path. 
print("Test a path exists or not:")
path = r'g:\\testpath\\a.txt'
print(os.path.exists(path))
path = r'g:\\testpath\\p.txt'
print(os.path.exists(path))
print("\nFile name of the path:")
print(os.path.basename(path))
print("\nDir name of the path:")
print(os.path.dirname(path))

# 13. Write a Python program to join one or more path components together and split a given path in directory and file. 
path = r'g:\\testpath\\a.txt'
print("Original path:")
print(path)
print("\nDir and file name of the said path:")
print(os.path.split(path))
print("\nJoin one or more path components together:")
print(os.path.join(r'g:\\testpath\\', 'a.txt'))

# 14. Write a Python program to alter the owner and the group id of a specified file. 
fd = os.open("/tmp", os.O_RDONLY)
os.fchown(fd, 100, -1)
os.fchown(fd, -1, 50)
print("Changed ownership successfully..")
os.close(fd)

# 15. Write a Python program to get information about the file pertaining to the file mode. Print the information - ID of device containing file, inode number, protection, number of hard links, user ID of owner, group ID of owner, total size (in bytes), time of last access, time of last modification and time of last status change. 
path = 'e:\\testpath\\p.txt'
fd = os.open(path, os.O_RDWR)
info = os.fstat(fd)
print(f"ID of device containing file: {info.st_dev}")
print(f"Inode number: {info.st_ino}")
print(f"Protection: {info.st_mode}")
print(f"Number of hard links: {info.st_nlink}")
print(f"User ID of owner: {info.st_uid}")
print(f"Group ID of owner: {info.st_gid}")
print(f"Total size, in bytes: {info.st_size}")
print(f"Time of last access: {info.st_atime}")
print(f"Time of last modification: {info.st_mtime }")
print(f"Time of last status change: {info.st_ctime }")
os.close(fd)

# 16. Write a Python program to write a string to a buffer and retrieve the value written, at the end discard buffer memory.
# Write a string to a buffer
output = io.StringIO()
output.write('Python Exercises, Practice, Solution')
# Retrieve the value written
print(output.getvalue())
# Discard buffer memory
output.close()

# 17. Write a Python program to run an operating system command using the os module. 
if os.name == "nt":
   command = "dir"
else:
   command = "ls -l"
os.system(command)

# 18. Write a Python program to start a new process replacing the current process. 
program = "python"
arguments = ["hello.py"]
print(os.execvp(program, (program,) + tuple(arguments)))
print("Goodbye")

# 19. The epoch is the point where the time starts, and is platform dependent. For Unix, the epoch is January 1, 1970, 00: 00: 00 (UTC). Write a Python program to find out what the epoch is on a given platform. Also convert a given time in seconds since the epoch. 
print("\nEpoch on a given platform:")
print(time.gmtime(0))
print("\nTime in seconds since the epoch:")
print(time.gmtime(36000))

# 20. Write a Python program to get time values with components using local time and gmtime. 
def time_struct(s):
   print(' tm_year :', s.tm_year)
   print(' tm_mon :', s.tm_mon)
   print(' tm_mday :', s.tm_mday)
   print(' tm_hour :', s.tm_hour)
   print(' tm_min :', s.tm_min)
   print(' tm_sec :', s.tm_sec)
   print(' tm_wday :', s.tm_wday)
   print(' tm_yday :', s.tm_yday)
   print(' tm_isdst:', s.tm_isdst)

print('\nlocaltime:')
time_struct(time.localtime())
print('\ngmtime:')
time_struct(time.gmtime())

# 21. Write a Python program to get different time values with components timezone, timezone abbreviations, the offset of the local(non-DST) timezone, DST timezone and time of different timezones. 


def zone_info():
   print('TZ   :', os.environ.get('TZ', '(not set)'))
   print('Timezone abbreviations:', time.tzname)
   print('Timezone : {} ({})'.format(
       time.timezone, (time.timezone / 3600)))
   print('DST timezone ', time.daylight)
   print('Time :', time.strftime('%X %x %Z'), '\n')


print('Default Zone:')
zone_info()
TIME_ZONES = [
    'Pacific/Auckland',
    'Europe/Berlin',
    'America/Detroit',
    'Singapore',
]
for zone in TIME_ZONES:
   os.environ['TZ'] = zone
   time.tzset()
   print(zone, ':')
   zone_info()

# 22. Write a Python program that can suspend execution of a given script a given number of seconds. 
for x in range(4):
   time.sleep(3)
   print("Sorry, Slept for 3 seconds...")

# 23. Write a Python program to convert a given time in seconds since the epoch to a string representing local time. 
print(time.ctime())
print(time.ctime(236543789))

# 24. Write a Python program to print simple format of time, full names and the representation format and preferred date time format. 
import time
print("\nSimple format of time:")
s = time.strftime("%a, %d %b %Y %H:%M:%S + 1010", time.gmtime())
print(s)
print("\nFull names and the representation:")
s = time.strftime("%A, %D %B %Y %H:%M:%S + 0000", time.gmtime())
print( s)
print("\nPreferred date time format:")
s = time.strftime("%c")
print(s)
s = time.strftime("%x, %X, %y, %Y")
print("Example 11:", s)

# 25. Write a Python program that takes a given number of seconds and pass since epoch as an argument. Print structure time in local time. 
result = time.localtime(414538698)
print("\nResult:", result)
print("\nYear:", result.tm_year)

# 26. Write a Python program that takes a tuple containing 9 elements corresponding to structure time as an argument and returns a string representing it. 
import time
t = (2020, 1, 22, 2, 34, 6, 6, 362, 0)
result = time.asctime(t)
print("Result:", result)
t = (1982, 11, 12, 2, 54, 8, 8, 360, 0)
result = time.asctime(t)
print("Result:", result)

# 27. Write a Python program to parse a string representing time and returns the structure time. 
time_string = "22 January, 2020"
print("String representing time:", time_string)
result = time.strptime(time_string, "%d %B, %Y")
print(result)
time_string = "30 Nov 00"
print("\nString representing time:", time_string)
result = time.strptime(time_string, "%d %b %y")
print(result)
time_string = '04/11/15 11:55:23'
print("\nString representing time:", time_string)
result = time.strptime(time_string, "%m/%d/%y %H:%M:%S")
print(result)
time_string = '12-11-2019'
print("\nString representing time:", time_string)
result = time.strptime(time_string, "%m-%d-%Y")
print(result)
time_string = '13::55::26'
print("\nString representing time:", time_string)
result = time.strptime(time_string, "%H::%M::%S")
print(result)
