#!/usr/bin/python
#-*- coding: utf-8 -*-
from Laberinto import Laberinto
from FactoryMethod.Habitacion import Habitacion
from FactoryMethod.Puerta import Puerta
from FactoryMethod.Pared import Pared
from Decorator.Bomba import Bomba
from Decorator.Fuego import Fuego
from Composite.Espada import Espada
from Composite.Baul import Baul


class Juego:
    def __init__(self):
        self.laberinto = None

    def fabricarLaberinto4hab(self):
        
        habitacion1 = self.fabricarHabitacion(1)
        habitacion2 = self.fabricarHabitacion(2)
        habitacion3 = self.fabricarHabitacion(3)
        habitacion4 = self.fabricarHabitacionLlamas(4)

        puerta1 = self.fabricarPuerta(1,2)
        puerta2 = self.fabricarPuerta(2,4)
        puerta3 = self.fabricarPuertaBomba(3,4)
        puerta4 = self.fabricarPuertaCerrada(1,3)

        habitacion1.este = puerta1
        habitacion2.oeste = puerta1

        habitacion2.sur = puerta2
        habitacion4.norte = puerta2
        
        habitacion3.este = puerta3
        habitacion4.oeste = puerta3

        habitacion3.norte = puerta4
        habitacion1.sur = puerta4

        espada = self.fabricarEspada()
        bomba = self.fabricarBomba(True)
        
        baul_hab2 = self.fabricarBaul()
        baul_hab3 = self.fabricarBaul()

        baul_hab2.agregarHijo(bomba)
        baul_hab3.agregarHijo(espada)
        
        habitacion2.agregarHijo(baul_hab2)
        habitacion3.agregarHijo(baul_hab3)

        self.laberinto = self.fabricarLaberinto()

        self.laberinto.agregarHabitacion(habitacion1)
        self.laberinto.agregarHabitacion(habitacion2)
        self.laberinto.agregarHabitacion(habitacion3)
        self.laberinto.agregarHabitacion(habitacion4)

    def fabricarLaberinto(self):
        return Laberinto()

    def fabricarPared(self):
        return Pared()

    def fabricarHabitacion(self,num):
        habitacion = Habitacion()
        habitacion.num = num
        habitacion.este = self.fabricarPared()
        habitacion.oeste = self.fabricarPared()
        habitacion.norte = self.fabricarPared()
        habitacion.sur = self.fabricarPared()
        return habitacion

    def fabricarPuerta(self, lado1, lado2):
        puerta = Puerta()
        puerta.abierta=True
        puerta.lado1=lado1
        puerta.lado2=lado2
        return puerta

    def fabricarPuertaCerrada(self, lado1, lado2):
        puerta = self.fabricarPuerta(lado1,lado2)
        puerta.abierta = False        
        return puerta
    
    def fabricarBomba(self, activa):
        bomba = Bomba()
        bomba.activa = activa
        return bomba
    
    def fabricarFuego(self, encendido):
        fuego = Fuego()
        fuego.encendido = encendido
        return fuego
    
    def bombaDecorar(self,component,activa):
        bomba = self.fabricarBomba(activa)
        bomba.decorar(component)
        return bomba
    
    def fabricarPuertaBomba(self,lado1,lado2,activa=True):
        puerta = self.fabricarPuerta(lado1,lado2)
        self.bombaDecorar(puerta,activa)
        return puerta
    
    def llamasDecorar(self,component,encendido):
        fuego = self.fabricarFuego(encendido)
        fuego.decorar(component)
        return fuego
    
    def fabricarHabitacionLlamas(self,num,encendido=True):
        habitacion = self.fabricarHabitacion(num)
        self.llamasDecorar(habitacion,encendido)
        return habitacion
    
    def fabricarEspada(self):
        return Espada()
    
    def fabricarBaul(self):
        return Baul()

    
    
    

        
    
