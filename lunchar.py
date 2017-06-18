# -*- coding: cp949 -*-
loopFlag = 1

from xml.dom.minidom import parse, parseString
from xml.etree import ElementTree
from http.client import HTTPConnection
from http.server import BaseHTTPRequestHandler, HTTPServer
import urllib
from tkinter import *
from tkinter import font
import tkinter.messagebox

g_Tk = Tk()
g_Tk.geometry("400x600+700+200")

DataList = []
##global
conn = None
numOfData = 5895
regKey = "6f6c5578597a7a6131326e4e654561"

# 네이버 OpenAPI 접속 정보 information
server = 'openapi.seoul.go.kr:8088'

# smtp 정보
host = "smtp.gmail.com"  # Gmail SMTP 서버 주소.
port = "587"




def userURIBuilder(server, **user):
    str = "http://" + server + "/"


    for key in user.keys():
        str += user[key] + "/"
    print(str)
    return str


def connectOpenAPIServer():
    global conn, server
    conn = HTTPConnection(server)


def getDataFromtitle(title, Location):

    global server, regKey, conn
    utf2 = urllib.parse.quote(Location)

    utf = urllib.parse.quote(title)


    uri = userURIBuilder(server, key = regKey, Type ="xml", Service="SearchLostArticleService", Startindex="1", endindex="8", wb_code=str(utf), wb_location = str(Location))

    if conn == None:
        connectOpenAPIServer()

    conn.request("GET", uri)

    req = conn.getresponse()
    print(req.status)
    if int(req.status) == 200:
        print("data downloading complete!")
        return printDetailWithname(req.read(), title, Location)
    else:
        print("OpenAPI request has been failed!! please retry")
        return None

def printDetailWithname(strXml, name, Location):
    from xml.etree import ElementTree
    tree = ElementTree.fromstring(strXml)

    global DataList
    DataList.clear()

    print(strXml)
        # Book 엘리먼트를 가져옵니다.
    itemElements = tree.getiterator("row")  # return list type
    print(itemElements)
    for item in itemElements:
        get_name = item.find('GET_NAME')
        if name in get_name.text:
            id = item.find('ID')
            adres = item.find('TAKE_PLACE')
            dataTitle = item.find('GET_DATE')
            location = item.find('GET_POSITION')
            #print('------------------')
            #RenderText.insert("물품 ID : ", id.text)
            #RenderText.insert("잃어버린 장소 : ", adres.text)
            #RenderText.insert("잃어버린 물품 : ", get_name.text)
            #RenderText.insert("잃어버린 날짜 : ", dataTitle.text)
            #RenderText.insert("현재 위치 : ", location.text)
            #print('------------------')


            for i in range(len(itemElements)):
                RenderText.insert(i, "[")
                RenderText.insert(i, i + 1)
                RenderText.insert(i, "] ")
                RenderText.insert(i, "물품 ID : ")
                RenderText.insert(i, id.text)
                RenderText.insert(i, "굈")
                RenderText.insert(i, "분실장소 : ")
                RenderText.insert(i, adres.text)
                RenderText.insert(i, "굈")
                RenderText.insert(i, "분실물품 : ")
                RenderText.insert(i, get_name.text)
                RenderText.insert(i, "굈")
                RenderText.insert(i, "분실날짜 : ")
                RenderText.insert(i, dataTitle.text)
                RenderText.insert(i, "굈")
                RenderText.insert(i, "현재위치 : ")
                RenderText.insert(i, location.text)
                RenderText.insert(i, "굈굈")

def checkConnection():
    global conn
    if conn == None:
        print("Error : connection is fail")
        return False
    return True


#### Menu  implementation
def printMenu():
    Tempfont = font.Font(g_Tk, size = 20, weight = 'bold', family = 'Consolas')
    mainText = Label(g_Tk, font = Tempfont, text = "서울특별시 귀중품 분실물 안내 프로그램")
    mainText.pack()
    mainText.place(x = 20)



