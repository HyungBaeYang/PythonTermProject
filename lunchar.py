# -*- coding: cp949 -*-
loopFlag = 1

from internet import *


#### Menu  implementation
def printMenu():
    print("\n서울특별시 귀중품 분실물 안내 프로그램")





def launcherFunction(menu):

    if menu == 'p':
        temp = 1
        # PrintDOMtoXML()

    elif menu == 'e':
        print("========Menu==========")
        print("b1 : 서울 버스, b2 : 마을 버스")
        print("s1 : 지하철 1 ~ 4호선, s2 : 지하철 5 ~ 8호선")
        print("s3 : 코레일")
        print("s4 : 지하철 9호선")
        print("t1 : 법인 택시, t2 : 개인 택시")
        print("========Menu==========")
        location = str(input('위치 코드 입력 : '))
        item = str(input('물품 : '))
        print(item)
        print(location)
        ret = getDataFromtitle(item, location)
        # keyword = str(input ('input keyword to search :'))
        # printBookList(SearchBookTitle(keyword))
    else:
        print("error : unknow menu key")


##### run #####
while (loopFlag > 0):
    printMenu()
    print("검색 단축키 : e")
    menuKey = str(input(' '))
    launcherFunction(menuKey)
else:
    print("Thank you! Good Bye")
