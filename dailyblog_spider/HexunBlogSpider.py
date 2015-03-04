import uuid
import sys
sys.path.append("../commonutils_spider/")
import CommonsMysqlUtils
from  selenium import webdriver

def searchHexunBlog(link,id):
    blogList = []
    print  link




    #blogList.append([id,title,linkUrl,pubDate,descriptContext,imageUrl])
    return blogList

def writeHexunBlog():
    dbManager = CommonsMysqlUtils._dbManager
    SQL = 'DELETE FROM  HSHY_RESOURCE_DETAIL_TABLE'
    #dbManager.executeUpdateOrDelete(SQL)

    SELECTSQL = "SELECT CJXJ.LINKURL , CJXJ.ID  FROM DAILYBLOG_AUTHOR_RESOURCE_TABLE CJXJ WHERE CJXJ.NET_FL='hexun' "
    rows = dbManager.selectMany(SELECTSQL)

    for row in rows:
        currentReult = searchHexunBlog(row[0],row[1])
        formatSQL = ' INSERT  INTO  HSHY_RESOURCE_DETAIL_TABLE' \
                    ' (ID,TITLE,LINKURL,PUBDATE,DESCRIPTCONTEXT,IMAGEURL)' \
                    ' VALUES (%s,%s,%s,%s,%s,%s)'
        #dbManager.executeManyInsert(formatSQL,currentReult)


if __name__=='__main__':
    writeHexunBlog()
    
    
    
    
    
    
    