import os

#A) 
Personajes = list()

class Personaje:
    def __init__(self, nombre, salud, fuerza):
        self.nombre = nombre
        self.salud = salud
        self.fuerza = fuerza

    def __add__(self, other):
        if isinstance(other, Personaje):
            primer = len(self.nombre)//2
            segundo = len(other.nombre)//2
            return Personaje(self.nombre[:primer]+other.nombre[segundo-1:],
                             self.salud + other.salud,
                             round(((self.fuerza + other.fuerza)/2)**1.2))
        return NotImplemented

Goku = Personaje("Goku", 100, 50)
Vegeta = Personaje("Vegeta", 90, 60)

resultado = Goku + Vegeta
print(f"La fusion entre {Goku.nombre} y {Vegeta.nombre} es {resultado.nombre}, Salud: {resultado.salud}, Fuerza: {resultado.fuerza}")

#D)

def Crear_Personaje():
    nombre = input("Ingrese el nombre del personaje: \n")
    salud = int(input("Ingrese la salud del personaje: \n"))
    fuerza = int(input("Ingrese la fuerza del personaje: \n"))
    nuevo_personaje = Personaje(nombre, salud, fuerza)
    Personajes.append(nuevo_personaje)
    return f"Personaje creado con éxito."

def Fusionar_Personajes(personaje1, personaje2):
    fusion = personaje1 + personaje2
    return fusion

def Mostrar_Personajes():
    if not Personajes:
        print("No hay personajes para mostrar.")
    else:
        for personaje in Personajes:
            print(f"Nombre: {personaje.nombre}, Salud: {personaje.salud}, Fuerza: {personaje.fuerza}")
        
while True:
    print("1. Crear Personaje")
    print("2. Fusionar Personajes")
    print("3. Mostrar Personajes")
    print("4. Salir")
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        Crear_Personaje()
        os.system("Pause")
        os.system("cls")
    elif opcion == "2":
        if len(Personajes) < 2:
            print("Se necesitan al menos dos personajes para fusionar.")
            os.system("Pause")
            os.system("cls")
        else:
            print("Seleccione los personajes a fusionar:")
            for i, personaje in enumerate(Personajes):
                print(f"{i + 1}. {personaje.nombre}")
            
            try:
                seleccion1 = int(input("Seleccione el primer personaje: ")) - 1
            except ValueError:
                print("Selección inválida.")
                os.system("Pause")
                os.system("cls")
                continue
            try:
                seleccion2 = int(input("Seleccione el segundo personaje: ")) - 1
            except ValueError:
                print("Selección inválida.")
                os.system("Pause")
                os.system("cls")
                continue
            if 0 <= seleccion1 < len(Personajes) and 0 <= seleccion2 < len(Personajes):
                fusion = Fusionar_Personajes(Personajes[seleccion1], Personajes[seleccion2])
                Personajes.append(fusion)
                print(f"Fusión creada: {fusion.nombre}, Salud: {fusion.salud}, Fuerza: {fusion.fuerza}")
                os.system("Pause")
                os.system("cls")
            else:
                print("Selección inválida.")
                os.system("Pause")
                os.system("cls")
    elif opcion == "3":
        Mostrar_Personajes()
        os.system("Pause")
        os.system("cls")
    elif opcion == "4":
        print("Saliendo...")
        os.system("cls")
        break
    else:
        print("Opción no válida.")
        os.system("Pause")
        os.system("cls")