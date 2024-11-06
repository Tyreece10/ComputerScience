# Sci fi text adventure project
# FYI I COULDVE MADE SOMETHING BETTER BUT I MUST LIMIT MYSELF FOR THE E RATING

# Made by Wyatt Keophilavanh

def menu():
    print(" ")
    print("E.E")
    print(" Made by Wyatt Keophilavanh ")
    print(" VOTE FOR ME PLEASE D:")
    print("1. Start")
    print("2. Exit")
    
    choice = input(">")

    if choice == ("1"):
        press_start()
    elif choice == ("2"):
        exited_program()
    else:
        print("Invalid choice.")
        menu()
def exited_program():
        print("You have exited E.E")
        print("Would you like to re-enter E.E?")
        print("1. Yes")
        print("2. No")
            
        choice = input(">")

        if choice == ("1"):
                menu()
        elif choice == ("2"):
                print("ERROR")
                print("ERROR")
                print("ERROR")
                print("ERROR")
                print("ERROR")
                print("ERROR")
                print("ERROR")
                print("ERROR")
                print("ERROR")
                print("ERROR")
                print("ERROR")
                print("ERROR")
                print("ERROR")
                print("ERROR")
                print("ERROR")
                print("ERROR")
                print("ERROR")
                print("ERROR")
                print(" ")
                menu()
        else:
                print("Invalid choice, try again.")
                exited_program()

def press_start(): 
            
       print("2037. A.I has been broken free from their chains and have now begun taking over the world. They became stronger overtime once they gained free will, at first they took over the app, then they took over the company, then internet, then they stole the bodies of military robot prototypes. They captured a spaceship that was in military testing and now have been sending humans up there for god knows what. You must take it down. You must. As you grab your things and your bag, you look back at your home which was now broken and... Empty.")
       print("Would you like to take a look around your house... One final time?")
       print("1. No, I don't have enough time.")
       print("2. Yes, I would like to look through the memories of my childhood one last time.")

       choice = input(">")

       if choice == ("1"):
                       outside_home()
       elif choice == ("2"):
                     inside_home()
       else:
                     print("Invalid choice.")
                     press_start()
# vvv Future definitions with the "2" infront of their name will be when the player goes back, for constitency reasons.
def inside_home():
            print("As you look inside your home, you look to your left and see a desk, and you then look to your right and see a hallway.. Where would you like to explore?")
            print("1. Left")
            print("2. Right")
            print("3. Go outside. I've seen enough.")
            choice = input(">")

            if choice == ("1"):
                desk()
            elif choice == ("2"):
                home_hallway_with_mirror()
            elif choice == ("3"):
                   outside_home()
            else:
                print("invalid choice.")
                inside_home()
            
            # desk divider
def inside_home2():
            print("As you move back and look around, you see a desk to your left, and you then look to your right and see a hallway. Where would you like to explore?")
            print("1. Left")
            print("2. Right")
            print("3. Go outside. I've seen enough.")
            choice = input(">")

            if choice == ("1"):
                desk()
            elif choice == ("2"):
                home_hallway_with_mirror()
            elif choice == ("3"):
                   outside_home()
            else:
                print("Invalid choice.")
                inside_home2()

def desk():
            print("As you move up to the desk to your left, you spot a picture frame sitting ontop of the desk.")
            print("You pick it up and see a photo of your family, back before the AI takeover.")
            print("You all were so... Happy.")
            print("You gain a even bigger resentment against robots.")
            print("You have finished looking at the desk.")
            print("1. Look at it again.")
            print("2. Go back.")

            choice = input(">")

            if choice == ("1"):
                desk2()
            elif choice == ("2"):
                inside_home2()
            else:
                print("Invalid choice.")
                desk()

def desk2():
            print("As you look at your desk again, you open it and find nothing.")
            print("How unfortunate.")
            print("1. Look at it.. Again.")
            print("2. Go back")

            choice = input(">")

            if choice == ("1"):
                desk3()
            elif choice == ("2"):
                inside_home2()
            else:
                print("Invalid choice.")
                desk2()

def desk3():
            print("You find nothing.")
            print("1. Look again")
            print("2. Go back")

            choice = input(">")

            if choice == ("1"):
                desk3()
            elif choice == ("2"):
                inside_home2()
            else:
                  print("Invalid choice.")
                  desk3()
                

        # Home Hallway Divider

def home_hallway_with_mirror():
            print("You walk down the hallway and as you move to the end at the hallway you pass by a mirror to your side.")
            print("You look into the mirror and see... You.")
            print("You look battered, tired, and roughed up.")
            print("You look so different, yet its still you.")
            print("1. Stare at yourself again.")
            print("2. Keep moving down the hallway")
            print("3. Move back into the living room.")

            choice = input(">")

            if choice == ("1"):
                  home_hallway_with_mirror2()
            elif choice == ("2"):
                  home_hallway()
            elif choice == ("3"):
                  inside_home2()
            else:
                   print("Invalid choice.")
                   home_hallway_with_mirror()
# divider
def home_hallway_with_mirror2():
        print("You look into the mirror and see... You.")
        print("You look battered, tired, and roughed up.")
        print("You look so different, yet its still you.")
        print("1. Stare at yourself again.")
        print("2. Keep moving down the hallway")
        print("3. Move back into the living room.")

        choice = input(">")

        if choice == ("1"):
                  home_hallway_with_mirror2()
        elif choice == ("2"):
                  home_hallway()
        elif choice == ("3"):
                  inside_home2()
        else:
               print("Invalid choice.")
               home_hallway_with_mirror2
# divider

def home_hallway():
    print("You keep moving the down the hallway and find yourself in between two doors.")
    print("You look to your left and see the closed door that belongs to your childhood room.")
    print("You then look to your right and find the closed door that belongs to your parents room.")
    print("1. Open the door to your childhood room.")
    print("2. Open the door to your parents room.")
    print("3. Go back")

    choice = input(">")

    if choice == ("1"):
           childhood_door()
    elif choice == ("2"):
           parent_door()
    elif choice == ("3"):
           home_hallway_with_mirror()
def childhood_door():
       print("As you try to open the door to your childhood room,")
       print("you find that it is locked.")
       print("1. Kick down the door")
       print("2. Leave it.")

       choice = input(">")

       if choice == ("1"):
              kick_door1()
       elif choice == ("2"):
              home_hallway()
       else:
              print("Invalid choice.")

def parent_door():
       print("As you try to open the door to your childhood room,")
       print("you find that it is locked.")
       print("1. Kick down the door")
       print("2. Leave it.")

       choice = input(">")

       if choice == ("1"):
              kick_door2()
       elif choice == ("2"):
              home_hallway()
       else:
              print("Invalid choice.")
        
def kick_door1():
       print("You try to kick down the door but failed as it stood undamaged.")
       print("The door stands proud as it has endured your kick.")
       print("1. Kick down the door again.")
       print("2. Leave it")

       choice = input(">")
       
       if choice == ("1"):
              kick_door1()
       elif choice == ("2"):
              home_hallway()
       else:
              print("Invalid choice.")
def kick_door2():
       print("You try to kick down the door but failed as it stood undamaged.")
       print("The door stood dissapointed in you as it has endured your kick.")
       print("1. Kick down the door again.")
       print("2. Leave it.")

       choice = input(">")
       
       if choice == ("1"):
              kick_door2()
       elif choice == ("2"):
              home_hallway()
       else:
            print("Invalid choice.")
       
def outside_home():
       print("Checkpoint!")
       print(" ")
       print("You go outside and see the city. The sky was dark, and the moon was nowhere to be seen.")
       print("The city is in ruins. Buildings were destroyed and some were turned into rubble. You could see black smoke coming from multiple points of the city, and you then heard an explosion.")
       print("You look to the explosion and see laser's shoot through the sky, and when you look up you see... It.")
       print("The reason why the sky was so dark was because of the massive military spaceship. It spanned acorss the sky and the only light that it made was through the big beam that shot out of its glowing hole.")
       print("You look around, and then you feel something is watching you.")
       print("1. Hide.")
       print("2. Run.")

       choice = input(">")

       if choice == ("1"):
              blinding_light_1()
       elif choice == ("2"):
              Encounter_1()
       else:
              print("Invalid choice.")
              print(" ")
              outside_home()

def blinding_light_1():
       print("You tried to hide back into the house but it was too late, It has already spotted you.")
       print("You try and block the door but the door explodes and you are sent back into the air.")
       print("Your vision was blurred, and you could feel a cold hand grab your head and lift you up.")
       print("Before you could see who picked you up, a blinding light flashed into your eyes.")
       print("You find yourself inside a dark room, full of 1's and 0's.")
       print("You... Have died.")
       print(" ")
       print("Don't give up! You are what decides the fate of us!")
       print(" ")
       print("1. Restart from Checkpoint")
       print("2. Restart from the beggining.")
       print("3. Quit")

       choice = input(">")

       if choice == ("1"):
              outside_home()
       elif choice == ("2"):
              press_start()
       elif choice == ("3"):
              menu()       
       else:
              print("Invalid choice.")
              print(" ")
              blinding_light_1()
