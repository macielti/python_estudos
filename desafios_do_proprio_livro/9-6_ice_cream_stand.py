class Restaurant():
    def __init__(self, name, cuisine_type):
        self.name= name
        self.cuisine_type= cuisine_type
        self.number_served = 0
    
    def describe_restaurant(self):
        print('The '+self.name.title()+' ha a cuisine '+ self.cuisine_type)
    
        
    def open_restarant(self):
        print('The '+self.name.title()+' is open.')


    def set_number_served(self, number):
        self.number_served= number
    

    def increment_number_served(self, number):
        self.number_served += number


class IceCreamStand(Restaurant):
    
    def __init__(self, name, cursine_type, *flavors):
        super().__init__(name, cursine_type)
        self.flavors= flavors
    
    
    def show_flavors(self):
        print('--Flavors--')
        for sabor in self.flavors:
            print(sabor.title())


juquinha= IceCreamStand('juquinha', 'food-truck', 'sorvete catuaba', 
                        'sorvete caipirinha', 'sorvete vodka', 
                        'sorvete cachaça')

juquinha.show_flavors()
        
    
