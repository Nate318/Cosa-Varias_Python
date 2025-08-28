# A)

CursoVisto = 1.5

CursosGenerales = [2.5,4.0,7.0]

CrudoCursoVisto = 3.5

CrudoPromedioCursosGenerales = 5

CursosGenerales.sort()

CursoMinimo = CursosGenerales[0]

CursoMaximo = CursosGenerales[-1]

CursoPromedio = CursosGenerales[-2]

print("------ Resultados ----")

print("Curso con menos horas:", CursoMinimo)
print("Curso con mas horas:", CursoMaximo)
print("Curso promedio:", CursoPromedio)

print("------- Diferencias porcentuales -------")

DiferenciaPorcentual1 = round(abs(CursoVisto - CursoMinimo) / CursoMinimo * 100,1)
DiferenciaPorcentual2 = round(abs(CursoMaximo - CursoVisto) / CursoMaximo * 100,1)
DiferenciaPorcentual3 = round(abs(CursoPromedio - CursoVisto) / CursoPromedio * 100,1)

print("------- Resultados de las diferencias porcentuales -------")

print(f"Diferencia porcentual con el curso con menos horas: {DiferenciaPorcentual1}%")
print(f"Diferencia porcentual con el curso con mas horas: {DiferenciaPorcentual2}%")
print(f"Diferencia porcentual con el curso promedio: {DiferenciaPorcentual3}%")

# B)

print("------ Resultados Crudos ----")

print("Crudo curso visto:", CrudoCursoVisto)
print("Crudo cursos generales:", CrudoPromedioCursosGenerales)

PorcentajeVisto = round(abs(CrudoCursoVisto - CursoVisto) / CrudoCursoVisto *100,1)
PorcentajeGenerales = round(abs(CrudoPromedioCursosGenerales - CursoPromedio) / CrudoPromedioCursosGenerales * 100, 1)

print("------- Resultados porcentuales -------")

print(f"Porcentaje Curso visto: {PorcentajeVisto}%")
print(f"Porcentaje Cursos generales: {PorcentajeGenerales}%")

# C)

print("------ Resultados de la comparacion ----")

print(f"Curso visto: {CursoVisto} horas del Curso Visto equivale a {CursoPromedio} horas del Curso Promedio.")

Comparacion = 4 * 10 * 10 // CursoVisto / 10

print(f"Comparacion: 10 horas del curso visto equivalen a {Comparacion} horas del curso promedio.")
