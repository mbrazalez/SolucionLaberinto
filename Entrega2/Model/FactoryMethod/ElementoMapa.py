#!/usr/bin/python
#-*- coding: utf-8 -*-
from abc import ABC, abstractmethod

class ElementoMapa(ABC):
    def __init__(self):
        self.hijos = list()

    @abstractmethod
    def agregarHijo(self, elementoMapa):
        self.hijos.append(elementoMapa)
    
    @abstractmethod
    def entrar(self, ):
        pass

