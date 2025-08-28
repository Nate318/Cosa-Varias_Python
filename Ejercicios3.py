#A)

nombres = ["Ana", "Luis", "Pedro", "María", "Juan"]
apellidos = ["Gómez", "Pérez", "López", "Martínez", "Sánchez"]

with open("Archivos\\nombres.txt", "w",encoding = "UTF-8") as arch:
    arch.writelines("Los datos son: \n\n")
    arch.writelines(f"Nombre: {n}\nApellido: {a}\n-------------- \n" for n, a in zip(nombres, apellidos))
    
