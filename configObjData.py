__author__ = 'stone'

import configobj
from configobj import ConfigObj

def getConfigPage():
    configPage = ConfigObj('pagesConf.conf')
    #print configPage
    return configPage