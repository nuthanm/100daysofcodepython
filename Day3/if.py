# Program to check user height in cm if height >120cm then his/her can ride else can't ride

height = int(input("Please enter your height in cm: "))

if height > 120:
  print("You are eligible for Rollercoaster to ride.")
else:
  print("Sorry!! You can't due to height issue as per the rules.")