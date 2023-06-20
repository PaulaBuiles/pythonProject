import random


def gamePPT(user):
    """
    Juega una ronda de piedra, papel o tijera contra Python, en la que podrás apostar y ganar dinero.

    Argumentos:
        user (int): La elección del usuario (1 para papel, 2 para tijera, 3 para piedra).
    Returns:
        int: El resultado de la ronda (0 para empate, 1 para victoria del usuario, -1 para victoria de Python).
    """
    choices = ["piedra", "papel", "tijera"]
    choicePython = random.choice(choices)

    if user == 1:
        choiceUser = "piedra"
    elif user == 2:
        choiceUser = "papel"
    elif user == 3:
        choiceUser = "tijera"
    else:
        print("Opción inválida.")
        return

    print("Tu elección:", choiceUser)
    print("Elección de Python:", choicePython)

    if choiceUser == choicePython:
        print("Empate!")
        return 0
    elif (choiceUser == "papel" and choicePython == "piedra"):
        print("¡El papel elimina la piedra!")
        return 1
    elif (choiceUser == "tijera" and choicePython == "papel"):
        print("¡La tijera corta el papel!")
        return 1
    elif (choiceUser == "piedra" and choicePython == "tijera"):
        print("¡La piedra rompe la tijera!")
        return 1
    else:
        print("Perdiste. Python gana.")
        return -1


# Pedir la cantidad de apuesta al inicio
bet = float(input("Ingresa la cantidad que deseas apostar: "))
if bet <= 0:
    print("La cantidad apostada debe ser mayor que cero.")
    exit()

# Juego principal
balance = bet

while True:
    # Pedir la entrada al usuario
    entradaUsuario = int(input("Elige una opción: 1 - papel, 2 - tijera, 3 - piedra: "))
    # Jugar al juego (se le manda la elección del usuario)
    resultado = gamePPT(entradaUsuario)

    if resultado == 0:
        print("No ganas ni pierdes dinero.")
    elif resultado == 1:
        print("Ganaste, suma $2000.")
        balance += 2000
    else:
        print("Perdiste, resta $2000.")
        balance -= 2000

    print("Monto actual: $", balance)

    if balance <= 0:
        print("Te quedaste sin dinero. Juego terminado.")
        break
    else:
        respuesta = input("¿Quieres seguir jugando? (si/no): ")
        if respuesta.lower() != "si":
            break

print("Monto final: $", balance)
