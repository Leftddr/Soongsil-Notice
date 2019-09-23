from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

url="http://iphak.ssu.ac.kr/2014/guide/notice.asp"
html=urlopen("http://iphak.ssu.ac.kr/2014/guide/notice.asp")
bsObj=BeautifulSoup(html,"html.parser")

for i in range(1,100):
    linkList=bsObj.find("table",{"class":"list_style_0"}).findAll("a",href=re.compile("((?!:).)*$"))
    titleList=bsObj.find("table",{"class":"list_style_0"}).findAll("dt")
    seeList=bsObj.find("table",{"class":"list_style_0"}).findAll("span",{"class":"list_data_right"})
    dateList=bsObj.find("table",{"class":"list_style_0"}).findAll("span",{"class":"list_data_left"})
    for title,see,date,link in zip(titleList,seeList,dateList,linkList):
        print(title.get_text()+"\n"+see.get_text()+"\n"+date.get_text()+"\n"+link.attrs['href']+"\n")

    btn=bsObj.find("li",{"id":"p_btn_rbt_0"}).find("a",href=re.compile("((?!:).)*$"))
    url_next=url+btn.attrs['href']
    html=urlopen(url_next)
    bsObj=BeautifulSoup(html,"html.parser")


