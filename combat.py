import os
import random
from weapons import Player


player = Player()
HP = 100
EnemyAlive = True

def get_player_weapon_stats():
    # Import location here to avoid circular import at module level
    import location
    weapon = location.player.equipped_weapon
    if weapon:
        return weapon.speed, weapon.damage
    else:
        return 1.0, 10  # Default values

def CombatTutorial():
    import location
    global HP
    HP = 100
    EnemyHP = 10
    global EnemyAlive
    EnemyAlive = True
    print("You have encountered an enemy!\n")
    while EnemyAlive == True:
        while EnemyAlive == True:
            print("Your HP = ???/???\n"
                "Enemy HP = ??/??\n")
            action = input("The blob is at rest. What will you do?\n"
                        "(1) Attack (2) Block (3) Dodge\n")
            os.system('cls')
            if action.replace(" ","") == "1":
                print("You take a swing at the blob, but it attacks first and hits you.\n")
                input("Press Enter to continue...")
                os.system('cls')
                HP -= 10
                checkHP(location.StartDungeon)
                continue
            elif action.replace(" ","") == "2":
                print("The blob attacks you, but you block the hit.\n")
                input("Press Enter to continue...")
                os.system('cls')
                break
            elif action.replace(" ","") == "3":
                print("The blob attacks you, but you dodge the hit.\n")
                input("Press Enter to continue...")
                os.system('cls')
                continue
            else:
                print("Please enter a valid input!\n")
                input("Press Enter to continue...")
                os.system('cls')
                continue
        print("Your HP = ???/???\n"
            "Enemy HP = ??/???\n")
        action = input("The blob seems to be stunned. What will you do?\n"
                        "(1) Attack (2) Block (3) Dodge\n")
        os.system('cls')
        if action.replace(" ","") == "1":
            print("You swing at the blob and hit it!\n")
            input("Press Enter to continue...")
            os.system('cls')
            EnemyHP -= 10
            checkEnemyHP(EnemyHP)
            if EnemyAlive == True:
                continue
            elif EnemyAlive == False:
                input("Press Enter to continue...")
                break
        elif action.replace(" ","") == "2":
            print("You block, but the blob does nothing.\n")
            input("Press Enter to continue...")
            os.system('cls')
            continue
        elif action.replace(" ","") == "3":
            print("You dodge, but the blob does nothing.\n")
            input("Press Enter to continue...")
            os.system('cls')
            continue
        else:
            print("Please enter a valid input!\n")
            input("Press Enter to continue...")
            os.system('cls')
            continue

def checkHP(scene):
    if HP <= 0:
        print("YOU DIED!\n")
        input("Press Enter to continue...")
        os.system('cls')
        scene()

def checkEnemyHP(HP):
    global EnemyAlive
    if HP <= 0:
        print("You won!\n")
        EnemyAlive = False
        
