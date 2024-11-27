n = 150000

base_salary = int(input("Enter Base salary: "));
spause = input("Spause ? (y or n): ");
if spause == 'y':
    child = int(input("Number of Spause: "));
    m = child * n;
    base_salary = base_salary - m;
else:
    m = 0;

if base_salary > 0 and base_salary <= 1300000:
    net_salary = base_salary;
    print("Net Salary: ", net_salary);
elif base_salary >= 1300001 and base_salary <= 2000000:
    net_salary = base_salary * (5/100) - 65000;
    print("Net Salary: ", net_salary);
elif base_salary >= 2000001 and base_salary <= 8500000:
    net_salary = base_salary * (10/100) - 165000;
    print("Net Salary: ", net_salary);
elif base_salary >= 8500001 and base_salary <= 12500000:
    net_salary = base_salary * (15/100) - 590000;
    print("Net Salary: ", net_salary);
else:
    net_salary = base_salary * (20/100) - 1215000;
    print("Net Salary: ", net_salary);