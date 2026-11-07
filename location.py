import os
import combat
import pickle
import weapons

hasSight = False
hasArms = False
hasNerves = False
hasUchi = False
savepoint = 0

player = weapons.Player()

Fist = weapons.Weapon("Fist", damage = 10, speed = 1)
Uchigatana = weapons.Weapon("Uchigatana", damage = 20, speed = 0.8)
MoonlightGS = weapons.Weapon("Moonlight Greatsword", damage = 45, speed = 0.5)

def StartDungeon():
    global hasSight
    global savepoint
    savepoint = 0
    player.equipped_weapon = Fist
    os.system('cls')
    print("You don't know where you are. You can't see, hear, or even feel.\n")
    input("Press Enter to continue...")
    os.system('cls')
    print("You can feel a sinister aura ahead of you.")
    while True:
        movement = input("Where will you go? (Up, Left, Right, Back): ")
        os.system('cls')
        if (movement.replace(" ","").upper()) == "UP":
            os.system('cls')
            break
        elif (movement.replace(" ","").upper()) == "LEFT":
            print("You should investigate the sinister aura!\n")
            input("Press Enter to continue...")
            os.system('cls')
            continue
        elif (movement.replace(" ","").upper()) == "RIGHT":
            print("You should investigate the sinister aura!\n")
            input("Press Enter to continue...")
            os.system('cls')
            continue
        elif (movement.replace(" ","").upper()) == "BACK":
            print("You should investigate the sinister aura!\n")
            input("Press Enter to continue...")
            os.system('cls')
            continue
        elif (movement.replace(" ","").upper()) == "SAVE":
            player.SaveGame()
            exit()
        else:
            os.system('cls')
            print("Please enter a valid input!\n")
            input("Press Enter to continue...")
            os.system('cls')
            continue

    print("The aura grows stronger as you move forward.")
    while True:
        movement = input("Where will you go? (Up, Left, Right, Back): ")
        os.system('cls')
        if (movement.replace(" ","").upper()) == "UP":
            print("The sinister aura is incredibly thick. You sense a small blob of aura approaching you.\n")
            input("Press Enter to continue...")
            os.system('cls')
            combat.CombatTutorial()
            os.system('cls')
            break
        elif (movement.replace(" ","").upper()) == "LEFT":
            print("You should investigate the sinister aura!\n")
            input("Press Enter to continue...")
            os.system('cls')
            continue
        elif (movement.replace(" ","").upper()) == "RIGHT":
            print("You should investigate the sinister aura!\n")
            input("Press Enter to continue...")
            os.system('cls')
            continue
        elif (movement.replace(" ","").upper()) == "BACK":
            print("You should investigate the sinister aura!\n")
            input("Press Enter to continue...")
            os.system('cls')
            continue
        elif (movement.replace(" ","").upper()) == "SAVE":
            player.SaveGame()
            exit()
        else:
            print("Please enter a valid input!\n")
            input("Press Enter to continue...")
            os.system('cls')
            continue

    print("The blob of aura dissipated; you can no longer sense it. However, you\ncan still sense the dense, sinister aura ahead of you.\n")
    while True:
        movement = input("Where will you go? (Up, Left, Right, Back): ")
        os.system('cls')
        if (movement.replace(" ","").upper()) == "UP":
            os.system('cls')
            break
        elif (movement.replace(" ","").upper()) == "LEFT":
            print("You should investigate the sinister aura!\n")
            input("Press Enter to continue...")
            os.system('cls')
            continue
        elif (movement.replace(" ","").upper()) == "RIGHT":
            print("You should investigate the sinister aura!\n")
            input("Press Enter to continue...")
            os.system('cls')
            continue
        elif (movement.replace(" ","").upper()) == "BACK":
            print("You should investigate the sinister aura!\n")
            input("Press Enter to continue...")
            os.system('cls')
            continue
        elif (movement.replace(" ","").upper()) == "SAVE":
            player.SaveGame()
            exit()
        else:
            print("Please enter a valid input!\n")
            input("Press Enter to continue...")
            os.system('cls')
            continue
    print("The aura is so dense you can barely stand it!\n")
    input("Press Enter to continue...")
    os.system('cls')
    print("Wait, something is coming! A large mass of aura is approaching you!\n")
    input("Press Enter to continue...")
    os.system('cls')
    combat.VitreousFight()
    input("Press Enter to continue...")
    os.system('cls')
    hasSight = True
    print("You have regained your sense of sight!\n")
    input("Press Enter to continue...")
    os.system('cls')
    print("With your regained sight, you can see light coming from up\nahead. It appears to be the exit!\n")
    input("Press Enter to continue...")
    os.system('cls')
    print("You exit the dungeon and see the beautiful world around you.\n")
    input("Press Enter to continue...")
    os.system('cls')
    CenterMap()
        
