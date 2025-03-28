import ast

# Función para cargar datos desde el archivo
def cargar_datos():
    with open(r"alumnos.txt", "r") as archivo:
            contenido = archivo.read()
            return ast.literal_eval(contenido) if contenido else {"Alumnos": []}

# Función para guardar datos en el archivo
def guardar_datos(datos):
    with open(r"alumnos.txt", "w") as archivo:
        archivo.write(str(datos))

# Cargar datos existentes
datos = cargar_datos()

dnis = [alumno["dni"] for alumno in datos["Alumnos"]]


# Pregunta si quiere agregar un nuevo alumno
pregunta = input("Quiere agregar un nuevo alumno?: ").lower()
while pregunta == "si":
    auxnotas = []
    nom = input("Ingrese el nombre del nuevo alumno: ")
    ap = input("Ingrese el apellido del nuevo alumno: ")
    DNI = int(input("Ingrese el DNI del nuevo alumno: "))
    while DNI in dnis:
        DNI = int(input("El DNI ya existe, ingrese otro: "))
    dnis.append(DNI)
    fecha_de_nac = input("Ingrese la fecha de nacimiento (dd/mm/aaaa): ")
    tutor = input("Ingrese el nombre y apellido del tutor: ")
    
    for i in range(6):
        nota = int(input(f"Ingrese la nota {i+1}: "))
        auxnotas.append(nota)
    
    faltas = int(input("Ingrese la cantidad de faltas: "))
    amonestaciones = int(input("Ingrese la cantidad de amonestaciones: "))
    
    nuevo_alumno = {
        "nombre": nom,
        "apellido": ap,
        "dni": DNI,
        "fecha de nacimiento": fecha_de_nac,
        "tutor": tutor,
        "notas": auxnotas,
        "faltas": faltas,
        "amonestaciones": amonestaciones
    }
    datos["Alumnos"].append(nuevo_alumno)
    guardar_datos(datos)
    pregunta = input("Quiere agregar un nuevo alumno?: ").lower()

# Pregunta si quiere editar algún dato
pregunta = input("Quieres cambiar el dato de algún alumno?: ").lower()
while pregunta == "si":
    auxpreg = int(input("De qué alumno (índice)?: ")) - 1
    auxpreg2 = input("Qué dato quieres cambiar?: ").lower()
    if auxpreg2 == "notas":
        auxnotas = [int(input(f"Ingrese la nota {i+1}: ")) for i in range(6)]
        datos["Alumnos"][auxpreg][auxpreg2] = auxnotas
    elif auxpreg2 == "dni":
        DNI = int(input("Ingrese el nuevo DNI: "))
        while DNI in dnis:
            DNI = int(input("El DNI ya existe, ingrese otro: "))
        dnis.append(DNI)
        datos["Alumnos"][auxpreg][auxpreg2] = DNI
    else:
        datos["Alumnos"][auxpreg][auxpreg2] = input("Ingresa el nuevo dato: ")
    guardar_datos(datos)
    pregunta = input("Quieres cambiar otro dato?: ").lower()

# Pregunta si desea eliminar a algún alumno
pregunta = input("Desea eliminar a un alumno?: ").lower()
while pregunta == "si":
    auxpreg3 = int(input("Qué alumno desea eliminar (índice)?: ")) - 1
    if 0 <= auxpreg3 < len(datos["Alumnos"]):
        dnis.remove(datos["Alumnos"][auxpreg3]["dni"])
        del datos["Alumnos"][auxpreg3]
        guardar_datos(datos)
    pregunta = input("Desea eliminar otro alumno?: ").lower()

# Mostrar alumnos
for x, alumno in enumerate(datos["Alumnos"], 1):
    print(f"El alumno {x} es {alumno}")

