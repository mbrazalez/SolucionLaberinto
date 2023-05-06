#!/usr/bin/python
#-*- coding: utf-8 -*-

from Composite.ElementoMapa import ElementoMapa
from abc import ABC

class Contenedor(ElementoMapa,ABC):
    def __init__(self):
        super(Contenedor,self).__init__()
        self.norte = None
        self.sur = None
        self.este = None
        self.oeste = None
        self.hijos = list()
    
    def agregarHijo(self, elementoMapa):
        self.hijos.append(elementoMapa)
        elementoMapa.padre = self
        
    def obtenerHijo(self,num):
        for hijo in self.hijos:
            if hijo.num == num:
                return hijo
    
    def obtener_str_Hijo(self,num):
        for hijo in self.hijos:
            if hijo.num == num:
                return str(hijo)


