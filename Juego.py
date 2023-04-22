#!/usr/bin/python
#-*- coding: utf-8 -*-

from Laberinto import Laberinto
from Habitacion import Habitacion
from Puerta import Puerta
from Pared import Pared

class Juego:
    def __init__(self) -> None:
         self.laberinto = None

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
        habitacion.este = self.fabricarPared()
        habitacion.oeste = self.fabricarPared()
        habitacion.norte = self.fabricarPared()
        habitacion.sur = self.fabricarPared()

        return habitacion
    
    def fabricarLaberinto2hab(self):
        habitacion1 = self.fabricarHabitacion(1)
        habitacion2 = self.fabricarHabitacion(2)     
        
        puerta = self.fabricarPuerta(True,1,2)
        habitacion1.sur=puerta
        habitacion2.norte=puerta

        self.laberinto = self.fabricarLaberinto()
        self.laberinto.agregarHabitacion(habitacion1)
        self.laberinto.agregarHabitacion(habitacion2)


    def fabricarLaberinto(self):
         return Laberinto()


