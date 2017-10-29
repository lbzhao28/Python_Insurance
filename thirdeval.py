#!/usr/bin/env python
# coding=utf8
__author__ = 'stone'
#2017.10.29.    add for test the third eval program.
import web
from web.contrib.template import render_mako

import configData
from configData import getConfig
from logHelper import getLogger
import traceback

import re
import base64

import json

import urlparse
import ThirdEvalDomainHandler

web.config.debug = False

urls = (
        '/thirdeval','thirdeval',
        '/thirdevalUpdate/(.*)/(.*)','thirdevalUpdate',
        '/thirdevalList/(.*)/(.*)','thirdevalList'
        )

app = web.application(urls,globals(),autoreload=True)

# input_encoding and output_encoding is important for unicode
# template file. Reference:
# http://www.makotemplates.org/docs/documentation.html#unicode
render = render_mako(
        directories = ['templates'],
        input_encoding = 'utf-8',
        output_encoding = 'utf-8',
        )

class thirdevalList:
    def GET(self,session_usr,session_grpid):
        try:
            logger = getLogger()
            logger.debug("start OrderList Page GET response")

            web.ctx.session.session_usrid =  session_usr
            web.ctx.session.session_grpid =  session_grpid

            globalDefine.globalOrderInfoErrorlog = "No Error"

            #TODO: open the auth in future.also need purview.
#            authreq = checkUserAuth(web)
#
#            if authreq:
#                web.header('WWW-Authenticate','Basic realm="Auth example"')
#                web.ctx.status = '401 Unauthorized'
#                logger.debug("no right HTTP_AUTHORIZATION")
#                return render.error(error = web.ctx.status)

            parsed_url = urlparse.urlparse(web.ctx.fullpath)
            query_url = parsed_url.query
            if (query_url != ''):
                query_dict = dict(urlparse.parse_qsl(query_url))

                if 'ROLE' in query_dict:
                    role = str(query_dict['ROLE'])
                else:
                    role = None
                web.ctx.session.session_role =  role

                if 'GRPID' in query_dict:
                    grpid = query_dict['GRPID']
                else:
                    grpid = None

                if 'CRUSR' in query_dict:
                    crusr = query_dict['CRUSR']
                else:
                    crusr = None

                if 'STARTDT' in query_dict:
                    startdt = query_dict['STARTDT']
                else:
                    startdt = None

                if 'ENDDT' in query_dict:
                    enddt = query_dict['ENDDT']
                else:
                    enddt = None

                if 'ORDERSTATUS' in query_dict:
                    orderstatus = query_dict['ORDERSTATUS']
                    #special for show all ,do not judge orderstatus.
                    if orderstatus == 'SHOWALL':
                        orderstatus = None
                else:
                    orderstatus = None

                if 'CONTACTID' in query_dict:
                    contactid = query_dict['CONTACTID']
                else:
                    contactid = None

                if 'ORDERID' in query_dict:
                    orderid = query_dict['ORDERID']
                else:
                    orderid = None

                if 'PAGEINDEX' in query_dict:
                    pageindex = query_dict['PAGEINDEX']
                else:
                    pageindex = None

                return render.orderList(session_usr=session_usr,session_grpid =  session_grpid,grpid=grpid,crusr=crusr,contactid = contactid,orderid=orderid,orderstatus=orderstatus,startdt=startdt,enddt=enddt,pageindex=pageindex,outrole=role)
            else:
                grpid = None
                crusr = None
                contactid = None
                orderid = None
                startdt = None
                enddt = None
                orderstatus = None
                pageindex  = None
                role = None
                return render.orderList(session_usr=session_usr,session_grpid =  session_grpid,grpid=grpid,crusr=crusr,contactid = contactid,orderid=orderid,orderstatus=orderstatus,startdt=startdt,enddt=enddt,pageindex=pageindex,outrole=role)
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

#in JS, can not use put directly, so we use POST　to simulate it.
class thirdevalUpdate:
    def POST(self,contactid,orderid):
        try:
            logger = getLogger()
            logger.debug("start Order Update POST response")

            globalDefine.globalOrderInfoErrorlog = "No Error"

            #TODO: open the auth in future.also need purview.
#            authreq = checkUserAuth(web)
#
#            if authreq:
#                web.header('WWW-Authenticate','Basic realm="Auth example"')
#                web.ctx.status = '401 Unauthorized'
#                logger.debug("no right HTTP_AUTHORIZATION")
#                return render.error(error = web.ctx.status)

            if orderid is None:
                return render.error(error = 'no orderid')
            else:
                #get POST form data
                data = web.input()
                #call REST post data
                #TODO: 1 待审核订单
                status = '1'
                retStr = OrderDomainHandler.putOrderInfoContact(orderid,data,status,web.ctx.session.session_usrid)

                #according the response

                if retStr is None:
                    return render.error(error = 'update failure!')

                retDict = json.loads(retStr)
                if (retDict["RETURNFLAG"] == True):
                    role = web.ctx.session.session_role;
                    return render.order(contactid = contactid,orderid = orderid,outrole = role)
                else:
                    return render.error(error = 'update failure!')

        except :
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

class thirdeval:
    def POST(self):
        logger = getLogger()
        try:
            logger.debug("start Order Page POST response")

            globalDefine.globalOrderInfoErrorlog = "No Error"

            #TODO: open the auth in future.also need purview.
#            authreq = checkUserAuth(web)
#
#            if authreq:
#                web.header('WWW-Authenticate','Basic realm="Auth example"')
#                web.ctx.status = '401 Unauthorized'
#                logger.debug("no right HTTP_AUTHORIZATION")
#                return render.error(error = web.ctx.status)

            if contactid is None:
                return render.error(error = 'no contactid')
            else:
                #get POST form data
                data = web.input()
                #call REST post data
                #TODO: 1 means 待审核订单
                status = '1'

                retStr = OrderDomainHandler.postOrderInfoContact(contactid,data,status,web.ctx.session.session_usrid,web.ctx.session.session_grpid)

                if retStr is None:
                    return render.error(error = 'add failure.')

                #according the response
                retDict = json.loads(retStr)
                if (retDict["RETURNFLAG"] == True):
                    #refresh the order.
                    orderidStr = retDict["OrderID"]
                    role = web.ctx.session.session_role;
                    return render.order(contactid = contactid,orderid = orderidStr,outrole = role)
                else:
                    return render.error(error = 'add failure.')

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

    def GET(self):
        logger = getLogger()
        try:
            logger.debug("start thirdval Page GET response")

            parsed_url = urlparse.urlparse(web.ctx.fullpath)
            query_url = parsed_url.query
            query_url = query_url.encode('utf-8')
            if (query_url != ''):
                query_dict = dict(urlparse.parse_qsl(query_url))

                if 'orderid' in query_dict:
                    orderid = query_dict['orderid']
                    role = web.ctx.session.session_role;
                    return render.thirdeval(orderid = orderid,queryDict = query_dict)
                else:
                    #if no orderid, according the query_dict to show a file.
                    orderid = None
                    return render.thirdeval(orderid = orderid,queryDict = query_dict)
            else:
                #if no querey string.  show blank file
                orderid = None
                query_dict = None
                return render.thirdeval(orderid = orderid,queryDict = query_dict)
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

if __name__ == "__main__":
    app.run()
