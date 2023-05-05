#!/usr/bin/python
#-*- coding: utf-8 -*-

from msilib.schema import Component
from Hoja import Hoja
from abc import ABC, abstractclassmethod

class Decorator(Hoja,ABC):
    @abstractclassmethod
    def __init__(self):
        super(Decorator,self).__init__()
        self.component = None

    def decorar(self,component):
        self.component = component
    
