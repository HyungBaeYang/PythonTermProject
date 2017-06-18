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

# ���̹� OpenAPI ���� ���� information
server = 'openapi.seoul.go.kr:8088'

# smtp ����
host = "smtp.gmail.com"  # Gmail SMTP ���� �ּ�.
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
        # Book ������Ʈ�� �����ɴϴ�.
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
            #RenderText.insert("��ǰ ID : ", id.text)
            #RenderText.insert("�Ҿ���� ��� : ", adres.text)
            #RenderText.insert("�Ҿ���� ��ǰ : ", get_name.text)
            #RenderText.insert("�Ҿ���� ��¥ : ", dataTitle.text)
            #RenderText.insert("���� ��ġ : ", location.text)
            #print('------------------')


            for i in range(len(itemElements)):
                RenderText.insert(i, "[")
                RenderText.insert(i, i + 1)
                RenderText.insert(i, "] ")
                RenderText.insert(i, "��ǰ ID : ")
                RenderText.insert(i, id.text)
                RenderText.insert(i, "�n")
                RenderText.insert(i, "�н���� : ")
                RenderText.insert(i, adres.text)
                RenderText.insert(i, "�n")
                RenderText.insert(i, "�нǹ�ǰ : ")
                RenderText.insert(i, get_name.text)
                RenderText.insert(i, "�n")
                RenderText.insert(i, "�нǳ�¥ : ")
                RenderText.insert(i, dataTitle.text)
                RenderText.insert(i, "�n")
                RenderText.insert(i, "������ġ : ")
                RenderText.insert(i, location.text)
                RenderText.insert(i, "�n�n")

def checkConnection():
    global conn
    if conn == None:
        print("Error : connection is fail")
        return False
    return True


#### Menu  implementation
def printMenu():
    Tempfont = font.Font(g_Tk, size = 20, weight = 'bold', family = 'Consolas')
    mainText = Label(g_Tk, font = Tempfont, text = "����Ư���� ����ǰ �нǹ� �ȳ� ���α׷�")
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

    eSearchListBox.insert(1, "���� ����")
    eSearchListBox.insert(2, "����ö 1~4")
    eSearchListBox.insert(3, "����ö 5~8")
    eSearchListBox.insert(4, "����ö9ȣ��")
    eSearchListBox.insert(5, "�ڷ���")
    eSearchListBox.insert(6, "���� �ý�")
    eSearchListBox.insert(7, "���� �ý�")
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
    SearchButton = Button(g_Tk, font = TempFont, text="��ǰ�˻�",  command=SearchButtonAction)
    SearchButton.pack()
    SearchButton.place(x=330, y=110)

def SearchButtonAction():
    global SearchListBox
    RenderText.configure(state='normal')
    RenderText.delete(0.0, END)  # ?��? �?? ?????모�? ???
    iSearchIndex = SearchListBox.curselection()[0]

    if iSearchIndex == 0:  # ??���?
        location = "b1"
        getDataFromtitle(Entry, location)
    elif iSearchIndex == 1:  # 모�????
        location = "b2"
        getDataFromtitle(Entry, location)
    elif iSearchIndex == 2:  # �??
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
#        print("b1 : ���� ����, b2 : ���� ����")
#        print("s1 : ����ö 1 ~ 4ȣ��, s2 : ����ö 5 ~ 8ȣ��")
#        print("s3 : �ڷ���")
#        print("s4 : ����ö 9ȣ��")
#        print("t1 : ���� �ý�, t2 : ���� �ý�")
#        print("========Menu==========")
#        location = str(input('��ġ �ڵ� �Է� : '))
#        item = str(input('��ǰ : '))
#        ret = getDataFromtitle(item, location)
#    else:
#        print("error : unknow menu key")


##### run #####
#while (loopFlag > 0):
#    printMenu()
#    print("�˻� ����Ű : e")
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
