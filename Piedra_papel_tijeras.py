import random

print("---------------Juego de piedra, papel y tijera.--------------\n")


class PPT:

    def __init__(self):
        self.__manos = ["Piedra", "Papel", "Tijera"]
        self.__jugado1_puntuacion = 0
        self.__jugado2_puntuacion = 0

    # Metodo que busca el arma para jugando
    def busca_arma(self, prueba: str):
        arma = prueba.capitalize()

        if not arma in self.__manos:
            return f"Intente de nuevo...\nSolo se permite: {self.__manos}"
        else:
            return arma

    # Metodo de comparacion de arma con los jugardores
    def comparacion(self, jugado1: object, jugado2: object):

        if jugado1 == jugado2:

            return f"Empate: Jugado 1:{jugado1} vs Jugado 2:{jugado2}"

        else:
            if jugado1 == self.__manos[0] and jugado2 == self.__manos[2] or jugado1 == self.__manos[1] and jugado2 == self.__manos[0] or jugado1 == self.__manos[2] and jugado2 == self.__manos[1]:
                self.__jugado1_puntuacion += 1
            else:
                self.__jugado2_puntuacion += 1

        datos = f"{self.__jugado1_puntuacion} vs {self.__jugado2_puntuacion}"

        return f"Jugado 1:{jugado} vs Jugado 2:{jugado2}\nPuntuacion: {datos}"

    # Un Bot para jugar con la computadora
    def bot(self):
        number = random.randint(0, 2)
        return self.__manos[number]

    def getManos(self):
        return self.__manos

    # Enseña el resultado a finaliza el juego
    def resultado(self):
        if self.__jugado1_puntuacion > self.__jugado2_puntuacion:
            return "Gano Jugado 1"
        elif self.__jugado1_puntuacion < self.__jugado2_puntuacion:
            return "Gano Jugado 2"


jugado_Manos = PPT()
prueba1 = PPT()
intento = 0

# inicia el juego con 3 intento
while intento < 3:
    print("Escoge uno:\n")
    for i in jugado_Manos.getManos():
        print("-" + str(i))

    # Aqui ingresa con el arma que vas jugar, Si te equivoca se repetira hasta que sea solo con 3 armas
    while True:
        jugado = str(input("Ingrese: "))
        jugado = jugado_Manos.busca_arma(jugado)
        print(f"\n{jugado}")
        if jugado in jugado_Manos.getManos():
            break

    jugado2 = prueba1.bot()

    # Enseña la puntuacion de los jugadores con el metodo comparacion
    print(f"\n{jugado_Manos.comparacion(jugado, jugado2)}\n")

    # Comprueba si ninguno de los jugadores gana, si es asi resta un intento hasta gana
    if jugado_Manos.resultado() is None:
        intento -= 1

    intento += 1

print(jugado_Manos.resultado())
