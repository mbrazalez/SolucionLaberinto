from Juego import Juego

if __name__=="__main__":
    juego = Juego()
    juego.fabricarLaberinto4hab()
    print(str(juego.laberinto))
    print(str(juego.laberinto.obtenerHijo(1)))
    print(str(juego.laberinto.obtenerHijo(2)))
    print(str(juego.laberinto.obtenerHijo(2).obtenerHijo(1)))
    print(str(juego.laberinto.obtenerHijo(3)))
    print(str(juego.laberinto.obtenerHijo(4)))