from colorama import *
from art import *
#Gen Dependencies
from pysteamcmdwrapper import SteamCMD, SteamCMDException

#local scripts
import router
import menu

init()

def main():
    global ready
    selection = ""
    tprint("PZ Server Control", font = "colossal")
    menu.printout("Manager for running your dedicated server", menu.colors[1])
    menu.printout("V1 by Bisqu3.", menu.colors[2])
    menu.printout("Type help for a list of commands", menu.colors[4])
    ready = True
    print(ready)
    while selection == "":
        x = input("> ")
        #MAIN LOOP FOR MENU CONSOLE INPUT
        for i in menu.menu_options:
            if i == x:
                selection = x
                #all functions should return a string, a color format, and a route number.
                #if the route number is 0  the terminal resets. if a code is sent that means another script needs to be ran and it will refer to the assigned dictionary to run the next one.
                p, c, n = menu.menu_options[selection]
                menu.printout(p,c)
                if n == 0:
                    selection = ""
                else:
                    while n != str(0):
                        a = router.route(n)
                        n = a 
                    selection = ""

main()