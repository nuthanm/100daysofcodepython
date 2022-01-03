# First python program


print('Please enter your name: ')
name = input()
print('Hello '+name)

# TypeError: can only concatenate str (not "int") to str
#print('Length of the name' + len(name))
# To fix the above statement
print('Length of the name: ' + str(len(name)))

print('What is your age? ')
age = input() # by default read value is in string format
print('Good to see you age is just: '+ age)
