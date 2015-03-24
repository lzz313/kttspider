from  selenium import webdriver
import sys
sys.path.append("../commonutils_spider/")
from selenium.common.exceptions import NoSuchElementException
import CommonsMysqlUtils
import time
import uuid

def crawMorningDailyNews(link):
    currentArray = []
    browsor = webdriver.PhantomJS()
    browsor.get(link)
    mainContext = browsor.find_element_by_id('search-result')
    listContext = mainContext.find_elements_by_class_name('news')
    for  context in listContext:
         title = context.find_element_by_class_name('title').text
         linkUrl = context.find_element_by_class_name('title').get_attribute('href')
         pubDate = time.strftime("%Y-%m-%d %X",time.localtime())
         browsors = webdriver.PhantomJS()
         browsors.get(linkUrl)
         mainContext = browsors.find_element_by_class_name('article-content')
         imageUrl =None
         try:
            imageUrl = mainContext.find_element_by_class_name('article-content').find_element_by_tag_name('img')
         except NoSuchElementException,e:
            continue
         imageUrl =imageUrl.get_attribute('src')
         descriptContext = mainContext.find_element_by_tag_name('p').text
         currentArray.append([str(uuid.uuid1()),linkUrl,imageUrl,title,pubDate,descriptContext,'STOCK','HEJNET'])

    return currentArray


def writeMorningDailyNews():
    link = 'http://wallstreetcn.com/news?cid=17'
    currentArray =  crawMorningDailyNews(link)
    dbManager = CommonsMysqlUtils._dbManager
    SQL = "DELETE  FROM  MORNING_FINANCENEWS_RESOURCE_TABLE  WHERE  SOURCEFLAG = 'HEJNET'  AND  NEWSFLAG='STOCK' "
    dbManager.executeUpdateOrDelete(SQL)

    formatSQL = ' INSERT MORNING_FINANCENEWS_RESOURCE_TABLE' \
                ' (KEYID,LINKURL,IMAGEURL,TITLE,PUBDATE,DESCRIPTCONTEXT,NEWSFLAG,SOURCEFLAG)' \
                ' VALUES (%s,%s,%s,%s,%s,%s,%s,%s)'
    dbManager.executeManyInsert(formatSQL,currentArray)
    
if __name__=='__main__':
    writeMorningDailyNews()