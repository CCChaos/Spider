import urllib2
from HTMLParser import HTMLParser
import Queue
import threading

id_query = Queue.Queue()
lock = threading.Lock()

class HouseHTMLParser(HTMLParser):
    def __init__(self, id):
        HTMLParser.__init__(self)
        self.id = id

    def handle_starttag(self, tags, attrs):
        f = open(self.id, 'a')
        content = "tags:%s \n\t attrs:%s\n" % (tags , attrs)
        f.write(content)
        f.close()

class IDHTMLParser(HTMLParser):
    
    def handle_starttag(self, tags, attrs):
        if tags == 'a':
            global id_query
            for attr in attrs:
                if attr[0] == 'data-housecode':
                    lock.acquire()
                    try:
                        id_query.put(attr[1])
                    finally:
                        lock.release()


def spider_house(id):
    url = "https://bj.lianjia.com/ershoufang/%s.html" % id
    req = urllib2.Request(url)
    res = urllib2.urlopen(request)
    hs = HouseHTMLParser(id)
    content = res.read()
    hs.feed(content)
    file_name='%s_text' % id
    f = open(file_name, 'w')
    f.write(content)
    f.close()


def thread_spider_house():
    global id_query
    i = 0
    while id_query.empty() == False:
        id = id_query.get()
        spider_house(id)
        i=i+1
        if i > 5:
            break



request = urllib2.Request("https://bj.lianjia.com/ershoufang/pg2/")
response = urllib2.urlopen(request)
content = response.read()
py = IDHTMLParser()
py.feed(content)
thread_spider_house()
