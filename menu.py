#Graphic Dependencies
from art import *
from colorama import *

#System Dependencies
import random
from pathlib import Path
import os
from pysteamcmdwrapper import SteamCMD, SteamCMDException

serverdest = "/workspaces/PZservercontrol/servertest"
logdest = "/workspaces/PZservercontrol/demopath"
#
progdest = str(Path.cwd())
steamdest = progdest

global ready 
ready = 1

colors = [Fore.RED, Fore.WHITE, Fore.BLUE, Fore.GREEN, Fore.YELLOW, Fore.MAGENTA, Style.RESET_ALL]
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
    print(color+str(text)+colors[6])

def getplayerstatus():
    f = open(logdest+"/log1.txt", "r")
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
    return status, colors[5], 0

def startserver():
    os.system(serverdest + "/start.bat")
    return "Server started. launching monitor", colors[0], 2
def updateserver():
    print("Checking SteamCMD...")
    s = SteamCMD(steamdest)
    global ready
    try:
        s.install()
        result = "SteamCMD Installed"
    except SteamCMDException:
        result = "SteamCMD Found."
    return result, colors[4], 1
    
def printhelp():
    f = open(progdest+"/text/help.txt", "r")
    a = f.read()
    f.close()
    return a, colors[0], 0

menu_options = {
    "start": startserver(),
    "status": getplayerstatus(),
    "update": updateserver(),
    "help": printhelp(),
    }