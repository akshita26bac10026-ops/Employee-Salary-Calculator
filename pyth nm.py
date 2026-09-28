# Employee Salary Calculation

basic_pay = float(input("Enter Basic Pay: "))
da_percentage = float(input("Enter DA Percentage: "))
hra_percentage = float(input("Enter HRA Percentage: "))
transport_allowance = float(input("Enter Transport Allowance: "))
pf_percentage = float(input("Enter PF Percentage: "))
professional_tax = float(input("Enter Professional Tax: "))

# Calculate allowances
da = (basic_pay * da_percentage) / 100
hra = (basic_pay * hra_percentage) / 100

# Calculate gross salary
gross_salary = basic_pay + da + hra + transport_allowance

# Calculate deductions
pf = (basic_pay * pf_percentage) / 100
total_deductions = pf + professional_tax

# Calculate net salary
net_salary = gross_salary - total_deductions

# Display salary details
print("\n========== EMPLOYEE SALARY DETAILS ==========")
print(f"Basic Pay            : ₹{basic_pay:.2f}")
print(f"Dearness Allowance   : ₹{da:.2f}")
print(f"House Rent Allowance : ₹{hra:.2f}")
print(f"Transport Allowance  : ₹{transport_allowance:.2f}")
print(f"Gross Salary         : ₹{gross_salary:.2f}")
print(f"Provident Fund       : ₹{pf:.2f}")
print(f"Professional Tax     : ₹{professional_tax:.2f}")
print(f"Total Deductions     : ₹{total_deductions:.2f}")
print(f"Net Salary           : ₹{net_salary:.2f}")
print("=============================================")
