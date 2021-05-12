# Mathematical operations

# Addition
print(1 + 2)
# Subraction
print(1 - 2)
# Multipication
print(1 * 2)
# Division - Gives output in float
print(1 / 2)
# Exponential
print(2 ** 2)
# Order of execution if more than one mathetacial operator
# Use PEMDAS - Paranthesis => Exponents => Multiplication => Division => Addition => Subtraction
print(1*2**3+4+(2-1)) # (2-1) and then 2**3 and then 1*2**3 and finnaly +
# output 1*8+4+1 = 13
print(3*3+3/3-1) # 9

# rounding number to whole or even floating based on specinfing number to round
print(8/2) # 4.0
print(8//2) # 4
print(round(8/2)) # 4
print(round(8/3,2)) #2.67


# Program - Calculate how many days, weeks and months left for you Ex: 90 Years
age = input("What is your current age? ")
years = 90
remainingYears = (int(years) - int(age))
days = remainingYears * 365
weeks = remainingYears * 52
months = remainingYears * 12
print(f"you have {days} days, {weeks} weeks and, {months} months left")