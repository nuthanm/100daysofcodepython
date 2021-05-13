# Program to check user height in cm if height >120cm then his/her can ride else can't ride

# If he/she can ride then consider age. Based on age price is varies

height = int(input("Please enter your height in cm: "))

if height > 120:
  print("You are eligible for Rollercoaster to ride.")  
  age = int(input("Please enter your age: "))
  if age >=18:
    print("If Age >=18 then price is $20.")
  else:
    print("Age is <18 then price is $10.")
else:
  print("Sorry!! You can't due to height issue as per the rules.")