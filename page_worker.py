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
    req_header = {'Host': 'bj.lianjia.com',
                'Connection': 'keep-alive',
                'Cache-Control': 'max-age=0',
                'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.91 Safari/537.36',
                'Upgrade-Insecure-Requests': '1',
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
                'Accept-Encoding': 'gzip, deflate, br',
                'Accept-Language': 'zh-CN,zh;q=0.8,en;q=0.6',
                'Cookie': 'lianjia_uuid=580f63d2-9118-4dbb-b587-763d549723b1; UM_distinctid=15e75ae64173a4-05e17e596a017-1a346c55-fa000-15e75ae6418b4; all-lj=826650ca2d8980f8a49f6d8acab99d41; select_city=110000; _jzqckmp=1; _jzqx=1.1505308548.1505444765.1.jzqsr=captcha%2Elianjia%2Ecom|jzqct=/.-; CNZZDATA1253477573=1929134341-1505211606-%7C1505440698; _smt_uid=59b7b9f6.231a8da2; CNZZDATA1254525948=529596489-1505207884-%7C1505442915; CNZZDATA1255633284=953079826-1505212423-%7C1505441304; CNZZDATA1255604082=463535240-1505207807-%7C1505441762; _qzja=1.398725517.1505212918301.1505441407229.1505444764696.1505444821663.1505444824848.0.0.0.13.6; _qzjb=1.1505444764695.7.0.0.0; _qzjc=1; _qzjto=8.2.0; _jzqa=1.2520528741479387000.1505212918.1505441407.1505444765.6; _jzqc=1; _jzqb=1.7.10.1505444765.1; Hm_lvt_9152f8221cb6243a53c83b956842be8a=1505212918,1505306098; Hm_lpvt_9152f8221cb6243a53c83b956842be8a=1505444825; _ga=GA1.2.572017146.1505212928; _gid=GA1.2.1897162458.1505441415; lianjia_ssid=47c151f6-9fb0-eec6-1e6b-70f3ae296edf'
             }
    request = urllib2.Request(url, None, req_header)
    response = urllib2.urlopen(request)
    content = response.read()
    f = open('tmp2','w')
    f.write(content)
    f.close()
    return
    id_dict = ParseHome4ID(content)

    for id in id_dict.iterkeys():
        print 'Spidering House:%s ...' % ( id )
        url = "https://bj.lianjia.com/ershoufang/%s.html" % id
        req_header = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
             'Accept':'text/html;q=0.9,*/*;q=0.8',
             'Accept-Charset':'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
             'Accept-Encoding':'gzip',
             'Connection':'close',
             'Referer':None #注意如果依然不能抓取的话，这里可以设置抓取网站的host
             }
        req = urllib2.Request(url, None, req_header)
        res = urllib2.urlopen(req)
        ret_house = ParseHouse4Info(res.read())
        ret_house['id'] = id
        rc = SQLInsertHouse(ret_house, table_name)
        if rc == True:
            print '\t Success'
        else:
            print '\t No Rows Effected'
        '''
        sleep = random.randint(5,10)
        print 'Sleep %ds' % sleep
        time.sleep(sleep)
        '''