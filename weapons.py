import os
import pickle

class Weapon:
    def __init__(self, name, damage, speed):
        self.name = name
        self.damage = damage
        self.speed = speed

class Player:
    def __init__(self):
        self.inventory = []
        self.equipped_weapon = None

    def pick_up_weapon(self, weapon):
        self.inventory.append(weapon)
        print(f"You picked up a {weapon.name}!")

    def show_inventory(self):
        if not self.inventory:
            print("Your inventory is empty.")
        else:
            print("Inventory:")
            for weapon in self.inventory:
                print(f"{weapon.name} (Damage: {weapon.damage}, Speed: {weapon.speed})\n")

    def equip_weapon(self, weapon_name):
        for weapon in self.inventory:
            if weapon.name == weapon_name:
                self.equipped_weapon = weapon
                os.system('cls')
                return
        print(f"You don't have a {weapon_name} in your inventory.")

    def get_equipped_weapon_speed(self):
        if self.equipped_weapon:
            return self.equipped_weapon.speed
        else:
            return "No weapon currently equipped"

    def SaveGame(self, savepoint):
        with open('savedata.dat', 'wb') as f:
            pickle.dump((savepoint, self.inventory), f, protocol=2)
        os.system('cls')
        print("Game has been saved!\n")
        input("Press Enter to continue...")

    def LoadGame(self):
        with open('savedata.dat', 'rb') as f:
            loaded_data = pickle.load(f)
            savepoint, self.inventory = loaded_data
        print("Saved Data has been loaded!\n")
        input("Press Enter to continue...")
        os.system('cls')
        return savepoint