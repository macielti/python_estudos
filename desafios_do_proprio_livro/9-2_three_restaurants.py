class Restaurant():
    def __init__(self, name, cuisine_type):
        self.name= name
        self.cuisine_type= cuisine_type
    
    
    def describe_restaurant(self):
        print('The '+self.name.title()+' ha a cuisine '+ self.cuisine_type)
    
        
    def open_restarant(self):
        print('The '+self.name.title()+' is open.')

restaurant= Restaurant('Dogão', 'nojeira')
restaurant2= Restaurant('Crap Mania', 'open source')
restaurant3= Restaurant('Garagem', 'mecanica')

restaurant.describe_restaurant()
restaurant2.describe_restaurant()
restaurant3.describe_restaurant()
