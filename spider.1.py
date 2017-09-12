import urllib2
from parser import ParseHome4ID
from parser import ParseHouse4Info


request = urllib2.Request("https://bj.lianjia.com/ershoufang/pg2/")
response = urllib2.urlopen(request)
content = response.read()
id_queue = ParseHome4ID(content)

url = "https://bj.lianjia.com/ershoufang/%s.html" % id_queue.get()
req = urllib2.Request(url)
res = urllib2.urlopen(req)
house = ParseHouse4Info(res.read())

print house

