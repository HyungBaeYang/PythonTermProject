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
    mainText = Label(g_Tk, font = Tempfont, text = "����Ư���� ����ǰ �нǹ� �ȳ� ���α׷�")
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

    SearchListBox.insert(1, "���� ����")
    SearchListBox.insert(2, "����ö 1~4")
    SearchListBox.insert(3, "����ö 5~8")
    SearchListBox.insert(4, "����ö9ȣ��")
    SearchListBox.insert(5, "�ڷ���")
    SearchListBox.insert(6, "���� �ý�")
    SearchListBox.insert(7, "���� �ý�")
    SearchListBox.pack()
    SearchListBox.place(x = 10, y = 50)

    SearchListBox.config(command = SearchListBox.yview)

def InitSearchButton():
    TempFont = font.Font(g_Tk, size=12, weight='bold', family = 'Consolas')
    SearchButton = Button(g_Tk, font = TempFont, text="��ǰ�˻�",  command=SearchButtonAction)
    SearchButton.pack()
    SearchButton.place(x=330, y=110)

def SearchButtonAction():
    global SearchListBox

    RenderText.configure(state='normal')
    RenderText.delete(0.0, END)  # ?��? �?? ?????모�? ???
    iSearchIndex = SearchListBox.curselection()[0]  # 리�??��????��???�??��?�?
    if iSearchIndex == 0:  # ??���?
        location = "b1"
        item = ""
        ret = getDataFromtitle(item, location)
    elif iSearchIndex == 1:  # 모�????
        item = ""
        location = "b2"
        ret = getDataFromtitle(item, location)
    elif iSearchIndex == 2:  # �??
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
        print("b1 : ���� ����, b2 : ���� ����")
        print("s1 : ����ö 1 ~ 4ȣ��, s2 : ����ö 5 ~ 8ȣ��")
        print("s3 : �ڷ���")
        print("s4 : ����ö 9ȣ��")
        print("t1 : ���� �ý�, t2 : ���� �ý�")
        print("========Menu==========")
        location = str(input('��ġ �ڵ� �Է� : '))
        item = str(input('��ǰ : '))
        ret = getDataFromtitle(item, location)
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
