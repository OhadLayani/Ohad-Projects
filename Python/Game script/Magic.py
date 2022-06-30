import random
class spell():
    def __init__ (self , name ,cost,dmg,type):
        self.name=name
        self.cost=cost
        self.type=type
        self.dmg=dmg
    def get_Cost(self):
        return self.cost

    def generate_Spelldamage(self):
        low = self.dmg-15
        high = self.dmg+15
        return random.randrange(low, high)