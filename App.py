'''
Created on Jan 27, 2016

@author: LenovoM
'''
from Domain.Route import *
from Repository.Repository import *
from Controller.Controller import *
from UI.UI import *
from Domain.income import *
from datetime import time

repo=Repositoryy()
inc=Incomee()
ctrl=Controllerr(repo)
ui=UI(ctrl,inc)
ui.menu()