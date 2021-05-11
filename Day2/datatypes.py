# Python Data types
'''
In Python, main data types we use in our day to day are
string, integer, float and boolean
No need to define data type i.e., 123 by default treated as integers, 12.34 treated as float, "Nani" or 'Potti' treated as string, True or False treated as boolean
'''
# String - Presents data in between either 'text' or "text" => Series of charecters or collection of charecters
print("Hello") # Hello is a string
print("Potti"[0]) # returns P because we set position/Index in string to get the character (We call this as Subscript).
# print("Potti"[5]) # This give index error

# Integer
print(123)

# Float
print(3.14)
print(29.20)

# Boolean
print(True)
# Wrong print(true) statement

# Type Error Example
#  print('My age '+ 29 + 'years old')
# Error gives as TypeError: can only concatenate str (not "int") to str

# Type checking with type()
print(type(23))

# Type Conversion => To fix the above concatenate issue
#str(), float(), int()
print(str(123)) # 123
print(str(143)+ " Potti") # 143 Potti
print(int(10.25)) # convert float to int 10
print(float(123)) # convert int to float 123.0
print(bool(1)) # True
print(bool(0)) # False
print(bool(-2)) # True
print(bool(-0)) # False



