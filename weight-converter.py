weight = float(input("Enter weight: "))

while True:
    unit = input("Enter unit (L)bs Or (K)g : ").lower()
    if unit in ['l', 'k']:
        break
    else:
        print("Please enter 'l/L' or 'k/K'.")

match unit:
    case 'k':
        weight_in_lbs = weight * 2.2046226218
        print(f"Converted to Pounds: {weight_in_lbs:.2f} lbs")
    case 'l':
        weight_in_kg = weight * 0.45359237
        print(f"Converted to Kilograms: {weight_in_kg:.2f} kg")