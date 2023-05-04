from colorama import *
#Gen Dependencies
from pysteamcmdwrapper import SteamCMD, SteamCMDException

#local scripts
import menu

init()

def main():
    global ready
    selection = ""
    r = menu.randomcol()
    menu.printout("""8888888b.  8888888888P      .d8888b.                                                  .d8888b.                    888                     888""", r)
    menu.printout("""888   Y88b       d88P      d88P  Y88b                                                d88P  Y88b                   888                     888""", r)
    menu.printout("""888    888      d88P       Y88b.                                                     888    888                   888                     888""", r)
    menu.printout("""888   d88P     d88P         "Y888b.    .d88b.  888d888 888  888  .d88b.  888d888     888         .d88b.  88888b.  888888 888d888  .d88b.  888""", r)
    menu.printout("""8888888P"     d88P             "Y88b. d8P  Y8b 888P"   888  888 d8P  Y8b 888P"       888        d88""88b 888 "88b 888    888P"   d88""88b 888""", r)
    menu.printout("""888          d88P                "888 88888888 888     Y88  88P 88888888 888         888    888 888  888 888  888 888    888     888  888 888""", r)
    menu.printout("""888         d88P           Y88b  d88P Y8b.     888      Y8bd8P  Y8b.     888         Y88b  d88P Y88..88P 888  888 Y88b.  888     Y88..88P 888""", r)
    menu.printout("""888        d8888888888      "Y8888P"   "Y8888  888       Y88P    "Y8888  888          "Y8888P"   "Y88P"  888  888  "Y888 888      "Y88P"  888""", r)
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
                p, c, n = menu.menu_options[selection]()
                menu.printout(p,c)
                if n == 0:
                    selection = ""
                else:
                    while n != 0:
                        print("TODO")
                        n = 0
                        selection = ""

main()