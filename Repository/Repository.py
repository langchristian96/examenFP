'''
Created on Jan 27, 2016

@author: LenovoM
'''
from time import *
from datetime import *
from Domain.Route import *
class Repositoryy:
    _fName='routes.txt'
    def __init__(self):
        self.__data=[]
        self.__rate=0
        self.__loadFromFile()
    
    def find(self,id):
        '''
        find function for id
        input:id
        output: None if its not in our repository or the object if it is
        '''
        for e in self.__data:
            if e.getId()==id:
                return e
        return None
    def getRate(self):
        #getter for rate
        return self.__rate
    def remove(self,id):
        #remover; used only for testing
        e=self.find(id)
        if e!=None:
            self.__data.remove(e)
            self.__storeToFile()
    
    def add(self,obj):
        '''
        Adds object to our repositories
        input:obj
        output:-
        raise:Value error if the id exists already
        '''
        e=self.find(obj.getId())
        if e!=None:
            raise ValueError("Id already exists")
        else:
            self.__data.append(obj)
            self.__storeToFile()
    def __loadFromFile(self):
        '''
        Function for loading from file
        '''
        try:
            f=open(self._fName,'r')
            t=f.readline().strip()
            self.__rate=int(t)
            t=f.readline().strip()
            while t!='':
               
                arg=t.strip().split(',')
                print(arg[0])
                time1=arg[2].strip().split(':')
                time2=arg[4].strip().split(':')
                print(arg)
                r=Route(int(arg[0]),arg[1],time(hour=int(time1[0]),minute=int(time1[1])),arg[3],time(int(time2[0]),int(time2[1])),int(arg[5]))
                self.__data.append(r)
                t=f.readline().strip()
                
            f.close()
        except IOError:
            return
        
    def store(self):
        #used for storing to file
        self.__storeToFile()
    def __storeToFile(self):
        '''
        Function for storing to file
        '''
        f=open(self._fName,'w')
        s=''
        s+=str(self.__rate)
        s+='\n'
        for e in self.__data:
            s+=str(e.getId())
            s+=','
            s+=e.getDCity()
            s+=','
            h=e.getDTime()
            s+=str(h)
            
            s+=','
            s+=e.getACity()
            s+=','
            h2=e.getATime()
            s+=str(h2)
            s+=','
            s+=str(e.getTickets())
            s+='\n'
        f.write(s)
        f.close()
    def getAll(self):
        #returns the entire list
        return self.__data
            
   
def testRepository():
    #tester for repository
    repo=Repositoryy()
    r1=Route(1,'bistrita',time(20,30),'cluj',time(21,40),4)
    l=len(repo.getAll())
    repo.add(r1)
    assert len(repo.getAll())==l+1
    repo.remove(1)
    assert len(repo.getAll())==l

if __name__=='__main__':    
    testRepository()

