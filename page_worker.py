#coding=utf-8
# coding:utf-8
import urllib2
import time
import random
from parser import ParseHome4ID
from parser import ParseHouse4Info
from sql import SQLInsertHouse


def WorkMainPage(page_index, table_name):
    url = "https://bj.lianjia.com/ershoufang/pg%d/" % page_index
    request = urllib2.Request(url)
    response = urllib2.urlopen(request)
    content = response.read()
    id_dict = ParseHome4ID(content)

    for id in id_dict.iterkeys():
        print 'Spidering House:%s ...' % ( id )
        url = "https://bj.lianjia.com/ershoufang/%s.html" % id
        req = urllib2.Request(url)
        res = urllib2.urlopen(req)
        ret_house = ParseHouse4Info(res.read())
        ret_house['id'] = id
        rc = SQLInsertHouse(ret_house, table_name)
        if rc == True:
            print '\t Success'
        else:
            print '\t No Rows Effected'
        
        sleep = random.randint(0,5)
        print 'Sleep %ds' % sleep
        time.sleep(sleep)