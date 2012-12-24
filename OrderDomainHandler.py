__author__ = 'stone'
#coding=UTF-8

import pycurl
import cStringIO
import json

import globalDefine
import traceback
import configData
import DbModule
from configData import getConfig
from logHelper import getLogger
from configObjData import getConfigPage

configPage = getConfigPage()
def addDictItemValue(srcDict,srcName,dstDict,dstName):
    """add value data from srcDict to dstDict .from item data to dic"""

    localVal = srcDict.pop(srcName)
    upDict = {dstName:localVal}
    dstDict.update(upDict)

def addItemDictValue(dstDict,dstName,srcDict,srcName):
    """add value data from srcDict to dstDict .from dic to item data."""

    localVal = srcDict.pop(srcName)
    upDict = {dstName:localVal}
    dstDict.update(upDict)

def flatOrderInfoOrder(inOrderInfo):
    """update the order info according the web page show.show the data.

        so we need pull all data in list ,make them flat to show in the page.so in the page, the show will be easy.
    """
    try:
        logger = getLogger()
        logger.debug("start flat Order Info .")

        if inOrderInfo is None:
            return None

        # we only get the message we needed:
        #change the list to flat data.
        localOrderInfo = inOrderInfo

        #InsurantUsr 投保人
        configPageUsing = configPage['InsurantUsr']
        item = localOrderInfo["INSURANT_USR"]
        addDictItemValue(item,'NAME',localOrderInfo,configPageUsing['name']['dataName'])
        addDictItemValue(item,'SEX',localOrderInfo,configPageUsing['sex']['dataName'])
        addDictItemValue(item,'BIRTHDAY',localOrderInfo,configPageUsing['birthday']['dataName'])
        addDictItemValue(item,'AGE',localOrderInfo,configPageUsing['age']['dataName'])
        addDictItemValue(item,'PROFESSION',localOrderInfo,configPageUsing['profession']['dataName'])
        addDictItemValue(item,'PHONE',localOrderInfo,configPageUsing['phone']['dataName'])
        addDictItemValue(item,'IDCARDTYPE',localOrderInfo,configPageUsing['idcardtype']['dataName'])
        addDictItemValue(item,'IDCARDNO',localOrderInfo,configPageUsing['idcardno']['dataName'])
        addDictItemValue(item,'HEIGHT',localOrderInfo,configPageUsing['height']['dataName'])
        addDictItemValue(item,'WEIGHT',localOrderInfo,configPageUsing['weight']['dataName'])
        addDictItemValue(item,'PROVINCE',localOrderInfo,configPageUsing['briefAddress']['select']['select1']['inDataName'])
        addDictItemValue(item,'CITY',localOrderInfo,configPageUsing['briefAddress']['select']['select2']['inDataName'])
        addDictItemValue(item,'AREA',localOrderInfo,configPageUsing['briefAddress']['select']['select3']['inDataName'])
        addDictItemValue(item,'ADDRESS',localOrderInfo,configPageUsing['detailAddress']['dataName'])
        addDictItemValue(item,'ZIPCODE',localOrderInfo,configPageUsing['postcode']['dataName'])

        #PolicyholderUsr 被保人
        #a loop for multi data
        i=0
        for item in localOrderInfo["LstINSURANT_USR"]:
            configLst = {0:'PolicyholderUsr',1:'PolicyholderUsrA',2:'PolicyholderUsrB',3:'PolicyholderUsrC'}

            #only show 4 Policyholder
            #TODO: how to dynamic in page?
            if i==len(configLst) :
                break

            configShowPage = configLst.get(i)

            configPageUsing = configPage[configShowPage]
            #TODO: wrong data in relation.
            addDictItemValue(item,"BENEFICIARIESRELATION",localOrderInfo,configPageUsing['relation']['dataName'])
            addDictItemValue(item,"NAME",localOrderInfo,configPageUsing['name']['dataName'])
            addDictItemValue(item,"SEX",localOrderInfo,configPageUsing['sex']['dataName'])
            addDictItemValue(item,"BIRTHDAY",localOrderInfo,configPageUsing['birthday']['dataName'])
            addDictItemValue(item,"AGE",localOrderInfo,configPageUsing['age']['dataName'])
            addDictItemValue(item,"PROFESSION",localOrderInfo,configPageUsing['profession']['dataName'])
            addDictItemValue(item,"PHONE",localOrderInfo,configPageUsing['phone']['dataName'])
            addDictItemValue(item,"IDCARDTYPE",localOrderInfo,configPageUsing['idcardtype']['dataName'])
            addDictItemValue(item,"IDCARDNO",localOrderInfo,configPageUsing['idcardno']['dataName'])
            addDictItemValue(item,"HEIGHT",localOrderInfo,configPageUsing['height']['dataName'])
            addDictItemValue(item,"WEIGHT",localOrderInfo,configPageUsing['weight']['dataName'])
            addDictItemValue(item,'PROVINCE',localOrderInfo,configPageUsing['briefAddress']['select']['select1']['inDataName'])
            addDictItemValue(item,'CITY',localOrderInfo,configPageUsing['briefAddress']['select']['select2']['inDataName'])
            addDictItemValue(item,'AREA',localOrderInfo,configPageUsing['briefAddress']['select']['select3']['inDataName'])
            addDictItemValue(item,"ADDRESS",localOrderInfo,configPageUsing['detailAddress']['dataName'])
            addDictItemValue(item,"ZIPCODE",localOrderInfo,configPageUsing['postcode']['dataName'])
            i=i+1

        #Lstbeneficiaries 受益人
        #a loop for multi data
        i=0
        for item in localOrderInfo["Lstbeneficiaries"]:
            configLst = {0:'BeneficiaryUsr'}

            #only show 1 BeneficiaryUsr
            #TODO: how to dynamic in page?
            if i==len(configLst) :
                break

            configShowPage = configLst.get(i)

            configPageUsing = configPage[configShowPage]
            addDictItemValue(item,"BENEFICIARIESRELATION",localOrderInfo,configPageUsing['relation']['dataName'])
            addDictItemValue(item,"NAME",localOrderInfo,configPageUsing['name']['dataName'])
            addDictItemValue(item,"SEX",localOrderInfo,configPageUsing['sex']['dataName'])
            addDictItemValue(item,"BIRTHDAY",localOrderInfo,configPageUsing['birthday']['dataName'])
            addDictItemValue(item,"AGE",localOrderInfo,configPageUsing['age']['dataName'])
            addDictItemValue(item,"PHONE",localOrderInfo,configPageUsing['phone']['dataName'])
            addDictItemValue(item,"IDCARDTYPE",localOrderInfo,configPageUsing['idcardtype']['dataName'])
            addDictItemValue(item,"IDCARDNO",localOrderInfo,configPageUsing['idcardno']['dataName'])
            i=i+1

        #InsurantPlan 保险计划
        configPageUsing = configPage['InsurantPlan']
        item = localOrderInfo
        addDictItemValue(item,'INSURANCECODE',localOrderInfo,configPageUsing['product']['dataName'])
        addDictItemValue(item,'SECURITYPLAN',localOrderInfo,configPageUsing['plan']['dataName'])
        addDictItemValue(item,'PREMIUMPLAN',localOrderInfo,configPageUsing['planFamily']['dataName'])
        addDictItemValue(item,'PAYMENTSTATUS',localOrderInfo,configPageUsing['paymentstatus']['dataName'])
        addDictItemValue(item,'DMPAYMODE',localOrderInfo,configPageUsing['dmpaymode']['dataName'])
        addDictItemValue(item,'DMPAYBANK',localOrderInfo,configPageUsing['paybank']['dataName'])
        addDictItemValue(item,'CARDID',localOrderInfo,configPageUsing['cardid']['dataName'])

        #TODO: right 续期帐号
        addDictItemValue(item,'DMPAYCOMPANY',localOrderInfo,configPageUsing['dmpaybankext']['dataName'])
        addDictItemValue(item,'PURCHASECOUNT',localOrderInfo,configPageUsing['purchasecount']['dataName'])
        addDictItemValue(item,'DMCONTINUATIONYEARS',localOrderInfo,configPageUsing['dmcontinuationyears']['dataName'])
        addDictItemValue(item,'DMPAYTYPE',localOrderInfo,configPageUsing['dmpaytype']['dataName'])
        addDictItemValue(item,'DMPOLICYDATES',localOrderInfo,configPageUsing['dmpolicydates']['dataName'])
        addDictItemValue(item,'NOTE',localOrderInfo,configPageUsing['note']['dataName'])

        #delivery 保单配送
        configPageUsing = configPage['delivery']
        item = localOrderInfo
        addDictItemValue(item,'DELIVERYDATE',localOrderInfo,configPageUsing['dateTime']['dataName'])
        addDictItemValue(item,'PROVINCE',localOrderInfo,configPageUsing['deliveryAddress']['select']['select1']['inDataName'])
        addDictItemValue(item,'CITY',localOrderInfo,configPageUsing['deliveryAddress']['select']['select2']['inDataName'])
        addDictItemValue(item,'AREA',localOrderInfo,configPageUsing['deliveryAddress']['select']['select3']['inDataName'])
        addDictItemValue(item,'DELIVERYADDRESS',localOrderInfo,configPageUsing['detailAddress']['dataName'])

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