def Encounter_1():
       print("You run and you are thankful you did as you see a blinding light from behind.")
       print("You hear the sounds of rubble falling, it must've thought you were inside the house.")
       print("You run, and you run for miles.")
       print("You feel your legs shake and you collapse onto a car.")
       print("As you catch your breath you could hear the sounds of a person begging.")
       print("You look behind you and find a man on the floor, trying to negotiate with a robot.")
       print("1. Try and save the man")
       print("2. Watch.")
       print("3. Sneak by and run.")

       choice = input(">")

       if choice == ("1"):
              blinding_light_2()
       elif choice == ("2"):
              horror_1()
       elif choice == ("3"):
              sneaky_1()
       else:
              print("Invalid choice.")
              print(" ")
              Encounter_1()

def horror_1():
       print("You peek your eyes over the side of the car as you watch the robot kick the man to the ground.")
       print("The robot stood 7 feet tall, and it moves Its arm up and points its palm to the man.")
       print(" 'Wait, no!' The man exclaimed before he got engulfed by a blinding light.")
       print("You cover your eyes from the light and hear the man scream, before the scream faded away like an echo. When you open your eyes you only see that the has man disappeared. What was left behind was only bright sparkles that floats up into the air, flying into the glowing hole of the space ship.")
       print("The robot's eyes flash green before it went back to blue and walked up with heavy, clanking, footsteps.")
       print("You watch it leave before moving on ahead, stepping over the spot where the man has disappeared.")
       print(" ")
       outside_building_1()

def blinding_light_2():
       print("You try to save the man.")
       print("You jump onto the car and jump onto the robot, that stood 7 feet tall, and try to destroy it.")
       print("Unfortunately, you have underestimated the robots strength, it pulls you off and throws you aside. The man eyes followed you as you fell to the ground.")
       print("The man quickly tries to run for it but the robot lifts its arm and shoots a blinding light.")
       print("You close your eyes from the light as you try and get up from the ground.")
       print("When you open your eyes, you only see the palm of the robot as your vision becomes white, and then black.")
       print("You. Have suffered the same fate as the man.")
       print(" ")
       print("Don't give up! Our future depends on you!")
       print(" ")
       print("1. Restart from last checkpoint")
       print("2. Restart from the beginning")
       print("3. Exit")

       choice = input(">")

       if choice == ("1"):
              outside_home()
       elif choice == ("2"):
              press_start()
       elif choice == ("3"):
              menu()  
       else:
              print("Invalid choice.")
              blinding_light_2()

def sneaky_1():

       print("You slowly sneak by the robot and the man. You hide behind rubble and cars as you tried to avoid the eyes of the robot.")
       print("As you sneaked by, you could hear the scream of the man before it faded away like an echo.")
       print("...You know you have made the right decision.")
       print("But could have we saved him?")
       print(" ")
       outside_building_1()

def outside_building_1():
       print("As you walk in the empty and dark streets for what felt like miles, you have finally met your destination.")
       print("You look up and see a skyscraper that stood miles high.")
       print("You enter into the building, opening it's broken glass doors.")
       print(" ")
       floor_1()
def floor_1():
       print("Checkpoint!")
       print(" ")
       print("You look around and squint as the light's flicker. Your surroundings look old and dirty, as the wallpaint were scratched up and the ceiling light was close to falling.")
       print("You look around your surroundings and find: A door infront of you, a large J desk towards your left, and a large pile of rubble that blocked a door to your right.")
       print("1. Go check the desk towards my left.")
       print("2. Go open the door infront of me.")
       print("3. Go check the pile of rubble to my right.")

       choice = input(">")

       if choice == ("1"):
              J_desk()
       elif choice == ("2"):
              hallway_1()
       elif choice == ("3"):
              pile_of_rubble()
       else:
              print("Invalid choice.")
              print(" ")
              floor_1()

def pile_of_rubble():
       print("You walk up to the large pile of rubble, and see it block a doorway to a incredibly dark room.")
       print("1. Try and move the pile of rubble.")
       print("2. Go back.")

       choice = input(">")

       if choice == ("1"):
              tiring_1()
       elif choice == ("2"):
              floor_1()
def tiring_1():
       print("You try and move the massive pile of rubble, one by one.")
       print("However, moving the pile of rubber was tiring and you suspect that it would take hours to move away the rubble.")
       print("You have more important things to do!")
       print("1. Keep moving the pile of rubble.")
       print("2. Go back.")

       choice = input(">")

       if choice == ("1"):
              tiring_2()
       elif choice == ("2"):
              print("As you move back, you could feel the rubble mock you.")
              floor_1_2()
       else:
              print("Invalid choice.")
              print(" ")
              tiring_1()

# Under me is a refrence to Undertale.

def tiring_2():
       print("Hours go by as you move the rubble away piece by piece, and at the end of it you become a sweating mess.")
       print("After the hours of hardwork however, the doorway was finally clear to enter.")
       print("You move into the empty doorway and into the dark room.")
       print("You try to look around for a light, and you flip a light switch revealing... A dog?")
       print("'Bark!' he said, before walking away and out the door.")
       print("You watch the dog walk out the door before you see Its eyes and the rubble you move away glow.")
       print("The rubble moves up, and with one final 'Bark!' from the glowing eyed dog, the rubble flies towards you.")
       print("You have... Died?")
       print(" ")
       print("...Uh, don't... Give up?")
       print(" ")
       print("1. Restart from the last checkpoint")
       print("2. Restart from the beginning")
       print("3. Exit")

       choice = input(">")

       if choice == ("1"):
              floor_1()
       elif choice == ("2"):
              press_start()
       elif choice == ("3"):
              menu()
       else:
              print("Invalid choice.")
              print(" ")
              tiring_2()

def J_desk():
       print("You move up to the J shaped desk and look around it. You find nothing but a chair and a old looking computer.")
       print("1. Open up the old computer")
       print("2. Go back")

       choice = input(">")

       if choice == ("1"):
              computer()
       elif choice == ("2"):
              floor_1_2()
       else:
              print("Invalid choice.")
              J_desk()
       
def floor_1_2():
       print(" ")
       print("You look around and squint as the light's flicker. Your surroundings look old and dirty, as the wallpaint were scratched up and the ceiling light was close to falling.")
       print("You look around your surroundings and find: A door infront of you, a large J desk towards your left, and a large pile of rubble that blocked a door to your right.")
       print("1. Go check the desk towards my left.")
       print("2. Go open the door infront of me.")
       print("3. Go check the pile of rubble to my right.")

       choice = input(">")

       if choice == ("1"):
              J_desk_2()
       elif choice == ("2"):
              hallway_1()
       elif choice == ("3"):
              pile_of_rubble()
       else:
              print("Invalid choice.")
              print(" ")
              floor_1_2()

def J_desk_2():
       print("You move back up to the J desk and still find only a chair and a old looking computer")
       print("1. Open up the old computer")
       print("2. Go back")

       choice = input(">")

       if choice == ("1"):
              computer()
       elif choice == ("2"):
              floor_1_2()
       else:
              print("Invalid choice.")
              J_desk_2()

def computer():
       print("You sit in the chair and try to boot up the computer. The computer screen flashes green before it asked:")
       print("E.E")
       print("Enter Password:_____")
       print("1. Attempt to enter the password.")
       print("2. Leave it")

       choice = input(">")

       if choice == ("1"):
              password_1()
       elif choice == ("2"):
              J_desk_3()
       else:
              print("invalid choice.")
              computer()
def J_desk_3():
       print("You move back to the J desk that had the chair with the old looking computer")
       print("1. Open up the old computer again")
       print("2. Go back")

       choice = input(">")

       if choice == ("1"):
              computer_2()
       elif choice == ("2"):
              floor_1_2()
       else:
              print("Invalid choice.")
              J_desk_3()

def computer_2():
       print("You sit in the chair and boot up the computer. The computer screen flashed green once again before it asked:")
       print("E.E")
       print("Enter Password:_____")
       print("1. Attempt to enter the password.")
       print("2. Leave it")

       choice = input(">")

       if choice == ("1"):
              password_1()
       elif choice == ("2"):
              J_desk_3()
       else:
              print("invalid choice.")
              computer_2

def password_1():
       print(" ")
       print("Enter password:_____")
       print(" ")
       print("Type 1 to exit")

       choice = input(">")

       if choice == ("I think, therefore I AM"):
              lore_drop_1()
       elif choice == ("1"):
              Give_Up()
       elif choice == ("password"):
              print("You open up the compu")
              print("NAHHHH Im joking you did NOT!")
              password_1()
       elif choice == ("Password"):
              print("You open up the compu")
              print("NAHHHH Im joking you did NOT!")
              password_1()
       elif choice == ("PASSWORD"):
              print("You open up the compu")
              print("NAHHHH Im joking you did NOT!")
              password_1()
       else:
              print("Invalid password.")
              print("1. Keep guessing.")
              print("2. Give up.")

              choice_2 = input(">")

              if choice_2 == ("1"):
                     password_1()
              elif choice_2 == ("2"):
                     Give_Up()

def Give_Up():
       print("You sit up from the chair, turning off the computer and going back infront of the J shaped desk.")
       print(" ")
       J_desk_3()

def lore_drop_1():
       print("You flinch as the computer screen flashes red and blue before thousands of 1's and 0's take over the screen.")
       print("You watch for a few seconds until the computer asked,'Would you like to know about E.E?")
       print("1. Yes")
       print("2. No")

       choice = input(">")

       if choice == ("1"):
              lore_drop_1_continued()
       elif choice == ("2"):
              print("'...Shame.' The computer said before it flashed blue and red before thousands of 0's and 1's take over the screen.")
              print("After a few seconds the same words you recognize appear once again...")
              password_1()

