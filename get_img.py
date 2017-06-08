# coding:utf-8 #

import codecs,requests,os,threading

def get_img(vol,url):
    headers={
    'User-Agent':'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.81 Safari/537.36',
    'Referer':'http://www.iibq.com/comic/82012129525/'
    }
    try:
        pic=requests.get(url=url,headers=headers)
        fo=open(str(vol)+"/"+url[-19:],'wb')
        fo.write(pic.content)
        fo.close()
    except requests.exceptions.ConnectionError:
        print 'error'

def start_get_img(vol):
    fi=codecs.open(str(vol)+".txt","r","utf-8")
    if os.path.exists(str(vol)):
        pass
    else:
        os.mkdir(str(vol))
    context=fi.readlines()
    for each in context:
        url=each.strip() #.replace("comic.dm33.lol:2813","comic.jmydm.com:8080")
        th=threading.Thread(target=get_img,args=(vol,url,))
        th.start()

