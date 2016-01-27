'''
Created on Jan 27, 2016

@author: LenovoM
'''
from Domain.Route import *
from Repository import *
from Controller import *

class UI:
    def __init__(self,ctrl,income):
        self.__ctrl=ctrl
        self.__income=income
    def printMenu(self):
        '''
        Printing Menu
        '''
        print('1.Add route')
        print('2.Sell ticket')
        print('3.Show total income')
        print('4.Ordered list')
        print('0.Exit')
        
    def valid(self,command):
        '''
        Validation function for command
        input:command
        output:True if it is valid
        False if it isnt
        '''
        commandd=['1','2','3','4','0']
        return (command in commandd)
    def __sellTicket(self):
        '''
        Function for selling tickets
        '''
        id=input("Input id")
        try:
            price=self.__ctrl.calculateTicket(id)
            print("The price for this route is: ")
            print(price)
            command2=input("Press 1 to accept or 2 to decline ")
            if command2=='1':
                self.__ctrl.sellTicket(int(id))
                self.__income.setIncome(price)
                print("Bought.")
            else:
                print("Cancelled")
                return
        except ValueError as e:
            print(e)
    def __report(self):
        '''
        Function for getting and printing the list of trains
        '''
        l=[]
        l=self.__ctrl.report()
        for e in l:
            print(e)
    def __getIncome(self):
        '''
        Function for getting the total income
        returns the total income
        '''
        print(self.__income.getIncome())
    def __addRoute(self):
        id=input("Input id")
        dCity=input("Input departure city")
        dTime=input("Input departure time")
        dTime=str(dTime).split(':')
        print(dTime)
        aCity=input("Input arrival city")
        aTime=input("Input arrival time")
        aTime=str(aTime).split(':')
        tickets=input("Input tickets")
        try:
            self.__ctrl.addTrain(Route(int(id),dCity,time(hour=int(dTime[0]),minute=int(dTime[1])),aCity,time(hour=int(aTime[0]),minute=int(aTime[1])),int(tickets)))
            
        except ValueError as e:
            print(e)
    def menu(self):
        commandDict={'1':self.__addRoute,
                     '2':self.__sellTicket,
                     '3':self.__getIncome,
                     '4':self.__report
                     
                     }
        while True:
            self.printMenu()
            command=input("Input command ")
            while not self.valid(command):
                command=input("Try again ")
            if command=='0':
                return
            commandDict[command]()
            
            