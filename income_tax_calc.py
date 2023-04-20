# income_tax_calc.py

income = float(input("Enter income:"))
if income <= 14000:
    tax = income*.105
    print(tax)
elif income <= 48000:
    tax = (income-14000)*.175+1470
    print(tax)
elif income <= 70000:
    tax = (income-48000)*.3+7420
    print(tax)
elif income <= 180000:
    tax = (income-70000)*.33+14020
    print(tax)
elif income > 18000:
    tax = (income-18000)*.39+50320
    print(tax)

