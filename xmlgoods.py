# -*- coding: cp949 -*-
from xml.dom.minidom import parse, parseString
from xml.etree import ElementTree

##### global
xmlFD = -1
goodsDoc = None

#### xml 관련 함수 구현
def LoadXMLFromFile():
    fileName = str(input ("로드할 xml 파일 이름을 입력하세요 :"))
    global xmlFD, goodsDoc
    try:
        xmlFD = open(fileName)
    except IOError:
        print ("invalid file name or path")
    else:
        try:
            dom = parse(xmlFD)
        except Exception:
            print ("loading fail!!!")
        else:
            print ("XML 로드 완료 !!")
            goodsDoc = dom
            return dom
    return None

def GoodsFree():
    if checkDocument():
        goodsDoc.unlink()

def PrintDOMtoXML():
    if checkDocument():
        print(goodsDoc.toxml())


def PrintBookList(tags):
    global GoodsDoc
    if not checkDocument():
        return None

    goodslist = goodsDoc.childNodes
    goods = goodslist[0].childNodes
    for item in goods:
        if item.nodeName == "goods":
            subitems = item.childNodes
            for atom in subitems:
                if atom.nodeName in tags:
                    print("title=", atom.firstChild.nodeValue)


def checkDocument():
    global GoodsDoc
    if GoodsDoc == None:
        print("Error : Document is empty")
        return False
    return True
