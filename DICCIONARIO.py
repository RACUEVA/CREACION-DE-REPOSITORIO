# Crear un diccionario con información personal ficticia
informacion_personal = {
    "Nombre": "Ronal",
    "Edad": 32,
    "Ciudad": "Tena",
}


# Acceder al valor asociado con la clave "ciudad" y modificarlo
informacion_personal["Ciudad"] = "Puyo"

# Agregar una nueva clave-valor que represente la "profesion" de la persona
informacion_personal["Profesion"] = "Estudiante"

# Verificar si la clave "telefono" existe y agregarla si no existe
if "Telefono" not in informacion_personal:
    informacion_personal["Telefono"] = "1234567890"

# Eliminar la clave "edad" del diccionario
if "Edad" in informacion_personal:
    del informacion_personal["Edad"]

# Imprimir el diccionario final
print (informacion_personal)

