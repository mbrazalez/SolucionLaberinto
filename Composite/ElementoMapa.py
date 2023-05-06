#!/usr/bin/python
#-*- coding: utf-8 -*-
from abc import ABC, abstractmethod

class ElementoMapa(ABC):
    def __init__(self):
        self.padre = None
        self.num = None
        
    @abstractmethod
    def entrar(self, ):
        pass

