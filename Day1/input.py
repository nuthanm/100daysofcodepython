# In this class different ways we use input() to prompt user to enter and display

# Program 1- Ask user to enter their name
# 1. input() function reads the user input.
# 2. Takes the input and concatenate the response with print statement. Ex: 'Hello ' + User input It may be any and output should be Hello Nani. Consider i type Nani from prompt.

print('Hello ' + input('What is your nick name?'))

# Program 2 - Returns length of your input. Ex: nani means 4, Chinni Talli means 12

print(len(input('Please enter your like? ')))

# From input() => len() => print() => Displays length of the input.

# len() is used to find how many charecters in the input string.


# use variables to modify above print statement
inputString = input('Please enter your like? ')
length = len(inputString)
print(length)
# inputString holds user Input
# length holds length of user input
# print statement prints the length using Length Variable.