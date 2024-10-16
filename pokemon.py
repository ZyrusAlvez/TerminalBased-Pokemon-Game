from termcolor import colored

class Pokemon:
    def __init__ (self, name: str, type: str, health: int, power: int, poison_rate: float, poison_description: str, potion_rate: float, potion_description: str):
        # name color
        if type == "fire":
            name_color = "red"
        if type == "grass":
            name_color = "green"
        if type == "water":
            name_color = "blue"
            
        # initialized variables
        self.name = colored(name, name_color, attrs=["bold"])
        self.type = type
        self.health = health
        self.power = power
        self.poison_rate = poison_rate
        self.poison_description = poison_description
        self.potion_rate = potion_rate
        self.potion_description = potion_description
  
        # These are the variables to make sure that poison and potion can only be used 1 time per Pokemon object
        self.poison_used = False
        self.potion_used = False
        self.initial_health = health
        self.initial_power = power

    def normal_attack(self, enemy_pokemon: object) -> tuple:
        if self.power == enemy_pokemon.power:
            return None
        elif self.power > enemy_pokemon.power:
            return (self, enemy_pokemon)
        else:
            return (enemy_pokemon, self)

    def poison(self, enemy_pokemon: object = None) -> bool:
        print("")
        if self.type == "fire":
            if not self.poison_used:
                self.poison_used = True
                print(f"{self.name} used Fire Poison: {self.poison_description}")
                
                # lifesteal
                amount = round(enemy_pokemon.health * self.poison_rate, 2)
                self.health += amount
                enemy_pokemon.health -= amount
                print(f"{self.name} stole {amount} health points from {enemy_pokemon.name}")
                return True
            else:
                return False
            
        if self.type == "grass":
            if not self.poison_used:
                self.poison_used = True
                print(f"{self.name} used Grass Poison: {self.poison_description}")
                
                # deal damage based on enemy's hp
                amount = round(enemy_pokemon.health * self.poison_rate, 2)
                enemy_pokemon.health -= amount
                print(f"{self.name} dealt {amount} health points to {enemy_pokemon.name}")
                return True
            else:
                return False
            
        if self.type == "water":
            if not self.poison_used:
                self.poison_used = True
                print(f"{self.name} used Water Poison: {self.poison_description}")
                
                # reduce enemy's power
                amount = round(enemy_pokemon.power * self.poison_rate, 2)
                enemy_pokemon.power -= amount
                print(f"{enemy_pokemon.name} power is reduced by {amount}")
                return True
            else:
                return False

    def potion(self, enemy_pokemon: object = None) -> bool:
        print("")
        if self.type == "fire":
            if not self.poison_used:
                self.poison_used = True
                print(f"{self.name} used Fire Potion: {self.poison_description}")
                
                # covert hp to power
                amount = round(self.health * self.potion_rate, 2)
                self.health -= amount
                self.power += amount
                print(f"{self.name} convert {amount} health points in to power!")
                return True
            else:
                return False
            
        if self.type == "grass":
            if not self.poison_used:
                self.poison_used = True
                print(f"{self.name} used Grass Potion: {self.poison_description}")
                
                # add hp based on enemy's hp
                amount = round(enemy_pokemon.health * self.potion_rate + self.health, 2)
                if amount > self.initial_health:
                    print(f"{self.name} restored {self.initial_health - self.health} health points")
                else:
                    print(f"{self.name} restored {amount} health points")
                return True
            else:
                return False
            
        if self.type == "water":
            if not self.poison_used:
                self.poison_used = True
                print(f"{self.name} used Water Potion: {self.poison_description}")
                
                # add hp and power
                amount_health = round(self.health * self.potion_rate, 2)
                amount_power = round(self.power * self.potion_rate, 2)
                print(f"{self.name} gained additional {amount_health} health points and {amount_power} power")
                return True
            else:
                return False

    @staticmethod
    def pre_battle_interface(player_name: str, player_pokemon: object, enemy_player_name: str, enemy_pokemon: object) -> int:
        while True:
            print("1. Fight")
            print("2. Pokemon")
            print("3. Record")
            print("4. Run")
            choice = int(input(f"What will {player_name} will do? "))
            if choice in list(range(1, 5)):
                if choice == 1:
                    Pokemon.battle_interface(player_pokemon, enemy_player_name, enemy_pokemon)
            else:
                print(f"{choice} was not a valid keyword\n")
    
    @staticmethod
    def battle_interface(player_pokemon: object, enemy_player_name: str, enemy_pokemon: object) -> int:
        print(f"{enemy_player_name} sent out {enemy_pokemon.name}")
        print(f"You sent {player_pokemon.name}\n")

        while True:   
            print("1. Normal Attack")
            print("2. Poison Spell")
            print("3. Potion Spell")
            player_action = int(input(f"{player_pokemon.name} will use: "))
            if player_action in list(range(1, 4)):
                return player_action
            else:
                print(f"{player_action} was not a valid keyword\n")
    
    @staticmethod
    def battle(player1_pokemon_action: int, player1_current_pokemon: object, player2_pokemon_action: int, player2_current_pokemon: object) -> None:
        # if either of the 2 players used a pokemon's poison or potion
        if player1_pokemon_action == 2:
            player1_current_pokemon.poison(player2_current_pokemon)
        if player1_pokemon_action == 3:
            player1_current_pokemon.potion(player2_current_pokemon)
        if player2_pokemon_action == 2:
            player2_current_pokemon.poison(player1_current_pokemon)
        if player2_pokemon_action == 3:
            player2_current_pokemon.potion(player1_current_pokemon)
        
        winner, loser = player1_current_pokemon.normal_attack(player2_current_pokemon)
            
        print(f"\n{winner.name} won the fight!")
        print(f"{winner.name}'s health points {colored('increased', 'green')} by {colored('5', 'yellow')}")
        winner.health += 5
        print(f"{loser.name}'s health points {colored('decreased', 'red')} by {colored('10', 'yellow')}")
        loser.health -= 10
        print(f"Both pokemon {colored('decreased', 'red')} by {colored('2', 'yellow')} health points due to fatigue")
