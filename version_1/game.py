import random
import time
from tabulate import tabulate
from termcolor import colored

# pokemon's attributes and methods (the blueprint of each pokemons in the game)
class Pokemon:
    def __init__(self, name: str, initial_power: int, current_power: int):
        self.name = name
        self.initial_power = initial_power
        self.current_power = current_power

    def calculate_power(self, random_variation: str):
        if random_variation == "weak":
            self.current_power *= 0.5
        if random_variation == "strong":
            self.current_power *= 2
        return self.current_power
    
    def add_power(self, addend: int):
        self.current_power += addend

    def dead(self):
        self.current_power = 0

pokemon_hashmap = {
    "pikachu": 50,
    "charmander": 55,
    "bulbasaur": 60,
    "squirtle": 58,
    "jigglypuff": 45,
    "eevee": 52,
    "snorlax": 80,
    "gengar": 70,
    "machamp": 75,
    "mewtwo": 90,
}
user_pokemon_list = []
enemy_pokemon_list = []

# created every pokemon from the pokemon_hashmap and put it in a list
for pokemon in pokemon_hashmap:
    user_pokemon_list.append(Pokemon(pokemon, pokemon_hashmap[pokemon], pokemon_hashmap[pokemon]))
    enemy_pokemon_list.append(Pokemon(pokemon, pokemon_hashmap[pokemon], pokemon_hashmap[pokemon]))
    
def loading_animation():
    print ("Loading", end="")
    for _ in range(3):  
        print(".", end="", flush=True)
        time.sleep(1)
    print("\n")

# variable initialization
history = []
select_character = True
win = 0
lose = 0
battle_number = 0

print (f"""
Welcome to the {colored('ultimate Pokémon challenge', 'yellow')}! 
Here’s your mission: choose a Pokémon to compete in a high-stakes game of chance and strategy. 
Each Pokémon will receive a random variation that could either double its power or halve it.

If you’re feeling daring, pick a Pokémon with a higher base power for the chance at even greater rewards. 
But beware, the risk is high! For a safer bet, opt for a Pokémon with lower base power to minimize potential losses.

Are you ready to test your luck and strategy? Choose your Pokémon wisely and let the game begin!\n""")

loading_animation()

