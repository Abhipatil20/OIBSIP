# BMI Calculator

while True:
    # Take input from user
    weight = float(input("Enter your weight in kg: "))
    height = float(input("Enter your height in meters: "))

    # Calculate BMI
    bmi = weight / (height ** 2)

    # Show result
    print("\nYour BMI is:", round(bmi, 2))

    # Check category
    if bmi < 18.5:
        print("Category: Underweight")
    elif bmi < 25:
        print("Category: Normal weight")
    elif bmi < 30:
        print("Category: Overweight")
    else:
        print("Category: Obese")

    # Ask user to continue
    choice = input("\nDo you want to calculate again? (yes/no): ")

    if choice.lower() != "yes":
        print("Thank you!")
        break