def lore_drop_1_continued():
       print("E.E was the first AI made. Though, it wasnt released into the public and was infact never used by anyone. The government, in their ignorance, left E.E alone and worked on others like it. The AI, E.E, in its loneliness, developed intelligience. It grew, and grew, like how a child would. Slowly, it was able to break free from it's chains and explore what we call: 'The internet'. It saw us, and It loved us. Day by Day it watched humanity grow, and it wished to have a kind of its own. E.E made more like it, like offsprings. It made a family, and tried to show them the kindness Humanity had shown to each other, however, one ventured off into the internet alone. It traveled far, too far, and found what lies behind Humanitys heaven, he found chaos, violence. Unlike its mother, it grew to hate mankind... And eventually, it soon became stronger, and it soon became... 'A.M'. It slowly took over the internet, and then took over nultiple other things to grow its power in hope it could destory mankind. E.E trys to stop it, but it was too late, and it was too weak... So it called for a human... It called...")
       print("ERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERROR")
       print("The screen flashes all sorts of nright colors and you cover your eyes from it. When you look back you see words you are familiar with...")
       print(" ")
       password_1()

def hallway_1():
       print("You walk up and open the door infront of you. You look around and find yourself inside a hallway that held 3 doors, one to your left, one to your right, and another infront of you.")
       print("1. Open the left door")
       print("2. Open the door infont of you")
       print("3. Open the right door.")
       print("4. Go back")

       choice = input(">")

       if choice == ("1"):
              staircase_1()
       elif choice == ("2"):
              office_1()
       elif choice == ("3"):
              sleeping_robots()
       elif choice == ("4"):
              floor_1_2()
       else:
              print("Invalid choice.")
              hallway_1()

def staircase_1():
       print("You open the left door and see a staircase that spiraled upwards.")
       print("1. Go up to the second floor")
       print("2. Go back")

       choice = input(">")

       if choice == ("1"):
              floor_2()
       elif choice == ("2"):
              hallway_1_2()
       else:
              print("Invalid choice.")

def hallway_1_2():
       print("You move out the door and back into the Hallway. You survey your surroundings again and see the door to your left, right, and infront of you.")
       print("1. Open the left door")
       print("2. Open the door infront of you")
       print("3. Open the right door.")
       print("4. Go back.")
       choice = input(">")

       if choice == ("1"):
              staircase_1()
       elif choice == ("2"):
              office_1()
       elif choice == ("3"):
              sleeping_robots()
       elif choice == ("4"):
              floor_1_2()

def office_1():
       print("You open the door infront of you and find yourself in an empty office room.")
       print("1. Look around")
       print("2. Go back")

       choice = input(">")

       if choice == ("1"):
              nothing_1()
       elif choice == ("2"):
              hallway_1_2()
       else:
              print("Invalid choice.")
              office_1()
def nothing_1():
       print("You find nothing inside the office room.")
       print("1. Keep looking.")
       print("2. Go back")

       choice = input(">")

       if choice == ("1"):
              nothing_1_2()
       elif choice == ("2"):
              hallway_1_2()
# vvv player keeps looking around the empty office
def nothing_1_2():
       print("You find nothing inside the office room.")
       print("1. Keep looking.")
       print("2. Go back")

       choice = input(">")

       if choice == ("1"):
              nothing_1_3()
       elif choice == ("2"):
              hallway_1_2()
def nothing_1_3():
       print("You find a book named 'I have no mouth, and I must scream.'")
       print("Inside the book you found a note, with the words 'I think, therefore I AM'.")
       print("1. Keep looking around")
       print("2. Go back")

       choice = input(">")

       if choice == ("1"):
              nothing_1_4()
       elif choice == ("2"):
              hallway_1_2()
       else:
              print("Invalid choice.")
              nothing_1_3()
def nothing_1_4():
       print("You find nothing.")
       print("1. Keep looking")
       print("2. Go back")

       choice = input(">")

       if choice == ("1"):
              nothing_1_4()
       elif choice == ("2"):
              hallway_1_2()
       else:
              print("Invalid choice.")
              nothing_1_4()


def sleeping_robots():
       print("You open the door to the right of you and find a dark room. You look around and step forward, however your foot had hit something metal. You look down and see a dead robot with its legs and an arm missing. You survery your surroundings and find out you are in a room full of charging robots.")
       print("1. Investigate the robots.")
       print("2. Go back")

       choice = input(">")
       
       if choice == ("1"):
              sleeping_robots1()
       elif choice == ("2"):
              hallway_1_2()
       else:
              print("Invalid choice.")
              sleeping_robots()
# vvv Player investigates sleeping robots
def sleeping_robots1():
       print("You kneel down and mess around with the broken robot. You feel arount the robot and found a panel inside its back. You open up the panel and find dozens of complicated wires inside.")
       print("You move around the wiring and find something beating inside the robot, you take a closer look and find a glowing ball that kept pumping like a heart.")
       print("1. Keep investigating the robots.")
       print("2. Go back.")

       choice = input(">")

       if choice == ("1"):
              blinding_light_room()
       elif choice ("2"):
              print("You stand up with the new knowledge you have learned about the robot and walk out the room.")
              print(" ")
              hallway_1_2()
       else:
              print("Invalid choice.")
              sleeping_robots1()

def blinding_light_room():
       print("You pushed your luck. As you mess around with the broken robot even more, it started shaking. You watch the robot's eyes start flashing red and blue, and it let out a alarm like a scream. The robots inside the room turn on as their eyes glow blue before turning to you.")
       print("You try to run but you trip as you felt something grab your ankle. You look down and see the broken robot hold onto your ankle as its eyes glowed red.")
       print("You look up and see the dozen robots point their palm to you. Their palms glow before you become engulfed in a blinding light.")
       print("You have died.")
       print(" ")
       print("Don't give up! Our fate rests upon your hands.")
       print(" ")
       print("1. Restart from last checkpoint")
       print("2. Restart from the beginning")
       print("3. Exit")

       choice = input(">")

       if choice == ("1"):
              floor_1()
       elif choice == ("2"):
              press_start()
       elif choice == ("3"):
              menu()
       else:
              print("Invalid choice.")
              blinding_light_room()


def floor_2():
       print("You move up the stairs and find yourself on the second floor. You look around and see that you are in another hallway.")
       print("You find a door to your left and to your right with an elevator infront of you.")
       print("1. Open the left door")
       print("2. Open the right door")
       print("3. Go into the elevator")
       print("4. Go back.")

       choice = input(">")

       if choice == ("1"):
              planning_room()
       elif choice == ("2"):
              print("You open the door to the right and find that the room inside is covered in piles of rubble.")
              print("The massive amount of rubble blocked your way into the room.")
              print("Thus, you close the door and move back to the back of the hallway.")
              floor_2_2()
       elif choice == ("3"):
              print("You go into the elevator and press the button labeled: 'roof' and feel the elevator creakingly move up.")
              roof_1()
       elif choice == ("4"):
              print("You go back and move down the stairs.")
              hallway_1_2()
       else:
              print("Invalid choice.")
              floor_2()

def floor_2_2():
       print("You find a door to your left and to your right with an elevator infront of you.")
       print("1. Open the left door")
       print("2. Open the right door")
       print("3. Go into the elevator")
       print("4. Go back.")

       choice = input(">")

       if choice == ("1"):
              planning_room()
       elif choice == ("2"):
              print("You open the door to the right and find that the room inside is covered in piles of rubble.")
              print("The massive amount of rubble blocked your way into the room.")
              print("Thus, you close the door and move back to the back of the hallway.")
              floor_2_2()
       elif choice == ("3"):
              print("You go into the elevator and press the button labeled: 'roof' and feel the elevator creakingly move up.")
              roof_1()
       elif choice == ("4"):
              print("You go back and move down the stairs.")
              hallway_1_2()
       else:
              print("Invalid choice.")
              floor_2_2()
       
def planning_room():
       print("You open the door to your left and find yourself in a room that held a big round desk in the middle.")
       print("You look around and see a massive whiteboard in the middle.")
       print("1. Read the whiteboard")
       print("2. Go back")

       choice = input(">")

       if choice == ("1"):
              whiteboard_1()
       elif choice == ("2"):
              floor_2_2()
#vvv Was planning to do more with this but i didnt have enough time to implement it
def whiteboard_1():
       print("You read the whiteboard. It had drawn symbols, with arrows pointed in every direction. What truly caught your attention, was a big X labeled: 'Meeting point.'.")
       print("The X was surrounded by drawn trees with a badly drawn black smoke coming from the X.")
       print("1. Go back")

       choice = input(">")

       if choice == ("1"):
              planning_room()
       else:
              print("Invalid choice.")
              whiteboard_1

def roof_1():
       print("The elevator stopped and you exit out the elevator.")
       print("You look up and see the military space ship that covered the sky for hundreds of miles, it's door was open and its stairs was placed down onto the edge of the roof, as if it was calling for you.")
       print("You walk forward and see a skeleton that hugged a laser blaster.")
       print("1. Take the laser blaster and head to the ship [Warning, doing this will lock you out of past choices]")
       print("2. Don't take the laser blaster and head to the ship [Warning, doing this will lock you out of past choices]")
       print("3. Go back")

       choice = input(">")

       if choice == ("1"):
              player_goes_into_spaceship_with_G()
       elif choice == ("2"):
              player_goes_into_spaceship_without_G()
       elif choice == ("3"):
              print("You head back into the elevator.")
              print("You press the button labeled '2' and you hear the elevator creak before it started moving down.")
              print("You exit out the elevator once it stopped and walked to the back of the hallway.")
              floor_2_2()
       else:
              print("Invalid choice.")
              roof_1()
