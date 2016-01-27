from datetime import time
class Route:
    def __init__(self,id,dCity,dTime,aCity,aTime,tickets):
        #instance creator for Route
        self.__id=id
        self.__dCity=dCity
        self.__dTime=dTime
        self.__aCity=aCity
        self.__aTime=aTime
        self.__tickets=tickets
        self.__sold=0
    def getId(self):
        #getter for id
        return self.__id
    def getSold(self):
        #getter for sold
        return self.__sold
    def getDCity(self):
        #getter for DCity
        return self.__dCity
    def getDTime(self):
        #getter for DTime
        return self.__dTime
    def getACity(self):
        #getter for ACity
        return self.__aCity
    def getATime(self):
        #getter for ATime
        return self.__aTime
    def getTickets(self):
        #getter for tickets
        return self.__tickets
    def setTickets(self):
        self.__tickets-=1
        self.__sold+=1
    
def testRoute():
    r=Route(1,'bistrita',time(20,30),'cluj',time(21,40),100)
    assert r.getId()==1
    assert r.getDCity()=='bistrita'
    assert r.getDTime()==time(20,30)
    assert r.getACity()=='cluj'
    assert r.getATime()==time(21,40)
    assert r.getTickets()==100
if __name__=='__main__':
    testRoute()
    
