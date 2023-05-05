#!/usr/bin/python
#-*- coding: utf-8 -*-

from Decorator.Decorator import Decorator

class Fuego(Decorator):
    def __init__(self):
        super(Fuego,self).__init__()
        self.encendido = None

