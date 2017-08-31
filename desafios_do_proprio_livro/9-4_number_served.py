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

restaurant= Restaurant('Dogão', 'nojeira')

print(restaurant.number_served)

restaurant.set_number_served(12)

print(restaurant.number_served)

restaurant.increment_number_served(23)

print(restaurant.number_served)
