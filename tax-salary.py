SPOUSE_DEDUCTION = 150000  

base_salary = int(input("Enter Base salary: "))

spouse = input("Do you have a spouse? (y/n): ").strip().lower()
if spouse == 'y':
    num_spouses = int(input("Enter number of spouses: "))
    spouse_deduction = num_spouses * SPOUSE_DEDUCTION
else:
    spouse_deduction = 0

calculated_salary = base_salary - spouse_deduction

if calculated_salary <= 1300000:
    tax_rate = 0
    tax_amount = 0
elif calculated_salary <= 2000000:
    tax_rate = 5
    tax_amount = calculated_salary * (tax_rate / 100) - 65000
elif calculated_salary <= 8500000:
    tax_rate = 10
    tax_amount = calculated_salary * (tax_rate / 100) - 165000
elif calculated_salary <= 12500000:
    tax_rate = 15
    tax_amount = calculated_salary * (tax_rate / 100) - 590000
else:
    tax_rate = 20
    tax_amount = calculated_salary * (tax_rate / 100) - 1215000

tax_amount = max(0, tax_amount)

net_salary = calculated_salary - tax_amount

print("\n-----------------------------")
print(f"Base Salary: {base_salary:,}")
print(f"Spouse Deduction: {spouse_deduction:,}")
print(f"Taxable Salary: {calculated_salary:,}")
print(f"Tax Rate: {tax_rate}%")
print(f"Tax Amount: {tax_amount:,}")
print(f"Net Salary: {net_salary:,}")
print("-----------------------------")
