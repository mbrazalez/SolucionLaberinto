#!/usr/bin/python
#-*- coding: utf-8 -*-
from abc import ABC, abstractmethod

class ElementoMapa(ABC):
    @abstractmethod
    def entrar(self):
        pass

