# coding:utf-8
import datetime
from sql import SQLCreateTable
from page_worker import WorkMainPage

house_table = {'id':id,
       'overview_price_total':'',
      'overview_houseInfo_room_mainInfo':'',
      'overview_houseInfo_room_subInfo':'',
      'overview_houseInfo_area_mainInfo':'',
      'overview_houseInfo_area_subInfo':''}

# 创建数据表
table_name = datetime.datetime.now().strftime('%Y%m%d_%H%M%S_lianjia')
if SQLCreateTable(house_table, table_name) == False:
    print 'Create Table Error'
    exit()

i = 1
while i <= 100:
    print 'Working on Page:%d  ============>' % i
    WorkMainPage(i, table_name)
    i = i + 1