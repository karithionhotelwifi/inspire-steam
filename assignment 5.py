# Name : Augustine Mwangi
# Date : 1/02/2026
6
# Program to Calculate income tax

salary = int(input("Enter your gross salary:"))
if salary< 500000:
    tax = (.5/100) *salary
    net_salary = salary - tax

print(f"Gross salary = {salary}")
print(f"net_salary = {net_salary}")
print(f"tax = {tax}")