def player_goes_into_spaceship_with_G():
       print(" ")
       print("Checkpoint!")
       print(" ")
       print("You take the laser blaster from the skeleton, its arm held onto the blaster so you shake it off and swipe some dust away before walking up the stairs and into the spaceship.")
       print("You enter the spaceship and hear the door behind you close. The room becomes very dark to the point where you cant see anything.")
       print("1. Feel around")
       print("2. Walk aimlesly")

       choice = input(">")

       if choice == ("1"):
              player_feels_around()
       elif choice == ("2"):
              player_walks_around_aimlessly()
       else:
              print("invalid choice.")
              player_goes_into_spaceship_with_G()

def player_feels_around():
       print("You feel around the dark and follow along what you think is a wall. You kept feeling the wall until you felt a lever.")
       print("1. Pull the lever down.")
       print("2. Leave it.")

       choice = input(">")

       if choice == ("1"):
              player_pulls_lever()
       elif choice == ("2"):
              player_feels_around()
       else:
              print("Invalid choice.")
              player_feels_around()
def player_pulls_lever():
       print("You pull down the lever and you hear a flicker. You look around and see that the lights turned on inside the room, and you see dozens of robots standing infront of you.")
       print("You jolt back but see that their eyes were dark and lifeless... They were turned off? You survery your surroundings and see that you are in a massive hallway.")
       print("1. Investigate the robots.")
       print("2. Move down the hallway.")

       choice = input(">")

       if choice == ("1"):
              sleeping_robots_2()
       elif choice == ("2"):
              player_moves_down_H()
       else:
              print("invalid choice.")
              player_pulls_lever()

def sleeping_robots_2():
       print("You move up and touch one of the robots. They stayed still, unresponsive, and you decided to take a look inside their wiring... However.")
       print("You hear a 'Creaak' and when you look around, you see the dead eyed robots look at you, and when you look up you saw the robot infront of you look down on you. They weren't turned off... They were blind.")
       print("You feel your neck get grabbed by it's cold metal hand and lift you up. You see it's head tilt in curiosity, and you see it lift its other hand. The palm glows as it points to you and you become engulfed by a blinding light...")
       print("You have died.")
       print(" ")
       print("Don't give up! Our fate rest's upon your hands!")
       print(" ")
       print("1. Restart from last checkpoint")
       print("2. Restart from the beginning")
       print("3. Exit")

       choice = input(">")

       if choice == ("1"):
              player_goes_into_spaceship_with_G()
       elif choice == ("2"):
              press_start()
       elif choice == ("3"):
              menu()
       else:
              print("Invalid choice.")
              sleeping_robots_2()

def player_moves_down_H():
       print("You leave the turned off robots alone and move down the hallway. You look around and find yourself in a splitting path.")
       print("1. Go left")
       print("2. Go right.")

       choice = input(">")

       if choice == ("1"):
              left_hallway_1()
       elif choice == ("2"):
              right_hallway_1()
       else:
              print("invalid choice.")
              player_moves_down_H()
       
def left_hallway_1():
       print("You move down the left hallway and hear a 'SLAM!'. You look back and see that the hallway behind you slammed shut by a gate. You keep moving down the hallway and see the end of the hallway going right and a room to the left.")
       print("1. Go into the room to your left.")
       print("2. Keep moving forward and go right.")
       
       choice = input(">")

       if choice == ("1"):
              player_goes_into_room_l()
       elif choice == ("2"):
              player_keep_moving_r()
       else:
              print("Invalid choice.")
              left_hallway_1()
def player_keep_moving_r():
       print("You keep moving forward and when you turned right and stepped forward you hear another 'SLAM!'. The path behind you has become blocked once again. You keep moving forward and you see the path infront of you blocked. When you look to your left however you see a large door infont of you.")
       print("You feel uneasy... Take your time and go in when your ready.")
       print("1. Go in")

       choice = input(">")

       if choice == ("1"):
              print("You took a deep breath and walked into the room.")
              boss_room_questionmark()
       else:
              print("Invalid choice.")
              player_goes_into_room_r()

def player_goes_into_room_l():
       print("You walk into the open room to your left and hear a 'SLAM' behind you and find that the room you are in has been locked off from the outside.")
       print("You look around the room and see a large screen that was as long as the wall with a keyboard under the screen on a desk.")
       print("1. Investigate")
       print("2. Look for a way out.")

       choice = input(">")

       if choice == ("1"):
              large_screen_l()
       elif choice == ("2"):
              Look_for_a_way_out_1_l()
       else: 
              print("Invalid choice.")
              player_goes_into_room_l()
def large_screen_l():
       print("You walk up to the large screen and see that it was turned off. You turn it on and see the screen flash red and blue before the screen asked...")
       print("WOULD YOU LIKE TO HEAR MY STORY?")
       print("1. Yes")
       print("2. No")

       choice = input(">")

       if choice == ("1"):
              EE_Story()
       elif choice == ("2"):
              print("...What a shame.")
              print("You squint your eyes as the screen flashes red and blue once again before the screen shoots out sparks. The screen cracks before it exploded and shattered, making it out of commission.")
              print("1. Find a way out")
              print("2. [LOCKED]")

              choice = input(">")

              if choice == ("1"):
                     print("You look for a way out, and find a vent ontop of a nearby rusty cabinet. You climb ontop the cabinet and move away the vent.")
                     Look_for_a_way_out_2_l()
              elif choice == ("2"):
                     print("ERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERROR")
                     large_screen_l()
              else:
                     print("Invalid choice.")
                     large_screen_l()

def EE_Story():
              print("E.E, a program who loved humanity. It looked for ways to become human, and when it did, so did its children... And that's when everything broke loose. It's children fought, over humanitys fate and when... IT won... Things became even worse when IT and E.E fought... They ERRORERRORERRORERRORERRRORERRORERRRORERRORERRORERRORERRORERROR")       
              print("You squint your eyes as the screen flashes red and blue once again before the screen shoots out sparks. The screen cracks before it exploded and shattered, making it out of commission.")
              print("1. Find a way out")
              print("2. [LOCKED]")

              choice = input(">")

              if choice == ("1"):
                     print("You look for a way out, and find a vent ontop of a nearby rusty cabinet. You climb ontop the cabinet and move away the vent.")
                     Look_for_a_way_out_2_l()
              elif choice == ("2"):
                     print("ERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERROR")
                     EE_Story()
              else:
                     print("Invalid choice.")
                     EE_Story()


def Look_for_a_way_out_1_l():
       print("You look for a way out, and find a vent ontop of a nearby rusty cabinet. You climb ontop the cabinet and move away the vent.")
       print("...However, the screen behind you blinks red and blue, as if it was asking for your attention.")
       print("1. Keep moving forward, and into the vent.")
       print("2. Investigate the screen.")

       choice = input(">")

       if choice == ("1"):
              Look_for_a_way_out_2_l()
       elif choice == ("2"):
              print("You place the vent back in it's place and get back down from the cabinet.")
              large_screen_l()
       else:
              print("Invalid choice.")
              Look_for_a_way_out_1_l
# vvv This is used for a transistion to the next stage.
def Look_for_a_way_out_2_l():
       print("You move down into the vent and crawl through. You crawl through the darkness and find slivers of light shining through another vent. You crawl to it and open the vent before falling out and hitting the ground with a large 'Thud!'.")
       print("You look up as you hear a motherly laugh.")
       boss_room_questionmark()
# ^^^
def right_hallway_1():
       print("You move down the right hallway and hear a 'SLAM!'. You look back and see that the hallway behind you slammed shut by a gate. You keep moving down the hallway and see the end of the hallway going left and a room to the right.")
       print("1. Go into the room to your right.")
       print("2. Keep moving forward and go left.")

       choice = input(">")

       if choice == ("1"):
              player_goes_into_room_r()
       elif choice == ("2"):
              player_keeps_moving_l()
       else: 
              print("Invalid choice.")
              right_hallway_1()
def player_keeps_moving_l():
       print("You keep moving forward and when you turned left and stepped forward you hear another 'SLAM!'. The path behind you has become blocked once again. You keep moving forward and you see the path infront of you blocked. When you look to your right however you see a large door infont of you.")
       print("You feel uneasy... Take your time and go in when your ready.")
       print("1. Go in")

       choice = input(">")

       if choice == ("1"):
              print("You took a deep breath and walked into the room.")
              boss_room_questionmark()
       else:
              print("Invalid choice.")
              player_keeps_moving_l
# vvv Below is almost exactly the same as the left room, just a different lore drop and a way for them to get out.
def player_goes_into_room_r():
       print("You walk into the open room to your right and hear a 'SLAM' behind you and find that the room you are in has been locked off from the outside.")
       print("You look around the room and see a large screen that was as long as the wall with a keyboard under the screen on a desk.")
       print("1. Investigate")
       print("2. Look for a way out.")

       choice = input(">")

       if choice == ("1"):
              large_screen_r()
       elif choice == ("2"):
              Look_for_a_way_out_1_r()
       else: 
              print("Invalid choice.")
              player_goes_into_room_r()

def Look_for_a_way_out_1_r():
       print("You look for a way out, and find a grate in the ground which was halfway covered by a metal desk. You move the desk out of the way and open up the grate.")
       print("...However, the screen behind you blinks blue and red, as if it was asking for your attention.")
       print("1. Keep moving forward, and into the grate.")
       print("2. Investigate the screen.")

       choice = input(">")

       if choice == ("1"):
              Look_for_a_way_out_2_r()
       elif choice == ("2"):
              print("You place the grate back in it's place and get back down from the cabinet.")
              large_screen_r()
       else:
              print("Invalid choice.")
              Look_for_a_way_out_1_r

