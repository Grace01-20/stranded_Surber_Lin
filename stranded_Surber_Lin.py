"""
Stranded - a choose your own adventure story
@Authors: Grace Surber, Daniel Lin
@Param: str
@Version: 1.0
@Date: 9/9/19
"""

#These are packages that we imported to allow us to manipulate the text throughout the adventure
import sys
import time
from colorama import Fore, Style
from os import system, name

#clears screen after game is restarted
def screenClear():
   if name == 'nt':
      _ = system('cls')
   else:
      _ = system('clear')

#writes out words faster than printSlow()
def printFast(str):
  for i in str:
    sys.stdout.write(i)
    sys.stdout.flush()
    time.sleep(0.01)
  return ' '

#writes out words individually  
def printSlow(str):
  for i in str:
    sys.stdout.write(i)
    sys.stdout.flush()
    time.sleep(0.06)
  return ' '

#Introduces the adventure and gets the user's name
def getName():
  printFast(" _______ _______  ______ _______ __   _ ______  _______ ______ \n")
  printFast(" |______    |    |_____/ |_____| | \  | |     \ |______ |     \ \n")
  printFast(" ______|    |    |    \_ |     | |  \_| |_____/ |______ |_____/\n")
  print("                 By: Daniel Lin and Grace Surber")
  print(' ')
  name = input(printSlow("What is your name? "))
  return name

