'''
Created on Jan 27, 2016

@author: LenovoM
'''
from Domain.Route import *
from Repository.Repository import *
from datetime import timedelta
from time import *
from datetime import datetime
from operator import itemgetter


class Controllerr:
    def __init__(self,repo):
        self.__repo=repo
    
    def addTrain(self,obj):
        '''
        Adds a route to our repo
        input:obj of type route
        output:-
        '''
        if obj.getDTime()>obj.getATime():
            raise ValueError("DTime must be < than ATime")
        self.__repo.add(obj)
    def calculateTicket(self,id):
        '''
        Calculates the value of the ticket
        input:ticket id-integer
        output:-the ticket price
        raise ValueError if no available tickets or if the id does not eixst
        
        '''
        e=self.__repo.find(int(id))
        if e!=None:
            if e.getTickets()==0:
                raise ValueError("Not having any available tickets")
            rate=self.__repo.getRate()
            hour1=e.getDTime()
            hour1=str(hour1).split(':')
            
            hour2=e.getATime()
            hour2=str(hour2).split(':')
            hours=int(hour2[0])-int(hour1[0])
            mins=int(hour2[1])-int(hour2[1])
            hours*=60
            hours+=mins
            hours/=60
            price=hours*rate
            return price
        else:
            raise ValueError("Does not exist")
        
        
    def sellTicket(self,objid):
        '''
        Sells a ticket for the given id
        input:id of the route(integer)
        output:-
        '''
        obj=self.__repo.find(objid)
        obj.setTickets()
        self.__repo.store()
        
    def report(self):
        '''
        returns the routes in descending order wrt the tickets sold for each route
        input:-
        output:list of dictionaries that correspond to each route and its sold tickets
        '''
        e=self.__repo.getAll()
        l=[]
        for i in e:
            w={'id':i.getId(),'sold':i.getSold(),'DCity':i.getDCity(),'ACity':i.getACity()}
            l.append(dict(w))
        l.sort(key=itemgetter('sold'),reverse=True)
        return l
            

    
    