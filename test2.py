def pounds_to_kg(pounds):
    return pounds / 2.20462

def kg_to_pounds(kg):
    return kg * 2.20462

# Get user input
weight = float(input("Enter your weight: "))
unit = input("Is this weight in kg or lb? ").lower()

# Convert and display results
if unit == "kg":
    print(f"{kg_to_pounds(weight):.2f} lb")
elif unit == "lb":
    print(f"{pounds_to_kg(weight):.2f} kg")
else:
    print("Invalid unit. Please enter either 'kg' or 'lb'.")
