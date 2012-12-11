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
import DbModule

def updateDictSingleValue(srcDict,dstName,dstValue):
    if dstName in srcDict:
        srcDict[dstName] = dstValue
        pass
    else:
        #add value data to dscName to srcDict
        upDict = {dstName:dstValue}
        srcDict.update(upDict)

def updateDictSingleUsr(srcDict,findName,dstName,newDstName):
    if srcDict is None:
        return
    if findName in srcDict:
        if dstName in srcDict:
            pass
        else:
            #add null data to dscName to srcDict
            upDict = {dstName:''}
            srcDict.update(upDict)

        #delete old data and return old data value.
        tempVal = srcDict.pop(findName)
        if tempVal is None:
            return srcDict
        #if tempVal == '':
        #    tempVal = '\'\''

        if srcDict[dstName] == '':
            srcDict[dstName] = srcDict[dstName] + '{\"'+newDstName+'\"' + ':' +'\"'+ tempVal+'\"}'
        else:
            # remove '{}' embrace.'
            srcDict[dstName] = srcDict[dstName][1:-1]

            srcDict[dstName] = srcDict[dstName] + ',' +'\"'+newDstName +'\"'+ ':' + '\"'+tempVal+'\"'

            # add '{}' embrace.
            srcDict[dstName] = '{' + srcDict[dstName] + '}'

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

        #add contactid
        updateDictSingleValue(dictData,"CONTACTID",inContactid)

        #add addressid
        updateDictSingleValue(dictData,"ADDRESSID",'1')

        #format the dict
        dictData = formatDictOrderInfo(dictData)

        #combine the json string

        #remove  and save the user string.
        uInsurantUsrVal = dictData.pop('INSURANT_USR')
        uPHUsrVal = dictData.pop('POLICYHOLDER_USR')

        #get no user json string
        jsonData =  json.dumps(dictData)

        #add user string to json string
        strInsurantUsrVal = uInsurantUsrVal.encode('UTF-8')
        strInsurantUsrVal = ',\"INSURANT_USR\":' + strInsurantUsrVal
        jsonData = jsonData[:-1] + strInsurantUsrVal + '}'

        #add user string to json string
        strPHUsrVal = uPHUsrVal.encode('UTF-8')
        strPHUsrVal = ',\"POLICYHOLDER_USR\":' + strPHUsrVal
        jsonData = jsonData[:-1] + strPHUsrVal + '}'

        buf = cStringIO.StringIO()
        c = pycurl.Curl()
        localURL = getConfig('RESTService','orderInfoUrl','str')
        localURL = str(localURL)
        c.setopt(pycurl.URL,localURL)
        c.setopt(pycurl.HTTPHEADER,['Content-Type: application/json','Content-Length: '+str(len(jsonData))])
        c.setopt(c.VERBOSE, True)
        c.setopt(pycurl.CUSTOMREQUEST,"POST")
        c.setopt(pycurl.POSTFIELDS,jsonData)
        c.setopt(c.WRITEFUNCTION,buf.write)
        c.setopt(pycurl.USERPWD,getConfig('allowedUser1','UserName','str')+':'+getConfig('allowedUser1','Password','str'))
        c.perform()
        c.close()

        logger.debug(buf.getvalue())
        retStr = buf.getvalue()

        buf.close()

        logger.debug("post OrderInfo success.")
        return retStr

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


