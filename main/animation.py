from os import system
from time import sleep
from random import choice
from termcolor import colored
import re
class Battle_Animation:
    round = 0
    def __init__(self, player1_pokemon: object, player2_pokemon: object, battlefield: str):
        Battle_Animation.round += 1
        self.player1_pokemon = player1_pokemon
        self.player2_pokemon = player2_pokemon
        self.battlefield = battlefield
        if battlefield == colored("Waterfall Arena", "blue", attrs=["bold"]):
            self.battlefield_color = "blue"
        if battlefield == colored("Volcanic Field", "red", attrs=["bold"]):
            self.battlefield_color = "red"
        if battlefield == colored("Green Land", "green", attrs=["bold"]):
            self.battlefield_color = "green"
        
        
        self.ansi_escape = re.compile(r'\x1B\[[0-?]*[ -/]*[@-~]')
                
        self.space_in_round = int((54 - (9 + len(self.ansi_escape.sub('', battlefield)) + len(str(Battle_Animation.round)))) / 2)
        self.space_in_title = 54 - (22 + len(self.ansi_escape.sub('', self.player1_pokemon.name)) + len(self.ansi_escape.sub('', self.player2_pokemon.name)))
        self.space_in_health = 54 - (6 + len(str(self.player1_pokemon.health)) + len(str(self.player2_pokemon.health)))
        self.space_in_power = 54 - (6 + len(str(self.player1_pokemon.power)) + len(str(self.player2_pokemon.power)))
        self.space_in_looks_player1 = 0
        self.space_in_looks_player2 = 0
        self.space_between_looks = 10
        
        if self.player1_pokemon.type == "fire":
            self.player1_power = "🔥"
        if self.player1_pokemon.type == "water":
            self.player1_power = "💦"
        if self.player1_pokemon.type == "grass":
            self.player1_power = "🍃"
        
        if self.player2_pokemon.type == "fire":
            self.player2_power = "🔥"
        if self.player2_pokemon.type == "water":
            self.player2_power = "💦"
        if self.player2_pokemon.type == "grass":
            self.player2_power = "🍃"
        
    def player1_won(self):
        system("cls")
        for i in range(14):
            print(f"{' ' * self.space_in_round}Round {Battle_Animation.round} - {self.battlefield}{' ' * self.space_in_round}")
            print("——————————————————————————————————————————————————————")
            print(f"Player 1's {self.player1_pokemon.name}{' ' * self.space_in_title}Player 2's {self.player2_pokemon.name}")
            print("——————————————————————————————————————————————————————")
            print(f"❤️  {self.player1_pokemon.health}{' ' * self.space_in_health}{self.player2_pokemon.health} ❤️")
            print("——————————————————————————————————————————————————————")
            print(colored(f"=================[{self.player1_pokemon.looks}{' ' * self.space_in_looks_player1}{self.player1_power}{' ' * self.space_between_looks}{self.player2_power}{' ' * self.space_in_looks_player2}{self.player2_pokemon.looks}]=================", self.battlefield_color, attrs=['bold']))
            print("——————————————————————————————————————————————————————")
            print(f"⚔️  {self.player1_pokemon.power}{' ' * self.space_in_power}{self.player2_pokemon.power} ⚔️")
            print("——————————————————————————————————————————————————————")
            if i != 13:
                sleep(0.3)
                system("cls")
            
            # Animation Logic
            self.space_in_looks_player1 += 1
            if self.space_in_looks_player1 > 5:
                # collision
                if self.space_in_looks_player1 == 6:
                    self.space_in_looks_player2 += 2
                if self.space_in_looks_player1 >= 13:
                    self.player2_pokemon.looks = "💀"
                    self.player1_power = " "
                else:
                    self.player2_power = ""
                    self.space_in_looks_player2 -= 1
            else:
                # before collision
                self.space_between_looks -= 2
                self.space_in_looks_player2 += 1
                
    def player2_won(self):
        system("cls")
        for i in range(14):
            print(f"{' ' * self.space_in_round}Round {Battle_Animation.round} - {self.battlefield}{' ' * self.space_in_round}")
            print("——————————————————————————————————————————————————————")
            print(f"Player 1's {self.player1_pokemon.name}{' ' * self.space_in_title}Player 2's {self.player2_pokemon.name}")
            print("——————————————————————————————————————————————————————")
            print(f"❤️  {self.player1_pokemon.health}{' ' * self.space_in_health}{self.player2_pokemon.health} ❤️")
            print("——————————————————————————————————————————————————————")
            print(colored(f"=================[{self.player1_pokemon.looks}{' ' * self.space_in_looks_player1}{self.player1_power}{' ' * self.space_between_looks}{self.player2_power}{' ' * self.space_in_looks_player2}{self.player2_pokemon.looks}]=================", self.battlefield_color, attrs=['bold']))
            print("——————————————————————————————————————————————————————")
            print(f"⚔️  {self.player1_pokemon.power}{' ' * self.space_in_power}{self.player2_pokemon.power} ⚔️")
            print("——————————————————————————————————————————————————————")
            if i != 13:
                sleep(0.3)
                system("cls")
            
            # Animation Logic
            self.space_in_looks_player2 += 1
            if self.space_in_looks_player2 > 5:
                # collision
                if self.space_in_looks_player2 == 6:
                    self.space_in_looks_player1 += 2
                if self.space_in_looks_player2 >= 13:
                    self.player1_pokemon.looks = "💀"
                    self.player2_power = " "
                else:
                    self.player1_power = ""
                    self.space_in_looks_player1 -= 1
            else:
                # before collision
                self.space_between_looks -= 2
                self.space_in_looks_player1 += 1
                
    def tie(self):
        system("cls")
        for i in range(7):
            print(f"{' ' * self.space_in_round}Round {Battle_Animation.round} - {self.battlefield}{' ' * self.space_in_round}")
            print("——————————————————————————————————————————————————————")
            print(f"Player 1's {self.player1_pokemon.name}{' ' * self.space_in_title}Player 2's {self.player2_pokemon.name}")
            print("——————————————————————————————————————————————————————")
            print(f"❤️  {self.player1_pokemon.health}{' ' * self.space_in_health}{self.player2_pokemon.health} ❤️")
            print("——————————————————————————————————————————————————————")
            print(colored(f"=================[{self.player1_pokemon.looks}{' ' * self.space_in_looks_player1}{self.player1_power}{' ' * self.space_between_looks}{self.player2_power}{' ' * self.space_in_looks_player2}{self.player2_pokemon.looks}]=================", self.battlefield_color, attrs=['bold']))
            print("——————————————————————————————————————————————————————")
            print(f"⚔️  {self.player1_pokemon.power}{' ' * self.space_in_power}{self.player2_pokemon.power} ⚔️")
            print("——————————————————————————————————————————————————————")
            if i != 6:
                sleep(0.3)
                system("cls")
            
            # Animation Logic
            self.space_in_looks_player2 += 1
            self.space_between_looks -= 2
            self.space_in_looks_player1 += 1
            
            if i == 5:
                self.space_between_looks += 4
                self.player1_power = ""
                self.player2_power = ""
                
