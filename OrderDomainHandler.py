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

def updateDictSingleUsr(srcDict,findName,dstName,newDstName):
    if srcDict is None:
        return
    if (findName in srcDict):
        if (dstName in srcDict):
            pass
        else:
            #add null data to dscName to srcDict
            upDict = {dstName:''}
            srcDict.update(upDict)
        #delete old data and return old data value.
        tempVal = srcDict.pop(findName)
        if tempVal is None:
            return srcDict
        if tempVal == '':
            tempVal = '\'\''

        if srcDict[dstName] == '':
            srcDict[dstName] = srcDict[dstName] + newDstName + ':' + tempVal
        else:
            srcDict[dstName] = srcDict[dstName] + ',' +newDstName + ':' + tempVal

    return srcDict

def formatDictOrderInfo(dictData):
    #convert insurant usr
    dictData = updateDictSingleUsr(dictData,'INSURANT_USR_NAME','INSURANT_USR','NAME')
    dictData = updateDictSingleUsr(dictData,'INSURANT_USR_AGE','INSURANT_USR','AGE')
    dictData = updateDictSingleUsr(dictData,'INSURANT_USR_BIRTHDAY','INSURANT_USR','BIRTHDAY')
    dictData = updateDictSingleUsr(dictData,'INSURANT_USR_IDCARDNO','INSURANT_USR','IDCARDNO')
    dictData = updateDictSingleUsr(dictData,'INSURANT_USR_IDCARDTYPE','INSURANT_USR','IDCARDTYPE')
    dictData = updateDictSingleUsr(dictData,'INSURANT_USR_PHONE','INSURANT_USR','PHONE')
    dictData = updateDictSingleUsr(dictData,'INSURANT_USR_PROFESSION','INSURANT_USR','PROFESSION')

    #convert POLICYHOLDER usr
    dictData = updateDictSingleUsr(dictData,'POLICYHOLDER_USR_NAME','POLICYHOLDER_USR','NAME')
    dictData = updateDictSingleUsr(dictData,'POLICYHOLDER_USR_AGE','POLICYHOLDER_USR','AGE')
    dictData = updateDictSingleUsr(dictData,'POLICYHOLDER_USR_BIRTHDAY','POLICYHOLDER_USR','BIRTHDAY')
    dictData = updateDictSingleUsr(dictData,'POLICYHOLDER_USR_IDCARDNO','POLICYHOLDER_USR','IDCARDNO')
    dictData = updateDictSingleUsr(dictData,'POLICYHOLDER_USR_IDCARDTYPE','POLICYHOLDER_USR','IDCARDTYPE')
    dictData = updateDictSingleUsr(dictData,'POLICYHOLDER_USR_PHONE','POLICYHOLDER_USR','PHONE')
    dictData = updateDictSingleUsr(dictData,'POLICYHOLDER_USR_PROFESSION','POLICYHOLDER_USR','PROFESSION')

    return dictData


def postOrderInfoContact(inContactid,storageData):
    try:
        logger = getLogger()
        logger.debug("start POST Order Info according contact id.")

        jsonData = json.dumps(storageData)
        dictData = json.loads(jsonData)

        #format the dict
        dictData = formatDictOrderInfo(dictData)

        buf = cStringIO.StringIO()
        c = pycurl.Curl()
        localURL = getConfig('RESTService','orderInfoUrl','str')
        localURL = str(localURL)
        c.setopt(pycurl.URL,localURL)
        c.setopt(pycurl.HTTPHEADER,['Content-Type: application/json','Content-Length: '+str(len(jsonStr))])
        c.setopt(c.VERBOSE, True)
        c.setopt(pycurl.CUSTOMREQUEST,"POST")
        c.setopt(pycurl.POSTFIELDS,jsonStr)
        c.setopt(c.WRITEFUNCTION,buf.write)
        c.setopt(pycurl.USERPWD,getConfig('allowedUser1','UserName','str')+':'+getConfig('allowedUser1','Password','str'))
        c.perform()
        c.close()
        print buf.getvalue()
        buf.close()

        logger.debug("post OrderInfo success.")

        return False
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

