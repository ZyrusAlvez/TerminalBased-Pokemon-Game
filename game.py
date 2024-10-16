from pokemon import Pokemon
from tabulate import tabulate
from termcolor import colored
import random

pokemon1 = Pokemon("Charizard", "fire", health=50, power=80, 
            poison_rate=0.15, poison_description="Charizard Lifesteal 15% of the enemy's current health points",
            potion_rate=0.2, potion_description="Charizard sacrifices 20% of his current health, converting it into a boost of power.")
pokemon2 = Pokemon("Infernow", "fire", health=45, power=85, 
            poison_rate=0.1, poison_description="Infernow Lifesteal 10% of the enemy's current health points",
            potion_rate=0.15, potion_description="Infernow sacrifices 20% of his current health, converting it into a boost of power.")
pokemon3 = Pokemon("Florac", "grass", health=90, power=50,
            poison_rate=0.3, poison_description="Florac Deals 30% damage based on her enemy's health points",
            potion_rate=0.2, potion_description="Florac Restore 20% HP based on the enemy’s current health points")
pokemon4 = Pokemon("Leaforn", "grass", health=110, power=35,
            poison_rate=0.25, poison_description="Leaforn Deals 25% damage based on her enemy's health points",
            potion_rate=0.15, potion_description="Leaforn Restore 15% HP based on the enemy’s current health points")
pokemon5 = Pokemon("Hydron", "water", health=70, power=70,
            poison_rate=0.25, poison_description="Hydron reduce his opponent's current power by 25%",
            potion_rate=0.20, potion_description="Hydron gain an additional 20% of his both current power and health points")
pokemon6 = Pokemon("Torrentis", "water", health=60, power=65,
            poison_rate=0.3, poison_description="Hydron reduce his opponent's current power by 30%",
            potion_rate=0.25, potion_description="Hydron gain an additional 25% of his both current power and health points")

# table showing the pokemons
table_data_pokemon1 = [["Type", pokemon1.type], ["Health", pokemon1.health], ["Power", pokemon1.power], ["Poison Effects", pokemon1.poison_description], ["Potion Effectts", pokemon1.potion_description]]
pokemon1_table = lambda: print(tabulate(table_data_pokemon1, headers=[colored("Stats", attrs=["bold"]), colored(pokemon1.name, "red", attrs=["bold"])], tablefmt="grid", numalign="left"))
table_data_pokemon2 = [["Type", pokemon2.type], ["Health", pokemon2.health], ["Power", pokemon2.power], ["Poison Effects", pokemon2.poison_description], ["Potion Effectts", pokemon2.potion_description]]
pokemon2_table = lambda: print(tabulate(table_data_pokemon2, headers=[colored("Stats", attrs=["bold"]), colored(pokemon2.name, "red", attrs=["bold"])], tablefmt="grid", numalign="left"))
table_data_pokemon3 = [["Type", pokemon3.type], ["Health", pokemon3.health], ["Power", pokemon3.power], ["Poison Effects", pokemon3.poison_description], ["Potion Effectts", pokemon3.potion_description]]
pokemon3_table = lambda: print(tabulate(table_data_pokemon3, headers=[colored("Stats", attrs=["bold"]), colored(pokemon3.name, "green", attrs=["bold"])], tablefmt="grid", numalign="left"))
table_data_pokemon4 = [["Type", pokemon4.type], ["Health", pokemon4.health], ["Power", pokemon4.power], ["Poison Effects", pokemon4.poison_description], ["Potion Effectts", pokemon4.potion_description]]
pokemon4_table = lambda: print(tabulate(table_data_pokemon4, headers=[colored("Stats", attrs=["bold"]), colored(pokemon4.name, "green", attrs=["bold"])], tablefmt="grid", numalign="left"))
table_data_pokemon5 = [["Type", pokemon5.type], ["Health", pokemon5.health], ["Power", pokemon5.power], ["Poison Effects", pokemon5.poison_description], ["Potion Effectts", pokemon5.potion_description]]
pokemon5_table = lambda: print(tabulate(table_data_pokemon5, headers=[colored("Stats", attrs=["bold"]), colored(pokemon5.name, "blue", attrs=["bold"])], tablefmt="grid", numalign="left"))
table_data_pokemon6 = [["Type", pokemon6.type], ["Health", pokemon6.health], ["Power", pokemon6.power], ["Poison Effects", pokemon6.poison_description], ["Potion Effectts", pokemon6.potion_description]]
pokemon6_table = lambda: print(tabulate(table_data_pokemon6, headers=[colored("Stats", attrs=["bold"]), colored(pokemon6.name, "blue", attrs=["bold"])], tablefmt="grid", numalign="left"))


pokemon_list = [pokemon1, pokemon2, pokemon3, pokemon4, pokemon5, pokemon6]
player1 = "Player 1"
player2 = "Player 2"

print("Welcome to Pokemon Spells\n")


player1_pokemon = []
player2_pokemon = []
for i in range(6):
    # shift to player 1 and 2
    player = player1 if i % 2 == 0 else player2
    
    # shows list of pokemon
    for i, pokemon in enumerate(pokemon_list, 1):
        print(f"{i}.", end=" ")
        print(colored(pokemon.name, attrs=["bold"]))
    
    # take input
    while True:
        pick_pokemon = int(input(f"{player} choose your pokemon: "))
        if pick_pokemon in list(range(1, len(pokemon_list) + 1)):
            while True:
                # show the chosen pokemon's data
                if pick_pokemon == 1:
                    pokemon1_table()
                if pick_pokemon == 2:
                    pokemon2_table()
                if pick_pokemon == 3:
                    pokemon3_table()
                if pick_pokemon == 4:
                    pokemon4_table()
                if pick_pokemon == 5:
                    pokemon5_table()
                if pick_pokemon == 6:
                    pokemon6_table()

                # confirmation
                done_confirmation = False
                confirm_pick_pokemon = input(f"\nAre you sure u want to pick {colored(pokemon_list[pick_pokemon-1].name, attrs=['bold'])} (y/n): ").lower()
                if confirm_pick_pokemon in ["y", "n"]:
                    if confirm_pick_pokemon == "y":
                        if i % 2 == 0:
                            player1_pokemon.append(pokemon_list[pick_pokemon-1])
                        else:
                            player2_pokemon.append(pokemon_list[pick_pokemon-1])
                        pokemon_list.remove(pokemon_list[pick_pokemon-1])
                        done_confirmation = True
                        break
                    else:
                        break
                else:
                    print(f"\n{confirm_pick_pokemon} is not a valid keyword\n")
            
            if done_confirmation:
                break
        else:
            print(f"\n{pick_pokemon} is not a valid keyword\n")

# each player initial pokemon that will fight will be random
player1_current_pokemon = player1_pokemon[random.choice(list(range(0, len(player1_pokemon))))]
player2_current_pokemon = player2_pokemon[random.choice(list(range(0, len(player2_pokemon))))]

# first fight random chosen pokemon
print(f"\nGive the device to Player 1\n")
player1_pokemon_action = Pokemon.battle_interface(player1_current_pokemon, player2, player2_current_pokemon)
print(f"\nGive the device to Player 2\n")
player2_pokemon_action = Pokemon.battle_interface(player2_current_pokemon, player1, player1_current_pokemon)
Pokemon.battle(player1_pokemon_action, player1_current_pokemon, player2_pokemon_action, player2_current_pokemon)

while True:
    print(f"\nGive the device to Player 1\n")
    Pokemon.pre_battle_interface(player1, player1_current_pokemon, player2, player2_current_pokemon)
    print(f"\nGive the device to Player 2\n")