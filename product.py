import departments # Importing the department class as one of the attribute of product is a Department object.

class Product:
    """
    Class representing the actual item.
    This class has attributes that all describe a real life item.
    All attributes are equally important to the item and certain inputs are ruled out logically.
    The margin of an item is defined as the gross profit made by selling the item.
    """
    def __init__(self, name, sku, department_name, cost, price, quantity,):
        if quantity < 0 or cost <= 0 or price <= 0 or sku < 0: # Quantity, cost, and price cannot be negative because it logically does not make sense too.
            raise ValueError # SKU's are always positive as well in the retail industry. If any are negative, value error is raised.
        else:
            # If all of the inputs make sense logically, the following attributes are set.
            self.department = departments.Departments(department_name)
            self.name = name
            self.sku = sku
            self.cost = cost
            self.price = price
            self.quantity = quantity
            self.margin = ((self.price - self.cost) / self.price ) * 100 # The margin of the item is calculated automatically based on the cost and price using this formula.

    def __str__(self):
        """
        As of Python 3.6, f formatting is the best way to format strings.
        This function returns the name, sku, cost price, margin, department, and quantity.
        :return: Formatted string containing attributes of item.
        """
        return f'''\nItem Name: {self.name}
Item SKU: {self.sku}
Item Cost: ${self.cost:.2f} Item Price: ${self.price:.2f}
Gross Item Margin: {self.margin:.2f}%
Department: {self.department}
Item Quantity: {self.quantity}\n
'''
    def update_margin(self):
        """
        Because the margin is calculated automatically, we need a way to update the margin if the cost or price changes.
        """
        self.margin = ((self.price - self.cost) / self.price ) * 100 # Formula to calculate margin



