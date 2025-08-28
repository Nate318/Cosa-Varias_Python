import random
import os

Jugadas = [" "," "," "," "," "," "," "," "," "] 
n = random.randrange(2)

def CrearTablero():
    for i in range(1,12):
        if i%4 == 0:
            print("-----------")
        elif i == 2:
            print(f" {Jugadas[0]} | {Jugadas[1]} |  {Jugadas[2]} ")
        elif i == 6:
            print(f" {Jugadas[3]} | {Jugadas[4]} |  {Jugadas[5]} ")
        elif i == 10:
            print(f" {Jugadas[6]} | {Jugadas[7]} |  {Jugadas[8]} ")
        else:
            print("   |   |   ")
            
def JugadaDelJugador():
    while True:
        if " " in Jugadas:
            try:  
                player = int(input("Ingrese una casilla (1-9): ")) - 1
                if player < 9 and player >= 0:
                    if Jugadas[player] == " ":
                        Jugadas[player] = "X"
                        break
                    else:
                        print("Ingrese una posicion vacia")
                        os.system("Pause")
                        os.system("cls")
                        CrearTablero()
                else:
                    print("Ingrese un numero entre los que se le pidio (1-9)")
                    os.system("Pause")
                    os.system("cls")
                    CrearTablero()
            except ValueError:
                print("Ingrese un numero entero :v")
                os.system("Pause")
                os.system("cls")
                CrearTablero()
        else:
            break
    
def JugadaDeLaMaquina():
    while True:
        cpu = random.randrange(9)
        if Jugadas[cpu] == " ":
            Jugadas[cpu] = "O"
            os.system("cls")
            CrearTablero()
            break
        elif " " not in Jugadas:
            break

def ElegirPlayer():
    if n == 0:
        JugadaDelJugador()
        if GanadorPlayer():
            os.system("cls")
            CrearTablero()
            print("Felicidades player tu ganas!!!!!")
            os.system("Pause")
            return
        JugadaDeLaMaquina()
        if GanadorMaquina():
            os.system("cls")
            CrearTablero()
            print("Perdiste player sigue intentando....")
            os.system("Pause")
    else:
        JugadaDeLaMaquina()
        if GanadorMaquina():
            os.system("cls")
            CrearTablero()
            print("Perdiste player sigue intentando....")
            os.system("Pause")
            return 
        JugadaDelJugador()
        if GanadorPlayer():
            os.system("cls")
            CrearTablero()
            print("Felicidades player tu ganas!!!!!")
            os.system("Pause")
        
def GanadorPlayer():
    if Jugadas[0] == "X" and Jugadas[0] == Jugadas[1] and Jugadas[0] == Jugadas[2]:
        return True
    elif Jugadas[3] == "X" and Jugadas[3] == Jugadas[4] and Jugadas[3] == Jugadas[5]:
        return True
    elif Jugadas[6] == "X" and Jugadas[6] == Jugadas[7] and Jugadas[6] == Jugadas[8]:
        return True
    elif Jugadas[0] == "X" and Jugadas[0] == Jugadas[3] and Jugadas[0] == Jugadas[6]:
        return True
    elif Jugadas[1] == "X" and Jugadas[1] == Jugadas[4] and Jugadas[1] == Jugadas[7]:
        return True
    elif Jugadas[2] == "X" and Jugadas[2] == Jugadas[5] and Jugadas[2] == Jugadas[8]:
        return True
    elif Jugadas[0] == "X" and Jugadas[0] == Jugadas[4] and Jugadas[0] == Jugadas[8]:
        return True
    elif Jugadas[2] == "X" and Jugadas[2] == Jugadas[4] and Jugadas[2] == Jugadas[6]:
        return True

def GanadorMaquina():
    if Jugadas[0] == "O" and Jugadas[0] == Jugadas[1] and Jugadas[0] == Jugadas[2]:
        return True
    elif Jugadas[3] == "O" and Jugadas[3] == Jugadas[4] and Jugadas[3] == Jugadas[5]:
        return True
    elif Jugadas[6] == "O" and Jugadas[6] == Jugadas[7] and Jugadas[6] == Jugadas[8]:
        return True
    elif Jugadas[0] == "O" and Jugadas[0] == Jugadas[3] and Jugadas[0] == Jugadas[6]:
        return True
    elif Jugadas[1] == "O" and Jugadas[1] == Jugadas[4] and Jugadas[1] == Jugadas[7]:
        return True
    elif Jugadas[2] == "O" and Jugadas[2] == Jugadas[5] and Jugadas[2] == Jugadas[8]:
        return True
    elif Jugadas[0] == "O" and Jugadas[0] == Jugadas[4] and Jugadas[0] == Jugadas[8]:
        return True  
    elif Jugadas[2] == "O" and Jugadas[2] == Jugadas[4] and Jugadas[2] == Jugadas[6]:
        return True

def Juego():
    
    while True:
        CrearTablero()
        ElegirPlayer()
        if GanadorMaquina() or GanadorPlayer():
            break
        elif " " not in Jugadas:
            os.system("cls")
            CrearTablero()
            print("Empate bien jugado....")
            os.system("Pause")
            break    
        os.system("cls")
    
Juego()

