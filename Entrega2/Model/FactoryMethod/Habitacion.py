#!/usr/bin/python
#-*- coding: utf-8 -*-

from typing_extensions import override
from Composite.Contenedor import Contenedor

class Habitacion(Contenedor):
    def __init__(self):
        super(Contenedor,self).__init__()

    @override
    def entrar(self):
        print('Has entrado a la habitacion')

