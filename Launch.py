from art import *
from colorama import *
import random
init()
menu_options = {}

colors = [Fore.RED, Fore.WHITE, Fore.BLUE, Fore.GREEN, Fore.YELLOW]
key = ["fully connected","disconnected","allowed"]
status = {
    "fully connected": 0,
    "disconnected": 0,
    "allowed": 0,
}

def randomcol():
    x = random.randint(0, 4)
    return colors[x]
def printout(text, color):
    print(color+str(text)+Style.RESET_ALL)

def getplayerstatus():
    f = open("/workspaces/PZservercontrol/demopath/log1.txt", "r")
    status["allowed"] = 0
    for i in f:
        for word in key:
            if i.find(word) != -1:
                status[word] += 1
    status["allowed"] -= status["fully connected"]
    if status["allowed"] < 0: status["allowed"] = 0
    status["fully connected"] -= status["disconnected"]
    status["disconnected"] = 0
    f.close()
    return status, Fore.MAGENTA, 0

def startserver():
    print("TODO")
    return "todo", Fore.RED, 0
def updateserver():
    print("TODO")
    return "todo", Fore.RED, 0
def printhelp():
    f = open("/workspaces/PZservercontrol/demopath/help.txt", "r")
    a = f.read()
    f.close()
    return a, Fore.RED, 0

def main():
    selection = ""
    tprint("PZ Server Control", font = "colossal")
    printout("Manager for running your dedicated server on windows", Fore.WHITE)
    printout("V1 by Bisqu3.", Fore.CYAN)
    printout("Type help for a list of commands", Fore.YELLOW)
    while selection == "":
        x = input("> ")
        #MAIN LOOP FOR MENU CONSOLE INPUT
        for i in menu_options:
            if i == x:
                selection = x
                #all functions should return a string, a color format, and a route number.
                #if the route number is 0  the terminal resets. if a code is sent that means another script needs to be ran and it will refer to the assigned dictionary to run the next one.
                p, c, n = menu_options[selection]
                printout(p,c)
                if n == 0:
                    selection = ""
                else:
                    print("TODO route to next script")

menu_options = {
    "start": startserver(),
    "status": getplayerstatus(),
    "update": updateserver(),
    "help": printhelp(),
    }

print(menu_options)
main()