def zipOrderInfoOrder(inOrderInfo):
    """update the order info according the web page show.post the data.

        so we need pull all data in form ,make them zip to post in the page.
    """
    try:
        logger = getLogger()
        logger.debug("start zip Order Info .")

        if inOrderInfo is None:
            return None

        # we only get the message we needed:
        #change the flat to list data.
        localOrderInfo = inOrderInfo

        #InsurantUsr 投保人
        configPageUsing = configPage['InsurantUsr']

        item = {}

        addItemDictValue(item,'NAME',localOrderInfo,configPageUsing['name']['dataName'])
        addItemDictValue(item,'SEX',localOrderInfo,configPageUsing['sex']['dataName'])
        addItemDictValue(item,'BIRTHDAY',localOrderInfo,configPageUsing['birthday']['dataName'])
        addItemDictValue(item,'AGE',localOrderInfo,configPageUsing['age']['dataName'])
        addItemDictValue(item,'PROFESSION',localOrderInfo,configPageUsing['profession']['dataName'])
        addItemDictValue(item,'PHONE',localOrderInfo,configPageUsing['phone']['dataName'])
        addItemDictValue(item,'IDCARDTYPE',localOrderInfo,configPageUsing['idcardtype']['dataName'])
        addItemDictValue(item,'IDCARDNO',localOrderInfo,configPageUsing['idcardno']['dataName'])
        addItemDictValue(item,'HEIGHT',localOrderInfo,configPageUsing['height']['dataName'])
        addItemDictValue(item,'WEIGHT',localOrderInfo,configPageUsing['weight']['dataName'])
        addItemDictValue(item,'PROVINCE',localOrderInfo,configPageUsing['briefAddress']['select']['select1']['inDataName'])
        addItemDictValue(item,'CITY',localOrderInfo,configPageUsing['briefAddress']['select']['select2']['inDataName'])
        addItemDictValue(item,'AREA',localOrderInfo,configPageUsing['briefAddress']['select']['select3']['inDataName'])
        addItemDictValue(item,'ADDRESS',localOrderInfo,configPageUsing['detailAddress']['dataName'])
        addItemDictValue(item,'ZIPCODE',localOrderInfo,configPageUsing['postcode']['dataName'])

        upDict = {'INSURANT_USR':item}
        localOrderInfo.update(upDict)

        #PolicyholderUsr 被保人
        #a loop for multi data
		#only save 4 Policyholder
		#TODO: every time ,save 4 data?


        configLst = {0:'PolicyholderUsr',1:'PolicyholderUsrA',2:'PolicyholderUsrB',3:'PolicyholderUsrC'}

        localLst =[]

        #a dictionary list
        step=len(configLst)
        #TODO: how to dynamic in page?
        for i in range(step):
            item = {}

            configShowPage = configLst.get(i)

            configPageUsing = configPage[configShowPage]
            #TODO: wrong data in relation.
            addItemDictValue(item,"BENEFICIARIESRELATION",localOrderInfo,configPageUsing['relation']['dataName'])
            addItemDictValue(item,"NAME",localOrderInfo,configPageUsing['name']['dataName'])
            addItemDictValue(item,"SEX",localOrderInfo,configPageUsing['sex']['dataName'])
            addItemDictValue(item,"BIRTHDAY",localOrderInfo,configPageUsing['birthday']['dataName'])
            addItemDictValue(item,"AGE",localOrderInfo,configPageUsing['age']['dataName'])
            addItemDictValue(item,"PROFESSION",localOrderInfo,configPageUsing['profession']['dataName'])
            addItemDictValue(item,"PHONE",localOrderInfo,configPageUsing['phone']['dataName'])
            addItemDictValue(item,"IDCARDTYPE",localOrderInfo,configPageUsing['idcardtype']['dataName'])
            addItemDictValue(item,"IDCARDNO",localOrderInfo,configPageUsing['idcardno']['dataName'])
            addItemDictValue(item,"HEIGHT",localOrderInfo,configPageUsing['height']['dataName'])
            addItemDictValue(item,"WEIGHT",localOrderInfo,configPageUsing['weight']['dataName'])
            #TODO:省市区的保存和显示还有问题.
            #addItemDictValue(item,'PROVINCE',localOrderInfo,configPageUsing['briefAddress']['select']['select1']['inDataName'])
            #addItemDictValue(item,'CITY',localOrderInfo,configPageUsing['briefAddress']['select']['select2']['inDataName'])
            #addItemDictValue(item,'AREA',localOrderInfo,configPageUsing['briefAddress']['select']['select3']['inDataName'])
            addItemDictValue(item,"ADDRESS",localOrderInfo,configPageUsing['detailAddress']['dataName'])
            addItemDictValue(item,"ZIPCODE",localOrderInfo,configPageUsing['postcode']['dataName'])

            localLst.append(item)

        upDict = {'LstINSURANT_USR':localLst}
        localOrderInfo.update(upDict)

        #Lstbeneficiaries 受益人
        #a loop for multi data
        #only show 1 BeneficiaryUsr
        #TODO: every time ,save 1 data?
        configLst = {0:'BeneficiaryUsr'}

        localLst = []

        #a dictionary list
        step=len(configLst)
        #TODO: how to dynamic in page?
        for i in range(step):
            item = {}

            configShowPage = configLst.get(i)

            configPageUsing = configPage[configShowPage]
            addItemDictValue(item,"BENEFICIARIESRELATION",localOrderInfo,configPageUsing['relation']['dataName'])
            addItemDictValue(item,"NAME",localOrderInfo,configPageUsing['name']['dataName'])
            addItemDictValue(item,"SEX",localOrderInfo,configPageUsing['sex']['dataName'])
            addItemDictValue(item,"BIRTHDAY",localOrderInfo,configPageUsing['birthday']['dataName'])
            addItemDictValue(item,"AGE",localOrderInfo,configPageUsing['age']['dataName'])
            addItemDictValue(item,"PHONE",localOrderInfo,configPageUsing['phone']['dataName'])
            addItemDictValue(item,"IDCARDTYPE",localOrderInfo,configPageUsing['idcardtype']['dataName'])
            addItemDictValue(item,"IDCARDNO",localOrderInfo,configPageUsing['idcardno']['dataName'])
            localLst.append(item)

        upDict = {'Lstbeneficiaries':localLst}
        localOrderInfo.update(upDict)

        #InsurantPlan 保险计划
        configPageUsing = configPage['InsurantPlan']
        item = localOrderInfo
        addItemDictValue(item,'INSURANCECODE',localOrderInfo,configPageUsing['product']['dataName'])
        addItemDictValue(item,'SECURITYPLAN',localOrderInfo,configPageUsing['plan']['dataName'])
        addItemDictValue(item,'PREMIUMPLAN',localOrderInfo,configPageUsing['planFamily']['dataName'])
        addItemDictValue(item,'PAYMENTSTATUS',localOrderInfo,configPageUsing['paymentstatus']['dataName'])
        addItemDictValue(item,'DMPAYMODE',localOrderInfo,configPageUsing['dmpaymode']['dataName'])
        addItemDictValue(item,'DMPAYBANK',localOrderInfo,configPageUsing['paybank']['dataName'])
        addItemDictValue(item,'CARDID',localOrderInfo,configPageUsing['cardid']['dataName'])

        #TODO: right 续期帐号
        addItemDictValue(item,'DMPAYCOMPANY',localOrderInfo,configPageUsing['dmpaybankext']['dataName'])
        addItemDictValue(item,'PURCHASECOUNT',localOrderInfo,configPageUsing['purchasecount']['dataName'])
        addItemDictValue(item,'DMCONTINUATIONYEARS',localOrderInfo,configPageUsing['dmcontinuationyears']['dataName'])
        addItemDictValue(item,'DMPAYTYPE',localOrderInfo,configPageUsing['dmpaytype']['dataName'])
        addItemDictValue(item,'DMPOLICYDATES',localOrderInfo,configPageUsing['dmpolicydates']['dataName'])
        addItemDictValue(item,'NOTE',localOrderInfo,configPageUsing['note']['dataName'])

        #delivery 保单配送
        configPageUsing = configPage['delivery']
        item = localOrderInfo
        addItemDictValue(item,'DELIVERYDATE',localOrderInfo,configPageUsing['dateTime']['dataName'])
        addItemDictValue(item,'PROVINCE',localOrderInfo,configPageUsing['deliveryAddress']['select']['select1']['inDataName'])
        addItemDictValue(item,'CITY',localOrderInfo,configPageUsing['deliveryAddress']['select']['select2']['inDataName'])
        addItemDictValue(item,'AREA',localOrderInfo,configPageUsing['deliveryAddress']['select']['select3']['inDataName'])
        addItemDictValue(item,'DELIVERYADDRESS',localOrderInfo,configPageUsing['detailAddress']['dataName'])

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

def updateDictSingleValue(srcDict,dstName,dstValue):
    if dstName in srcDict:
        srcDict[dstName] = dstValue
        pass
    else:
        #add value data to dscName to srcDict
        upDict = {dstName:dstValue}
        srcDict.update(upDict)

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

        #zip the dict
        dictData = zipOrderInfoOrder(dictData)

        jsonData =  json.dumps(dictData)

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

        jsonData = json.dumps(storageData)
        dictData = json.loads(jsonData)

        #update status
        updateDictSingleValue(dictData,"STATUS",inStatus)

        #add orderid
        updateDictSingleValue(dictData,"ORDERID",inOrderid)

        dictData = zipOrderInfoOrder(dictData)

        jsonData =  json.dumps(dictData)

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

            dictData = zipOrderInfoOrder(dictData)

            jsonData =  json.dumps(dictData)

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
