'''
Program : battlescript prototype
todo:add an instanced randomised number of foes on trigger
randomising enemy stats
battle script logic

'''


from GameScript.Game import Person,job,bColors
from GameScript.Magic import spell
from GameScript.Enemy import Enemy

import random

exp_defeated = 0


def combat(party,Foes):
    running=True
    i=0

    while running:
        Defeated_enemies=0

        print("================================")
        print(bColors.FAIL+bColors.BOLD+"AN ENEMY ATTACKS!"+bColors.ENDC)

        for enemy in Foes:
            print(str(enemy.get_BeingName()),
              " HP :" + bColors.FAIL + str(enemy.gethp()) + "/" + str(enemy.get_maxhp())+"\n" + bColors.ENDC)
        for player in party:
          player.get_stats()
        for enemy in Foes:
            enemy.getenemy_stats()
        for player in party:
            if len(Foes) == 0:
                break
            playerchoice=False
            while playerchoice==False:
                player.choose_actions()
                choice = input(" Quickly choose your action!")
                print("You have chosen : ",choice)
                index=int(choice)-1
                if index==0:#Attack logic
                     dmg =player.generate_damage()
                     enemy=player.choose_targets(Foes)
                     Foes[enemy].take_damage(dmg)
                     playerchoice = True

                     print(player.name+" hurt the "+Foes[enemy].name + " for :",dmg-Foes[enemy].getdf() ,"Points of damage ", "Enemy Remaining hp is :",Foes[enemy].gethp())
                     if check_enemy_defeat(Foes, party):
                         running = False
                         break

                elif index==1:#magic logic
                    player.choose_magic()

                    magicChoice=int(input("Please choose which spell to use"))-1

                    spell=player.magic[magicChoice]
                    magicdmg=spell.generate_Spelldamage()
                    cost=spell.cost

                    if (magicChoice == -1):
                        continue
                    if cost>player.getmp():
                        print(bColors.FAIL+"Spell used failed , not enough mp"+bColors.ENDC)
                        continue
                    player.Reduce_mp(cost)
                    if spell.type=="Healing":
                        player.Heal_player(magicdmg)
                        print(bColors.OKBLUE+ spell.name, "  Healed for :", magicdmg,
                              "points of damage "
                             +bColors.ENDC)
                        playerchoice = True

                    elif spell.type == "Black Magic":
                        enemy = player.choose_targets(Foes)
                        Foes[enemy].take_damage(magicdmg)
                        print(bColors.OKBLUE+spell.name," Deals :", magicdmg - Foes[enemy].get_mdef(), "Points of damage "+bColors.ENDC )
                        playerchoice = True
                        if check_enemy_defeat(Foes, party):
                            running = False
                            break

                elif index==2:#using inventory
                    player.choose_items()
                    ItemChoice=int(input("Please choose your item"))-1
                    Item=player.items[ItemChoice]["Item"]
                    if (player.items[ItemChoice]["Quantity"] == 0):
                        print(bColors.FAIL + "\n" + "Error! " + "Run out of item" + bColors.ENDC)
                        continue
                    player.items[ItemChoice]["Quantity"]-=1;
                    playerchoice = True

                    if(Item=="Consumable"):
                        player.Heal_player(Item.prop)
                        print(bColors.OKBLUE + Item.name, "  Healed for :", Item.prop,
                              "points of damage "
                              + bColors.ENDC)
                        playerchoice = True
                    elif(Item=="Attack"):
                        
                        enemy = player.choose_targets(Foes)
                        Foes[enemy].take_damage(Item.prop)
                        print(bColors.OKBLUE+Item.name," Deals :", Item.prop- Foes[enemy].getdf(), "Points of damage "+bColors.ENDC )
                        playerchoice = True
                        if check_enemy_defeat(Foes, party):
                            running = False
                            break

                    elif(Item=="Elixir"):
                        if Item.name=="HiElixir":
                            for player in party:
                                player.hp = player.max_hp
                                player.mp = player.max_mp
                        else:
                            player.hp=player.max_hp
                            player.mp=player.max_mp
                        playerchoice = True
                    if(ItemChoice==-1):
                        continue
                else:
                    print("Invalid choice. Please try again.")
        for enemy in Foes:
            if len(Foes) == 0:
                break
            enemy_choice=1
            enemydmg=enemy.generate_damage()
            target= random.randrange(0, 3)

            party[target].take_damage(enemydmg)
            print(enemy.name +" attacks " +party[target].name +"for :",enemydmg-party[target].getdf(), "Points of damage ", party[target].name+"Remaining hp is :", party[target].gethp())

            print("---------------------------------------------------------")
            print(str(enemy.get_BeingName())," HP :"+bColors.FAIL + str(enemy.gethp())+"/"+ str(enemy.get_maxhp())+bColors.ENDC)
        for player in party:
            player.get_stats()



        Defeated_players= 0
        for player in party:
            if player.gethp() == 0:
                Defeated_players+=1
        if Defeated_players==len(party):
            print(bColors.FAIL + "You have Died!!" + bColors.ENDC)
            running = False

def check_enemy_defeat(Foes, party):
        global exp_defeated

        defeated_indices = []

        for index, enemy in enumerate(Foes):
            if enemy.gethp() <= 0:
                defeated_indices.append(index)
                exp_defeated += Foes[index].getexp()

        for index in defeated_indices[::-1]:
            print(Foes[index].name + " has died!")
            del Foes[index]

        if len(Foes) == 0:
            print( exp_defeated)
            print(bColors.OKGREEN + "Congratulations, you have won!" + bColors.ENDC)
            # Assuming 'party' and 'Foes' are lists of player and enemy objects respectively
            for player in party:
                player.exp +=  exp_defeated   # Add enemy's exp to player's exp
                print(player.exp)

            # Assuming 'getCurrentexp' is a method to get current experience and 'getexpRem' is a method to get remaining experience
                if player.getCurrentexp() >= player.getexpRem():
                     player.levelup()
                     player.get_stats()

            return True  # All enemies are defeated, return True to indicate victory

        return False    # Enemies still remain, return False to continue the battle