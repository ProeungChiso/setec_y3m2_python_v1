total_bill = float(input("Enter total bill: "))

tax_rate = float(input("Enter tax: "))
tip_rate = float(input("Enter tip: "))

tax = total_bill * (tax_rate / 100)
tip = total_bill * (tip_rate / 100)
total_pay = total_bill + tax + tip

print(f"Total Pay: {total_pay:.2f}USD")