#!/usr/bin/python
#-*- coding: utf-8 -*-

from Composite.Hoja import Hoja
from abc import ABC, abstractclassmethod

class Decorator(Hoja,ABC):
    def __init__(self):
        super(Decorator,self).__init__()
        self.component = None

    def decorar(self,component):
        self.component = component
    