class Pre_Battle_Animation:
    round = 0
    def __init__(self, player1_pokemon_list, player2_pokemon_list):
        self.player1_pokemon_list = player1_pokemon_list
        self.player2_pokemon_list = player2_pokemon_list
        self.player1_ready = False
        self.player2_ready = False
        self.ansi_escape = re.compile(r'\x1B\[[0-?]*[ -/]*[@-~]')
        Pre_Battle_Animation.round += 1
        
    def randomizer_animation(self):
        for i in range(20):
            self.battlefield = choice([colored("Waterfall Arena", "blue", attrs=["bold"]), colored("Volcanic Field", "red", attrs=["bold"]), colored("Green Land", "green", attrs=["bold"])])
            if self.battlefield == colored("Waterfall Arena", "blue", attrs=["bold"]):
                self.battlefield_color = "blue"
            if self.battlefield == colored("Volcanic Field", "red", attrs=["bold"]):
                self.battlefield_color = "red"
            if self.battlefield == colored("Green Land", "green", attrs=["bold"]):
                self.battlefield_color = "green"
            self.player1_pokemon = choice(self.player1_pokemon_list)
            self.player2_pokemon = choice(self.player2_pokemon_list)
            clean_name1 = self.ansi_escape.sub('', self.player1_pokemon.name)
            clean_name2 = self.ansi_escape.sub('', self.player2_pokemon.name)
            self.space_in_round_left = int((54 - (9 + len(self.ansi_escape.sub('', self.battlefield)) + len(str(Pre_Battle_Animation.round)))) / 2)
            self.space_in_round_right = int((54 - (9 + len(self.ansi_escape.sub('', self.battlefield)) + len(str(Pre_Battle_Animation.round)))) / 2)
            self.space_in_title = 54 - (22 + len(clean_name1) + len(clean_name2))
            self.space_in_health = 54 - (6 + len(str(self.player1_pokemon.health)) + len(str(self.player2_pokemon.health)))
            self.space_in_power = 54 - (6 + len(str(self.player1_pokemon.power)) + len(str(self.player2_pokemon.power)))

            if (len(self.ansi_escape.sub('', self.battlefield)) + len(str(Pre_Battle_Animation.round)) + 9) % 2 != 0:
                self.space_in_round_right += 1
            
            sleep(0.2)
            system("cls")
            if i == 19:
                self.space_in_round_right -= 9
                self.space_in_round_left -= 9
                print(f"{colored('Not Ready', 'red', attrs=['bold'])}{' ' * self.space_in_round_left}Round {Pre_Battle_Animation.round} - {self.battlefield}{' ' * self.space_in_round_right}{colored('Not Ready', 'red', attrs=['bold'])}")
            else:
                print(f"{' ' * self.space_in_round_left}Round {Pre_Battle_Animation.round} - {self.battlefield}{' ' * self.space_in_round_right}")
            print("——————————————————————————————————————————————————————")
            print(f"Player 1's {self.player1_pokemon.name}{' ' * self.space_in_title}Player 2's {self.player2_pokemon.name}")
            print("——————————————————————————————————————————————————————")
            print(f"❤️  {self.player1_pokemon.health}{' ' * self.space_in_health}{self.player2_pokemon.health} ❤️")
            print("——————————————————————————————————————————————————————")
            print(colored(f"=================[{self.player1_pokemon.looks}              {self.player2_pokemon.looks}]=================", self.battlefield_color, attrs=["bold"]))
            print("——————————————————————————————————————————————————————")
            print(f"⚔️  {self.player1_pokemon.power}{' ' * self.space_in_power}{self.player2_pokemon.power} ⚔️")
            print("——————————————————————————————————————————————————————")            

    def last_frame(self):
        if self.player1_ready and not self.player2_ready:
            self.space_in_round_left += 4
            print(f"{colored('Ready', 'green', attrs=['bold'])}{' ' * self.space_in_round_left}Round {Pre_Battle_Animation.round} - {self.battlefield}{' ' * self.space_in_round_right}{colored('Not Ready', 'red', attrs=['bold'])}")
            self.space_in_round_left -= 4
        elif self.player1_ready and self.player2_ready:
            self.space_in_round_right += 4
            self.space_in_round_left += 4
            print(f"{colored('Ready', 'green', attrs=['bold'])}{' ' * self.space_in_round_left}Round {Pre_Battle_Animation.round} - {self.battlefield}{' ' * self.space_in_round_right}{colored('Ready', 'green', attrs=['bold'])}")
            self.space_in_round_right -= 4
            self.space_in_round_left -= 4
        else:
            print(f"{colored('Not Ready', 'red', attrs=['bold'])}{' ' * self.space_in_round_left}Round {Pre_Battle_Animation.round} - {self.battlefield}{' ' * self.space_in_round_right}{colored('Not Ready', 'red', attrs=['bold'])}")
            
        print("——————————————————————————————————————————————————————")
        print(f"Player 1's {self.player1_pokemon.name}{' ' * self.space_in_title}Player 2's {self.player2_pokemon.name}")
        print("——————————————————————————————————————————————————————")
        print(f"❤️  {self.player1_pokemon.health}{' ' * self.space_in_health}{self.player2_pokemon.health} ❤️")
        print("——————————————————————————————————————————————————————")
        print(colored(f"=================[{self.player1_pokemon.looks}              {self.player2_pokemon.looks}]=================", self.battlefield_color, attrs=["bold"]))
        print("——————————————————————————————————————————————————————")
        print(f"⚔️  {self.player1_pokemon.power}{' ' * self.space_in_power}{self.player2_pokemon.power} ⚔️")
        print("——————————————————————————————————————————————————————")
            
    def player1_buff(self, rate: int):
        print(f"The {self.battlefield} temporarily increased {self.player1_pokemon.name} attack stats")
        sleep(5)
        system("cls")
        
        self.space_in_power -= 4
        for _ in range(rate):
            self.player1_pokemon.power += 1
            
            if self.player1_ready and not self.player2_ready:
                self.space_in_round_left += 4
                print(f"{colored('Ready', 'green', attrs=['bold'])}{' ' * self.space_in_round_left}Round {Pre_Battle_Animation.round} - {self.battlefield}{' ' * self.space_in_round_right}{colored('Not Ready', 'red', attrs=['bold'])}")
            elif self.player1_ready and self.player2_ready:
                self.space_in_round_right += 4
                self.space_in_round_left += 4
                print(f"{colored('Ready', 'green', attrs=['bold'])}{' ' * self.space_in_round_left}Round {Pre_Battle_Animation.round} - {self.battlefield}{' ' * self.space_in_round_right}{colored('Ready', 'green', attrs=['bold'])}")
            else:
                print(f"{colored('Not Ready', 'red', attrs=['bold'])}{' ' * self.space_in_round_left}Round {Pre_Battle_Animation.round} - {self.battlefield}{' ' * self.space_in_round_right}{colored('Not Ready', 'red', attrs=['bold'])}")
            print("——————————————————————————————————————————————————————")
            print(f"Player 1's {self.player1_pokemon.name}{' ' * self.space_in_title}Player 2's {self.player2_pokemon.name}")
            print("——————————————————————————————————————————————————————")
            print(f"❤️  {self.player1_pokemon.health}{' ' * self.space_in_health}{self.player2_pokemon.health} ❤️")
            print("——————————————————————————————————————————————————————")
            print(colored(f"=================[{self.player1_pokemon.looks}              {self.player2_pokemon.looks}]=================", self.battlefield_color, attrs=["bold"]))
            print("——————————————————————————————————————————————————————")
            print(f"⚔️  {self.player1_pokemon.power}  ⬆️ {' ' * self.space_in_power}{self.player2_pokemon.power} ⚔️")
            print("——————————————————————————————————————————————————————")
            print(f"The {self.battlefield} temporarily increased {self.player1_pokemon.name} attack stats")
            sleep(0.2)
            system("cls")
        self.space_in_power += 4
        self.last_frame()
        
    def player2_buff(self, rate: int):
        print(f"The {self.battlefield} temporarily increased {self.player2_pokemon.name} attack stats")
        
        sleep(5)
        system("cls")
        
        self.space_in_power -= 4
        for _ in range(rate):
            self.player2_pokemon.power += 1
            
            if self.player1_ready and not self.player2_ready:
                self.space_in_round_left += 4
                print(f"{colored('Ready', 'green', attrs=['bold'])}{' ' * self.space_in_round_left}Round {Pre_Battle_Animation.round} - {self.battlefield}{' ' * self.space_in_round_right}{colored('Not Ready', 'red', attrs=['bold'])}")
            elif self.player1_ready and self.player2_ready:
                self.space_in_round_right += 4
                self.space_in_round_left += 4
                print(f"{colored('Ready', 'green', attrs=['bold'])}{' ' * self.space_in_round_left}Round {Pre_Battle_Animation.round} - {self.battlefield}{' ' * self.space_in_round_right}{colored('Ready', 'green', attrs=['bold'])}")
            else:
                print(f"{colored('Not Ready', 'red', attrs=['bold'])}{' ' * self.space_in_round_left}Round {Pre_Battle_Animation.round} - {self.battlefield}{' ' * self.space_in_round_right}{colored('Not Ready', 'red', attrs=['bold'])}")
            print("——————————————————————————————————————————————————————")
            print(f"Player 1's {self.player1_pokemon.name}{' ' * self.space_in_title}Player 2's {self.player2_pokemon.name}")
            print("——————————————————————————————————————————————————————")
            print(f"❤️  {self.player1_pokemon.health}{' ' * self.space_in_health}{self.player2_pokemon.health} ❤️")
            print("——————————————————————————————————————————————————————")
            print(colored(f"=================[{self.player1_pokemon.looks}              {self.player2_pokemon.looks}]=================", self.battlefield_color, attrs=["bold"]))
            print("——————————————————————————————————————————————————————")
            print(f"⚔️  {self.player1_pokemon.power}{' ' * self.space_in_power} ⬆️  {self.player2_pokemon.power} ⚔️")
            print("——————————————————————————————————————————————————————")
            print(f"The {self.battlefield} temporarily increased {self.player2_pokemon.name} attack stats")
            sleep(0.2)
            system("cls")
        self.space_in_power += 4
        self.last_frame()  