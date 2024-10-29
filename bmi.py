def calculate_bmi(height, weight):
    print("Height = " + str(height))
    print("Weight = " + str(weight))
    
    bmi = weight / (height ** 2)
    
    print("BMI = " + str(bmi))
    
    # BMI classification
    if bmi < 18.5:
        return -1
    elif bmi < 25:
        return 0
    else:
        return 1

# Capture and print the return value of the function
result = calculate_bmi(weight=57, height=1.73)
print("BMI Classification:", result)
