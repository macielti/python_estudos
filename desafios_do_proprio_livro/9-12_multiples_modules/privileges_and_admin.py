from user import User

class Privileges():
        
    def __init__(self, *privileges):
        self.privileges= privileges
    
    
    def show_privileges(self):
        print('--Privilegios--')
        for privilege in self.privileges:
            print(privilege.title())


class Admin(User):
    def __init__(self, f_name, l_name, age, location):
        super().__init__(f_name, l_name, age, location)
        self.privileges= Privileges()
