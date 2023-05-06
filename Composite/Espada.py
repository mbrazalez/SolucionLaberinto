#!/usr/bin/python
#-*- coding: utf-8 -*-

from Composite.Hoja import Hoja

class Espada(Hoja):
    def __init__(self):
        super(Espada,self).__init__()

    def entrar(self):
        print('Te has chocado con la espada')

    def __str__(self):
	    return ('Hay una espada')