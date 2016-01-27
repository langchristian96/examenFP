'''
Created on Jan 27, 2016

@author: LenovoM
'''
class Incomee:
    def __init__(self):
        #instantiation for Incomee
        self.__income=0
    def setIncome(self,money):
        #adds money to the income
        self.__income+=money
    def getIncome(self):
        #getter for income
        return self.__income