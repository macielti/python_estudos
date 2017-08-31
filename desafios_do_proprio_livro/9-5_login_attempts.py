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
    
    
 
user1= User('bruno', 'maciel', 18, 'brasil')

user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()

print('Login attempts: '+ str(user1.login_attempts))

user1.reset_login_attempts()

print('Login attempts: '+ str(user1.login_attempts))