def SearchListBox():
    global eSearchListBox
    ListBoxScrollbar = Scrollbar(g_Tk)
    ListBoxScrollbar.pack()
    ListBoxScrollbar.place(x = 150, y = 50)

    TempFont = font.Font(g_Tk, size = 15, weight = 'bold', family = 'Consolas')
    eSearchListBox = Listbox(g_Tk, font = TempFont, activestyle = 'none', width = 10, height = 1,
                            borderwidth = 12, relief = 'ridge', yscrollcommand = ListBoxScrollbar.set)

    eSearchListBox.insert(1, "서울 버스")
    eSearchListBox.insert(2, "지하철 1~4")
    eSearchListBox.insert(3, "지하철 5~8")
    eSearchListBox.insert(4, "지하철9호선")
    eSearchListBox.insert(5, "코레일")
    eSearchListBox.insert(6, "법인 택시")
    eSearchListBox.insert(7, "개인 택시")
    eSearchListBox.pack()
    eSearchListBox.place(x = 10, y = 50)

    ListBoxScrollbar.config(command = eSearchListBox.yview)

def InitInputLabel():
    global InputLabel
    TempFont = font.Font(g_Tk, size=15, weight='bold', family = 'Consolas')
    InputLabel = Entry(g_Tk, font = TempFont, width = 26, borderwidth = 12, relief = 'ridge')
    print(Entry)
    InputLabel.pack()
    InputLabel.place(x=10, y=105)


def InitSearchButton():
    TempFont = font.Font(g_Tk, size=12, weight='bold', family = 'Consolas')
    SearchButton = Button(g_Tk, font = TempFont, text="물품검색",  command=SearchButtonAction)
    SearchButton.pack()
    SearchButton.place(x=330, y=110)

def SearchButtonAction():
    global SearchListBox
    RenderText.configure(state='normal')
    RenderText.delete(0.0, END)  # ?댁? 異?? ?????紐⑤? ???
    iSearchIndex = SearchListBox.curselection()[0]

    if iSearchIndex == 0:  # ??왙愿?
        location = "b1"
        getDataFromtitle(Entry, location)
    elif iSearchIndex == 1:  # 紐⑤????
        location = "b2"
        getDataFromtitle(Entry, location)
    elif iSearchIndex == 2:  # 留??
        location = "s1"
        getDataFromtitle(Entry, location)
    elif iSearchIndex == 3:
        location = "s2"
        getDataFromtitle(Entry, location)
    elif iSearchIndex == 4:
        location = "s4"
        getDataFromtitle(Entry, location)
    elif iSearchIndex == 5:
        location = "s3"
        getDataFromtitle(Entry, location)
    elif iSearchIndex == 6:
        location = "t1"
        getDataFromtitle(Entry, location)
    elif iSearchIndex == 7:
        location = "t2"
        getDataFromtitle(Entry, location)


    RenderText.configure(state='disabled')


def InitRenderText():
    global RenderText

    RenderTextScrollbar = Scrollbar(g_Tk)
    RenderTextScrollbar.pack()
    RenderTextScrollbar.place(x=375, y=200)

    TempFont = font.Font(g_Tk, size=10, family='Consolas')
    RenderText = Text(g_Tk, width=49, height=27, borderwidth=12, relief='ridge', yscrollcommand=RenderTextScrollbar.set)
    RenderText.pack()
    RenderText.place(x=10, y=215)
    RenderTextScrollbar.config(command=RenderText.yview)
    RenderTextScrollbar.pack(side=RIGHT, fill=BOTH)

    RenderText.configure(state='disabled')



#def launcherFunction(menu):

#    if menu == 'e':
#        print("========Menu==========")
#        print("b1 : 서울 버스, b2 : 마을 버스")
#        print("s1 : 지하철 1 ~ 4호선, s2 : 지하철 5 ~ 8호선")
#        print("s3 : 코레일")
#        print("s4 : 지하철 9호선")
#        print("t1 : 법인 택시, t2 : 개인 택시")
#        print("========Menu==========")
#        location = str(input('위치 코드 입력 : '))
#        item = str(input('물품 : '))
#        ret = getDataFromtitle(item, location)
#    else:
#        print("error : unknow menu key")


##### run #####
#while (loopFlag > 0):
#    printMenu()
#    print("검색 단축키 : e")
#    menuKey = str(input(' '))
##    launcherFunction(menuKey)
#else:
#    print("Thank you! Good Bye")

printMenu()
SearchListBox()
InitInputLabel()
InitSearchButton()
InitRenderText()

g_Tk.mainloop()
