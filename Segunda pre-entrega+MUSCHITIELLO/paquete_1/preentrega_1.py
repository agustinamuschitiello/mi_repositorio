ruta ="/drive/MyDrive/"

archivo = "/primera_preentrega_Muschitiello.json"

import json

base_de_datos = {}

with open(ruta + "/primera_preentrega_Muschitiello.json", "w") as file:
  json.dump(base_de_datos, file, indent=4)

def abrir_archivo(base_de_datos):   
  with open(ruta + "/primera_preentrega_Muschitiello.json", "r") as file:   
    base_de_datos = json.load(file)   
    return base_de_datos   

def guardar(base_de_datos):
  with open(ruta + "/primera_preentrega_Muschitiello.json", "r") as file:   
    json.dump(base_de_datos, file, indent=4)

def registrar_usuario(base_de_datos):
    usuario = input("Ingresa el nombre de usuario: ")
    if usuario in base_de_datos:
      print("El usuario ya existe en la base de datos.")
    else:
      contraseña = input("Ingresa la contraseña: ")
      base_de_datos[usuario] = contraseña
      print("Registro exitoso.")
    with open(ruta + '/primera_preentrega_Muschitiello.json', 'w') as archivo:
        json.dump(base_de_datos, archivo)

def iniciar_sesion(base_de_datos):
    usuario = input("Introduzca el nombre de usuario: ")
    if usuario in base_de_datos:
        contraseña = input("Introduzca la contraseña: ")
        if base_de_datos[usuario] == contraseña:
            print("Inicio de sesión exitoso.")
        else:
            print("Contraseña incorrecta.")
    else:
        print("El usuario no existe en la base de datos.")

def mostrar_usuarios(base_de_datos):
    with open(ruta + "/primera_preentrega_Muschitiello.json", 'r') as archivo:
        base_de_datos = json.load(archivo)
        print("Usuarios y contraseñas almacenados: ")
        for usuario, contraseña in base_de_datos.items():
            print(f"Usuario: {usuario} | Contraseña: {contraseña}")

while True:
    print('Bienvenido al programa de gestión de usuarios.\nSelecciona una opción:\n1. Registrar un nuevo usuario.\n2. Mostrar todos los usuarios registrados.\n3. Iniciar sesión.\n4. Salir del programa.')
    opcion = input('Opción seleccionada: ')
    if opcion == '1':
        registrar_usuario(base_de_datos)
        break
    elif opcion == '2':
        mostrar_usuarios(base_de_datos)
        break
    elif opcion == '3':
        iniciar_sesion(base_de_datos)
        break
    elif opcion == '4':
        print("¡Hasta luego!")
        break
    else:
        print('Opción no válida. Intente de nuevo.')
        