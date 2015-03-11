from  selenium import webdriver
import sys
sys.path.append("../commonutils_spider/")
import CommonsMysqlUtils
import time
import uuid


def  crawXHNewsNetDataSource(link):
     currentArray = []
     browsor = webdriver.PhantomJS()
     browsor.get(link)
     mainDiv = browsor.find_element_by_id('showData2')
     listDiv = mainDiv.find_elements_by_class_name('clearfix')
     for div in listDiv:
         title = div.find_element_by_tag_name('h3').text
         linkUrl = div.find_element_by_class_name('imgs')\
                .find_element_by_tag_name('a').get_attribute('href')
         imageUrl = div.find_element_by_class_name('imgs')\
                .find_element_by_tag_name('img').get_attribute('src')
         descriptContext = div.find_element_by_class_name('imgs')\
                .find_element_by_class_name('summary').text
         createDate = div.find_element_by_class_name('time').text
         pubDate = time.strftime("%Y-%m-%d",time.localtime())
         if createDate == pubDate:
           currentArray.append([str(uuid.uuid1()),linkUrl,imageUrl,title,pubDate,descriptContext,'CHINA','XHNET'])
     return currentArray


def writeXHNewsNetDataSource():
    link = 'http://www.xinhuanet.com/fortune/index.htm'
    currentArray = crawXHNewsNetDataSource(link)

if __name__ == '__main__':
    writeXHNewsNetDataSource()