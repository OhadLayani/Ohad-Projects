import  random
class Enemy():
    hp=200
    def __init__(self,atkl,atkh,hp):
        self.atkl=  atkl
        self.atkh=atkh
        self.max_hp=hp
        self.hp=hp
        self.atk=random.randrange(atkl,atkh)
    def getatk(self):
        return self.atk
    def gethp(self):
        return self.hp
