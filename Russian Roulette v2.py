import random
import time

#globals
Game_running = True
Fatal_chamber = random.randint(1,5) #shot fired when fatal chamber hits 0 (goes down by 1 every pull)
turn = True #true = players turn false = opponents turn

def pulled_trigger(target): #checks if the trigger was pulled on the player or the opponent
    global Fatal_chamber
    global Game_running

    Fatal_chamber -= 1

    if Fatal_chamber == 0:
        if target == "player":
            print(scene_change(6))
            Game_running = False
            input("BANG!\n-GAME OVER-")
            breakpoint

        elif target == "opponent":
            print(scene_change(4))
            Game_running = False
            input("BANG!\nYou Win")
            breakpoint
    
    else:
        print("\n*click*")


def Player_turn(action): #processes the player's decision

    if action == 1: #spin
        Fatal_chamber = random.randint(1,5)
        print("\nYou spin the cylander")
        return True #returns true so the player still needs to make a move
    
    elif action == 2: #pull trigger
        print(scene_change(2))
        print("\nYou pull the trigger")

        time.sleep(2)

        pulled_trigger("player")
        return False
    
    elif action == 3: #shoot opponent
        print("\nYou pull the trigger on the opponent")
        print(scene_change(2))

        time.sleep(1)

        pulled_trigger("opponent")
        print("\nYou pull the trigger on yourself")
        
        time.sleep(2) 

        pulled_trigger("player")
        return False
        


def Opponent_turn(action): #processes the opponent's decision

    if action == 1:
        Fatal_chamber = random.randint(1,5)
        print("\nThey spin the cylander...")

        time.sleep(1)

        return False

    elif action == 2:
        print("opponent pulled trigger")

        time.sleep(1)

        pulled_trigger("opponent")
        return True
    
    elif action == 3:
        print("opponent pulls on you")
        print(scene_change(5))

        time.sleep(2)

        pulled_trigger("player")
        print("opponent pulls on themselves")
        print(scene_change(3))

        time.sleep(1)

        pulled_trigger("opponent")
        return True

def scene_change(scene):

    scene1 = """             0
       _____/|\_____
      /      __     \\
     /      /	     \\
    /                 \\
       """ #player turn decision
    
    scene2 = """             0	
       _____/|\_____
      /             \\
     /               \\
    /                 \\
        """ #player takes gun
    
    scene3 = """             0-
       _____/|/_____
      /             \\
     /               \\
    /                 \\
        """ #opponent takes gun
    
    scene4 = """           ###
       _____/|\_____
      /             \\
     /               \\
    /                 \\
        """ #opponent death
    
    scene5 = """             0
       _____/|._____
      /             \\
     /               \\
    /                 \\
        """ #opponent pulls on player
    
    scene6 = """####################
####################
####################
####################""" #player death

    if scene == 1:
        return scene1
    elif scene == 2:
        return scene2
    elif scene == 3:
        return scene3
    elif scene == 4:
        return scene4
    elif scene == 5:
        return scene5
    elif scene == 6:
        return scene6

print("""███████████████████████████████████████████
█▄─▄▄─█▄─█─▄█▄─▄███▄─▄▄─█─▄─▄─█─▄─▄─█▄─▄▄─█
██─▄▄▄██▄─▄███─██▀██─▄█▀███─█████─████─▄█▀█
▀▄▄▄▀▀▀▀▄▄▄▀▀▄▄▄▄▄▀▄▄▄▄▄▀▀▄▄▄▀▀▀▄▄▄▀▀▄▄▄▄▄▀\nRussian Roulette in python\na script by Oli R""")

#main
while Game_running:

    if turn == True:
        print("-Your turn-")
        print(scene_change(1))
        try:
            action = int(input("Enter action (1,2,3):\n1)spin cylander\n2)pull trigger\n3)shoot opponent\n"))
            
            if action != 1 and action != 2 and action != 3: #check if chosen action is valid
                print("\n--invalid response--")
            else:
                turn = Player_turn(action)
        except ValueError:
            print("\n--invalid response--")

    elif turn == False:
        print("-Opponent turn-")
        print(scene_change(3))
        opponent_choice = random.randint(1,3)
        turn = Opponent_turn(opponent_choice)