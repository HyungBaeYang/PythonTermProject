# -*- coding: cp949 -*-
loopFlag = 1

from internet import *


#### Menu  implementation
def printMenu():
    print("\n����Ư���� ����ǰ �нǹ� �ȳ� ���α׷�")





def launcherFunction(menu):

    if menu == 'p':
        temp = 1
        # PrintDOMtoXML()

    elif menu == 'e':
        print("========Menu==========")
        print("b1 : ���� ����, b2 : ���� ����")
        print("s1 : ����ö 1 ~ 4ȣ��, s2 : ����ö 5 ~ 8ȣ��")
        print("s3 : �ڷ���")
        print("s4 : ����ö 9ȣ��")
        print("t1 : ���� �ý�, t2 : ���� �ý�")
        print("========Menu==========")
        location = str(input('��ġ �ڵ� �Է� : '))
        item = str(input('��ǰ : '))
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
    print("�˻� ����Ű : e")
    menuKey = str(input(' '))
    launcherFunction(menuKey)
else:
    print("Thank you! Good Bye")
