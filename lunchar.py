
loopFlag = 1
from xmlgoods import *


def printMenu():
    print("₩nWelcome! Book Manager Program (xml version)")
    print("========Menu==========")
    print("Load xml:  l")
    print("Print dom to xml: p")
    print("Quit program:   q")
    print("print Goods list: b")
    print("========Menu==========")



def launcherFunction(menu):
    if menu ==  'l':
        LoadXMLFromFile()
    elif menu == 'q':
        QuitBookMgr()
    elif menu == 'p':
        PrintDOMtoXML()
    elif menu == 'b':
        PrintBookList(["title",])
    else:
        print ("error : unknow menu key")


def QuitBookMgr():
    global loopFlag
    loopFlag = 0
    #BooksFree()


while(loopFlag > 0):
    printMenu()
    menuKey = str(input ('select menu :'))
    launcherFunction(menuKey)
else:
    print ("Thank you! Good Bye")