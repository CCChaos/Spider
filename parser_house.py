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

def ParseNode4OVAroundInfo(tag_aroundInfo):
    around_info = {'overview_aroundInfo_cummunityID':'',
    'overview_aroundInfo_communityName':'',
    'overview_aroundInfo_areaName1':'',
    'overview_aroundInfo_areaName2':'',
    'overview_aroundInfo_houseRecordID':''}
    div_community = tag_aroundInfo.find('communityName')
    if not div_community is None:
        ret_comm = ParseNode4Communite(div_community)
        around_info['overview_aroundInfo_cummunityID'] = ret_comm['id']
        around_info['overview_aroundInfo_communityName'] = ret_comm['name']
    div_area = tag_aroundInfo.find('areaNanme')
    if not div_area is None:
        span_info = div_area.find('span',attrs={'class':'info'})
        if not span_info is None:
            i = 1
            for child in span_info.children:
                key = 'overview_aroundInfo_areaName%d' % i
                around_info[key] = child.string
                i = i + 1
    div_houseRecord = tag_aroundInfo.find('houseRecord')
    if not div_houseRecord is None:
        span_info = div_houseRecord.find('span',attrs={'class':'info'})
        if not span_info is None:
            around_info['overview_aroundInfo_houseRecordID']=span_info.string
    
    return around_info

def ParseNode4Communite(tag_commu):
    a = tag_commu.find('a', attrs={'class':'info'})
    if a is None:
        return None
    href = a.get('href')
    if href is None:
        return None
    m = re.match(r'^\/xiaoqu\/(\d*)\/$', href)
    if m is None:
        return None
    communite = dict({'id':m.group(1), 'name':a.string})
    return communite