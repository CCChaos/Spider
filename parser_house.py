# coding=utf-8
from bs4 import BeautifulSoup
import re

def ParseNode4OVPrice(tag_price):
    price = {'overview_price_total':''}
    span_total = tag_price.find(attrs={'class':'total'})
    if span_total != None:
        price['overview_price_total']=span_total.text
    return price

def ParseNode4OVHouseInfo(tag_houseInfo):
    house_info = {'overview_houseInfo_room_mainInfo':'',
    'overview_houseInfo_room_subInfo':'',
    'overview_houseInfo_area_mainInfo':'',
    'overview_houseInfo_area_subInfo':''}

    div_room = tag_houseInfo.find(attrs={'class':'room'})
    if div_room != None:
        div_room_main = div_room.find(attrs={'class':'mainInfo'})
        if div_room_main != None:
            house_info['overview_houseInfo_room_mainInfo']=div_room_main.text
        div_room_sub = div_room.find(attrs={'class':'subInfo'})
        if div_room_sub != None:
            house_info['overview_houseInfo_room_subInfo']=div_room_sub.text
    div_area = tag_houseInfo.find(attrs={'class':'area'})
    if div_area != None:
        div_area_main = div_area.find(attrs={'class':'mainInfo'})
        if div_area_main != None:
            house_info['overview_houseInfo_area_mainInfo']=div_area_main.text
        div_area_sub = div_area.find(attrs={'class':'subInfo'})
        if div_area_sub != None:
            house_info['overview_houseInfo_area_subInfo']=div_area_sub.text
    return house_info
        

def ParseNode4Communite(tag_commu):
    communite = []
    for child in tag_commu.children:
        if child.name == 'a':
            href = child.get('href')
            if href == None:
                continue
            m = re.match(r'^\/xiaoqu\/(\d*)\/$', href)
            if m == None:
                continue
            communite.append(['id', m.group(1)])
            communite.append(['name',child.string])
    return communite