def putOrderStatusInfoContact(inOrderid,inStatus,storageData):
    try:
        logger = getLogger()
        logger.debug("start PUT Order Status Info according contact id.")

        #TODO: simle the method?
        jsonData = json.dumps(storageData)
        dictData = json.loads(jsonData)

        #update status
        updateDictSingleValue(dictData,"STATUS",inStatus)

        #add orderid
        updateDictSingleValue(dictData,"ORDERID",inOrderid)

        #format the dict
        dictData = formatDictOrderInfo(dictData)

        #combine the json string

        #remove  and save the user string.
        uInsurantUsrVal = dictData.pop('INSURANT_USR')
        uPHUsrVal = dictData.pop('POLICYHOLDER_USR')

        #get no user json string
        jsonData =  json.dumps(dictData)

        #add user string to json string
        strInsurantUsrVal = uInsurantUsrVal.encode('UTF-8')
        strInsurantUsrVal = ',\"INSURANT_USR\":' + strInsurantUsrVal
        jsonData = jsonData[:-1] + strInsurantUsrVal + '}'

        #add user string to json string
        strPHUsrVal = uPHUsrVal.encode('UTF-8')
        strPHUsrVal = ',\"POLICYHOLDER_USR\":' + strPHUsrVal
        jsonData = jsonData[:-1] + strPHUsrVal + '}'

        buf = cStringIO.StringIO()
        c = pycurl.Curl()
        localURL = getConfig('RESTService','orderInfoUrl','str')
        localURL = str(localURL)
        c.setopt(pycurl.URL,localURL)
        c.setopt(pycurl.HTTPHEADER,['Content-Type: application/json','Content-Length: '+str(len(jsonData))])
        c.setopt(c.VERBOSE, True)
        c.setopt(pycurl.CUSTOMREQUEST,"PUT")
        c.setopt(pycurl.POSTFIELDS,jsonData)
        c.setopt(c.WRITEFUNCTION,buf.write)
        c.setopt(pycurl.USERPWD,getConfig('allowedUser1','UserName','str')+':'+getConfig('allowedUser1','Password','str'))
        c.perform()
        c.close()

        logger.debug(buf.getvalue())
        retStr = buf.getvalue()

        buf.close()

        logger.debug("put OrderInfo success.")
        return retStr

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

def getUsrPurview(inUsrid,inPwd):
    try:
        logger = getLogger()
        logger.debug("start check user and psswod and get user purview.")

        dict = {"right":False}
        updateDict = {"log":"no log"}
        dict.update(updateDict)

        #连接db层进行验证.
        if DbModule.IsValidUsrPwd(inUsrid,inPwd):
            dict["right"] = True
            dict["log"] = "login in success"
            logger.debug(inUsrid+" user is valid user")
            #连接db层取到权限
        else:
            dict["log"] = inUsrid+" user not exixts or password error"

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
        return dict

def putOrderInfoContact(inOrderid,storageData):
        try:
            logger = getLogger()
            logger.debug("start PUT Order Info according contact id.")

            jsonData = json.dumps(storageData)
            dictData = json.loads(jsonData)

            #add orderid
            updateDictSingleValue(dictData,"ORDERID",inOrderid)

            #format the dict
            dictData = formatDictOrderInfo(dictData)

            #combine the json string

            #remove  and save the user string.
            uInsurantUsrVal = dictData.pop('INSURANT_USR')
            uPHUsrVal = dictData.pop('POLICYHOLDER_USR')

            #get no user json string
            jsonData =  json.dumps(dictData)

            #add user string to json string
            strInsurantUsrVal = uInsurantUsrVal.encode('UTF-8')
            strInsurantUsrVal = ',\"INSURANT_USR\":' + strInsurantUsrVal
            jsonData = jsonData[:-1] + strInsurantUsrVal + '}'

            #add user string to json string
            strPHUsrVal = uPHUsrVal.encode('UTF-8')
            strPHUsrVal = ',\"POLICYHOLDER_USR\":' + strPHUsrVal
            jsonData = jsonData[:-1] + strPHUsrVal + '}'

            buf = cStringIO.StringIO()
            c = pycurl.Curl()
            localURL = getConfig('RESTService','orderInfoUrl','str')
            localURL = str(localURL)
            c.setopt(pycurl.URL,localURL)
            c.setopt(pycurl.HTTPHEADER,['Content-Type: application/json','Content-Length: '+str(len(jsonData))])
            c.setopt(c.VERBOSE, True)
            c.setopt(pycurl.CUSTOMREQUEST,"PUT")
            c.setopt(pycurl.POSTFIELDS,jsonData)
            c.setopt(c.WRITEFUNCTION,buf.write)
            c.setopt(pycurl.USERPWD,getConfig('allowedUser1','UserName','str')+':'+getConfig('allowedUser1','Password','str'))
            c.perform()
            c.close()

            logger.debug(buf.getvalue())
            retStr = buf.getvalue()

            buf.close()

            logger.debug("put OrderInfo success.")
            return retStr

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
