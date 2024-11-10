from pokemon import Pokemon
from tabulate import tabulate
from termcolor import colored
from utility import clean
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
pokemon_table_header = [colored("No.", "yellow", attrs=["bold"]), colored("Name", "yellow", attrs=["bold"]), colored("Type", "yellow", attrs=["bold"]), colored("Health", "yellow", attrs=["bold"]), colored("Power", "yellow", attrs=["bold"])]
# players will choose pokemon
i = 0
while i < 6:
    # shift to player 1 and 2
    player = player1 if i % 2 == 0 else player2
    
    # shows list of pokemon
    pokemon_data = [[f"{i}", pokemon.name, pokemon.type, pokemon.health, pokemon.power] for i, pokemon in enumerate(pokemon_list, 1)]
    print(tabulate(pokemon_data, headers=pokemon_table_header, tablefmt="github", numalign="center"))
        
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
player1_used_pokemons = []
player2_used_pokemons = []
history = []
i = 0
while True:
    round_history = []
    battle_stats = Pre_Battle_Animation(player1_pokemon, player2_pokemon)
    battle_stats.randomizer_animation()
    {colored(player1, 'yellow', attrs=['bold'])}
    if clean(battle_stats.player1_pokemon.name) not in player1_used_pokemons:
        player1_used_pokemons.append(clean(battle_stats.player1_pokemon.name))
    if clean(battle_stats.player2_pokemon.name) not in player2_used_pokemons:
        player2_used_pokemons.append(clean(battle_stats.player2_pokemon.name))
    round_history.append(battle_stats.round)
    round_history.append(f"Player 1's {battle_stats.player1_pokemon.name} vs Player's 2 {battle_stats.player2_pokemon.name}")
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
            choice = input(f"What will {colored(player_name, 'yellow', attrs=['bold'])} do? ")
            if choice.isdigit():
                choice = int(choice)
                if choice in list(range(1, 5)):
                    os.system("cls")
                    battle_stats.last_frame()
                    if choice == 1:
                        while True:   
                            print("\n1. Attack")
                            print("2. Poison Spell (Deals 50% of Enemy Pokemon's current health)")
                            print("3. Potion Spell (Restore your Pokemon's initial health)")
                            player_action = input(f"{player_pokemon.name} will use: ")
                            if player_action.isdigit():
                                player_action = int(player_action)
                                if player_action in list(range(1, 4)):
                                    if player_name == player1 and player1_use_poison and player_action == 2:
                                        os.system("cls")
                                        battle_stats.last_frame()
                                        print(f"\n{colored(player1, 'yellow', attrs=['bold'])} poison is already used")
                                        continue
                                    if player_name == player2 and player2_use_poison and player_action == 2:
                                        os.system("cls")
                                        battle_stats.last_frame()
                                        print(f"\n{colored(player2, 'yellow', attrs=['bold'])} poison is already used")
                                        continue
                                    if player_name == player1 and player1_use_potion and player_action == 3:
                                        os.system("cls")
                                        battle_stats.last_frame()
                                        print(f"\n{colored(player1, 'yellow', attrs=['bold'])} potion is already used")
                                        continue
                                    if player_name == player2 and player2_use_potion and player_action == 3:
                                        os.system("cls")
                                        battle_stats.last_frame()
                                        print(f"\n{colored(player2, 'yellow', attrs=['bold'])} potion is already used")
                                        continue
                                    
                                    # If there is no error input, proceed to animation part
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
                        pokemon_data_player1 = [[f"{i}", pokemon.name, pokemon.type, pokemon.health, pokemon.power] for i, pokemon in enumerate(player1_pokemon, 1)]
                        pokemon_data_player2 = [[f"{i}", pokemon.name, pokemon.type, pokemon.health, pokemon.power] for i, pokemon in enumerate(player2_pokemon, 1)]
                        print("")
                        if player_name == player1:
                            print("Player 1 Current Pokemon Data")
                            print(tabulate(pokemon_data_player1, headers=pokemon_table_header, tablefmt="github", numalign="center"))
                        if player_name == player2:
                            print("Player 2 Current Pokemon Data")
                            print(tabulate(pokemon_data_player2, headers=pokemon_table_header, tablefmt="github", numalign="center"))
                        input("\nPress any key to back: ")
                        os.system("cls")
                        battle_stats.last_frame()
                    if choice == 3:
                        print("")
                        print(tabulate(history, headers=[colored("Round no.", "yellow", attrs=["bold"]), colored("Match", "yellow", attrs=["bold"]), colored("Status", "yellow", attrs=["bold"])], tablefmt="github", numalign="center"))
                        input("\nPress any key to back: ")
                        os.system("cls")
                        battle_stats.last_frame()
                    if choice == 4:
                        if (player_name == player1 and len(player1_used_pokemons) >= 3) or (player_name == player2 and len(player2_used_pokemons) >= 3):
                            if player_name == player1:
                                print(player1, "ran away from the battle!\n")
                            else:
                                print(player2, "ran away from the battle!\n")
                            total_player1_health = sum([pokemon.health for pokemon in player1_pokemon])
                            total_player2_health = sum([pokemon.health for pokemon in player2_pokemon])
                            if total_player1_health > total_player2_health:
                                print(f"{colored(player1, 'yellow', attrs=['bold'])} won the battle!")
                            elif total_player1_health < total_player2_health:
                                print(f"{colored(player2, 'yellow', attrs=['bold'])} won the battle!")
                            else:
                                print(f"It's a tie")
                            print(f"\nPlayer 1 Overall Pokemon's Health: {colored(total_player1_health, 'yellow', attrs=['bold', 'underline'])}")
                            print(f"Player 2 Overall Pokemon's Health: {colored(total_player2_health, 'yellow', attrs=['bold', 'underline'])}")
                            exit()
                        else:
                            print("\nAll of your pokemons must be used for you able to run!")
                            input("\nPress any key to back: ")
                            os.system("cls")
                            battle_stats.last_frame()
                else:
                    os.system("cls")
                    battle_stats.last_frame()
                    print(f"Your input must be in 1-4\n")
            else:
                os.system("cls")
                battle_stats.last_frame()
                print(f"{colored(choice, 'yellow', attrs=['underline'])} was not a valid keyword\n")

    player1_action = pre_battle_interface(player1, battle_stats.player1_pokemon)
    os.system("cls")
    battle_stats.player1_ready = True
    if player1_action == 2:
        player1_use_poison = True
        battle_stats.player1_use_poison()
    if player1_action == 3:
        player1_use_potion = True
        battle_stats.player1_use_potion()    
    battle_stats.last_frame()
    player2_action = pre_battle_interface(player2, battle_stats.player2_pokemon)
    os.system("cls")
    battle_stats.player2_ready = True
    if player2_action == 2:
        player2_use_poison = True
        battle_stats.player2_use_poison()    
    if player2_action == 3:
        player2_use_potion = True
        battle_stats.player2_use_potion()    
    battle_stats.last_frame()
    time.sleep(1)
    battle = Battle_Animation(battle_stats.player1_pokemon, battle_stats.player2_pokemon, battle_stats.battlefield)
    if battle_stats.player1_pokemon.power > battle_stats.player2_pokemon.power:
        battle.player1_won()
        battle_stats.player1_health_increase(5)
        battle_stats.player2_health_decrease(10)
        battle_stats.fatigue(2)
        round_history.append("Player 1 Won")
    elif battle_stats.player1_pokemon.power < battle_stats.player2_pokemon.power:
        battle.player2_won()
        battle_stats.player2_health_increase(5)
        battle_stats.player1_health_decrease(10)
        battle_stats.fatigue(2)
        round_history.append("Player 2 Won")
    else:
        battle.tie()
        battle_stats.fatigue(2)
        round_history.append("Tie")
    battle.reset()
    if player1_temporary_buff:
        battle.player1_pokemon.power -= 10
    if player2_temporary_buff:
        battle.player2_pokemon.power -= 10
    i += 1
    history.append(round_history)
    
    if battle_stats.round % 3 == 0:
        print(tabulate(history, headers=[colored("Round no.", "yellow", attrs=["bold"]), colored("Match", "yellow", attrs=["bold"]), colored("Status", "yellow", attrs=["bold"])], tablefmt="github", numalign="center"))
        total_player1_health = sum([pokemon.health for pokemon in player1_pokemon])
        total_player2_health = sum([pokemon.health for pokemon in player2_pokemon])
        print(f"\nPlayer 1 Overall Pokemon's Health: {colored(total_player1_health, 'yellow', attrs=['bold', 'underline'])}")
        print(f"Player 2 Overall Pokemon's Health: {colored(total_player2_health, 'yellow', attrs=['bold', 'underline'])}")
        print(f"\n❗Player's Overall Pokemon's Health is out basis of the Winner ❗\n")
        
        if total_player1_health > total_player2_health:
            print(f"{colored(player1, 'yellow', attrs=['bold'])} is the currently overall Winner!")
        elif total_player1_health < total_player2_health:
            print(f"{colored(player2, 'yellow', attrs=['bold'])} is the currently overall Winner!")
        else:
            print(f"It's a tie")

        x = input("\nPress any key to continue or x to exit: ")
        if x.lower() == "x":
            exit()