# Escritura de Archivo de Texto
# Crear un nuevo archivo llamado my_notes.txt y escribir en él
with open("my_notes.txt", "w") as file:  # Abrir el archivo en modo de escritura
    file.write("Esta es mi primera nota.\n")  # Escribir la primera línea
    file.write("Hoy aprendí sobre archivos en Python.\n")  # Escribir la segunda línea
    file.write("Espero seguir aprendiendo más.\n")  # Escribir la tercera línea

# Lectura de Archivo de Texto
# Abrir el archivo my_notes.txt para leer su contenido
with open("my_notes.txt", "r") as file:  # Abrir el archivo en modo de lectura
    # Leer el contenido línea por línea
    for line in file:  # Iterar sobre cada línea en el archivo
        print(line.strip())  # Mostrar cada línea leída, eliminando espacios en blanco

# El archivo se cierra automáticamente al salir del bloque with