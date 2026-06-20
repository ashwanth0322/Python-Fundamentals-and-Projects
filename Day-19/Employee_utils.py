#Creating functions for Employee Salary Calculator 
def calculate_bonus(salary):
    bonus=salary*0.1
    return bonus
def calculate_tax(salary):
    tax=salary*0.05
    return tax
def calculate_final_salary(salary,bonus,tax):
    final_salary=salary+bonus-tax
    return final_salary
