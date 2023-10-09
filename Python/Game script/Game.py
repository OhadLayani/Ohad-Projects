import random
from Magic import spell
class bColors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

class Person:
    def __init__(self, atk, df, hp, mp, magic, mdef, name, items, job):
        self.atk=atk
        self.atkl = atk - 30
        self.atkh = atk + 30
        self.max_hp = hp
        self.hp = hp
        self.df = df
        self.mdef = mdef
        self.max_mp = mp
        self.mp = mp
        self.magic = magic
        self.action = ["Attack", "Magic", "Items"]
        self.name = name
        self.items = items
        self.job = job  # Assign the job object to the person
        self.lvl = 1
        self.exp = 0
        self.exp_to_lvl = self.lvl * 100

    def getlvl(self):
        return self.lvl

    def getCurrentexp(self):
        return self.exp

    def getexpRem(self):
        return self.exp_to_lvl

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
    def choose_actions(self):
        i=1
        print("\n"+"    "+bColors.BOLD+self.name+bColors.ENDC)
        print(bColors.OKBLUE+"    Actions"+bColors.ENDC)
        for item in self.action:
            print("    "+str(i) + ":" ,item)
            i=i+1
    def choose_magic(self):
        i=1
        print(bColors.OKBLUE+"Magic"+bColors.ENDC)
        print("0 : Back""\n")
        for spell in self.magic:
            print ("   "+str(i) + ":", spell.name,"( Cost: ",str(spell.cost)+")"+"\n")
            i+=1

    def take_damage(self, dmg):
        self.hp = self.hp -(dmg-self.df)
        if (self.hp < 0):
            self.hp = 0
        return self.hp
    def Heal_player(self,dmg):
        self.hp=self.hp+dmg
        if(self.hp>self.max_hp):
            self.hp=self.max_hp
        return self.hp
    def choose_items(self):
        i=1
        print(bColors.OKGREEN+"Items"+bColors.ENDC)
        print("0 : Back""\n")
        for item in self.items:
            if(item["type"]=="Consumable"or item["type"]=="Attack"):
                print("    "+str(i)+":",item["Item"].name,": \n",item["Item"].description,"(x"+str(item["Quantity"])+")"+"\n")
                i+=1

    def choose_targets(self,foes):
        i=1
        print(bColors.FAIL+"Target:"+bColors.ENDC)

        for enemy in foes:
            if enemy.gethp()!=0:
                print("         "+str(i)+": ",enemy.name)
                i+=1
        choice=int(input("Choose  target :"))-1
        return choice



    def get_stats(self):
        hp_bar=""
        bar_ticks=(self.hp/self.max_hp)*100/4
        mp_bar = ""
        mpbar_ticks = (self.mp / self.max_mp) * 100 /10

        #governs health point bar change
        while bar_ticks>=0:
           hp_bar+="█"
           bar_ticks=bar_ticks-1
        while len(hp_bar) < 25:
            hp_bar+= " "
        #governs mana point bar change
        while mpbar_ticks >= 0:
            mp_bar += "█"
            mpbar_ticks = mpbar_ticks - 1
        while len(mp_bar) < 10:
            mp_bar += " "
        hp_string=str(self.hp)+"/"+str(self.max_hp)
        current_hp=""
        if len(hp_string)<9:
            decreased=9-len(hp_string)
            while decreased>0:
                current_hp +=" "
                decreased-=1

            current_hp+=hp_string
        else:
            current_hp=hp_string

        mp_string=str(self.mp)+"/"+str(self.max_mp)
        current_mp=""
        if len(mp_string) < 7:
            mpdecreased = 7 - len(mp_string)
            while mpdecreased > 0:
                current_mp += " "
                mpdecreased -= 1

            current_mp += mp_string
        else:
            current_mp = mp_string

        print("Name            HP                                    MP")
        print("                           _________________________                  __________ ")
        print(
            bColors.BOLD + self.name+":     " ,current_hp, " |" + bColors.OKGREEN + hp_bar +
            bColors.ENDC + bColors.OKBLUE + "|    " ,current_mp, " |" + mp_bar + bColors.ENDC + "|")


    def levelup(self):
     self.max_hp = self.max_hp+self.job.hp
     self.mp= self.mp+self.job.mp
     self.df = self.df+self.job.df
     self.mdef = self.mdef+self.job.mdef
     self.atk=self.atk+self.job.atk
     self.exp -= self.lvl*100
     self.lvl=self.lvl+1
     self.exp_to_lvl = self.lvl * 100

     print("Level Up!   Your stats have been updated:")
     print (f"Name: {self.name}"+"\n")
     print (f"Level: {self.lvl}"+"\n")
     print(f"Max HP: {self.max_hp} "+"\n")
     print(f"MP: {self.mp}"+"\n")
     print(f"Defense: {self.df}"+"\n")
     print(f"Magic Defense: {self.mdef}"+"\n")
     print(f"Attack: {self.atk}"+"\n")


class job():
    def __init__(self,name, atk, df, hp,mp,mdef):
        self.name=name
        self.atk=atk
        self.mp = mp
        self.hp = hp
        self.df = df
        self.mdef = mdef

