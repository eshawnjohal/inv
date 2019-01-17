import product


class Inventory:
    def __init__(self):
        self.inventory = dict()
        self.sku_dictionary = dict()

    def add_item(self, item_name, sku, department_name, cost, price, quantity):
        if sku in self.inventory:
                print('SKU already exists. Try again.')
        else:
            self.inventory[sku] = product.Product(item_name, sku, department_name, cost, price, quantity)
            self.sku_dictionary[item_name.upper()] = sku

    def find_sku(self, item_name):
        try:
            print(self.sku_dictionary[item_name.upper()])
        except KeyError:
            print('No Item Found')

    def change_cost(self, sku, new_cost):
        try:
            self.inventory[sku].cost = new_cost
        except KeyError:
            print('SKU not found.')

    def change_price(self, sku, new_price):
        try:
            self.inventory[sku].price = new_price
        except KeyError:
            print('SKU not found.')

    def change_quantity(self, sku, new_quantity):
        try:
            self.inventory[sku].quantity = new_quantity
        except KeyError:
            print('SKU not found.')

    def change_department(self, sku, new_department):
        try:
            self.inventory[sku].department = new_department
        except KeyError:
            print('SKU not found.')

    def see_all_products(self):
        for items in self.inventory:
            print(self.inventory[items])

    def see_a_product(self, sku):
        print(self.inventory[sku])

    def delete_a_product(self, sku):
        try:
            del self.sku_dictionary[self.inventory[sku].name]
            del self.inventory[sku]
            print('Success.')
        except KeyError:
            print('SKU not found.')

