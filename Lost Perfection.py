import os
import location

def Story():
    os.system('cls')
    print("The Prophecy states that someday, a perfect child will be born.\nThis child will have superhuman abilities and senses, and will\nuse them to defeat Diablo, the evil king of the world.\n")
    input("Press Enter to continue...")
    os.system('cls')
    print("One day, a perfect child named " + name + " was born; The Prophecy\nwas coming true. Unfortunately, Diablo was notified\nof the child's birth, and he immediately killed them...\n")
    input("Press Enter to continue...")
    os.system('cls')
    print(name + "'s soul was split into fragments and distributed to\nDiablo's closest allies. This granted each of them a fraction\nof " + name + "'s power.\n")
    input("Press Enter to continue...")
    os.system('cls')
    print("Luckily, a very small part of " + name + "'s soul remained.\nThis small fragment was implanted in a wooden doll,\nallowing " + name + " to live on.\n")
    input("Press Enter to continue...")
    os.system('cls')
    print("Now, " + name + " wanders the land seeking out the lost fragments\nof their soul. As they defeat Diablo's allies, they\nregain their abilities and senses.\n")
    input("Press Enter to continue...")
    os.system('cls')
    print("Defeating Diablo's allies and regaining the fragments\nof their soul will be very difficult, but " + name + "\nwill regain them all and defeat Diablo no matter the cost.\n")
    input("Press Enter to continue...")
    os.system('cls')

def Intro():
    os.system('cls')
    global name
    name = input("Enter your name: ")
    os.system('cls')
    print("Welcome to Lost Perfection, " + str(name) + "!\nA Text-Based Adventure Game\nMade by Austin DeVore\n")
    input("Press Enter to continue...")
    os.system('cls')
    print("Type 'Save' at any point to save your game!\n")
    input("Press Enter to continue...")
    os.system('cls')
    menuchoice = input("(1) New Game\n"
                       "(2) Load Game\n")
    if menuchoice == "1":
        Story()
        while True:
            introchoice = input("Or will they succeed? Are you up to the task?\nDo you have the courage to fight? (y or n): ")
            if (introchoice.replace(" ","").upper()) == "N":
                os.system('cls')
                print("Too bad.\n")
                input("Press Enter to continue...")
                exit()
            elif (introchoice.replace(" ","").upper()) == "Y":
                break
            else:
                os.system('cls')
                print("Please enter a valid input.\n")
                continue
        location.StartDungeon()
    elif menuchoice == "2":
            os.system('cls')
            try:
                location.player.LoadGame()
            except:
                os.system('cls')
                print("No saved data found!\n")
                input("Press Enter to continue...")
                Intro()

Intro()