#!/usr/bin/python
#-*- coding: utf-8 -*-

from Composite.ElementoMapa import ElementoMapa

class Pared(ElementoMapa):
    def __init__(self):
        super(Pared,self).__init__()
    
    def entrar(self):
        print('Te has chocado')
    
    def __str__(self):
        return "Una pared"