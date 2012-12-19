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
        addDictListValue(localOrderInfo,configPageInsurantUsr['name']['dataName'],"INSURANT_USR","NAME")
        addDictListValue(localOrderInfo,configPageInsurantUsr['sex']['dataName'],"INSURANT_USR","SEX")
        addDictListValue(localOrderInfo,configPageInsurantUsr['birthday']['dataName'],"INSURANT_USR","BIRTHDAY")
        addDictListValue(localOrderInfo,configPageInsurantUsr['age']['dataName'],"INSURANT_USR","AGE")
        addDictListValue(localOrderInfo,configPageInsurantUsr['profession']['dataName'],"INSURANT_USR","PROFESSION")
        addDictListValue(localOrderInfo,configPageInsurantUsr['phone']['dataName'],"INSURANT_USR","PHONE")
        addDictListValue(localOrderInfo,configPageInsurantUsr['idcardtype']['dataName'],"INSURANT_USR","IDCARDTYPE")
        addDictListValue(localOrderInfo,configPageInsurantUsr['idcardno']['dataName'],"INSURANT_USR","IDCARDNO")
        addDictListValue(localOrderInfo,configPageInsurantUsr['height']['dataName'],"INSURANT_USR","HEIGHT")
        addDictListValue(localOrderInfo,configPageInsurantUsr['weight']['dataName'],"INSURANT_USR","WEIGHT")
        addDictListValue(localOrderInfo,configPageInsurantUsr['detailAddress']['dataName'],"INSURANT_USR","ADDRESS")
        addDictListValue(localOrderInfo,configPageInsurantUsr['postcode']['dataName'],"INSURANT_USR","ZIPCODE")

        configPagePolicyholderUsr = configPage['PolicyholderUsr']
        #TODO: wrong data in relation.
        addDictListValue(localOrderInfo,configPagePolicyholderUsr['relation']['dataName'],"INSURANT_USR","AREA")
        addDictListValue(localOrderInfo,configPagePolicyholderUsr['name']['dataName'],"POLICYHOLDER_USR","NAME")
        addDictListValue(localOrderInfo,configPagePolicyholderUsr['sex']['dataName'],"POLICYHOLDER_USR","SEX")
        addDictListValue(localOrderInfo,configPagePolicyholderUsr['birthday']['dataName'],"POLICYHOLDER_USR","BIRTHDAY")
        addDictListValue(localOrderInfo,configPagePolicyholderUsr['age']['dataName'],"POLICYHOLDER_USR","AGE")
        addDictListValue(localOrderInfo,configPagePolicyholderUsr['profession']['dataName'],"POLICYHOLDER_USR","PROFESSION")
        addDictListValue(localOrderInfo,configPagePolicyholderUsr['phone']['dataName'],"POLICYHOLDER_USR","PHONE")
        addDictListValue(localOrderInfo,configPagePolicyholderUsr['idcardtype']['dataName'],"POLICYHOLDER_USR","IDCARDTYPE")
        addDictListValue(localOrderInfo,configPagePolicyholderUsr['idcardno']['dataName'],"POLICYHOLDER_USR","IDCARDNO")
        addDictListValue(localOrderInfo,configPagePolicyholderUsr['height']['dataName'],"POLICYHOLDER_USR","HEIGHT")
        addDictListValue(localOrderInfo,configPagePolicyholderUsr['weight']['dataName'],"POLICYHOLDER_USR","WEIGHT")
        addDictListValue(localOrderInfo,configPagePolicyholderUsr['detailAddress']['dataName'],"POLICYHOLDER_USR","ADDRESS")
        addDictListValue(localOrderInfo,configPagePolicyholderUsr['postcode']['dataName'],"POLICYHOLDER_USR","ZIPCODE")

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
