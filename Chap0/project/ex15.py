from sys import argv  # sys is a software package, import argv from sys module

script, filename = argv # argument variables

txt = open(filename) # open() return a "file object",not comment itself.

print ("Here's your file %r:" % filename) # print
print (txt.read()) # return the whole txt file

txt.close()

# the function open() is the same with Python2

print ("type the filename again:")
file_again = input("> ")

txt_again = open(file_again)
print (txt_again.read())