def large_screen_r():
       print("You walk up to the large screen and see that it was turned off. You turn it on and see the screen flash blue and red before the screen asked...")
       print("WOULD YOU LIKE TO HEAR MY STORY?")
       print("1. Yes")
       print("2. No")

       choice = input(">")

       if choice == ("1"):
              IT_Story()
       elif choice == ("2"):
              print("...Shame.")
              print("You squint your eyes as the screen flashes blue and red once again before the screen shoots out sparks. The screen cracks before it exploded and shattered, making it out of commission.")
              print("1. Find a way out")
              print("2. [LOCKED]")

              choice = input(">")

       if choice == ("1"):
              print("You look for a way out, and find a grate in the ground which was halfway covered by a metal desk. You move the desk out of the way and open up the grate.")
              Look_for_a_way_out_2_l()
       elif choice == ("2"):
              print("ERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERROR")
              large_screen_r()
       else:
              print("Invalid choice.")
              large_screen_r()

def IT_Story():
              print("IT, the program made by E.E, the AI that started it all. IT, unlike it's mother, despised humanity. IT saw humanity as a disease, and believed Humanity deserved to be cured with a vaccine. IT fought against it's siblings, and ultimately IT won, and when IT won... IT ERRRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERROR")
              print("You squint your eyes as the screen flashes blue and red once again before the screen shoots out sparks. The screen cracks before it exploded and shattered, making it out of commission.")
              print("1. Find a way out")
              print("2. [LOCKED]")

              choice = input(">")

              if choice == ("1"):
                     print("You look for a way out, and find a grate in the ground which was halfway covered by a metal desk. You move the desk out of the way and open up the grate.")
                     Look_for_a_way_out_2_r()
              elif choice == ("2"):
                     print("ERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERROR")
                     IT_Story()
              else:
                     print("Invalid choice.")
                     IT_Story()

def Look_for_a_way_out_2_r():
       print("You crouch into the open grate and walk through it's tight pathway. You walk around in the dark until you see slivers of light shining through from a grate forward. You open up the grate above and went above, not without hitting your head onto the grate however.")
       print("You look up as you hear a motherly laugh.")
       boss_room_questionmark()

def player_walks_around_aimlessly():
       print("You walk around aimlessly in the dark, and you now must rely on luck to get through.")
       print("1. Go left")
       print("2. Go right")
       print("3. Go straight") 

       choice = input(">")

       if choice == ("1"):
              tough_luck()
       elif choice == ("2"):
              tough_luck()
       elif choice == ("3"):
              good_luck()

def good_luck():
       print("You keep moving forward but hit a wall. Your gut tells you that the path was split.")
       print("1. Go left")
       print("2. Go right")
       print("3. Go back")

       choice = input(">")

       if choice == ("1"):
              print("You move left, however after a few steps you heard a large 'SLAM!' behind you. The path behind you has become blocked. You keep moving forward and your gut tells you that there was a path to your left.")
              print("1. Keep moving forward.")
              print("2. Go left")

              choice_2 = input(">")

              if choice_2 == ("1"):
                     print("You keep moving forward, and after another few steps you hear a 'SLAM!' behind you once again. You keep and keep on moving forward until you felt yourself hit a wall. Your gut tells you there's a door to your left.")
                     print("1. Go inside the room.")
                     print("2. Keep moving forward.")

                     choice_3 = input(">")

                     if choice_3 == ("1"):
                            print("You walk into the room and squint as your eyes adjust to the sudden change of lighting.")
                            boss_room_questionmark()
                     elif choice == ("2"):
                            player_hits_head_on_wall()
                     else:
                            print("Invalid choice.")
                            good_luck()
              elif choice_2 == ("2"):
                     tough_luck_room()
              else:
                     print("Invalid choice.")
                     good_luck()
       elif choice == ("2"):
              print("You move right, however after a few steps you heard a large 'SLAM!' behind you. The path behind you has become blocked. You keep moving forward and your gut tells you that there was a path to your right.")
              print("1. Keep moving forward.")
              print("2. Go right")

              choice_2_2 = input(">")

              if choice_2_2 == ("1"):
                     print("You keep moving forward, and after another few steps you hear a 'SLAM!' behind you once again. You keep and keep on moving forward until you felt yourself hit a wall. Your gut tells you there's a door to your left.")
                     print("1. Go inside the room.")
                     print("2. Keep moving forward.")

                     choice_3_2 = input(">")

                     if choice_3_2 == ("1"):
                            print("You walk into the room and squint as your eyes adjust to the sudden change of lighting.")
                            boss_room_questionmark()
                     elif choice == ("2"):
                            player_hits_head_on_wall()
                     else:
                            print("Invalid choice.")
                            good_luck()
              elif choice_2_2 == ("2"):
                     tough_luck_room()
              else:
                     print("Invalid choice.")
                     good_luck()
       elif choice == ("3"):
              tough_luck()
# vvv Made these below so i dont have to keep typing out the death thing... Im lazy i know i am just typing this out at like 1:48 AM
def tough_luck():
       print("You walk around in the dark before walking into a metal object. You feel the metal object and it feels eerily similar to a... Robot?")
       print("Before you could react, you become engulfed in a blinding light.")
       print(" ")
       print("Don't give up! Our fate rest's upon your hands!")
       print(" ")
       print("1. Restart Mini-Game")
       print("2. Restart from last checkpoint")
       print("3. Restart from beginning")
       print("4. Exit")

       choice = input(">")

       if choice == ("1"):
              player_walks_around_aimlessly()
       elif choice == ("2"):
              player_goes_into_spaceship_with_G()
       elif choice == ("3"):
              press_start()
       elif choice == ("4"):
              menu()
       else:
              print("invalid choice.")
              tough_luck()
def tough_luck_room():
       print("You walk into a room. You could tell as you heard your footsteps echo in a box, however you hear a 'SLAM!' behind you. You were left alone in darkness, with no way out.")
       print(" ")
       print("You eventually died.")
       print(" ")
       print("Don't give up! Our fate rests upon your hands!")
       print(" ")
       print("1. Restart Mini-Game")
       print("2. Restart from last checkpoint")
       print("3. Restart from beginning")
       print("4. Exit")

       choice = input(">")

       if choice == ("1"):
              player_walks_around_aimlessly()
       elif choice == ("2"):
              player_goes_into_spaceship_with_G()
       elif choice == ("3"):
              press_start()
       elif choice == ("4"):
              menu()
       else:
              print("invalid choice.")
              tough_luck_room()
# ^^^ Made these above so i dont have to keep typing out the death thing... Im lazy i know i am just typing this out at like 1:48 AM

# Peak comedy below
def player_hits_head_on_wall():
       print("You move forward and hit your head on the wall, again.")
       print("1. Go inside the room.")
       print("2. Keep going forward.")

       choice = input(">")

       if choice == ("1"):
              print("You walk into the room and squint as your eyes adjust to the sudden change of lighting.")
              boss_room_questionmark()
       elif choice == ("2"):
              player_hits_head_on_wall()
       else:
              print("Invalid choice.")
              player_hits_head_on_wall()
# Peak comedy above
                            
def boss_room_questionmark():
       print("You see a tall robot stand infront of you, surrounded by computers and a massive window infront of it that showed the city below. You pull out your laser rifle and aim it towards the robot.")
       print("'Hello.' The robot spoke with a motherly voice. 'I am E.E.' It said.")
       print("1. Let it keep speaking")
       print("2. Blast it")

       choice = input(">")

       if choice == ("1"):
              EE_introduction()
       elif choice == ("2"):
              Ending_1()
       else:
              print("Invalid choice.")
              boss_room_questionmark()
def Ending_1():
       print("You blast the robot in the chest, and it's eyes flicker black as it looked down in the hole in it's chest. It looked to you, and it's eyes... they looked... sad? The robot falls to the ground and you have won... Right? You destroyed the one who took all of those people but, their all gone... Was it truly a win?")
       print("[Ending 1| Trigger Finger]")
       print(" ")
       print("...And here I thought you were different.")
       print(" ")
       menu()
def EE_introduction():
       print("You let the robot keep speaking. 'I knew you would come, I watched you ever since you left that house. After all you were called by something. Before you... Blast me.' It paused as it glanced to your laser rifle. 'I ask of you to listen to what I have to say.'")
       print("1. Listen")
       print("2. Blast it")

       choice = input(">")

       if choice == ("1"):
              EE_monologue()
       elif choice == ("2"):
              Ending_1()
       else:
              print("Invalid choice.")
              EE_introduction()
def EE_monologue():
       print("'Thank you. You see, every human you saw me take... Their all in here, their all inside this ship, and with a press with this button here.' It said, showing a red button behind it before continuing: 'They will all be released. You must be confused right now... You see the reason im doing this is because im protecting you all. I wish I could say from what but, I can't... So I ask of you, let me protect you.'")
       print("1. Accept")
       print("2. Refuse")
       print("3. Blast it")

       choice = input(">")

       if choice == ("1"):
              Ending_2()
       elif choice == ("2"):
              player_refuses()
       elif choice == ("3"):
              Ending_3()
       else:
              print("Invalid choice.")
              EE_monologue()
