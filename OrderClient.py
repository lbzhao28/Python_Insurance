__author__ = 'stone'
#coding=UTF-8

import pycurl
import cStringIO
import json

import globalDefine
import traceback
import configData
from configData import getConfig
from logHelper import getLogger

def getOrderInfoOrder(inOrderid):
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

def getOrderInfoContact(inContactid):
    try:
        logger = getLogger()
        logger.debug("start GET Order Info according contact id.")

        buf = cStringIO.StringIO() #define in function.
        c = pycurl.Curl()
        localURL = getConfig('RESTService','orderInfoOrderidUrl','str')+inContactid
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


