def calculate_bmi(weight, height):
    
    if weight <= 0 or height <= 0:
        return "Invalid input. Weight and height must be positive values."

    bmi = weight / (height ** 2)

    if bmi < 18.5:
        return -1
    elif bmi >= 18.5 and bmi <= 24.9:
        return 0
    elif bmi >= 25:
        return 1

