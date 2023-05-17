import random

# Función que muestra las cartas del jugador y su puntuación actual
def mostrar_cartas_jugador(cartas_jugador, puntuacion_jugador):
    print("Tus cartas son:")
    for carta in cartas_jugador:
        print(carta)
    print("Tu puntuación es:", puntuacion_jugador)

# Función que muestra la primera carta del crupier y su puntuación parcial
def mostrar_carta_crupier(cartas_crupier):
    print("La primera carta del crupier es:")
    print(cartas_crupier[0])
    print("La puntuación parcial del crupier es:", valor_carta(cartas_crupier[0]))

# Función que devuelve el valor de una carta
def valor_carta(carta):
    if carta in ["J", "Q", "K"]:
        return 10
    elif carta == "A":
        return 11
    else:
        return int(carta)

# Función que reparte una carta aleatoria de la baraja
def repartir_carta(baraja):
    return baraja.pop(random.randint(0, len(baraja)-1))

# Función que pide al jugador que elija entre plantarse o pedir otra carta
def pedir_decision():
    while True:
        decision = input("¿Quieres otra carta (p) o te plantas (s)? ")
        if decision in ["p", "s"]:
            return decision
        else:
            print("Por favor, introduce 'p' o 's'.")

# Función que juega una ronda
def jugar_ronda(baraja):
    # Inicializamos las variables de la ronda
    cartas_jugador = [repartir_carta(baraja), repartir_carta(baraja)]
    puntuacion_jugador = sum([valor_carta(carta) for carta in cartas_jugador])
    cartas_crupier = [repartir_carta(baraja), repartir_carta(baraja)]
    puntuacion_crupier = valor_carta(cartas_crupier[0])

    # Mostramos las cartas del jugador y del crupier
    mostrar_cartas_jugador(cartas_jugador, puntuacion_jugador)
    mostrar_carta_crupier(cartas_crupier)

    # Turno del jugador
    while True:
        decision = pedir_decision()
        if decision == "p":
            nueva_carta = repartir_carta(baraja)
            cartas_jugador.append(nueva_carta)
            puntuacion_jugador += valor_carta(nueva_carta)
            mostrar_cartas_jugador(cartas_jugador, puntuacion_jugador)
            if puntuacion_jugador > 21:
                print("Te has pasado de 21. ¡Has perdido!")
                return -1
        else:
            break

    # Turno del crupier
    while puntuacion_crupier < 17:
        nueva_carta = repartir_carta(baraja)
        cartas_crupier.append(nueva_carta)
        puntuacion_crupier += valor_carta(nueva_carta)

    # Mostramos las cartas del jugador y del crupier y comprobamos el resultado
    print("Las cartas del crupier son:")
    for carta in cartas_crupier:
        print(carta)
    print("La puntuación del crupier es:", puntuacion_crupier)

    # Comprobamos el resultado
    if puntuacion_crupier > 21:
        print("El crupier se ha pasado de 21. ¡Has ganado!")
        return 1
    elif puntuacion_jugador > puntuacion_crupier:
        print("¡Has ganado!")
        return 1
    elif puntuacion_jugador == puntuacion_crupier:
        print("Empate")
        return 0
    else:
        print("Has perdido")
        return -1

# Función principal del juego
def jugar_veintiuno():
    print("Bienvenido a Blackjack")
    while True:
        decision = input("¿Quieres jugar una ronda de Blackjack? (s/n) ")
        if decision == "s":
            baraja = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"] * 4
            resultado = jugar_ronda(baraja)
            if resultado == -1:
                print("Has perdido la ronda.")
            elif resultado == 0:
                print("La ronda terminó en empate.")
            else:
                print("¡Has ganado la ronda!")
        else:
            print("Gracias por jugar a Blackjack. ¡Hasta pronto!")
            break

# Iniciar el juego
jugar_veintiuno()
