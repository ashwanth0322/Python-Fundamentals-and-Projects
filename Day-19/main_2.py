#Creating Employee Salary Calculator using Module
import Employee_utils
salary=int(input("Enter the Salary: "))
name=input("Enter the Name of the Employee:")
print("Name of the Employee :",name)
print("Base Salary :",salary)
tax=Employee_utils.calculate_tax(salary)
print("Tax :",tax)
bonus=Employee_utils.calculate_bonus(salary)
print("Bonus :",bonus)
print("Final Salary :",Employee_utils.calculate_final_salary(salary,bonus,tax))