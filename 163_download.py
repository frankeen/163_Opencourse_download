# -*- coding: utf-8 -*-
#抓取网易公开课链接并下载对应的相视频名称和视频格式
#By  : obnjis@163.com
#Python 2.7 + BeautifulSoup 4
#2014-12-18
#断点续传功能等待下一版本
#eg: python 163—video.py http://v.163.com/special/opencourse/ios7.html
from bs4 import BeautifulSoup
import re
import sys,os
import urllib
import codecs
#显示百分比
def rpb(blocknum, blocksize, totalsize):
    percent = 100.0 * blocknum * blocksize / totalsize
    if percent > 100:percent = 100
    #格式化输出下载进度
    sys.stdout.write("'[%.2f%%]  \r" % (percent) )
    #让下载百分比再同一行不断刷新，不需要换行
    sys.stdout.flush()
def parser(url):
    #获取页面
    html = urllib.urlopen(url).read()
    #在已知文档编码类型的情况下，可以先将编码转换为unicode形式，在转换为utf-8编码，然后才传递给BeautifulSoup
    htm=unicode(html,'gb2312','ignore').encode('utf-8','ignore')
    #用BeautifulSoup来装载
    soup = BeautifulSoup(htm)
    #获取每集的真实下载MP4地址
    detail=soup.find('div',{"class":'f-pa menu j-downitem'})
    downlink=detail.findAll('a')[2]
    downlink1=downlink.attrs.get('href')
    print downlink1
    return downlink1

#def clearData(self):
     #网易有些公开课专辑抓下来时，前10集的链接会出现重复，需要去除重复链接






def downlaod(url):
    #获取页面
    html = urllib.urlopen(url).read()
    #在已知文档编码类型的情况下，可以先将编码转换为unicode形式，在转换为utf-8编码，然后才传递给BeautifulSoup
    htm=unicode(html,'gb2312','ignore').encode('utf-8','ignore')
    #用BeautifulSoup来装载
    soup = BeautifulSoup(htm)
    #获取课程详细列表信息
    detail=soup.findAll('tr',{'class':['u-odd','u-even']})
    for i in detail:
        #获取课程名称
        linkurl=i.find('td',{"class" : "u-ctitle"})
        downLink=linkurl.a['href']
        fileName=linkurl.contents[0].strip() .lstrip() .rstrip('>') + linkurl.a.string.strip() .lstrip() .rstrip('<')
        print fileName
        print downLink
        #L=[]
        #L.append(fileName)
        
        if not os.path.exists(fileName):
            downLink1=parser(downLink)
            urllib.urlretrieve(downLink1,fileName+".mp4",rpb)

def main(argv):
    if len(argv)>=2:
         downlaod(argv[1])

if __name__=="__main__":
     main(sys.argv)
