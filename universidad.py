# Definir la lista de cursos
cursos = [
    {"id": 1, "nombre": "Matemáticas", "profesor": "Dr. Pérez", "estudiantes": []},
    {"id": 2, "nombre": "Historia", "profesor": "Lic. Gómez", "estudiantes": []},
    {"id": 3, "nombre": "Programación", "profesor": "Ing. Rodríguez", "estudiantes": []}
]

# Definir la lista de estudiantes
estudiantes = [
    {"id": 101, "nombre": "Carlos López", "cursos": [
        {"id_curso": 1, "notas": [80, 90, 85], "horario": "Lunes y Miércoles 10:00 AM"}
    ]},
    {"id": 102, "nombre": "María Torres", "cursos": [
        {"id_curso": 2, "notas": [75, 88, 92], "horario": "Martes y Jueves 2:00 PM"}
    ]}
]

# Función para matricular un estudiante en un curso
def matricular_estudiante(id_estudiante, id_curso, horario):
    estudiante = next((e for e in estudiantes if e["id"] == id_estudiante), None)
    curso = next((c for c in cursos if c["id"] == id_curso), None)

    if estudiante and curso:
        estudiante["cursos"].append({"id_curso": id_curso, "notas": [], "horario": horario})
        curso["estudiantes"].append(estudiante["nombre"])
        print(f"{estudiante['nombre']} se ha matriculado en {curso['nombre']}.")
    else:
        print("Error: Estudiante o curso no encontrado.")

# Función para calcular el promedio de notas de un estudiante
def calcular_promedio(id_estudiante):
    estudiante = next((e for e in estudiantes if e["id"] == id_estudiante), None)
    
    if estudiante:
        total_notas = 0
        cantidad_notas = 0
        for curso in estudiante["cursos"]:
            total_notas += sum(curso["notas"])
            cantidad_notas += len(curso["notas"])
        
        promedio = total_notas / cantidad_notas if cantidad_notas > 0 else 0
        print(f"El promedio de {estudiante['nombre']} es: {promedio:.2f}")
    else:
        print("Estudiante no encontrado.")

# Función para listar estudiantes en un curso específico
def listar_estudiantes_curso(id_curso):
    curso = next((c for c in cursos if c["id"] == id_curso), None)
    
    if curso:
        print(f"\nEstudiantes matriculados en {curso['nombre']}:")
        for estudiante in curso["estudiantes"]:
            print(f"- {estudiante}")
    else:
        print("Curso no encontrado.")

# Agregar un nuevo estudiante y matricularlo en un curso
nuevo_estudiante = {"id": 103, "nombre": "Luis Ramírez", "cursos": []}
estudiantes.append(nuevo_estudiante)
matricular_estudiante(103, 3, "Viernes 3:00 PM")

# Calcular el promedio de notas de un estudiante
calcular_promedio(101)

# Listar todos los estudiantes de un curso específico
listar_estudiantes_curso(3)
