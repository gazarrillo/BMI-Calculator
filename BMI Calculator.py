# Height and Weight Input
height = input("Enter your height in inches: ")
weight = input("Enter your weight in pounds: ")
# BMI Calculation
BMI = float(weight)*703/float(height)**2
# Displays BMI
print("Your BMI is:", end =' ')
print(round(BMI,1))
# Health Diagnosis
if BMI < 18.5:
    print("Your BMI indicates that you are underweight")
elif BMI > 25:
    print("Your BMI indicates that you are overweight")
else:
    print("Your BMI indicates you are optimal weight")
