from  selenium import webdriver
import sys
sys.path.append("../commonutils_spider/")
import time
import uuid


def  crawXHNewsNetDataSource(link):
     currentArray = []
     browsor = webdriver.PhantomJS()
     browsor.get(link)
     mainDiv = browsor.find_element_by_id('showData2')
     print  mainDiv
     listDiv = mainDiv.find_elements_by_class_name('clearfix')
     print listDiv
     for div in listDiv:
         title = div.find_element_by_tag_name('h3').text
         print title
         linkUrl = div.find_element_by_class_name('imgs')\
                .find_element_by_tag_name('a').get_attribute('href')
         imageUrl = div.find_element_by_class_name('imgs')\
                .find_element_by_tag_name('img').get_attribute('src')
         descriptContext = div.find_element_by_class_name('imgs')\
                .find_element_by_class_name('summary').text
         createDate = div.find_element_by_class_name('time').text
         pubDate = time.strftime("%Y-%m-%d",time.localtime())
         print createDate
         if createDate == pubDate:
           currentArray.append([str(uuid.uuid1()),linkUrl,imageUrl,title,pubDate,descriptContext,'CHINA','XHNET'])
     return currentArray


def writeXHNewsNetDataSource():
    link = 'http://www.xinhuanet.com/fortune/index.htm'

    #dbManager = CommonsMysqlUtils._dbManager
    SQL = " DELETE  FROM  MORNING_FINANCENEWS_RESOURCE_TABLE  WHERE  SOURCEFLAG = 'XHNET' " \
          " AND  NEWSFLAG='CHINA' "
    #dbManager.executeUpdateOrDelete(SQL)

    currentArray = crawXHNewsNetDataSource(link)
    formatSQL =  'INSERT MORNING_FINANCENEWS_RESOURCE_TABLE ' \
                '(KEYID,LINKURL,IMAGEURL,TITLE,PUBDATE,DESCRIPTCONTEXT,NEWSFLAG,SOURCEFLAG)' \
                ' VALUES (%s,%s,%s,%s,%s,%s,%s,%s)'
    #dbManager.executeManyInsert(formatSQL,currentArray)

if __name__ == '__main__':
    writeXHNewsNetDataSource()