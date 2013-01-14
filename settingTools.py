__author__ = 'stone'
#encoding:utf-8
#File:settingTools.py
#this file to get the db to create js file.
import time

def writeArrayCityJs():
    f = open('./static/js/test.js','w')
    try:
        writeLst = []

        str = '/**\n'
        writeLst.append(str)

        str = '* Created by python tools\n'
        writeLst.append(str)

        str = '* User: stone\n'
        writeLst.append(str)

        str = '* Date: ' + time.strftime('%Y-%m-%d',time.localtime(time.time())) + '\n'
        writeLst.append(str)

        str = '* Time: ' + time.strftime('%H-%M-%S',time.localtime(time.time())) + '\n'
        writeLst.append(str)

        str = '* only change the file by tools.\n'
        writeLst.append(str)

        str = '*/\n'
        writeLst.append(str)

        str = 'function createArrayCity()\n'
        writeLst.append(str)

        str = '{\n'
        writeLst.append(str)

        str = '     var arrayCity=new Array();\n'
        writeLst.append(str)

        #TODO: a loop to get data from db.

        str = '}\n'
        writeLst.append(str)

        f.writelines(writeLst)
        pass
    finally:
        f.close()

if __name__ == "__main__":
    writeArrayCityJs()

