__author__ = 'stone'
#coding=UTF-8

import pycurl
import cStringIO
import json

import traceback
from configData import getConfig
from logHelper import getLogger
from configObjData import getConfigPage

configPage = getConfigPage()
def getOrderInfoOrder(inOrderid):
    """get the order info from REST """
    try:
        logger = getLogger()
        logger.debug("start GET Order Info according order id.")

        if inOrderid is None:
            return None

        buf = cStringIO.StringIO() #define in function.
        c = pycurl.Curl()
        localURL = getConfig('RESTService','orderInfoOrderidUrl','str')+inOrderid
        localURL = str(localURL)
        c.setopt(pycurl.URL,localURL)
        c.setopt(c.WRITEFUNCTION,buf.write)
        c.setopt(c.VERBOSE, True)
        c.setopt(pycurl.USERPWD,getConfig('allowedUser1','UserName','str')+':'+getConfig('allowedUser1','Password','str'))
        c.perform()

        #get the data from json.
        localOrderInfo = json.loads(buf.getvalue())
        buf.close()

        logger.debug("get localOrderInfo success.")

        #we need change the data structure, so the html show simple.
        localOrderInfo = updateOrderInfoOrder(localOrderInfo)

        return localOrderInfo
    except pycurl.error, error:
        logger.error("exception occur, see the traceback.log")

        #异常写入日志文件.
        f = open('traceback.txt','a')
        traceback.print_exc()
        traceback.print_exc(file = f)
        f.flush()
        f.close()

        errno, errstr = error
        print 'An error occurred: ', errstr
    else:
        pass
    finally:
        pass

def addDictListValue(srcDict,dstName,srcName1,srcName2):
    """add value data to dscName to srcDict"""
    localVal = srcDict[srcName1].pop(srcName2)
    upDict = {dstName:localVal}
    srcDict.update(upDict)


def updateOrderInfoOrder(inOrderInfo):
    """update the order info according the web page show"""
    try:
        logger = getLogger()
        logger.debug("start update Order Info .")

        if inOrderInfo is None:
            return None

        # we only get the message we needed:
        #change the list to flat data.
        localOrderInfo = inOrderInfo
        #TODO: add all order data here.
        # beneficiarierelationdsc = localOrderInfo["BENEFICIARIERELATIONDSC"]
        #deliveryaddress = localOrderInfo["DELIVERYADDRESS"]
        #crusr = localOrderInfo["CRUSR"]
        #purchasecount = localOrderInfo["PURCHASECOUNT"]
        #paymentstatus = localOrderInfo["PAYMENTSTATUS"]
        #insuranceid = localOrderInfo["INSURANCEID"]
        #status = localOrderInfo["STATUS"]
        configPageInsurantUsr = configPage['InsurantUsr']
        #addDictListValue(localOrderInfo,configPageInsurantUsr['INSURANT_USR_AGE'],"INSURANT_USR","AGE")
        addDictListValue(localOrderInfo,configPageInsurantUsr['name']['dataName'],"INSURANT_USR","NAME")
        addDictListValue(localOrderInfo,configPageInsurantUsr['sex']['dataName'],"INSURANT_USR","SEX")
        #addDictListValue(localOrderInfo,'INSURANT_USR_IDCARDNO',"INSURANT_USR","IDCARDNO")
        #addDictListValue(localOrderInfo,'POLICYHOLDER_USR_AGE',"POLICYHOLDER_USR","AGE")
        #addDictListValue(localOrderInfo,'POLICYHOLDER_USR_NAME',"POLICYHOLDER_USR","NAME")
        #addDictListValue(localOrderInfo,'POLICYHOLDER_USR_IDCARDNO',"POLICYHOLDER_USR","IDCARDNO")

        logger.debug("update localOrderInfo success.")

        return localOrderInfo
    except:
        logger.error("exception occur, see the traceback.log")

        #异常写入日志文件.
        f = open('traceback.txt','a')
        traceback.print_exc()
        traceback.print_exc(file = f)
        f.flush()
        f.close()
    else:
        pass
    finally:
        pass

def getOrderInfoLstContact(inContactid,inOrderid):
    try:
        #TODO: add orderid and so on query.
        logger = getLogger()
        logger.debug("start GET Order Info according contact id.")

        buf = cStringIO.StringIO() #define in function.
        c = pycurl.Curl()
        localURL = getConfig('RESTService','orderInfoContactidUrl','str')+inContactid
        localURL = str(localURL)
        c.setopt(pycurl.URL,localURL)
        c.setopt(c.WRITEFUNCTION,buf.write)
        c.setopt(c.VERBOSE, True)
        c.setopt(pycurl.USERPWD,getConfig('allowedUser1','UserName','str')+':'+getConfig('allowedUser1','Password','str'))
        c.perform()

        #get the data from json.
        localOrderInfoLst = json.loads(buf.getvalue())
        buf.close()

        logger.debug("get localOrderInfo List success.")

        return localOrderInfoLst
    except pycurl.error, error:
        logger.error("exception occur, see the traceback.log")

        #异常写入日志文件.
        f = open('traceback.txt','a')
        traceback.print_exc()
        traceback.print_exc(file = f)
        f.flush()
        f.close()

        errno, errstr = error
        print 'An error occurred: ', errstr
    else:
        pass
    finally:
        pass

def getOrderProductInfoLst(insurancecodeid,securityplanid,premiumplanid):
    try:
        logger = getLogger()
        logger.debug("start GET Order Product Info.")

        buf = cStringIO.StringIO() #define in function.
        c = pycurl.Curl()
        localURL = getConfig('RESTService','orderProductInfourl','str')+'?INSURANCECODE='+insurancecodeid+"&SECURITYPLAN="+securityplanid+"&PREMIUMPLAN="+premiumplanid
        localURL = str(localURL)
        c.setopt(pycurl.URL,localURL)
        c.setopt(c.WRITEFUNCTION,buf.write)
        c.setopt(c.VERBOSE, True)
        c.setopt(pycurl.USERPWD,getConfig('allowedUser1','UserName','str')+':'+getConfig('allowedUser1','Password','str'))
        c.perform()

        #get the data from json.
        localOrderInfoLst = json.loads(buf.getvalue())
        buf.close()

        logger.debug("get localOrder Product Info List success.")

        return localOrderInfoLst
    except pycurl.error, error:
        logger.error("exception occur, see the traceback.log")

        #异常写入日志文件.
        f = open('traceback.txt','a')
        traceback.print_exc()
        traceback.print_exc(file = f)
        f.flush()
        f.close()

        errno, errstr = error
        print 'An error occurred: ', errstr
    else:
        pass
    finally:
        pass