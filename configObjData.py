__author__ = 'stone'

from configobj import ConfigObj
import os

def getConfigPage():
    """get the page config file"""


    #print os.getcwd()
    #os.chdir('..')
    #os.chdir('D:\Stone\Python\Python_Insurance')
    #print os.getcwd()

    configPage = ConfigObj('pagesConf.conf')

    #configPageInsurantUsr = configPage['InsurantUsr']
    #dictFirst = configPageInsurantUsr.dict()
    #for member in configPageInsurantUsr:
        #dictSecond = configPageInsurantUsr[member]
        #print dictSecond
        #for item in configPageInsurantUsr[member]:
        #    print configPageInsurantUsr[member][item]
        #for item in member:
        #    print member[item]
    #print configPage
    #print configPageInsurantUsr
    #configPageInsurantUsr = configPage['InsurantUsr']
    #print configPageInsurantUsr

    #print configPageInsurantUsr.as_int( 'rowNumber')
    #print configPage.as_bool("hasInsurantUsr")
    return configPage

if __name__ == "__main__":
    getConfigPage()
