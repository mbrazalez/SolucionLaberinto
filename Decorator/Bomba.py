#!/usr/bin/python
#-*- coding: utf-8 -*-

from Decorator.Decorator import Decorator

class Bomba(Decorator):
    def __init__(self):
        super(Bomba,self).__init__()
        self.activa = None
    
    def entrar(self):
        print('Te has chocado con la bomba')


    def __str__(self):
	     return "Soy una bomba y estoy decorando -> " + str(self.component)