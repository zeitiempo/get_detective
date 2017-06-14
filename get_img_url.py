# coding:utf-8 #

import codecs,threading
from selenium import webdriver

fi=codecs.open("vol_url_page.txt","r","utf-8")
context=fi.readlines()
options=webdriver.ChromeOptions()
options.add_extension("fpdnjdlbdmifoocedhkighhlbchbiikl_3_2_1.crx")
for line in context:
    list=line.strip().split()
    vol=list[0]
    start_url=list[1]
    page=list[2]
    fo=codecs.open(vol+".txt","w","utf-8")
    browser=webdriver.Chrome(chrome_options=options)
    for i in xrange(1,int(page)+1):
        url=start_url+r"#p="+str(i)+r"&s=0"
        browser.refresh()
        browser.get(url)
        browser.refresh()
        src=browser.find_element_by_id("imgCurr").get_attribute("src")
        fo.write(src+"\n")
    fo.close()
    browser.quit()
fi.close()
