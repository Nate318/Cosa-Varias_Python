import re

#A)
numero = int(input("Introduce un número entero de cinco cifras: "))
len_numero = 5
if len_numero != 5:
    print("El número no tiene cinco cifras.")
else:
    digito1 = numero % 10
    numero //= 10
    digito2 = numero % 10
    numero //= 10
    digito3 = numero % 10
    numero //= 10
    digito4 = numero % 10
    numero //= 10
    digito5 = numero % 10
    Suma_1 = digito5 + digito4 + digito3
    Suma_2 = digito3 + digito2 + digito1
    print("La suma de los primeros tres dígitos es:", Suma_1)
    print("La suma de los últimos tres dígitos es:", Suma_2)
    print("La suma de los dos resultados es:", Suma_1 + Suma_2)

#B)

numero = int(input("Introduce un numero entero positivo: "))

if numero <1000:
    print("El número es menor que 1000.")
else:
    
    cifras = 0
    aux = numero
    
    while aux > 0:
        aux //= 10
        cifras += 1
        
    aux = numero
    aux2 = cifras
    mayor = 0
    contAux = 1
    
    while aux2 > 0:
        digito = aux % 10
        aux //= 10
        if digito > mayor:
            mayor = digito
        elif digito == mayor: 
            contAux += 1
        aux2 -= 1
        
    new_num = 0
    
    band = False    
    if contAux == cifras:
        band = True
    
    fact = 1
    
    while cifras > 0:
        digito = numero % 10
        numero //= 10
        if digito == mayor:
            pass
        else:
            new_num = new_num + digito*fact
            fact *= 10
        cifras -= 1
    
    if band:
        print("Todos los dígitos son iguales. No se puede formar un nuevo número.")
    else:
        print("El nuevo número es:", new_num)
        
#C)

class Diccionario:
    def __init__(self):
        self.Dia = ""
        self.Temperatura = list()
        self.Apariciones = list()
        
    def __str__(self):
        return f"Dia: {self.Dia}, Temperatura: {self.Temperatura}, Apariciones: {self.Apariciones}"
    
    def __repr__(self):
        return self.__str__()

Orden_dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
Dias = list()
lista = list()

with open("Archivos\\TEMPERATURAS.txt", "r") as archivo:
    contenido = archivo.read()
    patron = r"-?\d+\.?\d*[LMJSVD][UAIO]"

    resultados = re.findall(patron, contenido)
    
for i,resultado in zip(range(len(resultados)), resultados):
    Numeros = re.findall(r"-?\d+\.?\d*", resultado)
    Abreviacion = re.findall(r"[LMJSVD][UAIO]", resultado)
    Temperatura = Numeros[0]

    for dia, abreviacion in zip(Orden_dias, ["LU", "MA", "MI", "JU", "VI", "SA", "DO"]):
        if Abreviacion == [abreviacion]:
            Dia = dia
            break

    if not lista:
        dic = Diccionario()
        dic.Dia = Dia
        dic.Temperatura.append(Temperatura)
        dic.Apariciones.append(1)
        lista.append(dic)
        Dias.append(Dia)
    else:
        for item in lista:
            if Dia in Dias:
                if item.Dia == Dia:
                    if Temperatura in item.Temperatura:
                        item.Apariciones[item.Temperatura.index(Temperatura)] += 1
                        break
                    else:
                        item.Temperatura.append(Temperatura)
                        item.Apariciones.append(1)
                        break
            else: 
                dic = Diccionario()
                dic.Dia = Dia
                dic.Temperatura.append(Temperatura)
                dic.Apariciones.append(1)
                lista.append(dic)
                Dias.append(Dia)
                break

lista.sort(key=lambda x: Orden_dias.index(x.Dia))

for item in lista:
    print(item)