# -*- coding:utf-8 -*-
loopFlag = 1

from xml.dom.minidom import parse, parseString
from xml.etree import ElementTree
from http.client import HTTPConnection
from http.server import BaseHTTPRequestHandler, HTTPServer
import urllib
from tkinter import *
from tkinter import font
import tkinter.messagebox

import smtplib
import mimetypes

from email.mime.base import MIMEBase
from email.mime.text import MIMEText 	#텍스트를 위해서





#global value



g_Tk = Tk()
g_Tk.geometry("800x600+700+200")

DataList = []
##global
conn = None
numOfData = 5895
regKey = "6f6c5578597a7a6131326e4e654561"

#서울 열린 데이터 광장 연결 변수.
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

    # Book 엘리먼트를 가져옵니다.
    itemElements = tree.getiterator("row")  # return list type
    for item in itemElements:
        get_name = item.find('GET_NAME')
        if name in get_name.text:
            id = item.find('ID')
            adres = item.find('TAKE_PLACE')
            dataTitle = item.find('GET_DATE')
            location = item.find('GET_POSITION')
            for i in range(len(item)):
                RenderText.insert(INSERT, "[")
                RenderText.insert(INSERT, i + 1)
                RenderText.insert(INSERT, "] ")
                RenderText.insert(INSERT, "물품 ID : ")
                RenderText.insert(INSERT, id.text)
                RenderText.insert(INSERT, "\n")
                RenderText.insert(INSERT, "분실장소 : ")
                RenderText.insert(INSERT, adres.text)
                RenderText.insert(INSERT, "\n")
                RenderText.insert(INSERT, "분실물품 : ")
                RenderText.insert(INSERT, get_name.text)
                RenderText.insert(INSERT, "\n")
                RenderText.insert(INSERT, "분실날짜 : ")
                RenderText.insert(INSERT, dataTitle.text)
                RenderText.insert(INSERT, "\n")
                RenderText.insert(INSERT, "현재위치 : ")
                RenderText.insert(INSERT, location.text)
                RenderText.insert(INSERT, "\n\n")

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



def initSearchListBox():
    global SearchListBox
    ListBoxScrollbar = Scrollbar(g_Tk)
    ListBoxScrollbar.pack()
    ListBoxScrollbar.place(x = 150, y = 50)

    TempFont = font.Font(g_Tk, size = 15, weight = 'bold', family = 'Consolas')
    SearchListBox = Listbox(g_Tk, font = TempFont, activestyle = 'none', width = 10, height = 1,
                            borderwidth = 12, relief = 'ridge', yscrollcommand = ListBoxScrollbar.set)

    SearchListBox.insert(1, "서울 버스")
    SearchListBox.insert(2, "지하철 1~4")
    SearchListBox.insert(3, "지하철 5~8")
    SearchListBox.insert(4, "지하철9호선")
    SearchListBox.insert(5, "코레일")
    SearchListBox.insert(6, "법인 택시")
    SearchListBox.insert(7, "개인 택시")
    SearchListBox.pack()
    SearchListBox.place(x = 10, y = 50)

    ListBoxScrollbar.config(command = SearchListBox.yview)

def InitInputLabel():
    global InputLabel
    TempFont = font.Font(g_Tk, size=15, weight='bold', family = 'Consolas')
    InputLabel = Entry(g_Tk, font = TempFont, width = 26, borderwidth = 12, relief = 'ridge')
    InputLabel.pack()
    InputLabel.place(x=10, y=105)


def InitSearchButton():
    TempFont = font.Font(g_Tk, size=12, weight='bold', family = 'Consolas')
    SearchButton = Button(g_Tk, font = TempFont, text="물품검색",  command=SearchButtonAction)
    SearchButton.pack()
    SearchButton.place(x=330, y=110)

def mailSendButton():
    TempFont = font.Font(g_Tk, size=12, weight='bold', family = 'Consolas')
    SearchButton = Button(g_Tk, font = TempFont, text="메일전송 ",  command=SearchButtonAction)
    SearchButton.pack()
    SearchButton.place(x=330, y=150)


def mailSendButtonAction():

    host = "smtp.gmail.com"  # Gmail STMP 서버 주소.
    port = "587"
    htmlFileName = "logo.html"

    senderAddr = "zzang1725@gmail.com"  # 보내는 사람 email 주소.
    recipientAddr = "zzang1725@naver.com"  # 받는 사람 email 주소.

    msg = MIMEBase("multipart", "alternative")
    msg['Subject'] = "분실물 정보 메일입니다."

    msg['From'] = senderAddr
    msg['To'] = recipientAddr

    SendEmail()


def SearchButtonAction():
    global SearchListBox
    RenderText.configure(state='normal')
    RenderText.delete(0.0, END)  # ?댁? 異?? ?????紐⑤? ???
    iSearchIndex = SearchListBox.curselection()[0]
    if iSearchIndex == 0:  # ??꽌愿?
        print(InputLabel.get())
        location = "b1"
        getDataFromtitle(InputLabel.get(), location)
    elif iSearchIndex == 1:  # 紐⑤????
        location = "b2"
        getDataFromtitle(InputLabel.get(), location)
    elif iSearchIndex == 2:  # 留??
        location = "s1"
        getDataFromtitle(InputLabel.get(), location)
    elif iSearchIndex == 3:
        location = "s2"
        getDataFromtitle(InputLabel.get(), location)
    elif iSearchIndex == 4:
        location = "s4"
        getDataFromtitle(InputLabel.get(), location)
    elif iSearchIndex == 5:
        location = "s3"
        getDataFromtitle(InputLabel.get(), location)
    elif iSearchIndex == 6:
        location = "t1"
        getDataFromtitle(InputLabel.get(), location)
    elif iSearchIndex == 7:
        location = "t2"
        getDataFromtitle(InputLabel.get(), location)


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


def SendEmail():
    # 메일을 발송한다.
    s = smtplib.MySMTP(host, port)
    # s.set_debuglevel(1)        # 디버깅이 필요할 경우 주석을 푼다.
    s.ehlo()
    s.starttls()
    s.ehlo()
    s.login("milkelf.choi@gmail.com", "**********")
    s.sendmail(senderAddr, [recipientAddr], msg.as_string())
    s.close()


printMenu()
initSearchListBox()
InitInputLabel()
InitSearchButton()
mailSendButton()
InitRenderText()

g_Tk.mainloop()
