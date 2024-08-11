import random, os

def selec_mov_maquina():
    mov_m = random.randint(1,3)
    return mov_m

def check_ganador_turno(mov, mov_m, cont_j, cont_m):

    matriz_decision = [[1,2,0],[0,1,2],[2,0,1]]
    ganador = ''
    
    pos = [mov_m-1, mov-1]

    if matriz_decision[pos[0]][pos[1]] == 0:
        cont_m += 1
        ganador = 'Maquina'
    elif matriz_decision[pos[0]][pos[1]] == 1:
        ganador = "Empate"
    else:
        cont_j += 1
        ganador = "Jugador"

    return cont_j, cont_m, ganador

def main():

    os.system('cls')
    cont_j = 0
    cont_m = 0
    
    diccionario_movimientos = {1:"piedra", 2:"papel", 3:"tijera"}

    print("\nSeleccione total de rondas")
    rondas = int(input("--> "))
    os.system('cls')

    while (cont_j < rondas) and (cont_m < rondas):
        
        print("\nSeleccione una de los siguientes movimientos")
        print("1 --> piedra\n2 --> papel\n3 --> tijera\n")

        mov = int(input("--> "))
        os.system('cls')

        while mov not in diccionario_movimientos.keys():
            print("\nIngrese un movimiento valido")
            mov = int(input("--> "))
            os.system('cls')

        mov_m = selec_mov_maquina()

        cont_j, cont_m, ganador = check_ganador_turno(mov, mov_m, cont_j, cont_m)

        print(f"Movimiento jugador: {diccionario_movimientos[mov]}")
        print(f"Movimiento maquina: {diccionario_movimientos[mov_m]}")
        print(f"\npuntos jugador: {cont_j}")
        print(f"puntos maquina: {cont_m}")
        print(f"\nGanador ronda: {ganador}")
    
    os.system('cls')
    print(f"\npuntos jugador: {cont_j}")
    print(f"puntos maquina: {cont_m}")

    if cont_j == rondas:
        print("\nEl jugador gano la partida!\n")
    else:
        print("\nLa maquina gano la partida!\n")

main()