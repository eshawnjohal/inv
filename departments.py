class Departments:
    def __init__(self, department_name):
        department_list = ('MEAT', 'PRODUCE', 'GROCERY')
        if department_name.upper() not in department_list:
            raise ValueError
        else:
            self.department = department_name.upper()

    def __str__(self):
        return self.department