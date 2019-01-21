class Departments:
    """
    This class represents the department in which the item is from.
    It only has three departments right now, and has not really been explored.
    In the future, with the implementation of the sell function, I hope to be able to use excel to represent
    the performance, the profits, and sales of each department.
    """
    def __init__(self, department_name):
        department_list = ('MEAT', 'PRODUCE', 'GROCERY') #  Defining the three departments in uppercase.
        if department_name.upper() not in department_list: # Removing case sensitivity by making it uppercase.
            raise ValueError # If the department name does not match, it will raise an error.
        else:
            self.department = department_name.upper() # Sets attribute 'department' as the department name in uppercase.

    def __str__(self):
        """
        This function returns the departments name.
        :return: Attribute 'department' which is the name of the department.
        """
        return self.department