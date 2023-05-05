#!/usr/bin/python
#-*- coding: utf-8 -*-

from FactoryMethod.ElementoMapa import ElementoMapa
from abc import ABC

class Hoja(ElementoMapa,ABC):
    def __init__(self):
        super(Hoja,self).__init__()

