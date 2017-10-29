#!/usr/bin/env python
# coding=utf8
__author__ = 'stone'

import cStringIO
import json

import traceback
from configData import getConfig
from logHelper import getLogger
from OrderDomainHandler import flatOrderInfoOrder

from configObjData import getConfigPage

configPage = getConfigPage()

def getOrderInfoOrder(inOrderid):
    """
        get the order info from DB
        now, we simulate some json data.
    """
    logger = getLogger()
    try:
        logger.debug("start GET Order Info according order id.")

        if inOrderid is None:
            return None

        localOrderInfo = {}

        logger.debug("get localOrderInfo success.")

        #we need change the data structure, so the html show simple.
        if localOrderInfo is not None:
            localOrderInfo = flatOrderInfoOrder(localOrderInfo)

        return localOrderInfo
    except:
        logger.error("exception occur, see the traceback.log")

        #异常写入日志文件.
        f = open('traceback.txt','a')
        traceback.print_exc()
        traceback.print_exc(file = f)
        f.flush()
        f.close()
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

        http_code = c.getinfo(pycurl.HTTP_CODE)
        #judge get success.
        if http_code != 200:
            return None

        #get the data from json.
        localOrderInfoLst = json.loads(buf.getvalue())
        buf.close()
        c.close()

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

def addItemDictValue(dstDict,dstName,srcDict,srcName):
    """add value data from srcDict to dstDict .from dic to item data."""

    localVal = srcDict.pop(srcName)
    upDict = {dstName:localVal}
    dstDict.update(upDict)

