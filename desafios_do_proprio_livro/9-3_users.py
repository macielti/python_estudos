class User():
    def __init__(self, f_name, l_name, age, location):
        self.f_name = f_name
        self.l_name = l_name
        self.age = age
        self.location = location
    

    def describe_user(self):
        print('first name: '.title()+self.f_name)
        print('last name: '.title()+self.l_name)
        print('age: '.title()+str(self.age))
        print('location: '.title()+self.location)
    

    def greet_user(self):
        print('Olá '+self.f_name.title()+' '+self.l_name.title())

user1= User('bruno', 'maciel', 18, 'brasil')
user2= User('bruno', 'cunha', 18, 'brasil')
user3= User('paulo', 'guina', 32, 'brasil')

user1.describe_user()
user1.greet_user()

user2.describe_user()
user2.greet_user()

user3.describe_user()
user3.greet_user()
