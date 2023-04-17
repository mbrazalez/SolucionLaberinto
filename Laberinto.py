#!/usr/bin/python
#-*- coding: utf-8 -*-

from Habitacion import Habitacion

class Laberinto(Habitacion):

    def __init__(self):
        self.habitaciones = list()

    def agregarHabitacion(self,hab):
        self.habitaciones.append(hab)

    def obtenerHabitaciones(self):
        for habitacion in self.habitaciones:
            print(habitacion)