while True:
    
    # checks if the user chose to select a new pokemon
    if select_character:
        print(colored("Your Available Pokemons: ", "yellow", attrs=["bold"]))
        # Create data for the table
        table_data = [[colored(pokemon_object.name.capitalize(), "yellow"), colored(pokemon_object.current_power, "blue"), colored("Alive", "green") if pokemon_object.current_power != 0 else colored("Dead", "red")] for pokemon_object in user_pokemon_list]
        
        # Print the table with headers
        print(tabulate(table_data, headers=[colored("Name", attrs=["bold"]), colored("Current Power", attrs=["bold"]), colored("State", attrs=["bold"])], tablefmt="pretty"))
        user_pokemon = input(colored("Choose your pokemon: ", "yellow", attrs=["bold"])).lower()
        print("")

    # checks if the chosen pokemon is valid
    if user_pokemon in pokemon_hashmap.keys():

        for pokemon_object in user_pokemon_list:
            # finds the chosen pokemon using it's name attribute
            if user_pokemon == pokemon_object.name:
                # attached the chosen pokemon to the object
                user_pokemon_object = pokemon_object
        
        # checks if the chosen pokemon is not dead
        if user_pokemon_object.current_power != 0:

            # user pokemon (random variation)   
            user_random_variation = random.choice(["weak", "strong"])
            print(f"you selected a {colored(user_random_variation, attrs=['bold', 'underline'])} {colored(user_pokemon_object.name.capitalize(), 'yellow', attrs=['bold'])}")
            
            if user_random_variation == "weak":
                print (f"{colored(user_pokemon_object.name.capitalize(), 'yellow')}'s current power will be {colored('halved', 'red')}")
                print (f"{user_pokemon_object.current_power} / 2 = {colored(user_pokemon_object.calculate_power('weak'), 'blue')}")
            else:
                print (f"{colored(user_pokemon_object.name.capitalize(), 'yellow')}'s current power will be {colored('doubled', 'green')}")
                print (f"{user_pokemon_object.current_power} x 2 = {colored(user_pokemon_object.calculate_power('strong'), 'blue')}")

            print("")
            time.sleep(1)

            # enemy pokemon (random pokemon and variation)
            enemy_pokemon_object = random.choice(enemy_pokemon_list)
            enemy_random_variation = random.choice(["weak", "strong"])
            
            print(f"{colored('Enemy', 'red')} selected a {colored(enemy_random_variation, attrs=['bold', 'underline'])} {colored(enemy_pokemon_object.name.capitalize(), 'yellow', attrs=['bold'])}")
            if enemy_random_variation == "weak":
                print (f"{colored(enemy_pokemon_object.name.capitalize(), 'yellow')}'s current power will be {colored('halved', 'red')}")
                print (f"{enemy_pokemon_object.current_power} / 2 = {colored(enemy_pokemon_object.calculate_power('weak'), 'blue')}")
            else:
                print (f"{colored(enemy_pokemon_object.name.capitalize(), 'yellow')}'s current power will be {colored('doubled', 'green')}")
                print (f"{enemy_pokemon_object.current_power} x 2 = {colored(enemy_pokemon_object.calculate_power('strong'), 'blue')}")

            print("")
            loading_animation()
            print("")

            # Battle starts
            battle_number += 1
            
            # if the battle comes out to be TIE
            if user_pokemon_object.current_power == enemy_pokemon_object.current_power:
                history.append([battle_number, colored(user_pokemon_object.name.capitalize(), "yellow"), colored(user_pokemon_object.current_power, "blue"), colored(enemy_pokemon_object.name.capitalize(), "yellow"), colored(enemy_pokemon_object.current_power, "blue"), colored("Tie", 'yellow')])
                print ("its a tie!")
                print("")
                
                while True:
                    print ("What do you want to do next?")
                    print(f"Press {colored('c', 'green')} to continue the battle\nPress {colored('n', 'yellow')} for a new pokemon character selection\nPress {colored('m', 'blue')} for match history\nPress {colored('x', 'red')} to quit")
                    next = input("Enter the key: ")
                    if next == "c":
                        select_character = False
                        break
                    if next == "n":
                        select_character = True
                        break
                    if next == "x":
                        print (colored("thank you for playing!", "green", attrs=["bold"]))
                        exit()
                    if next == "m":
                        print(tabulate(history, headers=["Battle Number", "User's Pokemon", "User's Power", "Computer's Pokemon", "Computer's Power", "Status"], tablefmt="pretty"))
                        print("")
                    else:
                        print(colored("Not a valid key", "red"))
                        print("")

            # if the user won
            elif user_pokemon_object.current_power > enemy_pokemon_object.current_power:
                
                # backend methods and functions of the user winning
                history.append([battle_number, colored(user_pokemon_object.name.capitalize(), "yellow"), colored(user_pokemon_object.current_power, "blue"), colored(enemy_pokemon_object.name.capitalize(), "yellow"), colored(enemy_pokemon_object.current_power, "blue"), colored("User Wins", 'green')])
                user_pokemon_object.add_power(enemy_pokemon_object.current_power)
                enemy_pokemon_object.dead()
                enemy_pokemon_list.remove(enemy_pokemon_object)
                win += 1

                print(colored('Victory!', 'green', attrs=["bold"]))
                print("")

                if len(enemy_pokemon_list) == 0:
                    print('Enemy ran out of pokemon')
                    print('Congratulations!, you won the Pokemon battle')
                    break
                
                while True:
                    print ("What do you want to do next?")
                    print(f"Press {colored('c', 'green')} to continue the battle\nPress {colored('n', 'yellow')} for a new pokemon character selection\nPress {colored('m', 'blue')} for match history\nPress {colored('x', 'red')} to quit")
                    next = input("Enter the key: ")
                    if next == "c":
                        select_character = False
                        break
                    if next == "n":
                        select_character = True
                        break
                    if next == "x":
                        print (colored("thank you for playing!", "green", attrs=["bold"]))
                        exit()
                    if next == "m":
                        print(tabulate(history, headers=["Battle Number", "User's Pokemon", "User's Power", "Computer's Pokemon", "Computer's Power", "Status"], tablefmt="pretty"))
                        print("")
                    else:
                        print(colored("Not a valid key", "red"))
                        print("")

            # if the user lose
            else:
                history.append([battle_number, colored(user_pokemon_object.name.capitalize(), "yellow"), colored(user_pokemon_object.current_power, "blue"), colored(enemy_pokemon_object.name.capitalize(), "yellow"), colored(enemy_pokemon_object.current_power, "blue"), colored("Computer Wins", 'red')])
                enemy_pokemon_object.add_power(user_pokemon_object.current_power)
                user_pokemon_object.dead()
                select_character = True
                lose += 1
                
                print(colored('Defeat!', 'red', attrs=['bold']))
                print("")

                if len(user_pokemon_list) == lose:
                    print('You ran out of pokemon')
                    print('You entirely lost the Pokemon battle')

                while True:
                    print ("What do you want to do next?")
                    print(f"Press {colored('n', 'yellow')} for a new pokemon character selection\nPress {colored('m', 'blue')} for match history\nPress {colored('x', 'red')} to quit")
                    next = input("Enter the key: ")
                    if next == "n":
                        select_character = True
                        break
                    if next == "x":
                        print (colored("thank you for playing!", "green", attrs=["bold"]))
                        exit()
                    if next == "m":
                        print(tabulate(history, headers=["Battle Number", "User's Pokemon", "User's Power", "Computer's Pokemon", "Computer's Power", "Status"], tablefmt="pretty"))
                        print("")
                    else:
                        print(colored("Not a valid key", "red"))
                        print("")
    
        else:
            print (f"{colored(user_pokemon_object.name.capitalize(), 'yellow')} is already dead, please choose another Pokemon")
    else:
        if user_pokemon == "":
            print("No selection made")
        else:
            print ("Invalid Invalid input selection")
            print ({colored(user_pokemon, 'yellow')}, "not in the pokemon list")    