#!/usr/bin/env python
# coding=utf8
__author__ = 'stone'

import cStringIO
import json

import traceback
from configData import getConfig
from logHelper import getLogger
from ThirdEvalDomainHandler import flatThirdEvalInfo

from configObjData import getConfigPage

configPage = getConfigPage()

def getThirdEvalInfo(inOrderid):
    """
        get the third eval info from DB
        now, we simulate some json data.
    """
    logger = getLogger()
    try:
        logger.debug("start GET Order Info according order id.")

        if inOrderid is None:
            return None

        localOrderInfo = {"third":{
            "NORMAL_ADL":10,
            "NORMAL_IADL":20,
            "NORMAL_RECOGNIZE":30,
            "THIRDEVAL_CLASS":1
        },
                          "leer":{
                              "NORMAL_ADL":22
                          }
                          }

        logger.debug("get localOrderInfo success.")

        #we need change the data structure, so the html show simple.
        if localOrderInfo is not None:
            localOrderInfo = flatThirdEvalInfo(localOrderInfo)

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

def getThirdEvalInfoLst(inOrderid,inPageIndex):
    logger = getLogger()
    try:
        logger.debug("start GET ThirdEval Info according query condition.")

        localURL = ''

        if inOrderid is None:
            inOrderid = ''
        if inOrderid != '':
            localURL = localURL+'&orderid='+ inOrderid

        if inPageIndex  is None:
            inPageIndex = ''
        if inPageIndex != '':
            localURL = localURL+'&pageindex='+ inPageIndex

       #get the data from json.
        localThirdEvalInfoLst = {"ThirdEvalInfoLst":[{'orderid':1,'name':'stone'}],
                                 "PageManager":{
                                     "DataCount":1,
                                     "PageSize":5,
                                     "PageCount":1,
                                     "PageIndex":1,
                                 },
                                 }

        logger.debug("get localThirdEvalInfoLst List success.")

        return localThirdEvalInfoLst
    except :
        logger.error("exception occur, see the traceback.log")

        #异常写入日志文件.
        f = open('traceback.txt','a')
        traceback.print_exc()
        traceback.print_exc(file = f)
        f.flush()
        f.close()

    finally:
        pass

def addItemDictValue(dstDict,dstName,srcDict,srcName):
    """add value data from srcDict to dstDict .from dic to item data."""

    localVal = srcDict.pop(srcName)
    upDict = {dstName:localVal}
    dstDict.update(upDict)