def CenterMap():
    global savepoint
    savepoint = 1
    print("You are in the center of a vast world. There appears to\n"
          "be a tundra to the North, a desert to the West,\n"
          "a beach to the South, and plains to the East.\n")
    movement = input("Where will you go? (N, S, W, E): ")
    if (movement.replace(" ","").upper()) == "N":
        Tundra()
    elif (movement.replace(" ","").upper()) == "S":
        Beach()
    elif (movement.replace(" ","").upper()) == "W":
        Desert()
    elif (movement.replace(" ","").upper()) == "E":
        Plains()
    elif (movement.replace(" ","").upper()) == "SAVE":
        player.SaveGame()
        exit()

def Tundra():
    global savepoint
    savepoint = 2
    os.system('cls')
    print("There is snow up to your ankles and snowy trees all around you.\nIt's probably very cold, but you don't have the senses to feel it.\n")
    input("Press Enter to continue...")
    os.system('cls')
    print("To the northwest, there is a mountain. To the north and northeast,\nthere appears to be nothing.\n")
    movement = input("Where will you go? (NW, N, NE, S): ")
    os.system('cls')
    match (movement.replace(" ","").upper()):
        case "NW":
            Mountain()
        case "N":
            tundraField()
        case "NE":
            tundraForest()
        case "S":
            CenterMap()
        case "SAVE":
            player.SaveGame()
        case "INV":
            InventoryMenu(Tundra)

def Mountain():
    global savepoint
    savepoint = 3
    print("You come across a large mountain. There appears to be a cave at the\nfoot of the mountain. There is also a path leading to the top.\n")
    movement = input("Where will you go? (Cave, Path, Back): ")
    os.system('cls')
    match (movement.replace(" ","").upper()):
        case "CAVE":
            Cave()
        case "PATH":
            Peak()
        case "BACK":
            Tundra()
        case "SAVE":
            player.SaveGame()

def Cave():
    global savepoint
    global hasUchi
    savepoint = 4
    if hasUchi == False:
        print("It's very dark inside the cave. You can't see anything!\n")
        input("Press Enter to continue...")
        os.system('cls')
        print("Wait... something's coming!\n")
        input("Press Enter to continue...")
        os.system('cls')
        combat.SwordMasterFight()
        print("You have obtained the Uchigatana!")
        player.pick_up_weapon(Uchigatana)
        hasUchi = True
        input("Press Enter to continue...")
        os.system('cls')
        Cave()
    else:
        print("You are inside a dark cave. There seems to be nothing.")
        while True:
            movement = input("Where will you go? (Forward, Back): ")
            if movement.replace(" ", "").upper() == "FORWARD":
                print("You walk forward and run into the cave wall.\n")
                continue
            elif movement.replace(" ", "").upper() == "BACK":
                break
        Mountain()

def Peak():
    global savepoint
    savepoint = 5
    print("You reach the peak of the mountain and find a large nest.\n")
    movement = input("Will you enter the nest? (Y or N): ")
    os.system('cls')
    match (movement.replace(" ","").upper()):
        case "Y":
            print("There's a dragon inside the nest!\n")
            input("Press Enter to continue...")
            os.system('cls')
            combat.LunarisFight()
        case "N":
            print("You decided against entering the nest and retreated.\n")
            input("Press Enter to continue...")
            os.system('cls')
            Mountain()
        case "SAVE":
            player.SaveGame()

def tundraField():
    global savepoint
    savepoint = 6

def tundraForest():
    global savepoint
    savepoint = 7
    print()

def Beach():
    global savepoint

    os.system('cls')
    print("This isn't coded yet! :skull:")

def Desert():
    global savepoint

    os.system('cls')
    print("This isn't coded yet! :skull:")

def Plains():
    global savepoint

    os.system('cls')
    print("This isn't coded yet! :skull:")


def InventoryMenu(scene):
    player.show_inventory()
    choice = input("What would you like to do? (Equip [name], Back): ")
    os.system('cls')
    if (choice.upper()).startswith("EQUIP"):
        player.show_inventory()
        weapon = input("Which weapon would you like to equip? ")
        match weapon.replace(" ","").upper():
            case "UCHIGATANA":
                player.equipped_weapon = Uchigatana
                os.system('cls')
                print("You have equipped the Uchigatana!\n")
                input("Press Enter to continue...")
                os.system('cls')
            case "MOONLIGHTGREATSWORD":
                player.equipped_weapon = MoonlightGS
                os.system('cls')
                print("You have equipped the Moonlight Greatsword!\n")
                input("Press Enter to continue...")
                os.system('cls')
        
        scene()
    elif choice.replace(" ","").upper() == "BACK":
        scene()
        