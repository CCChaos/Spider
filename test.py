import re

m = re.match(r'.*\/xiaoqu\/(\d*)\/$', "https://bj.lianjia/xiaoqu/1111027379065/")
print m

m = re.match(r'.*\/xiaoqu\/(\d*)\/$', "/xiaoqu/1111027379065/")
print m
