__author__ = 'stone'
#encoding:utf-8
#File:order.py
import web
from web.contrib.template import render_mako

import globalDefine
import traceback
import configData
from configData import getConfig
from logHelper import getLogger

import re
import base64

import json

import urlparse

urls = (
        '/order/(.*)','order',
        '/orderList/(.*)','orderList'
        )

app = web.application(urls,globals(),autoreload=True)

allowed = (
    (getConfig('allowedUser1','UserName','str'),getConfig('allowedUser1','Password','str')),
    (getConfig('allowedUser2','UserName','str'),getConfig('allowedUser2','Password','str'))
    )

# input_encoding and output_encoding is important for unicode
# template file. Reference:
# http://www.makotemplates.org/docs/documentation.html#unicode
render = render_mako(
        directories = ['templates'],
        input_encoding = 'utf-8',
        output_encoding = 'utf-8',
        )

# according the contactid ,to show the orderlist.
class orderList:
    #TODO:  always show all the order according the contactid?
    def GET(self,contactid):
        try:
            logger = getLogger()
            logger.debug("start OrderList Page GET response")
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

class order:
    def POST(self,contactid):
        try:
            logger = getLogger()
            logger.debug("start Order Page POST response")

            globalDefine.globalOrderInfoErrorlog = "No Error"

            authreq = checkUserAuth(web)

            if authreq:
                web.header('WWW-Authenticate','Basic realm="Auth example"')
                web.ctx.status = '401 Unauthorized'
                logger.debug("no right HTTP_AUTHORIZATION")
                return render.error(error = web.ctx.status)

            #get POST form data.
            data = web.input()

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

    def GET(self,contactid):
    #must have contactid, otherwise,the data will be wrong.
        try:
            logger = getLogger()
            logger.debug("start Order Page GET response")

            globalDefine.globalOrderInfoErrorlog = "No Error"

            authreq = checkUserAuth(web)

            if authreq:
                web.header('WWW-Authenticate','Basic realm="Auth example"')
                web.ctx.status = '401 Unauthorized'
                logger.debug("no right HTTP_AUTHORIZATION")
                return render.error(error = web.ctx.status)

            if not contactid:
                return render.error(error = 'no contactid')
            else:
                #if has orderid according the orderid to get the order info.
                #query_dict = dict(urlparse.parse_qsl(web.ctx.env['QUERY_STRING']))
                parsed_url = urlparse.urlparse(web.ctx.fullpath)
                query_url = parsed_url.query
                if (query_url != ''):
                    query_dict = dict(urlparse.parse_qsl(query_url))
                    orderid = query_dict['orderid']
                    return render.order(contactid = contactid,orderid = orderid)
                else:
                    #if no orderid,show a blank file.
                    orderid = None
                    return render.order(contactid = contactid,orderid = orderid)
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

def checkUserAuth(inWeb):
    logger = getLogger()
    auth = inWeb.ctx.env.get('HTTP_AUTHORIZATION')
    authreq = False
    if auth is None:
        authreq = True
    else:
        auth = re.sub('^Basic ','',auth)
        username,password = base64.decodestring(auth).split(':')
        if (username,password) in allowed:
            logger.debug("has right HTTP_AUTHORIZATION")
            pass
        else:
            authreq = True
    return authreq

if __name__ == "__main__":
    app.run()
