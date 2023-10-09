from GameScript.Game import Person,job,bColors
from GameScript.Magic import spell
import Attack
from GameScript.inventory import item
from GameScript.Enemy import Enemy
import MenuLogic
def main():
    print("\n\n")


    #Attack spells
    Firebolt=spell("Firebolt",40,90,"Black Magic")
    Iceshard=spell("IceShard",20,50,"Black Magic")
    LightningBolt=spell("Lightningbolt",70,140,"Black Magic")
    Meteor=spell("Meteor",300,500,"Black Magic")

    #White magic
    CureWounds=spell("Cure wounds",40,80,"Healing")
    Heal=spell("Heal",150,300,"Healing")

    # some items
    Potion = item("Potion", "Consumable", "A mass produced  bottle with clear red liquid inside, Heals for 50 Hp", 50)
    hiPotion = item("HiPotion", "Consumable", "An ornate bottle filled with bubbling crimson liquid , Heals for 200 Hp",
                    400)
    Elixir = item("Elixir", "Elixir",
                  "A Rare commodity highly sought after by adventurers and healers alike,Fully restores health and mana",
                  9999)
    HiElixir = item("HiElixir", "Elixir",
                    "Legends tell of this miraculous cure,Fully restores health and mana for all party", 9999)

    Grenade = item("Grenade", "Attack", "A new device made to destroy foes, damage foes for 500 points", 500)
    IronArmour = item("Iron armor", "Epuipment",
                      "A simple iron plate,the mainstay of armies, increase defense by 10 points", 10)


    Player_items=[{"Item":Potion,"Quantity":15,"type":"Consumable"},{"Item":hiPotion,"Quantity":5,"type":"Consumable"},{"Item":Elixir,"Quantity":3,"type":"Consumable"}
        ,{"Item":HiElixir,"Quantity":1,"type":"Consumable"} ,{"Item":Grenade,"Quantity":3,"type":"Attack"},{"Item":IronArmour,"Quantity":1,"type":"Epuipment"}]
    Player_magic=[Firebolt,Iceshard,LightningBolt,Meteor,CureWounds,Heal]

    Class1=job("Summoner",2,3,5,8,5)
    Class2=job("Cleric",4,5,3,6,5)
    Class3=job("Occultist",6,4,4,2,3)
    Class4=job("Witch",1,2,4,10,9)


    player1=Person(120,80,700,400,Player_magic,80,"Denzured",Player_items,Class1)
    player2=Person(200,130,1200,600,Player_magic,80,"Sigrid ",Player_items,Class2)
    player3=Person(180,150,1500,200,Player_magic,80,"Khair   ",Player_items,Class3)
    player4=Person(90,100,800,600,Player_magic,80,"Roni    ",Player_items,Class4)
    party=[player1,player2,player3,player4]



    #Henchman1=Enemy(150,10,10,500,[Firebolt,LightningBolt],10,"Imp",20)
    #Henchman2=Enemy(150,10,10,500,[Firebolt,LightningBolt],10,"Imp",20)
    #MiniBoss=Enemy(200,15,25,750,[],15,"Ogre",60)
   # Foes=[MiniBoss,Henchman1,Henchman2]





    MenuLogic.MenuPrint(party)


if __name__ == "__main__":
    main()