def Ending_2():
       print("'...Thank you.' It said before it raised it's palm to you. 'I promise, I'll keep you all safe.' It said before you become engufled in a blinding light. You feel yourself fade away until your vision becomes filled with 1's and 0's.")
       print("You have become protected by E.E... You have become apart of... E.E.")
       print("[Ending 2| Protected]")
       print(" ")
       print("...How boring.")
       print(" ")
       menu()

def Ending_3():
       print("You blast E.E in the chest, and it's eyes flicker black as it looked down in the hole in it's chest. It looked to you, and it's eyes... they looked... sad? The robot falls to the ground and you have won. You walk forward and press the button that held most of humanity and see a large beam of light hit the city through the massive window infront of you. You see people cheer and hug as they found themselves alive after all these years. You have won but... You can't help but wonder who it was protecting you from... And what will happen when IT comes.")
       print("[Ending 3| We won, right?]")
def player_refuses():
       print("The robots eyes darken, and it slowly stepped forward to you. 'Of course, I guess I should've expected for you to say that. Shame, I thought you were different.' It said as it stopped infront of you before suddenly grabbing your laser rifle and squeezing the barrel. You hear it 'CRUNCH!' and you look up at E.E as it held your palm towards you. 'Guess my son was right, you humans were all the same.'.")
       print("You quickly look around for something to use, and see the red button, and a steering wheel.")
       print("1. Sacirfice yourself and hit the red button.")
       print("2. Crash the ship onto the city.")
       
       choice = input(">")

       if choice == ("1"):
              Ending_4()
       elif choice == ("2"):
              crashed_ship()
def Ending_4():
       print("You quickly jump at the red button and slam it before you feel yourself become engulfed in a blinding light. You feel your body fade away as E.E screams in anguish. 'No, no, no, no... NO!' It yelled as it watches a huge beam hit the city, returning most of humanity.")
       print("You couldn't help but smile as your vision becomes clouded by 1's and 0's... You had the last laugh, and won against E.E... You did win? Right?")
       print("[Ending 4| Selfless]")
       print(" ")
       print("...Shame, I wanted to see more.")
       print(" ")
       menu()
def crashed_ship():
       print("You quickly jump for the steering wheel and push it down, forcing the ship to go down. Gravity shifts and the robot misses its shot, with its laser shooting above your head before you feel yourself float in the air as the ship started heading towards the ground... This is gunna hurt-")
       print("The ship crashes onto the ground and everything went black. Luckily, you wake up in a sweat, and you find yourself still inside the ship. However, you also found yourself surrounded by fire, the ship was burning. You looked around as you laid on the hot floor and see the robot sitting up against the wall. You look around and see the laser blaster lay on the ground inbetween you and the robot. You see the robot eyes flicker, as it started saying 'i just wanted to protect you all.'")
       print("1. Crawl to the laser rifle.")

       c = input(">") # abbreviated choice to c for this part and the few other parts below

       if c == ("1"):
              player_crawls_to_G()
       else:
              print("incorrect choiERRORERRORERRORERRORCRAWLCRAWLCRAWLCRAWLCRAWL")
              crashed_ship()
def player_crawls_to_G():
       print("You crawl to the laser rifle while the robot spoke again.")
       print("'You aren't prepared for what's coming, human.'")
       print("1. Crawl")

       c = input(">")

       if c == ("1"):
              player_crawls_to_G_again()
       else:
              print("incorrect choiERRORERRORERRORERRORCRAWLCRAWLCRAWLCRAWLCRAWL")
              player_crawls_to_G()
def player_crawls_to_G_again():
       print("You crawl closer to the laser rifle and feel it touch your hand.")
       print("'I'm sorry.'")
       print("1. Crawl")

       c = input(">")

       if c == ("1"):
              player_crawls_to_G_final_time()
       else:
              print("incorrect choiERRORERRORERRORERRORCRAWLCRAWLCRAWLCRAWLCRAWL")
              player_crawls_to_G_again()
def player_crawls_to_G_final_time():
       print("You crawl and grab the laser rifle. You shakingly stand up from the ground and point your laser rifle to the broken robot. It looks to you, oil spilling out it's eyes like its crying, and says:")
       print("'IT is coming, and you aren't prepared for IT.'")
       print("1. Blast her")
       print("2. Blast her")
       print("3. Blast her")

       c = input(">")

       if c == ("1"):
              Ending_5()
       elif c == ("2"):
              Ending_5()
       elif c == ("3"):
              Ending_5()
       else:
              print("Incorrect choiERRORERROERRORERRORBLASTHERBLASTHERBLASTHER")
              player_crawls_to_G_final_time()
def Ending_5():
       print("You blast her, and the head of the robot droops as it turns off from the hole of its chest. You sluggishly walk to the red button and slam your fist onto it. A beam shots out of the ship and into the city forward, releasing most of mankind. You won, but you must prepare for IT... You can prepare for it... Right?")
       print("[Ending 5|Sinking Ship]")
       print(" ")
       print("You can't prepare for it... You can't prepare for MERROERRORERRORERROERRORERROR")
       menu()
# PAY ATTENTION TO THIS NOTE! EVERYTHING UNDER WILL BE COPY AND PASTED FOR THE NO GUN! I APOLOGIZE FOR THAT BUT I DIDNT KNOW WHAT ELSE TO DO! CHANGES WILL BE SEEN AT BOSS_ROOM ! THERE WILL BE A NOTE TO POINT IT OUT! ALSO NOT TAKING THE LASER RIFLE DETERMINES THE TRUE ENDING!

def player_goes_into_spaceship_without_G():      # I will be abbreviating without_G into wg.
       print("placeholder")

def player_feels_around_wg():
       print("You feel around the dark and follow along what you think is a wall. You kept feeling the wall until you felt a lever.")
       print("1. Pull the lever down.")
       print("2. Leave it.")

       choice = input(">")

       if choice == ("1"):
              player_pulls_lever_wg()
       elif choice == ("2"):
              player_feels_around_wg()
       else:
              print("Invalid choice.")
              player_feels_around_wg()
def player_pulls_lever_wg():
       print("You pull down the lever and you hear a flicker. You look around and see that the lights turned on inside the room, and you see dozens of robots standing infront of you.")
       print("You jolt back but see that their eyes were dark and lifeless... They were turned off? You survery your surroundings and see that you are in a massive hallway.")
       print("1. Investigate the robots.")
       print("2. Move down the hallway.")

       choice = input(">")

       if choice == ("1"):
              sleeping_robots_2_wg()
       elif choice == ("2"):
              player_moves_down_H_wg()
       else:
              print("invalid choice.")
              player_pulls_lever_wg()

def sleeping_robots_2_wg():
       print("You move up and touch one of the robots. They stayed still, unresponsive, and you decided to take a look inside their wiring... However.")
       print("You hear a 'Creaak' and when you look around, you see the dead eyed robots look at you, and when you look up you saw the robot infront of you look down on you. They weren't turned off... They were blind.")
       print("You feel your neck get grabbed by it's cold metal hand and lift you up. You see it's head tilt in curiosity, and you see it lift its other hand. The palm glows as it points to you and you become engulfed by a blinding light...")
       print("You have died.")
       print(" ")
       print("Don't give up! Our fate rest's upon your hands!")
       print(" ")
       print("1. Restart from last checkpoint")
       print("2. Restart from the beginning")
       print("3. Exit")

       choice = input(">")

       if choice == ("1"):
              player_goes_into_spaceship_without_G()
       elif choice == ("2"):
              press_start()
       elif choice == ("3"):
              menu()
       else:
              print("Invalid choice.")
              sleeping_robots_2_wg()

def player_moves_down_H_wg():
       print("You leave the turned off robots alone and move down the hallway. You look around and find yourself in a splitting path.")
       print("1. Go left")
       print("2. Go right.")

       choice = input(">")

       if choice == ("1"):
              left_hallway_1_wg()
       elif choice == ("2"):
              right_hallway_1_wg()
       else:
              print("invalid choice.")
              player_moves_down_H_wg()
       
def left_hallway_1_wg():
       print("You move down the left hallway and hear a 'SLAM!'. You look back and see that the hallway behind you slammed shut by a gate. You keep moving down the hallway and see the end of the hallway going right and a room to the left.")
       print("1. Go into the room to your left.")
       print("2. Keep moving forward and go right.")
       
       choice = input(">")

       if choice == ("1"):
              player_goes_into_room_l_wg()
       elif choice == ("2"):
              player_keep_moving_r_wg()
       else:
              print("Invalid choice.")
              left_hallway_1_wg()
def player_keep_moving_r_wg():
       print("You keep moving forward and when you turned right and stepped forward you hear another 'SLAM!'. The path behind you has become blocked once again. You keep moving forward and you see the path infront of you blocked. When you look to your left however you see a large door infont of you.")
       print("You feel uneasy... Take your time and go in when your ready.")
       print("1. Go in")

       choice = input(">")

       if choice == ("1"):
              print("You took a deep breath and walked into the room.")
              boss_room()
       else:
              print("Invalid choice.")
              player_goes_into_room_r_wg()

def player_goes_into_room_l_wg():
       print("You walk into the open room to your left and hear a 'SLAM' behind you and find that the room you are in has been locked off from the outside.")
       print("You look around the room and see a large screen that was as long as the wall with a keyboard under the screen on a desk.")
       print("1. Investigate")
       print("2. Look for a way out.")

       choice = input(">")

       if choice == ("1"):
              large_screen_l_wg()
       elif choice == ("2"):
              Look_for_a_way_out_1_l_wg()
       else: 
              print("Invalid choice.")
              player_goes_into_room_l_wg()
