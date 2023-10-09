from GameScript.Game import Person,job,bColors
from GameScript.Magic import spell
import Attack
from GameScript.inventory import item
from GameScript.Enemy import Enemy


def display_menu():
    print("Menu:")
    print("1. Player Stats")
    print("2. Inventory")
    print("3. Explore")
    print("4. Save")
    print("5. Quit")

def MenuPrint(party):
    running = True


    while running:
            display_menu()
            choice = input("Enter your choice: "+ "\n")

            if choice == "1":
                print("Displaying Player Stats..."+ "\n")

                for index, player in enumerate(party):
                    print(f"{index + 1}. Name: {player.name}")

                # Get user input for choosing a character
                while True:
                    try:
                        menu_player_choice = int(input("Choose a character to display (1 to {}): ".format(len(party))))
                        if 1 <= menu_player_choice <= len(party):
                            chosen_player = party[menu_player_choice - 1]
                            getChosen_playerstats(chosen_player)
                            break
                        else:
                            print("Invalid choice. Please enter a number between 1 and {}.".format(len(party)))
                    except ValueError:
                        print("Invalid input. Please enter a valid number.")


                # Code for displaying player stats goes here
            elif choice == "2":
                print("Displaying Inventory..."+ "\n")
                # Code for displaying inventory goes here
            elif choice == "3":
                max_enemies_in_encounter = 5  # Set your maximum number of enemies in an encounter
                random_enemy_group = Enemy.generate_random_enemy_group(max_enemies_in_encounter)
                print("Exploring..."+ "\n")
                Attack.combat(party, random_enemy_group)

                # Code for exploring goes here
            elif choice == "4":
                print("Saving..."+ "\n")
                # Code for saving goes here
            elif choice == "5":
                print("Quitting the game. Goodbye!"+ "\n")
                running=False;
                break
            else:
                print("Invalid choice. Please try again."+ "\n")

#print chosen player status
def getChosen_playerstats(player):
    player.get_stats()
    print(f" Defense: {player.df}" + "\n")
    print(f" Magic Defense: {player.mdef}" + "\n")
    print(f" Attack: {player.atk}" + "\n")
    print(f" Class: {player.job.name}" + "\n")
    print(f" Level : {player.lvl}" + "\n")
    print(f" Exp : {player.exp}" + "\n")
    print(f" Exp to level up: {player.exp_to_lvl}" + "\n")
