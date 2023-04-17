#!/usr/bin/python
#-*- coding: utf-8 -*-

from Laberinto import Laberinto
from Habitacion import Habitacion
from Puerta import Puerta
from Pared import Pared

class Juego:

    def __init__(self):
        self.laberinto=None

    def fabricarPared(self):
        return Pared()

    def fabricarPuerta(self,abierta,lado1,lado2):
            puerta = Puerta()
            puerta.abierta=abierta
            puerta.lado1=1
            puerta.lado2=2
            return puerta

    def fabricarHabitacion(self,num):
        habitacion = Habitacion()
        habitacion.num = num
        habitacion.orientacion=norte
        habitacion.orientacion=sur
        habitacion.orientacion=este
        habitacion.orientacion=oeste
        return habitacion
    
    def fabricarLaberinto2hab():
        habitacion1 = fabricarHabitacion(1)
        habitacion2 = fabricarHabitacion(1)

        habitacion1.norte=fabricarPared()
        habitacion1.este=fabricarPared()
        habitacion1.oeste=fabricarPared()

        habitacion2.sur=fabricarPuerta()
        habitacion2.este=fabricarPared()
        habitacion2.oeste=fabricarPared()        
        
        puerta = fabricarPuerta(True,1,2)
        habitacion1.sur=puerta
        habitacion2.norte=puerta

        self.laberinto = fabricarLaberinto()
        self.laberinto.agregarHabitacion(habitacion1)
        self.laberinto.agregarHabitacion(habitacion2)


    def fabricarLaberinto(self):
         return Laberinto()


