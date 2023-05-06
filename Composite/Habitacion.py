#!/usr/bin/python
#-*- coding: utf-8 -*-

from Composite.Contenedor import Contenedor

class Habitacion(Contenedor):
    def __init__(self):
        super(Habitacion,self).__init__()

    def entrar(self):
        print("Estás en la habitación" + str(self.num))

    def __str__(self):
	        return ("\n\nLA HABITACIÓN NÚMERO: " + str(self.num) +
        "\n Tiene en Norte: " + str(self.norte) +
        "\n Tiene en Sur: " + str(self.sur) +
        "\n Tiene en Este: " + str(self.este) +
        "\n Tiene en Oeste: " + str(self.oeste))