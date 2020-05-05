"""
Python makes performing file I/O simple. Take a look
at how to read and write to files here:

https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
"""

# Open up the "foo.txt" file (which already exists) for reading
# Print all the contents of the file, then close the file
# Note: pay close attention to your current directory when trying to open "foo.txt"

# YOUR CODE HERE

# according to documentation, it's good practice to use 'with' keyword when dealing with file objects
# attempting to use file object after it's closed will fail
with open("foo.txt") as f:
    read_file = f.read()

    print(read_file)


# Open up a file called "bar.txt" (which doesn't exist yet) for
# writing. Write three lines of arbitrary content to that file,
# then close the file. Open up "bar.txt" and inspect it to make
# sure that it contains what you expect it to contain

# YOUR CODE HERE

# "\n" will start a new line
with open("bar.txt", "w") as new_file:
    new_file.write("This is the first line.\n")
    new_file.write("This is the second line.\n")
    new_file.write("This is the third line.")


with open("bar.txt", "r") as new_f:
    read_new_file = new_f.read()

    print(read_new_file)
