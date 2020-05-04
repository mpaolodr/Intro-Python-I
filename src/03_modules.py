"""
In this exercise, you'll be playing around with the sys module,
which allows you to access many system specific variables and
methods, and the os module, which gives you access to lower-
level operating system functionality.
"""


import sys
import os
# See docs for the sys module: https://docs.python.org/3.7/library/sys.html

# Print out the command line arguments in sys.argv, one per line:
# YOUR CODE HERE

for arg in sys.argv:
    print("Arguments in sys.argv:", arg)


# Print out the OS platform you're using:
# YOUR CODE HERE

print("Concatenation. This is the OS Platform: " + sys.platform)

# Print out the version of Python you're using:
# YOUR CODE HERE

print(f"Interpolation. This is version of Python:", sys.winver)
# See the docs for the OS module: https://docs.python.org/3.7/library/os.html


# Print the current process ID
# YOUR CODE HERE
# getpid is the correct one, getppid is parent's process id? what's that parent?

print("This is the process ID:", str(os.getpid()))

# Print the current working directory (cwd):
# YOUR CODE HERE
# getcwd unicode string, getcwdb bytes string

print("This is the working directory unicode string: " + str(os.getcwd()))
print("This is the working directory in bytes string: " + str(os.getcwdb()))

# Print out your machine's login name
# YOUR CODE HERE

print("This is the login name:", str(os.getlogin()))
