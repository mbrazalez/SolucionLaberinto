#!/usr/bin/python
#-*- coding: utf-8 -*-
from Composite.Laberinto import Laberinto
from Composite.Habitacion import Habitacion
from Composite.Puerta import Puerta
from Composite.Pared import Pared
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

        puerta1 = self.fabricarPuerta(1,2,1)
        puerta2 = self.fabricarPuerta(2,4,2)
        puerta3 = self.fabricarPuertaBomba(3,4,1)
        puerta4 = self.fabricarPuertaCerrada(1,3,1)

        habitacion1.este = puerta1
        habitacion2.oeste = puerta1

        habitacion2.sur = puerta2
        habitacion4.component.norte = puerta2
        
        habitacion3.este = puerta3
        habitacion4.component.oeste = puerta3

        habitacion3.norte = puerta4
        habitacion1.sur = puerta4

        espada = self.fabricarEspada(1)
        bomba = self.fabricarBomba(True,1)
        
        baul_hab2 = self.fabricarBaul(1)
        baul_hab3 = self.fabricarBaul(1)

        baul_hab2.agregarHijo(bomba)
        baul_hab3.agregarHijo(espada)
        
        habitacion2.agregarHijo(baul_hab2)
        habitacion3.agregarHijo(baul_hab3)

        self.laberinto = self.fabricarLaberinto()

        self.laberinto.agregarHijo(habitacion1)
        self.laberinto.agregarHijo(habitacion2)
        self.laberinto.agregarHijo(habitacion3)
        self.laberinto.agregarHijo(habitacion4)

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

    def fabricarPuerta(self, lado1, lado2, num):
        puerta = Puerta()
        puerta.abierta=True
        puerta.num = num
        puerta.lado1=lado1
        puerta.lado2=lado2
        return puerta

    def fabricarPuertaCerrada(self, lado1, lado2,num):
        puerta = self.fabricarPuerta(lado1,lado2,num)
        puerta.abierta = False        
        return puerta
    
    def fabricarBomba(self, activa, num):
        bomba = Bomba()
        bomba.num = num
        bomba.activa = activa
        return bomba
    
    def fabricarFuego(self, encendido, num):
        fuego = Fuego()
        fuego.num =num
        fuego.encendido = encendido
        return fuego
    
    def bombaDecorar(self,component,activa,num):
        bomba = self.fabricarBomba(activa,num)
        bomba.decorar(component)
        return bomba
    
    def fabricarPuertaBomba(self,lado1,lado2,num,activa=True):
        puerta = self.fabricarPuerta(lado1,lado2,num)
        puerta_bomba = self.bombaDecorar(puerta,activa,num)
        return puerta_bomba
    
    def llamasDecorar(self,component,encendido,num):
        fuego = self.fabricarFuego(encendido,num)
        fuego.decorar(component)
        return fuego
    
    def fabricarHabitacionLlamas(self,num,encendido=True):
        habitacion = self.fabricarHabitacion(num)
        habitacion_llamas = self.llamasDecorar(habitacion,encendido,num)
        return habitacion_llamas
    
    def fabricarEspada(self,num):
        espada = Espada()
        espada.num = num
        return espada
    
    def fabricarBaul(self,num):
        baul = Baul()
        baul.num = num
        return baul
    
    
    

        
    
