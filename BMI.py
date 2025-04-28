def calculate_bmi(weight, height):
    
    if weight <= 0 or height <= 0:
        return "Invalid input. Weight and height must be positive values."
    print("Height =  ",height)
    print("Weight =  ",weight)
    bmi = weight / (height ** 2)
    return bmi

Weight = float(input("Enter your weight in kilograms: "))
Height = float(input("Enter your height in meters: "))
bmi = calculate_bmi(Weight, Height)
print("Your BMI is:", bmi)
if (bmi < 18.5):
    print("You are underweight.")
elif (bmi >= 18.5 and bmi <= 24.9):
    print("You are in the normal weight range.")
elif (bmi >= 25):
    print("You are overweight.")