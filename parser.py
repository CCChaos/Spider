from bs4 import BeautifulSoup
import Queue
import re

def ParseHome4ID(homepage):
    id_queue = Queue.Queue()
    soup = BeautifulSoup(homepage, "lxml")
    for link in soup.find_all('a'):
        code = link.get('data-housecode')
        if code != None:
            id_queue.put(code)

    return id_queue

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

def ParseHouse4Info(housepage):
    house = []
    soup = BeautifulSoup(housepage, "lxml")
    div = soup.find(attrs={'class':"aroundInfo"})
    if div != None:
        communityName = div.find(attrs={'class':'communityName'})
        if communityName != None:
            community = ParseNode4Communite(communityName)
            house.append(('community', community))
    return house
