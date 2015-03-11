from  selenium import webdriver
import sys
sys.path.append("../commonutils_spider/")
import CommonsMysqlUtils


def  crawXHNewsNetDataSource(link):
     currentArray = []



     print link

     return currentArray


def writeXHNewsNetDataSource():
    link = 'http://www.xinhuanet.com/fortune/index.htm'
    currentArray = crawXHNewsNetDataSource(link)

if __name__ == '__main__':
    writeXHNewsNetDataSource()