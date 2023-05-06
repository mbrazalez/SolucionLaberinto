#!/usr/bin/python
#-*- coding: utf-8 -*-

from Decorator.Decorator import Decorator

class Fuego(Decorator):
    def __init__(self):
        super(Fuego,self).__init__()
        self.encendido = None

    def entrar(self):
        print('Te has quemado')
    
    def __str__(self):
		    return "Soy fuego y estoy decorando -> " + str(self.component)