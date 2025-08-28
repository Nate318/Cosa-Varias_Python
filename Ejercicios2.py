# A)

def obtener_compañeros(cantidad):
    compañeros = list()
    for i in range(cantidad):
        
        nombre = input(f"Ingrese el nombre del compañero {i + 1}: ")
        edad = int(input(f"Ingrese la edad del compañero {i + 1}: "))
        compañero = (nombre, edad)
        compañeros.append(compañero)
        
    compañeros.sort(key=lambda x: x[1])
    profesor = compañeros[-1][0]
    asistente = compañeros[0][0]
    return profesor, asistente

Exponente = lambda x,y: x ** y

Resultado = Exponente(5,20)

print(Resultado)

profesor,asistente = obtener_compañeros(1)

print(f"El asistente es: {asistente} y el profesor es: {profesor}")

# B) 

def Primos(n):
    primos = list()
    
    for i in range(n):
        if i < 2:
            continue
        es_primo = True
        for j in range(2,int(i**0.5)+1):
            if i % j == 0 and i != j:
                es_primo = False
                break
        if es_primo:
            primos.append(i)
    return primos

primos = Primos(100)

print("Los números primos hasta 100 son:")
print(primos)

# C)

def Fibonacci(n):
    
    Sucesion = [0,1]
    while len(Sucesion) < n:
        siguiente = Sucesion[-1] + Sucesion[-2]
        Sucesion.append(siguiente)
    return Sucesion

n = int(input("Ingrese el número de términos de la sucesión de Fibonacci: "))
fibonacci = Fibonacci(n)

print(f"La sucesión de Fibonacci hasta {n} términos es:")
print(fibonacci)