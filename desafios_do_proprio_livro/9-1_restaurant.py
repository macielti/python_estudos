class Restaurant():
    def __init__(self, name, cuisine_type):
        self.name= name
        self.cuisine_type= cuisine_type
    
    
    def describe_restaurant(self):
        print('The '+self.name.title()+' ha a cuisine '+ self.cuisine_type)
    
        
    def open_restarant(self):
        print('The '+self.name.title()+' is open.')

restaurant= Restaurant('Dogão', 'nojeira')

print(restaurant.name)
print(restaurant.cuisine_type)

restaurant.describe_restaurant()
restaurant.open_restarant()
