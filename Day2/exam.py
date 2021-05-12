# Program 
'''
1. Take two digit number as an input
2. Ex: 29
3. Output: 2 + 9 = 11
'''
two_digit_number = input(" Enter two digit number ")

if len(two_digit_number) > 2:
  print('Input length crosses 2 digit')
else:  
  first_digit = int(two_digit_number[0])
  second_digit = int(two_digit_number[1])
  total = first_digit + second_digit
  print('First digit' + str(first_digit))
  print('Second digit' + str(second_digit))
  print('Total digit value ' + str(total))

# Program 2 - Calculate Body Mass Index 
weight_in_kgs = input('Enter weight in kilograms: ')
height_in_meters = input('Enter height in meters: ')

bmi = int(weight_in_kgs)/ (float(height_in_meters) ** 2)
print(int(bmi))