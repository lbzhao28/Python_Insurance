__author__ = 'stone'

import configObjData
from configObjData import getConfigFile

def getDictStatic(inSourceID):
    """get the static data from the different source

        Source may be: web cache,db,REST and web service , config file.
        Now ,we user cache to accelerate the speed.
        return a dictionary.
    """

    #TODO: use cache or Redis to finish this function.

    #TODO: use global to get data from db or web service.

    #TODO: two data value OK to select,how about radio?
    configFile = getConfigFile("staticConf.conf")
    retDict = configFile.dict()
    return retDict[inSourceID]

if __name__ == "__main__":
    print getDictStatic("profession")
