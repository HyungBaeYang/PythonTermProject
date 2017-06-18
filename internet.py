
from xml.dom.minidom import parse, parseString
from xml.etree import ElementTree
from http.client import HTTPConnection
from http.server import BaseHTTPRequestHandler, HTTPServer
from tkinter import *
from tkinter import font

import urllib
import tkinter.messagebox

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
            print('------------------')
            print("물품 ID : ", id.text)
            print("잃어버린 장소 : ", adres.text)
            print("잃어버린 물품 : ", get_name.text)
            print("잃어버린 날짜 : ", dataTitle.text)
            print("현재 위치 : ", location.text)
            print('------------------')


def checkConnection():
    global conn
    if conn == None:
        print("Error : connection is fail")
        return False
    return True
