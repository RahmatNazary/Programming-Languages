age=25
name="John Doe"

salary = 25000
commission = 0.2
tax = 0.1
print("My name is :",name, " I am ",age, " years old")

gross_salary = salary + salary * commission
net_salary = gross_salary - (gross_salary * tax)

print("Monthly Gross Salary:",gross_salary)
print("Monthly Net Salary:",net_salary)

