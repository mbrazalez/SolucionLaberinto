#!/usr/bin/python
#-*- coding: utf-8 -*-

from Decorator import Decorator

class Bomba(Decorator):
    def __init__(self):
        super(Bomba,self).__init__()
        self.activa = None
    


