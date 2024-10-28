from pokemon import Pokemon
from tabulate import tabulate
from termcolor import colored
import time
import os
import random
from animation import Battle_Animation, Pre_Battle_Animation
os.system("cls")
pokemon1 = Pokemon("Charizard", "fire", health=50, power=80, looks="👹",
            poison_rate=0.15, poison_description="Charizard Lifesteal 15% of the enemy's current health points",
            potion_rate=0.2, potion_description="Charizard sacrifices 20% of his current health, converting it into a boost of power.")
pokemon2 = Pokemon("Phoenix", "fire", health=45, power=85, looks="🐦",
            poison_rate=0.1, poison_description="Phoenix Lifesteal 10% of the enemy's current health points",
            potion_rate=0.15, potion_description="Phoenix sacrifices 20% of his current health, converting it into a boost of power.")
pokemon3 = Pokemon("Peacock", "grass", health=90, power=50, looks="🦚",
            poison_rate=0.3, poison_description="Peacock Deals 30% damage based on her enemy's health points",
            potion_rate=0.2, potion_description="Peacock Restore 20% HP based on the enemy’s current health points")
pokemon4 = Pokemon("Caterpie", "grass", health=110, power=35, looks="🐛",
            poison_rate=0.25, poison_description="Caterpie Deals 25% damage based on her enemy's health points",
            potion_rate=0.15, potion_description="Caterpie Restore 15% HP based on the enemy’s current health points")
pokemon5 = Pokemon("Wailord", "water", health=70, power=70, looks="🐋",
            poison_rate=0.25, poison_description="Wailord reduce his opponent's current power by 25%",
            potion_rate=0.20, potion_description="Wailord gain an additional 20% of his both current power and health points")
pokemon6 = Pokemon("Magicarp", "water", health=60, power=65, looks="🐟",
            poison_rate=0.3, poison_description="Magicarp reduce his opponent's current power by 30%",
            potion_rate=0.25, potion_description="Magicarp gain an additional 25% of his both current power and health points")

# table showing the pokemons
table_data_pokemon1 = [["Type", pokemon1.type], ["Health", pokemon1.health], ["Power", pokemon1.power], ["Poison Effects", pokemon1.poison_description], ["Potion Effectts", pokemon1.potion_description]]
pokemon1_table = lambda: print(tabulate(table_data_pokemon1, headers=[colored("Stats", attrs=["bold"]), f"{pokemon1.looks} {pokemon1.name}"], tablefmt="grid", numalign="left"))
table_data_pokemon2 = [["Type", pokemon2.type], ["Health", pokemon2.health], ["Power", pokemon2.power], ["Poison Effects", pokemon2.poison_description], ["Potion Effectts", pokemon2.potion_description]]
pokemon2_table = lambda: print(tabulate(table_data_pokemon2, headers=[colored("Stats", attrs=["bold"]), f"{pokemon2.looks} {pokemon2.name}"], tablefmt="grid", numalign="left"))
table_data_pokemon3 = [["Type", pokemon3.type], ["Health", pokemon3.health], ["Power", pokemon3.power], ["Poison Effects", pokemon3.poison_description], ["Potion Effectts", pokemon3.potion_description]]
pokemon3_table = lambda: print(tabulate(table_data_pokemon3, headers=[colored("Stats", attrs=["bold"]), f"{pokemon3.looks} {pokemon3.name}"], tablefmt="grid", numalign="left"))
table_data_pokemon4 = [["Type", pokemon4.type], ["Health", pokemon4.health], ["Power", pokemon4.power], ["Poison Effects", pokemon4.poison_description], ["Potion Effectts", pokemon4.potion_description]]
pokemon4_table = lambda: print(tabulate(table_data_pokemon4, headers=[colored("Stats", attrs=["bold"]), f"{pokemon4.looks} {pokemon4.name}"], tablefmt="grid", numalign="left"))
table_data_pokemon5 = [["Type", pokemon5.type], ["Health", pokemon5.health], ["Power", pokemon5.power], ["Poison Effects", pokemon5.poison_description], ["Potion Effectts", pokemon5.potion_description]]
pokemon5_table = lambda: print(tabulate(table_data_pokemon5, headers=[colored("Stats", attrs=["bold"]), f"{pokemon5.looks} {pokemon5.name}"], tablefmt="grid", numalign="left"))
table_data_pokemon6 = [["Type", pokemon6.type], ["Health", pokemon6.health], ["Power", pokemon6.power], ["Poison Effects", pokemon6.poison_description], ["Potion Effectts", pokemon6.potion_description]]
pokemon6_table = lambda: print(tabulate(table_data_pokemon6, headers=[colored("Stats", attrs=["bold"]), f"{pokemon6.looks} {pokemon6.name}"], tablefmt="grid", numalign="left"))


pokemon_list = [pokemon1, pokemon2, pokemon3, pokemon4, pokemon5, pokemon6]
player1 = "Player 1"
player2 = "Player 2"

player1_pokemon = []
player2_pokemon = []


