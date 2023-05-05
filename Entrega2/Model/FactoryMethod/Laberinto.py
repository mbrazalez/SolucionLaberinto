#!/usr/bin/python
#-*- coding: utf-8 -*-

from Composite.Contenedor import Contenedor

class Laberinto(Contenedor):
    
    def __init__(self):
        self.habitaciones = list()

    def agregarHabitacion(self,hab):
        self.habitaciones.append(hab)

    def obtenerHabitaciones(self):
        for habitacion in self.habitaciones:
            print(habitacion)


