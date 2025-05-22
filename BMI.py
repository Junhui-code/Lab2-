def calculate_bmi(weight, height):
    
    if weight <= 0 or height <= 0:
        return "Invalid input. Weight and height must be positive values."
    else:
        print ("Height = " + str(height))
        print ("Weight = " + str(weight))
    bmi = weight / (height ** 2)

    if bmi < 18.5:
        return -1
    elif bmi >= 18.5 and bmi <= 24.9:
        return 0
    elif bmi >= 25:
        return 1
    
def get_user_input():
    weight = float(input("Enter your weight in kilograms: "))
    height = float(input("Enter your height in meters: "))
    return weight, height


def main():
    weight, height = get_user_input()
    bmi = calculate_bmi(weight, height)
    if bmi == -1:
        print("Your BMI is considered underweight.")
    elif bmi == 0:
        print("Your BMI is within the normal range.")
    elif bmi == 1:
        print("Your BMI is considered overweight.")

if __name__ == "__main__":
    main()