# players will choose pokemon
i = 0
while i < 6:
    # shift to player 1 and 2
    player = player1 if i % 2 == 0 else player2
    
    # shows list of pokemon
    for j, pokemon in enumerate(pokemon_list, 1):
        print(f"{j}. {pokemon.looks} {pokemon.name}")
        
    # take input
    pick_pokemon = input(f"\n{player} choose your pokemon: ")
    
    if pick_pokemon == "test":
        player1_pokemon = [pokemon1, pokemon3, pokemon5]
        player2_pokemon = [pokemon2, pokemon4, pokemon6]
        os.system("cls")
        break
    
    if pick_pokemon.isnumeric():
        pick_pokemon = int(pick_pokemon) - 1    
        if pick_pokemon in list(range(len(pokemon_list))):
            os.system("cls")
            while True:
                # show the chosen pokemon's data
                if pokemon_list[pick_pokemon].name == pokemon1.name:
                    pokemon1_table()
                if pokemon_list[pick_pokemon].name == pokemon2.name:
                    pokemon2_table()
                if pokemon_list[pick_pokemon].name == pokemon3.name:
                    pokemon3_table()
                if pokemon_list[pick_pokemon].name == pokemon4.name:
                    pokemon4_table()
                if pokemon_list[pick_pokemon].name == pokemon5.name:
                    pokemon5_table()
                if pokemon_list[pick_pokemon].name == pokemon6.name:
                    pokemon6_table()

                confirm_pick_pokemon = input(f"\nAre you sure u want to pick {pokemon_list[pick_pokemon].looks} {pokemon_list[pick_pokemon].name} (y/n): ").lower()
                if confirm_pick_pokemon in ["y", "n"]:
                    os.system("cls")
                    if confirm_pick_pokemon == "y":
                        if i % 2 == 0:
                            player1_pokemon.append(pokemon_list[pick_pokemon])
                        else:
                            player2_pokemon.append(pokemon_list[pick_pokemon])
                        pokemon_list.pop(pick_pokemon)
                        i += 1
                        break
                    else:
                        break
                else:
                    print(f"\n{confirm_pick_pokemon} is not a valid keyword\n")
        else:
            os.system("cls")
            print(f"Your input must be in 1-{len(pokemon_list)}\n")
    else:
        os.system("cls")
        print(f"{pick_pokemon} is not a valid keyword\n")

# Game
pre_battle = Pre_Battle_Animation(player1_pokemon, player2_pokemon)
pre_battle.randomizer_animation()

player1_temporary_buff = False
player2_temporary_buff = False

if pre_battle.battlefield == colored("Waterfall Arena", "blue", attrs=["bold"]) and pre_battle.player1_pokemon.type == "water":
    pre_battle.player1_buff(10)
    player1_temporary_buff = True
if pre_battle.battlefield == colored("Volcanic Field", "red", attrs=["bold"]) and pre_battle.player1_pokemon.type == "fire":
    pre_battle.player1_buff(10)
    player1_temporary_buff = True
if pre_battle.battlefield == colored("Green Land", "green", attrs=["bold"]) and pre_battle.player1_pokemon.type == "grass":
    pre_battle.player1_buff(10)
    player1_temporary_buff = True
if pre_battle.battlefield == colored("Waterfall Arena", "blue", attrs=["bold"]) and pre_battle.player2_pokemon.type == "water":
    pre_battle.player2_buff(10)
    player2_temporary_buff = True
if pre_battle.battlefield == colored("Volcanic Field", "red", attrs=["bold"]) and pre_battle.player2_pokemon.type == "fire":
    pre_battle.player2_buff(10)
    player2_temporary_buff = True
if pre_battle.battlefield == colored("Green Land", "green", attrs=["bold"]) and pre_battle.player2_pokemon.type == "grass":
    pre_battle.player2_buff(10)
    player2_temporary_buff = True
    

def pre_battle_interface(player_name: str, player_pokemon: object):
    while True:
        print("1. Fight")
        print("2. Pokemon")
        print("3. Record")
        print("4. Run")
        choice = int(input(f"What will {player_name} do? "))
        if choice in list(range(1, 5)):
            os.system("cls")
            pre_battle.last_frame()
            if choice == 1:
                print(f"\nYou randomly sent {player_pokemon.name}\n")
                while True:   
                    print("1. Attack")
                    print("2. Poison Spell")
                    print("3. Potion Spell")
                    player_action = int(input(f"{player_pokemon.name} will use: "))
                    if player_action in list(range(1, 4)): 
                        return player_action
                    else:
                        print(f"{player_action} was not a valid keyword\n")
            if choice == 2:
                pass
            if choice == 3:
                pass
            if choice == 4:
                pass
        else:
            print(f"{choice} was not a valid keyword\n")

while True:
    player1_action = pre_battle_interface(player1, pre_battle.player1_pokemon)  
    pre_battle.player1_ready = True 
    os.system("cls")
    pre_battle.last_frame()
    player2_action = pre_battle_interface(player2, pre_battle.player2_pokemon)
    pre_battle.player2_ready = True
    os.system("cls")
    pre_battle.last_frame()
    time.sleep(1)

    battle = Battle_Animation(pre_battle.player1_pokemon, pre_battle.player2_pokemon, pre_battle.battlefield)
    if pre_battle.player1_pokemon.power > pre_battle.player2_pokemon.power:
        battle.player1_won()
    elif pre_battle.player1_pokemon.power < pre_battle.player2_pokemon.power:
        battle.player2_won()
    else:
        battle.tie()