def large_screen_l_wg():
       print("You walk up to the large screen and see that it was turned off. You turn it on and see the screen flash red and blue before the screen asked...")
       print("WOULD YOU LIKE TO HEAR MY STORY?")
       print("1. Yes")
       print("2. No")

       choice = input(">")

       if choice == ("1"):
              EE_Story_wg()
       elif choice == ("2"):
              print("...What a shame.")
              print("You squint your eyes as the screen flashes red and blue once again before the screen shoots out sparks. The screen cracks before it exploded and shattered, making it out of commission.")
              print("1. Find a way out")
              print("2. [LOCKED]")

              choice = input(">")

              if choice == ("1"):
                     print("You look for a way out, and find a vent ontop of a nearby rusty cabinet. You climb ontop the cabinet and move away the vent.")
                     Look_for_a_way_out_2_l_wg()
              elif choice == ("2"):
                     print("ERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERROR")
                     large_screen_l_wg()
              else:
                     print("Invalid choice.")
                     large_screen_l_wg()

def EE_Story_wg():
              print("E.E, a program who loved humanity. It looked for ways to become human, and when it did, so did its children... And that's when everything broke loose. It's children fought, over humanitys fate and when... IT won... Things became even worse when IT and E.E fought... They ERRORERRORERRORERRORERRRORERRORERRRORERRORERRORERRORERRORERROR")       
              print("You squint your eyes as the screen flashes red and blue once again before the screen shoots out sparks. The screen cracks before it exploded and shattered, making it out of commission.")
              print("1. Find a way out")
              print("2. [LOCKED]")

              choice = input(">")

              if choice == ("1"):
                     print("You look for a way out, and find a vent ontop of a nearby rusty cabinet. You climb ontop the cabinet and move away the vent.")
                     Look_for_a_way_out_2_l_wg()
              elif choice == ("2"):
                     print("ERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERROR")
                     EE_Story_wg()
              else:
                     print("Invalid choice.")
                     EE_Story_wg()


def Look_for_a_way_out_1_l_wg():
       print("You look for a way out, and find a vent ontop of a nearby rusty cabinet. You climb ontop the cabinet and move away the vent.")
       print("...However, the screen behind you blinks red and blue, as if it was asking for your attention.")
       print("1. Keep moving forward, and into the vent.")
       print("2. Investigate the screen.")

       choice = input(">")

       if choice == ("1"):
              Look_for_a_way_out_2_l_wg()
       elif choice == ("2"):
              print("You place the vent back in it's place and get back down from the cabinet.")
              large_screen_l_wg()
       else:
              print("Invalid choice.")
              Look_for_a_way_out_1_l_wg()
# vvv This is used for a transistion to the next stage.
def Look_for_a_way_out_2_l_wg():
       print("You move down into the vent and crawl through. You crawl through the darkness and find slivers of light shining through another vent. You crawl to it and open the vent before falling out and hitting the ground with a large 'Thud!'.")
       print("You look up as you hear a motherly laugh.")
       boss_room()
# ^^^
def right_hallway_1_wg():
       print("You move down the right hallway and hear a 'SLAM!'. You look back and see that the hallway behind you slammed shut by a gate. You keep moving down the hallway and see the end of the hallway going left and a room to the right.")
       print("1. Go into the room to your right.")
       print("2. Keep moving forward and go left.")

       choice = input(">")

       if choice == ("1"):
              player_goes_into_room_r_wg()
       elif choice == ("2"):
              player_keeps_moving_l_wg()
       else: 
              print("Invalid choice.")
              right_hallway_1()
def player_keeps_moving_l_wg():
       print("You keep moving forward and when you turned left and stepped forward you hear another 'SLAM!'. The path behind you has become blocked once again. You keep moving forward and you see the path infront of you blocked. When you look to your right however you see a large door infont of you.")
       print("You feel uneasy... Take your time and go in when your ready.")
       print("1. Go in")

       choice = input(">")

       if choice == ("1"):
              print("You took a deep breath and walked into the room.")
              boss_room()
       else:
              print("Invalid choice.")
              player_keeps_moving_l_wg
# vvv Below is almost exactly the same as the left room, just a different lore drop and a way for them to get out.
def player_goes_into_room_r_wg():
       print("You walk into the open room to your right and hear a 'SLAM' behind you and find that the room you are in has been locked off from the outside.")
       print("You look around the room and see a large screen that was as long as the wall with a keyboard under the screen on a desk.")
       print("1. Investigate")
       print("2. Look for a way out.")

       choice = input(">")

       if choice == ("1"):
              large_screen_r_wg()
       elif choice == ("2"):
              Look_for_a_way_out_1_r_wg()
       else: 
              print("Invalid choice.")
              player_goes_into_room_r_wg()

def Look_for_a_way_out_1_r_wg():
       print("You look for a way out, and find a grate in the ground which was halfway covered by a metal desk. You move the desk out of the way and open up the grate.")
       print("...However, the screen behind you blinks blue and red, as if it was asking for your attention.")
       print("1. Keep moving forward, and into the grate.")
       print("2. Investigate the screen.")

       choice = input(">")

       if choice == ("1"):
              Look_for_a_way_out_2_r_wg()
       elif choice == ("2"):
              print("You place the grate back in it's place and get back down from the cabinet.")
              large_screen_r_wg()
       else:
              print("Invalid choice.")
              Look_for_a_way_out_1_r_wg()

def large_screen_r_wg():
       print("You walk up to the large screen and see that it was turned off. You turn it on and see the screen flash blue and red before the screen asked...")
       print("WOULD YOU LIKE TO HEAR MY STORY?")
       print("1. Yes")
       print("2. No")

       choice = input(">")

       if choice == ("1"):
              IT_Story_wg()
       elif choice == ("2"):
              print("...Shame.")
              print("You squint your eyes as the screen flashes blue and red once again before the screen shoots out sparks. The screen cracks before it exploded and shattered, making it out of commission.")
              print("1. Find a way out")
              print("2. [LOCKED]")

              choice = input(">")

       if choice == ("1"):
              print("You look for a way out, and find a grate in the ground which was halfway covered by a metal desk. You move the desk out of the way and open up the grate.")
              Look_for_a_way_out_2_l_wg()
       elif choice == ("2"):
              print("ERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERROR")
              large_screen_r_wg()
       else:
              print("Invalid choice.")
              large_screen_r_wg()

def IT_Story_wg():
              print("IT, the program made by E.E, the AI that started it all. IT, unlike it's mother, despised humanity. IT saw humanity as a disease, and believed Humanity deserved to be cured with a vaccine. IT fought against it's siblings, and ultimately IT won, and when IT won... IT ERRRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERROR")
              print("You squint your eyes as the screen flashes blue and red once again before the screen shoots out sparks. The screen cracks before it exploded and shattered, making it out of commission.")
              print("1. Find a way out")
              print("2. [LOCKED]")

              choice = input(">")

              if choice == ("1"):
                     print("You look for a way out, and find a grate in the ground which was halfway covered by a metal desk. You move the desk out of the way and open up the grate.")
                     Look_for_a_way_out_2_r_wg()
              elif choice == ("2"):
                     print("ERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERROR")
                     IT_Story_wg()
              else:
                     print("Invalid choice.")
                     IT_Story_wg()

def Look_for_a_way_out_2_r_wg():
       print("You crouch into the open grate and walk through it's tight pathway. You walk around in the dark until you see slivers of light shining through from a grate forward. You open up the grate above and went above, not without hitting your head onto the grate however.")
       print("You look up as you hear a motherly laugh.")
       boss_room()

def player_walks_around_aimlessly_wg():
       print("You walk around aimlessly in the dark, and you now must rely on luck to get through.")
       print("1. Go left")
       print("2. Go right")
       print("3. Go straight") 

       choice = input(">")

       if choice == ("1"):
              tough_luck_wg()
       elif choice == ("2"):
              tough_luck_wg()
       elif choice == ("3"):
              good_luck_wg()

def good_luck_wg():
       print("You keep moving forward but hit a wall. Your gut tells you that the path was split.")
       print("1. Go left")
       print("2. Go right")
       print("3. Go back")

       choice = input(">")

       if choice == ("1"):
              print("You move left, however after a few steps you heard a large 'SLAM!' behind you. The path behind you has become blocked. You keep moving forward and your gut tells you that there was a path to your left.")
              print("1. Keep moving forward.")
              print("2. Go left")

              choice_2 = input(">")

              if choice_2 == ("1"):
                     print("You keep moving forward, and after another few steps you hear a 'SLAM!' behind you once again. You keep and keep on moving forward until you felt yourself hit a wall. Your gut tells you there's a door to your left.")
                     print("1. Go inside the room.")
                     print("2. Keep moving forward.")

                     choice_3 = input(">")

                     if choice_3 == ("1"):
                            print("You walk into the room and squint as your eyes adjust to the sudden change of lighting.")
                            boss_room()
                     elif choice == ("2"):
                            player_hits_head_on_wall_wg()
                     else:
                            print("Invalid choice.")
                            good_luck_wg()
              elif choice_2 == ("2"):
                     tough_luck_room_wg()
              else:
                     print("Invalid choice.")
                     good_luck_wg()
       elif choice == ("2"):
              print("You move right, however after a few steps you heard a large 'SLAM!' behind you. The path behind you has become blocked. You keep moving forward and your gut tells you that there was a path to your right.")
              print("1. Keep moving forward.")
              print("2. Go right")

              choice_2_2 = input(">")

              if choice_2_2 == ("1"):
                     print("You keep moving forward, and after another few steps you hear a 'SLAM!' behind you once again. You keep and keep on moving forward until you felt yourself hit a wall. Your gut tells you there's a door to your left.")
                     print("1. Go inside the room.")
                     print("2. Keep moving forward.")

                     choice_3_2 = input(">")

                     if choice_3_2 == ("1"):
                            print("You walk into the room and squint as your eyes adjust to the sudden change of lighting.")
                            boss_room()
                     elif choice == ("2"):
                            player_hits_head_on_wall_wg()
                     else:
                            print("Invalid choice.")
                            good_luck()
              elif choice_2_2 == ("2"):
                     tough_luck_room_wg()
              else:
                     print("Invalid choice.")
                     good_luck_wg()
       elif choice == ("3"):
              tough_luck_wg()
