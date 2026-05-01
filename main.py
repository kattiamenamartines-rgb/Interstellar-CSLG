import os
import time
from datetime import datetime

def pantalla_principal():
    os.system('clear' if os.name == 'posix' else 'cls')
    print("\033[1;32m") # Color Verde Interstellar
    print("  ______________________________________________________")
    print(" |                                                      |")
    print(" |            COLEGIO DE SAN LUIS GONZAGA               |")
    print(" |          - DEPARTAMENTO DE TECNOLOGÍA -              |")
    print(" |______________________________________________________|")
    print(" |                                                      |")
    print(" |                PROYECTO INTERSTELLAR                 |")
    print(" |       SISTEMA CENTRAL DE CONTROL Y GESTIÓN           |")
    print(" |______________________________________________________|")
    print("\033[0m")
    
    print(" [1] INICIAR MÓDULO DE DIAGNÓSTICO")
    print(" [2] VER ESTADO DE CONEXIÓN SATELITAL")
    print(" [3] CRÉDITOS DEL EQUIPO")
    print(" [4] SALIR")
    print("\n")

def ejecutar():
    while True:
        pantalla_principal()
        opcion = input(" Seleccione una opción de misión > ")
        
        if opcion == "1":
            print("\n [+] Analizando hardware... CPU: OK | RAM: OK")
            time.sleep(2)
        elif opcion == "2":
            print("\n [!] Buscando receptor... (Antena no detectada)")
            time.sleep(2)
        elif opcion == "3":
            print("\n --- EQUIPO INTERSTELLAR ---")
            print(" Diseñado por: Isaac David Mena")
            print(" Institución: Colegio de San Luis Gonzaga")
            input("\n Presione Enter para volver...")
        elif opcion == "4":
            print("\n Cerrando sistemas... ¡Hacia las estrellas!")
            break

if __name__ == "__main__":
    ejecutar()
