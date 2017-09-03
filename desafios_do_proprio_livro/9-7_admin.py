class User():
    def __init__(self, f_name, l_name, age, location):
        self.f_name = f_name
        self.l_name = l_name
        self.age = age
        self.location = location
        self.login_attempts= 0
    

    def describe_user(self):
        print('first name: '.title()+self.f_name)
        print('last name: '.title()+self.l_name)
        print('age: '.title()+str(self.age))
        print('location: '.title()+self.location)
    

    def greet_user(self):
        print('Olá '+self.f_name.title()+' '+self.l_name.title())

    def increment_login_attempts(self):
        self.login_attempts+= 1
    

    def reset_login_attempts(self):
        self.login_attempts= 0


class Admin(User):
    def __init__(self, f_name, l_name, age, location, *privilegios):
        super().__init__(f_name, l_name, age, location)
        self.privilegios= privilegios
    
    
    def show_privileges(self):
        print('--Privilegios--')
        for privilege in self.privilegios:
            print(privilege.title())


bruno= Admin('bruno', 'do nascimento maciel', 18, 'brasil',
            'adicionar usuários', 'ver senhas', 'ver emails', 
            'excluir usuarios', 'alterar atributos')

bruno.show_privileges()
