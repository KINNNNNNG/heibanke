#encoding UTF-8

import urllib.request
import re

url = "http://www.heibanke.com/lesson/crawler_ex00/"
data = urllib.request.urlopen(url)
html = str(data.read(),'utf-8')
reler = re.compile(r'数字[^\d]*(\d+)[\.<]')
num = reler.findall(html)
while num:
    url1 = url+num[0]
    data = urllib.request.urlopen(url1)
    html = str(data.read(),'utf-8')
    reler = re.compile(r'数字[^\d]*(\d+)[\.<]')
    num = reler.findall(html)
    print(url1)
