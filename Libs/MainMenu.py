import os as OS
from time import sleep as Sleep, time as GetCurrentEpoch
def cls():OS.system("cls" if OS.name == "nt" else "clear")
BigLettering
def DisplayMainMenu():
    IndexCounter = 0
    ShowMenu = True
    StartTime = int(GetCurrentEpoch())
    while ShowMenu:
        cls()
        IrradiatedName = ""
        for Index, Letter in enumerate("IRRADIATED"):
            IrradiatedName+="_" if Index == IndexCounter else Letter
        print(IrradiatedName)
        IndexCounter += 1
        if IndexCounter > 9:
            IndexCounter = 0

        if int(GetCurrentEpoch())-StartTime >= 10: ShowMenu = False
        Sleep(0.1)
DisplayMainMenu()
