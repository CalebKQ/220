"""
Name: Caleb Quattlebaum
sales_person.py

Purpose: Create a class that creates a SalesPerson object with employee id, employee name,
         and sales. Create methods in the class that work with these instance variables.

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""

class SalesPerson:
    """
    Creates an object of an employee with their name and employee id.
    With methods to get and set the name and id, to add sales, add
    sales for total sales, see if the employee met a quota, and
    compare the employee with another employee.
    """

    def __init__(self, employee_id, name):
        self.employee_id = int(employee_id)
        self.name = str(name)
        self.sales = []

    def get_id(self):
        return self.employee_id

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = str(name)

    def enter_sale(self, sale):
        self.sales.append(float(sale))

    def total_sales(self):
        return sum(self.sales)

    def get_sales(self):
        return self.sales

    def met_quota(self, quota):
        return self.total_sales() >= quota

    def compare_to(self, other):
        if self.total_sales() < other.total_sales():
            return -1
        if self.total_sales() == other.total_sales():
            return 0
        if self.total_sales() > other.total_sales():
            return 1

    def __str__(self):
        return str(self.employee_id) + '-' + self.name + ": " + str(self.total_sales())
