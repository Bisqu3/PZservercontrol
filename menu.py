#Graphic Dependencies
from colorama import *

#System Dependencies
import random
import datetime
from pathlib import Path
from subprocess import call
from pysteamcmdwrapper import SteamCMD, SteamCMDException

import config

run32 = config.server32
serverdest = config.serverdest
logdest = config.logdest
#
progdest = str(Path.cwd())
steamdest = progdest

global ready 
ready = 1

global _time 
_time = datetime.datetime.now()
print(str(_time.day)+"-"+str(_time.month))

colors = [Fore.RED, Fore.WHITE, Fore.BLUE, Fore.GREEN, Fore.YELLOW, Fore.MAGENTA, Style.RESET_ALL]
key = ["fully connected","disconnected","allowed"]
status = {
    "fully connected": 0,
    "disconnected": 0,
    "allowed": 0,
}

def randomcol():
    #assigns a random color from the colors list
    x = random.randint(0, 5)
    return colors[x]
def printout(text, color):
    #pairs text with color and prints the result.
    print(color+str(text)+colors[6])

def getplayerstatus():
    f = open(logdest+"/28-04-23_10-23-38_user.txt", "r")
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
    return status, colors[1], 0

def start():
    if run32 == True:
        call(serverdest + "/StartServer32.bat")
    else:
        call(serverdest + "/StartServer64.bat")

def startserver():
    x = input("restart server automatically if it crashes? Y/N > ")
    if x.upper() == "Y":
        while True:
            start()
    elif x.upper() == "N":
        start()
    else: 
        startserver()
    return "Server returned from running state.", colors[0], 0
def updateserver():
    print("Checking SteamCMD...")
    s = SteamCMD(steamdest)
    global ready
    try:
        s.install()
        result = "SteamCMD Installed to "+steamdest
    except SteamCMDException:
        result = "SteamCMD already installed at "+steamdest
    try:
        s.app_update(380870, serverdest, validate=True)
        result = "Server at "+serverdest+" is up to date"
    except SteamCMDException:
        result = "Install Error "+serverdest
    return result, colors[4], 0
    
def printhelp():
    f = open(progdest+"/text/help.txt", "r")
    a = f.read()
    f.close()
    return a, colors[0], 0

def rcon():
    with open("server_control.py") as f:
        exec(f.read())
    return "connected?", colors[1], 0

menu_options = {
    "start": startserver,
    "status": getplayerstatus,
    "update": updateserver,
    "help": printhelp,
    "connect": rcon,
    }