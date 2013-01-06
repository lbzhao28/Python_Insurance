__author__ = 'stone'
#coding=UTF-8

import pycurl
import cStringIO
import json

import traceback
from configData import getConfig
from logHelper import getLogger
from OrderDomainHandler import flatOrderInfoOrder

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
        localOrderInfo = flatOrderInfoOrder(localOrderInfo)

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

def getOrderInfoLst(inGrpid,inCrusr,inContactid,inOrderid,inStartDt,inEndDt,inOrderStatus,inPageIndex):
    try:
        logger = getLogger()
        logger.debug("start GET Order Info according query condition.")

        localURL = ''


        if inGrpid is None:
            inGrpid = ''
        if inGrpid != '':
            localURL = localURL+'&Grpid='+inGrpid

        if inCrusr is None:
            inCrusr = ''
        if inCrusr != '':
            localURL = localURL+'&Crusr='+inCrusr


        if inContactid is None:
            inContactid = ''
        if inContactid != '':
            localURL = localURL+'&Contactid='+inContactid

        if inOrderid is None:
            inOrderid = ''
        if inOrderid != '':
            localURL = localURL+'&Orderid='+ inOrderid

        if inStartDt is None:
            inStartDt = ''
        if inStartDt != '':
            localURL = localURL+'&Scrdt='+ inStartDt

        if inEndDt is None:
            inEndDt = ''
        if inEndDt != '':
            localURL = localURL+'&Ecrdt='+ inEndDt

        if inOrderStatus  is None:
            inOrderStatus = ''
        if inOrderStatus != '':
            localURL = localURL+'&Status='+ inOrderStatus

        if inPageIndex  is None:
            inPageIndex = ''
        if inPageIndex != '':
            localURL = localURL+'&PageIndex='+ inPageIndex

        buf = cStringIO.StringIO() #define in function.
        c = pycurl.Curl()
        if localURL != '':
            #use 1=1 to use all condition.
            localURL = getConfig('RESTService','orderInfoSearchUrl','str') + '?1=1' + localURL
        else:
            localURL = getConfig('RESTService','orderInfoSearchUrl','str')
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

def getOrderProductInfoLst(insurancecodeid,securityplanid,premiumplanid,ageplan):
    try:
        logger = getLogger()
        logger.debug("start GET Order Product Info.")

        buf = cStringIO.StringIO() #define in function.
        c = pycurl.Curl()
        #TODO: how to disable the age.
        if (ageplan != 'null') & (ageplan is not None):
            localURL = getConfig('RESTService','orderProductInfourl','str')+'?INSURANCECODE='+insurancecodeid+"&SECURITYPLAN="+securityplanid+"&PREMIUMPLAN="+premiumplanid+"&AGEPLAN="+ageplan
        else:
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
