from pokemon import Pokemon
from tabulate import tabulate
from termcolor import colored
import time
import os
import random
from animation import Battle_Animation, Pre_Battle_Animation
os.system("cls")
pokemon1 = Pokemon("Charizard", "fire", health=50, power=80, looks="👹")
pokemon2 = Pokemon("Phoenix", "fire", health=45, power=85, looks="🐦")
pokemon3 = Pokemon("Peacock", "grass", health=90, power=50, looks="🦚")
pokemon4 = Pokemon("Caterpie", "grass", health=110, power=35, looks="🐛")
pokemon5 = Pokemon("Wailord", "water", health=70, power=70, looks="🐋")
pokemon6 = Pokemon("Magicarp", "water", health=60, power=65, looks="🐟")


player1 = "Player 1"
player2 = "Player 2"
pokemon_list = [pokemon1, pokemon2, pokemon3, pokemon4, pokemon5, pokemon6]
player1_pokemon = []
player2_pokemon = []

# players will choose pokemon
i = 0
while i < 6:
    # shift to player 1 and 2
    player = player1 if i % 2 == 0 else player2
    
    # shows list of pokemon
    pokemon_data = [[f"{i}", pokemon.name, pokemon.type, pokemon.health, pokemon.power] for i, pokemon in enumerate(pokemon_list, 1)]
    print(tabulate(pokemon_data, headers=[colored("No.", "yellow", attrs=["bold"]), colored("Name", "yellow", attrs=["bold"]), colored("Type", "yellow", attrs=["bold"]), colored("Health", "yellow", attrs=["bold"]), colored("Power", "yellow", attrs=["bold"])], tablefmt="github", numalign="center"))
        
    # take input
    pick_pokemon = input(f"\n{player} choose your pokemon: ")
    os.system("cls")
    if pick_pokemon == "test":
        player1_pokemon = [pokemon1, pokemon3, pokemon5]
        player2_pokemon = [pokemon2, pokemon4, pokemon6]
        os.system("cls")
        break
    
    if pick_pokemon.isdigit():
        pick_pokemon = int(pick_pokemon) - 1    
        if pick_pokemon in list(range(len(pokemon_list))):
            if i % 2 == 0:
                player1_pokemon.append(pokemon_list[pick_pokemon])
            else:
                player2_pokemon.append(pokemon_list[pick_pokemon])
            pokemon_list.pop(pick_pokemon)
            i += 1
        else:
            print(f"Your input must be in 1-{len(pokemon_list)}\n")
    else:
        print(f"{colored(pick_pokemon, 'yellow', attrs=['underline'])} is not a valid keyword\n")

# Game
player1_use_potion = False
player1_use_poison = False
player2_use_potion = False
player2_use_poison = False
while True:
    battle_stats = Pre_Battle_Animation(player1_pokemon, player2_pokemon)
    battle_stats.randomizer_animation()

    player1_temporary_buff = False
    player2_temporary_buff = False

    if battle_stats.battlefield == colored("Waterfall Arena", "blue", attrs=["bold"]) and battle_stats.player1_pokemon.type == "water":
        battle_stats.player1_buff(10)
        player1_temporary_buff = True
    if battle_stats.battlefield == colored("Volcanic Field", "red", attrs=["bold"]) and battle_stats.player1_pokemon.type == "fire":
        battle_stats.player1_buff(10)
        player1_temporary_buff = True
    if battle_stats.battlefield == colored("Green Land", "green", attrs=["bold"]) and battle_stats.player1_pokemon.type == "grass":
        battle_stats.player1_buff(10)
        player1_temporary_buff = True
    if battle_stats.battlefield == colored("Waterfall Arena", "blue", attrs=["bold"]) and battle_stats.player2_pokemon.type == "water":
        battle_stats.player2_buff(10)
        player2_temporary_buff = True
    if battle_stats.battlefield == colored("Volcanic Field", "red", attrs=["bold"]) and battle_stats.player2_pokemon.type == "fire":
        battle_stats.player2_buff(10)
        player2_temporary_buff = True
    if battle_stats.battlefield == colored("Green Land", "green", attrs=["bold"]) and battle_stats.player2_pokemon.type == "grass":
        battle_stats.player2_buff(10)
        player2_temporary_buff = True

    def pre_battle_interface(player_name: str, player_pokemon: object):
        while True:
            print("1. Fight")
            print("2. Pokemon")
            print("3. Record")
            print("4. Run")
            choice = input(f"What will {player_name} do? ")
            if choice.isdigit():
                choice = int(choice)
                if choice in list(range(1, 5)):
                    os.system("cls")
                    battle_stats.last_frame()
                    if choice == 1:
                        print(f"\nYou randomly sent {player_pokemon.name}\n")
                        while True:   
                            print("1. Attack")
                            print("2. Poison Spell")
                            print("3. Potion Spell")
                            player_action = input(f"{player_pokemon.name} will use: ")
                            if player_action.isdigit():
                                player_action = int(player_action)
                                if player_action in list(range(1, 4)): 
                                    return player_action
                                else:
                                    os.system("cls")
                                    battle_stats.last_frame()
                                    print(f"Your input must be in 1-3\n")
                            else:
                                os.system("cls")
                                battle_stats.last_frame()
                                print(f"{colored(player_action, 'yellow', attrs=['underline'])} was not a valid keyword\n")
                    if choice == 2:
                        pass
                    if choice == 3:
                        pass
                    if choice == 4:
                        pass
                else:
                    os.system("cls")
                    battle_stats.last_frame()
                    print(f"Your input must be in 1-4\n")
            else:
                os.system("cls")
                battle_stats.last_frame()
                print(f"{colored(choice, 'yellow', attrs=['underline'])} was not a valid keyword\n")

    player1_action = pre_battle_interface(player1, battle_stats.player1_pokemon)  
    battle_stats.player1_ready = True
    os.system("cls")
    battle_stats.last_frame()
    player2_action = pre_battle_interface(player2, battle_stats.player2_pokemon)
    battle_stats.player2_ready = True
    os.system("cls")
    battle_stats.last_frame()
    time.sleep(1)
    battle = Battle_Animation(battle_stats.player1_pokemon, battle_stats.player2_pokemon, battle_stats.battlefield)
    if battle_stats.player1_pokemon.power > battle_stats.player2_pokemon.power:
        battle.player1_won()
        battle_stats.player1_health_increase(5)
        battle_stats.player2_health_decrease(10)
        battle_stats.fatigue(2)
    elif battle_stats.player1_pokemon.power < battle_stats.player2_pokemon.power:
        battle.player2_won()
        battle_stats.player2_health_increase(5)
        battle_stats.player1_health_decrease(10)
        battle_stats.fatigue(2)
    else:
        battle.tie()
        battle_stats.fatigue(2)
    battle.reset()
    if player1_temporary_buff:
        battle.player1_pokemon.power -= 10
    if player2_temporary_buff:
        battle.player2_pokemon.power -= 10