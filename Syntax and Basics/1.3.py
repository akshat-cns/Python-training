principal = float(input("Enter the loan amount (Principal): "))
annual_rate = float(input("Enter the annual interest rate (in %): "))
tenure_years = int(input("Enter the loan tenure (in yrs): "))

monthly_rate = (annual_rate / 100) / 12
num_payments = tenure_years * 12

# monthly payment formula
# M = P * (r(1 + r)^n) / ((1 + r)^n - 1)

if monthly_rate != 0:  
    monthly_payment = principal * (monthly_rate * (1 + monthly_rate)**num_payments) / ((1 + monthly_rate)**num_payments - 1)
else:
    monthly_payment = principal / num_payments

print(f"Your monthly payment will be: ${monthly_payment:.2f}")
