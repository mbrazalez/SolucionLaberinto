#!/usr/bin/python
#-*- coding: utf-8 -*-

from Composite.ElementoMapa import ElementoMapa
from abc import ABC

class Hoja(ElementoMapa,ABC):
    def __init__(self):
        super(Hoja,self).__init__()

