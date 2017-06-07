# coding:utf-8 #

import codecs
from selenium import webdriver

fi=codecs.open("vol_url_list.txt","r","utf-8")
fo=codecs.open("vol_url_page.txt","w","utf-8")
urls=fi.readlines()
options=webdriver.ChromeOptions()
options.add_extension("fpdnjdlbdmifoocedhkighhlbchbiikl_3_2_1.crx")
browser=webdriver.Chrome(chrome_options=options)
vol=1
for url in urls:
    browser.get(url.strip())
    page=browser.find_element_by_id("spPageCount").text
    fo.write(str(vol)+" "+url.strip()+" "+page+"\n")
    vol+=1
    #src=browser.find_element_by_id("imgCurr").get_attribute("src")
browser.quit()
fo.close()
fi.close()