#This function explains what the scenario that the user begins in is: stranded on an island
def explainScenario():
  printSlow("You find yourself tired, hungry, and STRANDED on an unfamiliar island, with no one in sight, and you have no reccolection of how you arrived there...\n")
  time.sleep(0.6)
  printFast("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
  time.sleep(0.6)
  wakeUp()

#this function asks the user what they want to do when they wake up
def wakeUp():
  x = input(printSlow(name + ", what do you do when you wake up? " + Fore.BLUE + 'Explore' + Style.RESET_ALL + " or " + Fore.BLUE + 'Panic' + Style.RESET_ALL))
  if (x.lower() == "explore"):
    explore()
  elif (x.lower() == "panic"):
    panic()
  else:
    printSlow("Please enter either " + Fore.BLUE + 'explore' + Style.RESET_ALL + ' or ' + Fore.BLUE + 'panic\n' + Style.RESET_ALL)
    wakeUp()

#This function is one possible ending for the story: what happens if they chose to panic
def panic():
  printSlow('You wasted valuable time panicking\n')
  stormDecision()

#This function tells the user what will happen if they chose to explore, and calls the next decision
def explore():
  printSlow("You begin to wander around the seemingly deserted island, and stumble upon the slightly warm remains of a fire.\n")
  stormDecision()

#asks the user what to do when they see a storm forming and calls the resulting functions based on their decision
def stormDecision():
  time.sleep(0.6)
  printFast("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
  time.sleep(0.6)
  printSlow("Suddenly, the deafening sound of thunder roars. You look around and see a storm heading towards you from the east. ")
  x = input(printSlow("What do you do, " + name + "? '" + Fore.BLUE + "Stay" + Style.RESET_ALL +"' or '" + Fore.BLUE + "Find"+ Style.RESET_ALL + "' Shelter?"))
  if (x.lower() == "stay"):
    printSlow("You drowned in the storm surge. " + Fore.RED +"The End.\n" + Style.RESET_ALL)
    playAgain()
  elif (x.lower() == "find"):
    cave()
  else:
    printSlow('Please enter ' + Fore.BLUE + 'stay' + Style.RESET_ALL + ' or ' + Fore.BLUE+ 'find '+ Style.RESET_ALL + 'shelter\n')
    stormDecision()

#tells the user what happens if they chose to find shelter and asks the user to decide what to do when the bear wakes up
def cave():
  time.sleep(0.6)
  printFast("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
  time.sleep(0.6)
  printSlow("You find a cave that seems perfect to protect you from the brewing storm. When you enter the cave, you find a hibernating bear inside.")
  x = input(printSlow(" The Bear wakes up! What do you do: '" + Fore. BLUE + "Stay" + Style.RESET_ALL + "' or '" + Fore.BLUE + "RUN" + Style.RESET_ALL + "'?"))
  if (x.lower() == "stay"):
    printSlow("It turns out that the bear is tame, and ends up being your only friend as you live out the rest of your sad life, forever stranded on the island. Hey...one friend is better than none, right " + name + "?")
    #this is another possible ending to the story, it is all dependent on what the user choses to input
    playAgain()
  elif (x.lower() == "run"):
    printSlow("You escape from the cave leaving the bear to return to his peaceful hibernation. While running, you fall into a hole and twist your ankle. Luckily, it is safe, and you fall asleep from pure exhaustion.\n")
    wakeUp2()
  else:
    printSlow("Please enter " + Fore.BLUE + 'stay' + Style.RESET_ALL + ' or ' + Fore.BLUE + "'run'\n" + Style.RESET_ALL)
    cave()

#asks the user what they wake up in the hole and calls the resulting functions based on the user's response
def wakeUp2():
  time.sleep(0.6)
  printFast("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
  time.sleep(0.6)
  x = input(printSlow("What do you do when you wake up in the hole? " + Fore.BLUE + 'Yell' + Style.RESET_ALL + ' for help or meticulously ' + Fore.BLUE + 'dig ' + Style.RESET_ALL + "yourself out? "))
  if (x.lower() == 'yell'):
    voice()
  elif(x.lower() == 'dig'):
    smell()
  else:
    printSlow("Please enter " + Fore.BLUE + 'yell' + Style.RESET_ALL + ' or ' + Fore.BLUE + "dig'\n" + Style.RESET_ALL)
    wakeUp2()
  
#asks the user what they would like to do when they hear a voice and calls other functions depending on the user's input
def voice():
  time.sleep(0.6)
  printFast("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
  time.sleep(0.6)
  x = input(printSlow("To your suprise, you hear someone say something but they are too far away for you to hear. What do you do " + name + "? " + Fore.BLUE + 'Stop' + Style.RESET_ALL + ' talking or ' + Fore.BLUE + 'Yell' + Style.RESET_ALL + " louder. "))
  if (x.lower() == 'stop'):
    printSlow(Fore.RED + "You stay in the hole forever, " + Style.RESET_ALL + "living off the roots and moss you find on the walls of the hole, and a meager supply of rain water for the rest of your days.\n")
    playAgain()
  elif (x.lower() == 'yell'):
    footsteps()
  else:
    printSlow("Please enter " + Fore.BLUE + 'stop' + Style.RESET_ALL + ' or ' + Fore.BLUE + "yell\n" + Style.RESET_ALL)
    voice()

#asks the user what they want to do when they smell food being cooked and calls other functions
def smell():
  time.sleep(0.6)
  printFast("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
  time.sleep(0.6)
  x = input(printSlow("You smell something being cooked off in the distance, do you " + Fore.BLUE + 'ignore' + Style.RESET_ALL + ' it or ' + Fore.BLUE + 'go' + Style.RESET_ALL + " to investigate. "))
  if (x.lower() == 'ignore'):
    remainStranded()
  elif(x.lower() == 'go'):
    printSlow("When you walk over to where the smell is coming from, you suprisingly find another person cooking an unidentified meat.")
    findBob()
  else:
    printSlow("Please enter " + Fore.BLUE + 'ignore' + Style.RESET_ALL + ' or ' + Fore.BLUE + "go\n" + Style.RESET_ALL)
    smell()

#Terminator
def remainStranded():
  time.sleep(0.6)
  printFast("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
  time.sleep(0.6)
  printSlow(Fore.RED + "You remain on the island for 15 years, " + Style.RESET_ALL + "living off of the bitter food found on the island. One day a random boat finds you and rescues you. Hey, its better late than never!\n")#this is another possible ending
  playAgain()

#asks the user what they want to do when they hear footsteps approaching and calls other functions
def footsteps():
  time.sleep(0.6)
  printFast("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
  time.sleep(0.6)
  x = input(printSlow("You hear footsteps approaching and are filled with dread, wondering what type of monster is coming for you; however, right before you panic, you see someone look down the hole. Do you " + Fore.BLUE + 'run away'  + Style.RESET_ALL + ' or ' + Fore.BLUE + 'greet' + Style.RESET_ALL + " the individual? "))
  if (x.lower() == 'run away'):
    remainStranded()
  elif (x.lower() == 'greet'):
    findBob()
  else:
    printSlow("Please enter " + Fore.BLUE + 'run away' + Style.RESET_ALL + ' or ' + Fore.BLUE + "greet\n" + Style.RESET_ALL)
    footsteps()
    
#introduces Bob, asks the user if they will fix his plane, and calls other functions based on the user's input
def findBob():
  time.sleep(0.6)
  printFast("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
  time.sleep(0.6)
  printSlow("You greet the other individual and learn that his name is Bob, and that Bob has been stranded on the island when his plane crashed.")
  x = input(printSlow(" Bob shows you his damaged plane. Do you use your knowledge of plane engines to fix Bob's plane? " + Fore.BLUE + 'Yes' + Style.RESET_ALL + ' or ' + Fore.BLUE + "No\n" + Style.RESET_ALL))
  if (x.lower() == 'yes'):
    fixedIt()
  elif (x.lower() == 'no'):
    printSlow("Bob is enraged and you die a very tragic death when he sets his rabid turtle on you.")#one possible ending :)
    playAgain()
  else:
    printSlow("Please enter " + Fore.BLUE + 'yes' + Style.RESET_ALL + ' or ' + Fore.BLUE + "no\n" + Style.RESET_ALL)
    findBob()

#gives the user options on where to go after fixing the plane
def fixedIt():
  time.sleep(0.6)
  printFast("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
  time.sleep(0.6)
  printSlow(Fore.GREEN + "Hurray! " + Style.RESET_ALL + "You knew just how to fix it, " + name + " and you both escaped from the island safely.")
  x = input(printSlow("When you fly away from the island, which direction do you go? " + Fore.BLUE + 'North' + Style.RESET_ALL + ' or ' + Fore.BLUE + "East.\n" + Style.RESET_ALL))
  if (x.lower() == 'north'):
    printSlow("You land in Alaska, where you live out the rest of your life as the captain of a very successful Alaskan cruise line, and entertain anyone who asks with the tales of your adventure on the island.")
    playAgain()
  elif (x.lower() == 'east'):
    printSlow("You land in California, where a movie is made about your adventure, and you become famous. ")
    playAgain()
  else:
    printSlow("Please enter " + Fore.BLUE + 'north' + Style.RESET_ALL + ' or ' + Fore.BLUE + "east\n" + Style.RESET_ALL)
    fixedIt()

#lets user run the story again
def playAgain():
  time.sleep(0.6)
  printFast("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
  time.sleep(0.6)
  x = input(printSlow("Do you want to play again? "))
  if (x.lower() == 'yes', 'y', 'yeah','yep','sure','ok','okay'):
    screenClear() #clears text on screen
    explainScenario()
  else:
    printSlow("Goodbye :)")
    return

#allows the user's name to be used throughout the dialogue as a global variable
name = getName()

#starts the story - all of the other functions are called withing the functions
explainScenario()
