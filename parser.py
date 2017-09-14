# coding=utf-8
from bs4 import BeautifulSoup
import Queue
import re
from parser_house import ParseNode4Communite
from parser_house import ParseNode4OVHouseInfo
from parser_house import ParseNode4OVPrice

def ParseHome4ID(homepage):
    id_dict = {}
    soup = BeautifulSoup(homepage, "lxml")
    for link in soup.find_all('a'):
        code = link.get('data-housecode')
        if code != None:
            id_dict[code] = None

    return id_dict

def ParseHouse4Info(housepage):
    ret_house = {}
    soup = BeautifulSoup(housepage, "lxml")
    div = soup.find(attrs={'class':'overview'})
    if div == None:
        return ret_house
    content = div.find(attrs={'class':'content'})
    if content == None:
        return ret_house

    ov_price = content.find(attrs={'class':'price'})
    if ov_price != None:
        ret_price = ParseNode4OVPrice(ov_price)
        ret_house.update(ret_price)

    ov_houseInfo = content.find(attrs={'class':'houseInfo'})
    if ov_houseInfo != None:
        ret_houseInfo = ParseNode4OVHouseInfo(ov_houseInfo)
        ret_house.update(ret_houseInfo)
    return ret_house