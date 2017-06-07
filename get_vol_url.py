# coding:utf-8 #

import requests,codecs
from lxml import etree
from bs4 import BeautifulSoup as bs

def get_html(url):
    headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.81 Safari/537.36'}
    request=requests.get(url=url,headers=headers)
    response=request.content
    return response

def get_vol_html(response):
    f=codecs.open("vol_list.txt","w","utf-8")
    soup=bs(response,'lxml')
    all_vol=soup.find('div',class_='cVolList').find_all('a')
    vol_pair={}
    for vol in all_vol:
        key=vol.get_text()
        value=vol['href']
        vol_pair[key]=value
        f.write(key+" "+value+"\n")
        print key+":"+value
    f.close()

root_url="http://www.iibq.com/comic/82012129525/"
root_response=get_html(root_url)
get_vol_html(root_response)

#vol_url="http://www.iibq.com/comic/82012129525/viewcomic139416/"
#get_img_html(vol_url)
