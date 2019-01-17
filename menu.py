import inventory
import pickle

class Menu:
    def __init__(self):
        self.inventory = inventory.Inventory()

    def menu(self):
        self.load_inventory()
        while True:
            action = input('''
			          Inventory Manager
			    =============================
			          Enter    Function
			          -----    --------    
			          1 -------- Find product SKU
			          2 -------- Add new product
			          3 -------- Change product price
			          4 -------- Change product cost
			          5 -------- Change product quantity
			          6 -------- Change product department
			          7 -------- See all products
			          8 -------- See a product   
			          9 -------- Delete a product   
			         10 -------- Save Database
			         11 -------- Exit\n       
			    ''')
            if action == '1':
                self.find_product_sku()
            elif action == '2':
                self.add_new_product()
            elif action == '3':
                self.change_product_price()
            elif action == '4':
                self.change_product_cost()
            elif action == '5':
                self.change_product_quantity()
            elif action == '6':
                self.change_product_department()
            elif action == '7':
                self.see_all_products()
            elif action == '8':
                self.see_a_product()
            elif action == '9':
                self.delete_a_product()
            elif action == '10':
                self.save_inventory()
            elif action == '11':
                self.save_inventory()
                break
            else:
                print('Invalid Input.')


    def add_new_product(self):
        try:
            name = input('Input Items Name:\n')
            sku = int(input('Input Item SKU:\n'))
            department_name = input('Input Department Name [Meat, Grocery, Produce]:\n')
            cost = float(input('Input Cost:\n'))
            price = float(input('Input Price:\n'))
            quantity = int(input('Input Quantity:\n'))
            self.inventory.add_item(name,sku,department_name,cost,price,quantity)
        except ValueError:
            print('\nInvalid Input... Try again.\n')

    def find_product_sku(self):
        try:
            name = input('Input Item Name:\n')
            self.inventory.find_sku(name)
        except ValueError:
            print('\nInvalid Input... Try again.\n')

    def change_product_cost(self):
        try:
            sku = int(input('Input Item SKU:\n'))
            new_cost = float(input('Input the New Cost:\n'))
            self.inventory.change_cost(sku, new_cost)
            self.inventory.see_a_product(sku)
        except ValueError:
            print('\nInvalid Input... Try again.\n')


    def change_product_price(self):
        try:
            sku = int(input('Input Item SKU:\n'))
            new_price = float(input('Input the New Price:\n'))
            self.inventory.change_price(sku, new_price)
            self.inventory.see_a_product(sku)
        except ValueError:
            print('\nInvalid Input... Try again.\n')

    def change_product_quantity(self):
        try:
            sku = int(input('Input Item SKU:\n'))
            new_quantity = int(input('Input the New Quantity:\n'))
            self.inventory.change_quantity(sku,new_quantity)
            self.inventory.see_a_product(sku)
        except ValueError:
            print('\nInvalid Input... Try again.\n')

    def change_product_department(self):
        try:
            sku = int(input('Input Item SKU:\n'))
            new_department = input('Input the New Department:\n')
            self.inventory.change_department(sku, new_department)
            self.inventory.see_a_product(sku)
        except ValueError:
            print('\nInvalid Input... Try again.\n')

    def see_all_products(self):
        self.inventory.see_all_products()

    def see_a_product(self):
        try:
            sku = int(input('Input Item SKU:\n'))
            self.inventory.see_a_product(sku)
        except ValueError:
            print('\nInvalid Input... Try again.\n')

    def delete_a_product(self):
        try:
            sku = int(input('Input Item SKU:\n'))
            self.inventory.delete_a_product(sku)
        except ValueError:
            print('\nInvalid Input... Try again.\n')

    def save_inventory(self):
        output_pickle = open("inventory.pickle", "wb")
        pickle.dump(self.inventory, output_pickle)
        print('Saved!')

    def load_inventory(self):
        input_pickle = open("inventory.pickle", "rb")
        self.inventory = pickle.load(input_pickle)

    def main(self):
        self.menu()