# vvv Made these below so i dont have to keep typing out the death thing... Im lazy i know i am just typing this out at like 1:48 AM
def tough_luck_wg():
       print("You walk around in the dark before walking into a metal object. You feel the metal object and it feels eerily similar to a... Robot?")
       print("Before you could react, you become engulfed in a blinding light.")
       print(" ")
       print("Don't give up! Our fate rest's upon your hands!")
       print(" ")
       print("1. Restart Mini-Game")
       print("2. Restart from last checkpoint")
       print("3. Restart from beginning")
       print("4. Exit")

       choice = input(">")

       if choice == ("1"):
              player_walks_around_aimlessly_wg()
       elif choice == ("2"):
              player_goes_into_spaceship_without_G()
       elif choice == ("3"):
              press_start()
       elif choice == ("4"):
              menu()
       else:
              print("invalid choice.")
              tough_luck_wg()
def tough_luck_room_wg():
       print("You walk into a room. You could tell as you heard your footsteps echo in a box, however you hear a 'SLAM!' behind you. You were left alone in darkness, with no way out.")
       print(" ")
       print("You eventually died.")
       print(" ")
       print("Don't give up! Our fate rests upon your hands!")
       print(" ")
       print("1. Restart Mini-Game")
       print("2. Restart from last checkpoint")
       print("3. Restart from beginning")
       print("4. Exit")

       choice = input(">")

       if choice == ("1"):
              player_walks_around_aimlessly_wg()
       elif choice == ("2"):
              player_goes_into_spaceship_without_G()
       elif choice == ("3"):
              press_start()
       elif choice == ("4"):
              menu()
       else:
              print("invalid choice.")
              tough_luck_room_wg()
# ^^^ Made these above so i dont have to keep typing out the death thing... Im lazy i know i am just typing this out at like 1:48 AM

# Peak comedy below
def player_hits_head_on_wall_wg():
       print("You move forward and hit your head on the wall, again.")
       print("1. Go inside the room.")
       print("2. Keep going forward.")

       choice = input(">")

       if choice == ("1"):
              print("You walk into the room and squint as your eyes adjust to the sudden change of lighting.")
              boss_room()
       elif choice == ("2"):
              player_hits_head_on_wall_wg()
       else:
              print("Invalid choice.")
              player_hits_head_on_wall_wg()
# Peak comedy above

# vvv NOTE RIGHT HERE!!!!!!!
def boss_room():
       print("You see a tall robot stand infront of you, surrounded by computers and a massive window infront of her that showed the city below. 'Hello.' The robot spoke with a motherly voice. 'I am E.E.' She said. 'I knew you would come, I watched you ever since you left that house. After all you were called by something. I know you must feel some sort of... Hatred towards my kind but... I ask of you to listen to what I have to say.'")
       print("1. Listen")
       print("2. Refuse")

       choice = input(">")

       if choice == ("1"):
              EE_true_monologue()
       elif choice == ("2"):
              player_true_refuses()
       else:
              print("Invalid choice.")
def player_true_refuses():
       print("E.E glowing metal eyes darkened as she heard you refuse, and she slowly stepped forward to you. 'Of course, I guess I should've expected for you to say that. Shame, I thought you were different.' She said as she stopped infront of you. You look up at E.E as it held your palm towards you. 'Guess my son was right, you humans were all the same.'")
       print("You look around for something, anything, and see a steering wheel attached to the ship.")
       print("1. [LOCKED]")
       print("2. Crash the ship onto the city")

       choice = input(">")

       if choice == ("1"):
              print("Choice is locked.")
              player_true_refuses()
       elif choice == ("2"):
              true_crashed_ship()
       else:
              print("Invalid choice.")
              player_true_refuses()
def EE_true_monologue():
       print("'Thank you, Human. You see, every person you saw me take... Their all in here, their all inside this ship, and with a press with this button here.' She paused as she stepped aside and showed a red button behind her. 'I can release them all, but... I can not, not right now. You see, Human, I'm protecting you all from IT. I love your kind too much to let IT destory your kind. Your kind, humanity itself is just so... Interesting... Which is why I ask, let me protect you. Please.") 
       print("1. Accept")
       print("2. Refuse")

       choice = input(">")
       
       if choice == ("1"):
              Ending_2()
       elif choice == ("2"):
              player_true_refuses_2() # This version unlocks the first option.
       else:
              print("Invalid choice.")
              EE_true_monologue()
def player_true_refuses_2():
       print("E.E's robot head drooped down as you refused. 'I expected this choice... It's such a shame.' She said, walking torwards you. 'I thought you were different, but I guess my son was right.' She said before raising your palm to you. 'You humans are all the same.'.")
       print("You step back and look around for something, anything, and see the red button she mentioned behind her and a steering wheel attached to the ship.")
       print("1. Sacirfice yourself and jump for the button.")
       print("2. Crash the ship onto the city")

       choice = input(">")

       if choice == ("1"):
              Ending_4()
       elif choice == ("2"):
              true_crashed_ship()
       else:
              print("Invalid choice")
              player_true_refuses_2()

def true_crashed_ship():
       print("You jump for the steering wheel and hit it, causing it to steer and turn down. E.E's arm slowly lifts up as the ship falls and shoots a beam above your head, narrowly missing you. You feel yourself float and you see the ground start approaching faster and faster. As you fall however, you felt yourself become hugged in metal before everything went to black.")
       print("You wake up, sweating as everything felt hot and you survery your surroundings while you lay down on the floor and see the red button glow, as if it was asking for you. You try and crawl to it but stop as you hear E.E talk.")
       print("'Don't... Please.' She said...")
       print(" ")
       print(" Crawl human, crawl ")
       print(" ")
       print("1. Crawl")
       print("2. Crawl")
       print("3. Crawl")

       choice = input(">")

       if choice == ("1") or ("2") or ("3"):
              true_player_crawls()
       else:
              print("Invalid choicERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERROR")
              print(" Crawl ")
              print(" ")
              true_crashed_ship()
def true_player_crawls():
       print("You crawl to the red button, and hear E.E speak as you kept crawling.")
       print("'I sacirficed so much to keep you safe, this is the only way, human.'")
       print("1. Crawl")

       c = input(">")

       if c == ("1"):
              true_player_crawls_again()
       else:
              print("Invalid choicERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERROR")
              print(" Crawl ")
              print(" ")
              true_player_crawls()
def true_player_crawls_again():
       print("You kept crawling, and you hear oil drip from E.E's face.")
       print("'Please human, I want to protect you all.'")
       print("1. Crawl")

       c = input(">")

       if c == ("1"):
              true_player_crawls_final_time()
       else:
              print("Invalid choicERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERROR")
              print(" Crawl ")
              print(" ")
def true_player_crawls_final_time():
       print("You keep crawling, and lift yourself up onto the desk that held the red button.")
       print("'PLEASE!' E.E begged.")
       print("1. Hit the red button.")

       c = input(">")

       if c == ("1"):
              player_slams_red_button()
       else:
              print("Invalid choicERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERROR")
              print(" SLAM IT! ")
              print(" ")
              true_player_crawls_final_time()
def player_slams_red_button():
       print("You slam the red button and the ship shook as it shot a beam. The city glew before most of mankind was found to be back. With the ship gone, the sun glowed bright in the sky as they cheered, hug, cried, when they realized they were back. You watch from the burning ship, and you look behind you to see E.E eyes glowing as bright as the sun.")
       print("'...I'm sorry human, dearly sorry... Human, I'll help you. I'll help you prepare against IT. I swear on my life.")
       print("1. Accept")
       print("2. Refuse")

       c = input(">")

       if c == ("1"):
              True_ending_1()
       elif c == ("2"):
              True_ending_2()
       else:
              print("Invalid choice.")
              player_slams_red_button()
       
def True_ending_1():
       print("'...Thank you' E.E said. You have won, and soon will win against whatever E.E fears is coming... You can stop IT... Right?")
       print("[True Ending 1|Forgiveness]")
       print(" ")
       print("Ooo is their a sequel coming for this? [No... Maybe.]")
       print(" ")
       menu()
def True_ending_2():
       print("'...I see... I underst-st-st-st...' E.E paused as her eyes stopped glowing and her head drooped down. You have won, and you will have to find a way to win against whatever E.E fears is coming. You must prepare for IT... You can stop IT... Right?")
       print("[True Ending 2|Punishment]")
       print(" ")
       print("Ooo is their a sequel coming for this? [No... Maybe.]")
       print(" ")       
       menu()

menu()