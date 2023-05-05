#!/usr/bin/python
#-*- coding: utf-8 -*-

from FactoryMethod.ElementoMapa import ElementoMapa
from abc import ABC

class Contenedor(ElementoMapa,ABC):
    def __init__(self):
        super(Contenedor,self).__init__()
        self.norte = None
        self.sur = None
        self.este = None
        self.oeste = None
    


