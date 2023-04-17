#!/usr/bin/python
#-*- coding: utf-8 -*-

from ElementoMapa import ElementoMapa

class Puerta(ElementoMapa):
    
    def __init__(self):
        self.abierta = None
        self.lado1 = None
        self.lado2 = None

    def entrar(self):
        if self.abierta:
            print('Has entrado a la habitacion')
        else:
            print('Esta cerrada')


