#A)

def dibujar(n):
    for i in range(1,n+1):
        lista = list(x for x in range(1,i+1))
        print(*lista)
    for i in range(n-1,0,-1):
        lista = list(x for x in range(1,i+1))
        print(*lista)

n = int(input("Ingrese un numero entero positivo: "))    
dibujar(n)

#B)

notas = []

for i in range(10):
    n = float(input(f"Ingrese la nota {i+1}: "))
    notas.append(n)

notas.sort()

promedio = sum(notas) / len(notas)

print("-" * 16)
print(f"{'Notas':>10}")
print("-" * 16)

for nota in notas:
    print(f"{nota:>10.2f}")

print("-" * 16)
print(f"{'Promedio':<10}{promedio:>6.2f}")