def VitreousFight():
    import location
    global VitreousAlive
    VitreousAlive = True
    global VitreousHP
    VitreousHP = 150
    global HP
    print("You have encountered Vitreous, the All-Seeing!\n")
    input("Press Enter to continue...")
    while VitreousAlive == True:
        os.system('cls')
        print("Your HP = ???/???\n"
            "Vitreous HP = ???/???\n")
        vattack = random.randint(1, 10)
        if vattack in range(1, 3):
            action = input("Vitreous seems to be raising his arm! What will you do?\n"
                           "(1) Attack (2) Block/Parry (3) Dodge\n")
            os.system('cls')
            if action.replace(" ","") == "1":
                print("You go for an attack but get grabbed and pummeled by Vitreous!\n")
                input("Press Enter to continue...")
                os.system('cls')
                HP -= 50
                checkHP(location.StartDungeon)
                continue
            elif action.replace(" ","") == "2":
                print("You block, but Vitreous grabs and pummels you!\n")
                input("Press Enter to continue...")
                os.system('cls')
                HP -= 25
                checkHP(location.StartDungeon)
                continue
            elif action.replace(" ","") == "3":
                print("Vitreous tries to grab you, but you dodge it!\n")
                input("Press Enter to continue...")
                os.system('cls')
                continue
            else:
                print("Please enter a valid input!\n")
                input("Press Enter to continue...")
                os.system('cls')
                continue
        elif vattack in range(4, 6):
            action = input("Vitreous seems to be raising his arm! What will you do?\n"
                           "(1) Attack (2) Block/Parry (3) Dodge\n")
            os.system('cls')
            if action.replace(" ","") == "1":
                print("You go for an attack, but Vitreous slams his arm down and crushes you!\n")
                input("Press Enter to continue...")
                os.system('cls')
                HP -= 60
                checkHP(location.StartDungeon)
                continue
            elif action.replace(" ","") == "2":
                print("Vitreous slams his arm down and hits you, but you parry the hit!\n")
                input("Press Enter to continue...")
                os.system('cls')
                print("Your HP = ???/???\n"
                    "Vitreous HP = ???/???\n")
                action = input("Vitreous seems to be stunned! What will you do?\n"
                            "(1) Attack (2) Block/Parry (3) Dodge\n")
                os.system('cls')
                if action.replace(" ","") == "1":
                    print("You viciously attack Vitreous!\n")
                    input("Press Enter to continue...")
                    os.system('cls')
                    VitreousHP -= 50
                    checkVitreousHP(VitreousHP)
                    continue
                elif action.replace(" ","") == "2":
                    print("You block, but Vitreous does nothing!\n")
                    input("Press Enter to continue...")
                    os.system('cls')
                    continue
                elif action.replace(" ","") == "3":
                    print("You dodge, but Vitreous does nothing!\n")
                    input("Press Enter to continue...")
                    os.system('cls')
                    continue
                else:
                    print("Please enter a valid input!\n")
                    input("Press Enter to continue...")
                    os.system('cls')
                    continue
            elif action.replace(" ","") == "3":
                print("You dodge, but Vitreous sees it coming and slams his arm down on you!\n")
                input("Press Enter to continue...")
                HP -= 60
                checkHP(location.StartDungeon)
                os.system('cls')
                continue
            else:
                print("Please enter a valid input!\n")
                input("Press Enter to continue...")
                os.system('cls')
                continue
        elif vattack in range(7, 9):
            action = input("Vitreous is standing still! What will you do?\n"
                           "(1) Attack (2) Block/Parry (3) Dodge\n")
            os.system('cls')
            if action.replace(" ","") == "1":
                print("You land a hit on Vitreous, but he hits back!\n")
                input("Press Enter to continue...")
                os.system('cls')
                VitreousHP -= 15
                HP -= 25
                checkHP(location.StartDungeon)
                checkVitreousHP(VitreousHP)
                continue
            elif action.replace(" ","") == "2":
                print("You block, but Vitreous does nothing!")
                input("Press Enter to continue...")
                os.system('cls')
                continue
            elif action.replace(" ","") == "3":
                print("You dodge, but Vitreous does nothing!\n")
                input("Press Enter to continue...")
                os.system('cls')
                continue
            else:
                print("Please enter a valid input!\n")
                input("Press Enter to continue...")
                os.system('cls')
                continue
        elif vattack == 10:
            print("Vitreous shoots a fast bolt of aura from his eye and hits you before you can react\n")
            input("Press Enter to continue...")
            os.system('cls')
            HP -= 20
            checkHP(location.StartDungeon)
            continue
    
def checkVitreousHP(HP):
    global VitreousAlive
    if HP <= 0:
        print ("You defeated Vitreous!\n")
        print("Yippee!!!\n")
        VitreousAlive = False

def SwordMasterFight():
    import location
    get_player_weapon_stats()
    global HP
    HP = 100
    global EnemyAlive
    EnemyAlive = True
    EnemyHP = 50
    global speed
    global damage
    print("You have encountered Zoro, the Sword Master!\n")
    input("Press Enter to continue...")
    os.system('cls')
    print("Zoro unsheaths his sword in a swift arc and hits you before you can react.\n")
    input("Press Enter to continue...")
    HP -= 75
    os.system('cls')
    while EnemyAlive == True:
        if location.hasNerves == False:
            print("Your HP = ???/???"
                  "Zoro HP = ??/??")
        elif location.hasNerves == True:
            print("Your HP = {HP}/100"
                  "Zoro HP = {EnemyHP}/50")
        attack = random.randint(1,7)
        if attack in range(1,3):
            print("Zoro holds his sword above his head. What will you do?\n")
            action = input("(1) Attack (2) Block/Parry (3) Dodge\n")
            if action == "1":
                if speed > 0.8:
                    if damage > 15:
                        print("You hit Zoro and stagger him out of his attack!\n")
                        EnemyHP -= damage
                        checkEnemyHP(EnemyHP)
                        input("Press Enter to continue...")
                        os.system('cls')
                        continue
                    else:
                        print("You hit Zoro, but he hit back!")
                        EnemyHP -= damage
                        HP -= 25
                        checkHP(location.Mountain)
                        checkEnemyHP(EnemyHP)
                        input("Press Enter to continue...")
                        os.system('cls')
                        continue
                else:
                    print("You tried to attack Zoro, but you were too slow, and\nhe hit you first!\n")
                    HP -= 25
                    input("Press Enter to continue...")
        if attack in range (4,6):
            print("Hello")
        if attack == 7:
            print("Bye")


def LunarisFight():
    import location
    global EnemyAlive
    EnemyAlive = True
    print("You have encountered Lunaris, the Moonlight Dragon!")