# ejercicio 1
# observaciones_lunes = ""
# observaciones_martes = ""
# observaciones_miercoles = ""
# observaciones_jueves = ""
# observaciones_viernes = ""

# dia = input("Ingrese el día de la semana (lunes, martes, miércoles, jueves o viernes): ")
# observacion = input("Ingrese la observación de la clase: ")

# if dia.lower() == "lunes":
#     observaciones_lunes += observacion + "\n"
# elif dia.lower() == "martes":
#     observaciones_martes += observacion + "\n"
# elif dia.lower() == "miércoles":
#     observaciones_miercoles += observacion + "\n"
# elif dia.lower() == "jueves":
#     observaciones_jueves += observacion + "\n"
# elif dia.lower() == "viernes":
#     observaciones_viernes += observacion + "\n"
# else:
#     print("Día no válido. Por favor, ingrese un día de la semana válido.")

# print("\nObservaciones de las clases:")
# print("Lunes:", observaciones_lunes)
# print("Martes:", observaciones_martes)
# print("Miércoles:", observaciones_miercoles)
# print("Jueves:", observaciones_jueves)
# print("Viernes:", observaciones_viernes)



# # ejercicio 2 
# fecha_input = input("Por favor, ingrese la fecha en formato día, DD/MM: ")

# parts = fecha_input.split(', ')
# if len(parts) != 2:
#     print("Error: Formato de entrada incorrecto.")
# else:
#     dia, fecha = parts
#     dia = dia.strip().capitalize()
#     dd, mm = fecha.split('/')
#     dd, mm = int(dd), int(mm)

#     # Verificar si el día de la semana es válido
#     dias_validos = ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado', 'Domingo']
#     if dia not in map(str.capitalize, dias_validos): 
#         print("Error: Día de la semana inválido.")
#     elif dd > 31 or dd < 1 or mm > 12 or mm < 1:
#         print("Error: Fecha inválida.")
#     else:
#         print("Fecha ingresada correctamente:", dia, dd, mm)

# # ejercicio 3
# fecha = input("Por favor, ingrese la fecha (DD/MM/AAAA): ")
# nivel = input("Indique el nivel del examen (inicial, intermedio o avanzado): ").lower()
# if nivel in ["inicial", "intermedio", "avanzado"]:
#     aprobados = int(input("Ingrese la cantidad de alumnos que aprobaron el examen: "))
#     total_alumnos = int(input("Ingrese el total de alumnos que realizaron el examen: "))
#     if total_alumnos > 0:
#         porcentaje_aprobados = (aprobados / total_alumnos) * 100
#         print(f"El porcentaje de aprobados es: {porcentaje_aprobados}%")
#     else:
#         print("No se ingresó un número válido de alumnos.")
# else:
#     print("Este nivel no tiene examen.")

# # ejercicio 4
# fecha = input("Por favor, ingrese la fecha (DD/MM/AAAA): ")

# practica_hablada = input("¿Fue un día de práctica hablada? (Si/No): ").lower()

# if practica_hablada == "si":
#     porcentaje_asistencia = float(input("Ingrese el porcentaje de asistencia a clase: "))
    
#     if porcentaje_asistencia > 50:
#         print("Asistió la mayoría.")
#     else:
#         print("No asistió la mayoría.")
# elif practica_hablada == "no":
#     nivel = input("Indique el nivel del examen (inicial, intermedio o avanzado): ").lower()
    

#     if nivel in ["inicial", "intermedio", "avanzado"]:

#         aprobados = int(input("Ingrese la cantidad de alumnos que aprobaron el examen: "))
#         total_alumnos = int(input("Ingrese el total de alumnos que realizaron el examen: "))

#         if total_alumnos > 0:
#             porcentaje_aprobados = (aprobados / total_alumnos) * 100
#             print(f"El porcentaje de aprobados es: {porcentaje_aprobados}%")
#         else:
#             print("No se ingresó un número válido de alumnos.")
#     else:
#         print("Este nivel no tiene examen.")
# else:
#     print("Respuesta inválida. Por favor, ingrese 'Sí' o 'No' para indicar si fue un día de práctica hablada.")

# ejercicio 5
# dia = 1
# mes = int(input("Ingrese el mes actual: "))

# if dia == 1 and (mes == 1 or mes == 7):
#     print("Comienzo de nuevo ciclo.")
    
#     alumnos_nuevo_ciclo = int(input("Ingrese la cantidad de alumnos del nuevo ciclo: "))
    
#     arancel_por_alumno = float(input("Ingrese el arancel en $ por cada alumno: "))
    
#     ingreso_total = alumnos_nuevo_ciclo * arancel_por_alumno
    
#     print(f"El ingreso total es: ${ingreso_total}")
# else:
#     print("No es el comienzo de un nuevo ciclo.")


