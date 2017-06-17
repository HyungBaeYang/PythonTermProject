# -*- coding: cp949 -*-
loopFlag = 1

from internet import *
from tkinter import *
from tkinter import font
import tkinter.messagebox

g_Tk = Tk()
g_Tk.geometry("400x600+700+200")

DataList = []





#### Menu  implementation
def printMenu():
    Tempfont = font.Font(g_Tk, size = 20, weight = 'bold', family = 'Consolas')
    mainText = Label(g_Tk, font = Tempfont, text = "서울특별시 귀중품 분실물 안내 프로그램")
    mainText.pack()
    mainText.place(x = 20)



def SearchListBox():
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

    SearchListBox.config(command = SearchListBox.yview)

def InitSearchButton():
    TempFont = font.Font(g_Tk, size=12, weight='bold', family = 'Consolas')
    SearchButton = Button(g_Tk, font = TempFont, text="물품검색",  command=SearchButtonAction)
    SearchButton.pack()
    SearchButton.place(x=330, y=110)

def SearchButtonAction():
    global SearchListBox

    RenderText.configure(state='normal')
    RenderText.delete(0.0, END)  # ?댁? 異?? ?????紐⑤? ???
    iSearchIndex = SearchListBox.curselection()[0]  # 由ъ??몃????몃???媛??몄?湲?
    if iSearchIndex == 0:  # ??왙愿?
        location = "b1"
        item = ""
        ret = getDataFromtitle(item, location)
    elif iSearchIndex == 1:  # 紐⑤????
        item = ""
        location = "b2"
        ret = getDataFromtitle(item, location)
    elif iSearchIndex == 2:  # 留??
        item = ""
        location = "s1"
        ret = getDataFromtitle(item, location)
        item = ""
    elif iSearchIndex == 3:
        item = ""
        location = "s2"
        ret = getDataFromtitle(item, location)
    elif iSearchIndex == 4:
        item = ""
        location = "s4"
        ret = getDataFromtitle(item, location)
    elif iSearchIndex == 5:
        item = ""
        location = "s3"
        ret = getDataFromtitle(item, location)
    elif iSearchIndex == 6:
        item = ""
        location = "t1"
        ret = getDataFromtitle(item, location)
    elif iSearchIndex == 7:
        item = ""
        location = "t2"
        ret = getDataFromtitle(item, location)


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



def launcherFunction(menu):

    if menu == 'e':
        print("========Menu==========")
        print("b1 : 서울 버스, b2 : 마을 버스")
        print("s1 : 지하철 1 ~ 4호선, s2 : 지하철 5 ~ 8호선")
        print("s3 : 코레일")
        print("s4 : 지하철 9호선")
        print("t1 : 법인 택시, t2 : 개인 택시")
        print("========Menu==========")
        location = str(input('위치 코드 입력 : '))
        item = str(input('물품 : '))
        ret = getDataFromtitle(item, location)
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
