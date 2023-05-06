#!/usr/bin/python
#-*- coding: utf-8 -*-

from Composite.Contenedor import Contenedor

class Baul(Contenedor):
    def __init__(self):
        super(Baul,self).__init__()
        
    def entrar(self):
            print('Te has metido al baul')
    
    def __str__(self):
        hijos = ''
        for hijo in self.hijos:
            hijos += str(hijo)
	
        return ('Hay un baúl y mis hijos son' + hijos)