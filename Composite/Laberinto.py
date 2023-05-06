#!/usr/bin/python
#-*- coding: utf-8 -*-

from Composite.Contenedor import Contenedor

class Laberinto(Contenedor):
    
    def __init__(self):
        super(Laberinto, self).__init__()
        self.num = 1
    
    def entrar(self):
        print('Has entrado al laberinto')

    def __str__(self):
        return "\nBIENVENIDO AL LABERINTO NÚMERO: " + str(self.num)