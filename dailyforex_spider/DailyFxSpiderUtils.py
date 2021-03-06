import sys
sys.path.append("../commonutils_spider/")
import  CommonsSpiderUtils
import  CommonsMysqlUtils

def retrunStartContext(link):
    context = CommonsSpiderUtils.openUrl(link)
    startContext = CommonsSpiderUtils.startContext(context,'<tr class="record" valign="top">')
    return startContext

def findAllTarget(context):
    return CommonsSpiderUtils.findAllTarget(context,r'<tr class="record" valign="top">')

def filterTargetFlag(filterContext,filter):
    if  CommonsSpiderUtils.filterContext(filterContext,filter) < 0:
        return False
    else:
        return True
        
def divisionTarget(startcontext,startfilter,endfilter):
    startIndex = CommonsSpiderUtils.filterContext(startcontext,startfilter)
    endIndex = CommonsSpiderUtils.filterContext(startcontext,endfilter)+len(endfilter)
    return {'targetContext':startcontext[startIndex:endIndex],'nextContext':startcontext[endIndex:]}

def filterSubSetContext(startcontext,startfilter,endfilter):
    startIndex =  CommonsSpiderUtils.filterContext(startcontext,startfilter)+len(startfilter)
    endIndex = CommonsSpiderUtils.filterContext(startcontext,endfilter)
    return startcontext[startIndex:endIndex]

# GET MYSQL CONNECTION
def getMySQLConn():
    return CommonsMysqlUtils.returnMySQLConn()

    