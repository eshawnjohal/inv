import product # Imports product class. Product class is used in thee inventory attribute.

class Inventory:
    def __init__(self):
        """
        Initializes two dictionaries that store the product. The SKU is the key and the value is a product object.
        SKU Dictionary pairs the items name to the SKU so the SKU can be easily retrieved if a SKU is forgotten.
        """
        self.inventory = dict() # Creating the dictionary that contains {SKU:Product Object}
        self.sku_dictionary = dict() # Creating the dictionary that contains {Product Name:SKU}

    def add_item(self, name, sku, department_name, cost, price, quantity):
        """
        This function adds an item to the inventory.
        The SKU is the key and a product item is its value.
        :param name: String. Name of the value.
        :param sku: Positive integer. The SKU of the product.
        :param department_name: String, either Meat, Produce, or Grocery. More Departments
                                can be added in departments.py
        :param cost: Positive floating point number. The cost of the product to purchase for the store.
        :param price: Positive floating point number. The price of the product for consumers.
        :param quantity: Positive integer. The quantity of products that they have.
        """
        if sku in self.inventory:  # Checks if the SKU exists in the inventory already. If it does, it will print an error and will not add it again.
            print('SKU already exists. Try again.')
        elif name.upper() in self.sku_dictionary:  #  Checks if the same name exists in the SKU dictionary. Without it, the SKU dictionary will not work properly.
            print('Name already exists. Try again.')
        else:
            self.inventory[sku] = product.Product(name, sku, department_name, cost, price, quantity)  # If the SKU is unique, will add it to inventory.
            self.sku_dictionary[name.upper()] = sku  # This adds the name mapped to the SKU into the SKU dictionary.

    def find_sku(self, name):
        """
        This function will check the SKU dictionary to find the SKU of the product name provided.
        :param name: String. The name of the product they're trying to find.
        :return: Prints the SKU if found.
        """
        try:
            print(f'The SKU is: {self.sku_dictionary[name.upper()]}') # Prints SKU of the item with matching name.
        except KeyError:  # This key error will trigger if the key (name) is not in the dictionary. This means the item is not found.
            print('No Item Found')

    def change_cost(self, sku, new_cost):
        """
        This function changes the cost of the product specified.
        :param sku: Integer. The SKU of the product.
        :param new_cost: Positive floating point number that is also greater then 0. The cost of the product will be changed to new_cost.
        """
        if new_cost <= 0:  # Checking if the new cost is negative. Cost is usually positive, and it effects the margin.
            raise ValueError # Raises error if it is negative.
        try:
            self.inventory[sku].cost = new_cost  # Changes cost to the new cost inputted.
        except KeyError: # This will run if the SKU inputted is not found in the dictionary.
            print('SKU not found.')

    def change_price(self, sku, new_price):
        """
        This function changes the price of the product specified.
        :param sku: Integer. The SKU of the product.
        :param new_price: Positive floating point number that is also greater then 0. The price of the product will be changed to new_price.
        """
        if new_price <= 0: # Checking if the new price is negative. If new price is negative, the margin will break and prices tend to be positive.
            raise ValueError # Raises error if it is negative.
        try:
            self.inventory[sku].price = new_price
        except KeyError: # This will run if the SKU inputted is not found in the dictionary.
            print('SKU not found.')

    def change_quantity(self, sku, new_quantity):
        """
        This function changes the quantity of the product specified.
        :param sku: Integer. The SKU of the product.
        :param new_quantity: Positive integer that is also greater then 0. The quantity of the product will be changed to new_quantity.
        :return:
        """
        if new_quantity < 0:  # Checking if quantity if negative. Quantity tends to be positive.
            raise ValueError # Raises error if it is negative.
        try:
            self.inventory[sku].quantity = new_quantity
        except KeyError: # This will run if the SKU inputted is not found in the dictionary.
            print('SKU not found.')

    def change_department(self, sku, new_department):
        """
        This function changes the department of the product specified.
        :param sku: Integer. The SKU of the product.
        :param new_department: String. The new department and must also either be meat, grocery, or produce.
        """
        try:
            self.inventory[sku].department = new_department # This will change the original department to the new department.
        except KeyError: # This will run if the SKU inputted is not found in the dictionary.
            print('SKU not found.')

    def see_all_products(self):
        """
        This function prints every product that is in the inventory dictionary.
        """
        for products in self.inventory:
            print(self.inventory[products])

    def see_a_product(self, sku):
        """
        This function prints the product specified by the user.
        :param sku: Integer. The SKU of the product.
        :return: Information of the product. Includes: name, sku, cost, price, margin, department, and quantity.
        """
        try:
            print(self.inventory[sku]) # This will try to display the items if the SKU exists in the dictionary. If not, the KeyError is caught.
        except KeyError: # This will run if the SKU inputted is not found in the dictionary.
            print('SKU not found.')

    def delete_a_product(self, sku):
        """
        This function will delete the product specified by the user.
        :param sku: Integer. The SKU of the product.
        :return: Success if deletion is successful.
        """
        try:
            del self.sku_dictionary[self.inventory[sku].name.upper()] # Uses the the entered SKU's name to delete itself from the SKU dictionary.
            del self.inventory[sku] # Deletes entry from inventory dictionary.
            print('Success.')
        except KeyError: # This will run if the SKU inputted is not found in the dictionary.
            print('SKU not found.')

    def see_product_margin(self, sku):
        """
        This function will print the margin of the product specified by the user.
        :param sku: Positive integer. The SKU of the product.
        :return: Margin of the product
        """
        try:
            return f'{self.inventory[sku].margin:.2f}%'  # Prints margin of the item.
        except KeyError: # This will run if the SKU inputted is not found in the dictionary.
            print('SKU not found.')





