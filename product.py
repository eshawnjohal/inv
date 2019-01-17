import departments

class Product:
    def __init__(self, name, sku, department_name, cost, price, quantity):
        if quantity < 0 or cost < 0 or price < 0:
            raise ValueError
		else:
        	self.department = departments.Departments(department_name)
        	self.name = name
        	self.sku = sku
        	self.cost = cost
        	self.price = price
        	self.quantity = quantity

    def __str__(self):
        return f'''\nItem Name: {self.name}
Item SKU: {self.sku}
Item Cost: ${self.cost:.2f} Item Price: ${self.price:.2f}
Department: {self.department}
Item Quantity: {self.quantity}\n
'''


