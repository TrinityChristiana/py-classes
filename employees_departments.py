# **************************** Challenge: Pizza Joint ****************************
"""
Author: Trinity Terry
pyrun: python classes.py
"""
from random_names import random_name

# Create an Employee type that contains information about employees of a company. Each employee must have a name, job title, and employment start date.
class Employee:
    def __init__(self, name, title, start_date):
        self.name = name
        self.title = title
        self.start_date = start_date

# Create a Company type that employees can work for. A company should have a business name, address, and industry type.
class Company:
    def __init__(self, name, address, industry_type):
        self.name = name
        self.address = address
        self.industry_type = industry_type
        self.employees = list()
    
    def hire(self, employee):
        self.employees.append(employee)

    def show_detail(self):
        company = self.__dict__
        employees = company["employees"]
        print(f"{company['name']} is in the {company['industry_type']} industry and has the following employees")
        for employee in employees:
            name = employee.__dict__["name"]
            print(f"\t* {name}")


# Create two companies, and 5 people who want to work for them.
netflix = Company("Netflix", "Los Gatos, CA", "entertainment")
kroger = Company("Kroger", "5319 Mt View Rd", "grocery")
employee1 = Employee(random_name(), "Watcher", "05/29/2019")
employee2 = Employee(random_name(), "Secretary", "03/14/2020")
employee3 = Employee(random_name(), "Cashier", "12/24/2019")
employee4 = Employee(random_name(), "Stocker", "08/25/2019")
employee5 = Employee(random_name(), "Greeter", "02/22/2020")

# Assign 2 people to be employees of the first company.
netflix.hire(employee1)
netflix.hire(employee2)

# Assign 3 people to be employees of the second company.
kroger.hire(employee3)
kroger.hire(employee4)
kroger.hire(employee5)

# Output a report to the terminal the displays a business name, and its employees.
netflix.show_detail()
kroger.show_detail()
