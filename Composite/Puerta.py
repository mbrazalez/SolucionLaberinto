#!/usr/bin/python
#-*- coding: utf-8 -*-

from Composite.ElementoMapa import ElementoMapa

class Puerta(ElementoMapa):
    def __init__(self):
        super(Puerta,self).__init__()
        self.abierta = None
        self.hab1 = None
        self.hab2 = None

    def entrar(self):
            print('Has pasado la puerta')
    
    def __str__(self):
        return 'Soy una puerta'
