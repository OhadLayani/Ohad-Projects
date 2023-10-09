import  random
class bColors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

class Enemy():
    def __init__(self, atk, df, hp, mp, magic, mdef, name,exp):
        self.atkl = atk - 30
        self.atkh = atk + 30
        self.max_hp = hp
        self.hp = hp
        self.df = df
        self.mdef = mdef
        self.max_mp = mp
        self.mp = mp
        self.magic = magic
        self.action = ["Attack", "Magic"]
        self.name = name

        self.exp=exp




    def getexp(self):
        return self.exp
    def getatk(self):
        return self.atk

    def gethp(self):
        return self.hp

    def getdf(self):
        return self.df

    def getmp(self):
        return self.mp
    def get_maxhp(self):
        return self.max_hp
    def getmp(self):
        return self.mp
    def get_maxmp(self):
        return self.max_mp
    def get_mdef(self):
        return self.mdef
    def generate_damage(self):
        return random.randrange(self.atkl,self.atkh)

    def Reduce_mp(self,cost):
      self.mp=self.mp-cost

    def get_BeingName(self):
        return self.name
    def take_damage(self, dmg):
        self.hp = self.hp -(dmg-self.df)
        if (self.hp < 0):
            self.hp = 0
        return self.hp
    def getenemy_stats(self):
        hp_bar = ""
        bar_ticks = (self.hp / self.max_hp) * 100 / 2

        while bar_ticks >= 0:
            hp_bar += "█"
            bar_ticks = bar_ticks - 1
        while len(hp_bar) < 50:
            hp_bar += " "
        hp_string = str(self.hp) + "/" + str(self.max_hp)
        current_hp = ""
        if len(hp_string) < 9:
            decreased = 9 - len(hp_string)
            while decreased > 0:
                current_hp += " "
                decreased -= 1

            current_hp += hp_string
        else:
            current_hp = hp_string

        print("Name            HP                                    ")
        print("                          ___________________________________________________ ")
        print(
            bColors.BOLD + self.name + ":     ", current_hp, " |" + bColors.FAIL + hp_bar +
            bColors.ENDC  + "|")
    @staticmethod
    def generate_random_enemy():
        # Define your enemy options here
        enemies = [
            Enemy(150, 10, 10, 500, ["Firebolt", "LightningBolt"], 10, "Imp", 20),
            Enemy(200, 15, 25, 750, [], 15, "Ogre", 60),
            Enemy(100,5,100,0,[],20,"Skeleton",10),
            Enemy(50,10,300,10,[],15,"Slime",30)
            # Add more enemy options as needed
        ]
        Boss=[Enemy(300,30,5000,1000,["Firebolt","LightningBolt"],10,"BigBoss",200)]
        return random.choice(enemies)
    @staticmethod
    def generate_random_enemy_group(max_enemies):
        # Generate a random group of enemies within the specified limit
        num_enemies = random.randint(1, max_enemies)
        enemy_group = [Enemy.generate_random_enemy() for _ in range(num_enemies)]
        return enemy_group
