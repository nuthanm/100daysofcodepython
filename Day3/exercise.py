#program - 1 - Given number is even or odd
# Note: If given number is divisible by 0 (It means remainder value is 0) then even else odd.

number = int(input("Check whether input is even or not? "))

if number % 2 == 0:
  print(f"{number} is even.")
else:
  print(f"{number} is odd.")

#program 2 - BMI Calculator 2.0

weight = float(input("Weight in kgs: "))
height = float(input("height in m: "))

bmi = weight/(height ** 2)

if bmi < 18.5:
  print(f"Your bmi is {bmi}, You are Underweight")
elif bmi > 18.5 and bmi < 25:
  print(f"Your bmi is {bmi}, You are Normal Weight")
elif bmi > 25 and bmi < 30:
  print(f"Your bmi is {bmi}, You are Overweight")
elif bmi > 30 and bmi < 35:
  print(f"Your bmi is {bmi}, You are in Obese")
else:
  print(f"Your bmi is {bmi}, You need Clinically Obese")
  
print(bmi)