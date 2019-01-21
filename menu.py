import inventory # The backend of the program is being imported.
import pickle # I chose to use the pickle module to allow the object to be saved and reloaded.

class Menu:
    """
    The menu class is the front end of the program. This approach was taken after a discussion with Mr. Peterson
    of another portfolio of mine.
    The backend is all separated from the frontend.
    """
    def __init__(self):
        """
        This sets one attribute, 'inventory', as an inventory item.
        """
        self.inventory = inventory.Inventory() # Creates attribute inventory from imported module.

    def menu(self):
        """
        Front end of program.
        When this is first ran, the inventory is unpickled and loaded for the user.
        If the inventory is not found, it will be created. If it is empty, it will proceed anyways.
        This function, depending on the user input, will point to a variety of different functions.
        """
        try:
            self.load_inventory() # This will attempt to load the inventory
        except EOFError:  # If the pickle file is empty, will display an error saying no items were found.
            print('Error loading inventory. No items found.')
        while True: # Will loop until user chooses to exit.
            # Beautiful Art Incoming
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
			         10 -------- See product margin
			         11 -------- Save inventory
			         12 -------- Exit\n       
			    ''')
            # Each option below will point to different functions.
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
                self.see_product_margin()
            elif action == '11':
                self.save_inventory()
            elif action == '12':
                self.save_inventory() #Always save before exiting!
                break
            else:
                print('\nInvalid Input... Try Again.\n') #If their input does not match, will run the loop again.
            #An idea for improvement would be to create a dictionary that would map user input to callbacks.

    def add_new_product(self):
        """
        This function takes input from the user and attempts to make a product item. If any input is invalid
        the attempt is aborted and the user is returned to the main menu.
        :return:
        """
        try:
            name = input('Input Items Name:\n')
            sku = int(input('Input Item SKU:\n')) # SKU must be an integer. SKUs are always integers.
            department_name = input('Input Department Name [Meat, Grocery, Produce]:\n')
            cost = float(input('Input Cost:\n')) # The cost is a floating point value to represent currency.
            price = float(input('Input Price:\n')) # The price is a floating point value to represent currency.
            quantity = int(input('Input Quantity:\n')) # The quantity must be a integer. Quantity is always a whole number (ie: Cannot have 2.5 computers.)
            # If the inputs for SKU, cost, price, or quantity are invalid, a ValueError will be excepted.
            self.inventory.add_item(name,sku,department_name,cost,price,quantity) # Uses function in inventory module. Adds item to inventory module.
            self.inventory.see_a_product(sku) # Uses function in inventory module. Prints off the item that was just added.
        except ValueError:
            # If any of the inputs do not follow the conventions, user is returned to main menu.
            print('\nInvalid Input... Try again.\n')

    def find_product_sku(self):
        """
        This function takes the items name as an input and tries to find its SKU in the SKU dictionary.
        :return: The SKU of the item.
        """
        name = input('Input Item Name:\n')
        self.inventory.find_sku(name) # Uses function in inventory module. Prints off SKU if item name is found.


    def change_product_cost(self):
        """
        This function changes the attribute 'cost' that represents the cost of the item and updates the margin.
        """
        try:
            sku = int(input('Input Item SKU:\n')) # Checks if SKU is an integer, else will return to main menu.
            new_cost = float(input('Input the New Cost:\n')) # Checks if the new cost is a floating value (currency), else will return to main menu.
            self.inventory.change_cost(sku, new_cost) # Uses function in inventory module. Changes attribute 'cost'.
            self.inventory.inventory[sku].update_margin() # Because margin depends on cost, margin of product is updated.
            self.inventory.see_a_product(sku) # Prints item with updated information.
        except ValueError:
            # If any input is invalid based on context, will do nothing but return to the main menu.
            print('\nInvalid Input... Try again.\n')


    def change_product_price(self):
        """
        This function changes the attribute 'cost' that represents the cost of the item and updates the margin.
        """
        try:
            sku = int(input('Input Item SKU:\n')) # Checks if SKU is an integer, else will return to main menu.
            new_price = float(input('Input the New Price:\n')) # Checks if the new cost is a floating value (currency), else will return to main menu.
            self.inventory.change_price(sku, new_price) # Changes attribute price to the new price inputted.
            self.inventory.inventory[sku].update_margin() # Because margin depends on price, margin of product is updated.
            self.inventory.see_a_product(sku) # Prints item with updated information.
        except ValueError:
            # If any input is invalid based on context, will do nothing but return to the main menu.
            print('\nInvalid Input... Try again.\n')

    def change_product_quantity(self):
        """

        """
        try:
            sku = int(input('Input Item SKU:\n')) # Checks if SKU is an integer, else will return to main menu.
            new_quantity = int(input('Input the New Quantity:\n')) # Checks if the new quantity is a new item (logic), else will return to main menu.
            self.inventory.change_quantity(sku,new_quantity) # Changes attribute quantity to the new quantity.
            self.inventory.see_a_product(sku) # Prints item with updated information.
        except ValueError:
            # If any input is invalid based on context, will do nothing but return to the main menu.
            print('\nInvalid Input... Try again.\n')

    def change_product_department(self):
        try:
            sku = int(input('Input Item SKU:\n')) # Checks if SKU is an integer, else will return to main menu.
            new_department = input('Input the New Department:\n')
            self.inventory.change_department(sku, new_department)
            self.inventory.see_a_product(sku)
        except ValueError:
            # If any input is invalid based on context, will do nothing but return to the main menu.
            print('\nInvalid Input... Try again.\n')

    def see_all_products(self):
        self.inventory.see_all_products()

    def see_a_product(self):
        try:
            sku = int(input('Input Item SKU:\n')) # Checks if SKU is an integer, else will return to main menu.
            self.inventory.see_a_product(sku)
        except ValueError:
            # If any input is invalid based on context, will do nothing but return to the main menu.
            print('\nInvalid Input... Try again.\n')

    def see_product_margin(self):
        try:
            sku = int(input('Input Item SKU:\n')) # Checks if SKU is an integer, else will return to main menu.
            print ('Gross Margin: ',self.inventory.see_product_margin(sku))
        except ValueError:
            # If any input is invalid based on context, will do nothing but return to the main menu.
            print('\nInvalid Input... Try again.\n')

    def delete_a_product(self):
        try:
            sku = int(input('Input Item SKU:\n')) # Checks if SKU is an integer, else will return to main menu.
            self.inventory.delete_a_product(sku)
        except ValueError:
            # If any input is invalid based on context, will do nothing but return to the main menu.
            print('\nInvalid Input... Try again.\n')

    def save_inventory(self):
        output_pickle = open("inventory.pickle", "wb")
        pickle.dump(self.inventory, output_pickle)
        print('Saved!\n')

    def load_inventory(self):
        try:
            input_pickle = open("inventory.pickle", "rb")
            self.inventory = pickle.load(input_pickle)
        except FileNotFoundError:
            open("inventory.pickle", "w+" )
            self.load_inventory()
