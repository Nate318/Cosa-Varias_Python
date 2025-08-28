#A)

class Persona:
    def __init__(self,nombre,edad):
        self.nombre = nombre
        self.edad = edad

    def mostrar_informacion(self):
        print(f"Nombre: {self.nombre} \nEdad: {self.edad}")
                
class Estudiante(Persona):
    def __init__(self,nombre,edad,grado):
        super().__init__(nombre,edad)
        self.grado = grado
        
    def GradoEstudiante(self):
        print(f"Grado: {self.grado}")

Estudiante = Estudiante("Juan", 20, "3ro")
Estudiante.mostrar_informacion()
Estudiante.GradoEstudiante()

#B)

class Animal:
    def comer(self):
        print("El animal está comiendo.")

class Mamifero(Animal):
    def amamantar(self):
        print("El mamífero está amamantando a su cría.")

class Ave(Animal):
    def volar(self):
        print("El ave está volando.")
        
class Murcielago(Mamifero,Ave):
    pass

buho = Murcielago()

buho.comer()
buho.amamantar()
buho.volar()

print(Murcielago.mro()) # Muestra el orden de resolución de métodos