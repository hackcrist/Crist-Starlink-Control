#!/usr/bin/env python3
import requests
import time
import os
import json
from colorama import Fore, Style, init
from pyfiglet import Figlet

init(autoreset=True)

ROUTER_URL = "http://192.168.100.1"

def banner():
    os.system("clear")
    f = Figlet(font="slant")
    print(Fore.CYAN + f.renderText("Crist Starlink"))
    print(Fore.YELLOW + "🌐 Herramienta de control para sistemas Starlink")
    print(Fore.GREEN + "By Crist Hack - Solo uso ético")
    print("-" * 60)

def ver_estado():
    try:
        response = requests.get(f"{ROUTER_URL}/status", timeout=5)
        data = response.json()
        dish = data.get("dish", {})
        obstruction = dish.get("obstruction_stats", {}).get("fraction_obstructed", 0)
        print(Fore.CYAN + f"📶 Estado: {dish.get('state', 'Desconocido')}")
        print(Fore.CYAN + f"🕒 Uptime: {dish.get('uptime', 0)} segundos")
        print(Fore.CYAN + f"🌫️ Obstrucción: {obstruction*100:.2f}%")
    except Exception as e:
        print(Fore.RED + f"❌ Error al obtener estado: {e}")

def reiniciar_router():
    print(Fore.YELLOW + "♻️ Reiniciando router Starlink...")
    # Nota: Este endpoint no está público. Se simula la opción.
    print(Fore.GREEN + "✅ Reinicio simulado (agregar endpoint real si se habilita)")

def ver_latencia():
    print(Fore.CYAN + "📡 Probando latencia con ping a 8.8.8.8...")
    result = os.popen("ping -c 4 8.8.8.8").read()
    print(Fore.GREEN + result)

def guardar_log():
    try:
        response = requests.get(f"{ROUTER_URL}/status", timeout=5)
        data = response.json()
        timestamp = time.strftime("%Y-%m-%d_%H-%M")
        with open(f"logs/starlink_log_{timestamp}.txt", "w") as file:
            json.dump(data, file, indent=4)
        print(Fore.GREEN + f"✅ Log guardado como logs/starlink_log_{timestamp}.txt")
    except Exception as e:
        print(Fore.RED + f"❌ No se pudo guardar el log: {e}")

def modo_diagnostico():
    banner()
    ver_estado()
    print(" " * 3)
    ver_latencia()
    print(" " * 3)
    guardar_log()

def menu():
    while True:
        banner()
        print(Fore.MAGENTA + "1) Ver estado del sistema")
        print("   " * 2 + "2) Reiniciar router")
        print("   " * 2 + "3) Ver latencia de red")
        print("   " * 2 + "4) Guardar log actual")
        print("   " * 2 + "5) Modo diagnóstico completo")
        print("   " * 2 + "6) Salir")
        print("-" * 60)
        print(Fore.YELLOW + "⭐ Si te gusta el proyecto, regálame una estrella en GitHub")
        print("💸 O apóyame con una donación: miniosjuan89@gmail.com (PayPal)")
        print("-" * 60)
        choice = input("👉 Selecciona una opción: ")

        if choice == '1':
            ver_estado()
        elif choice == '2':
            reiniciar_router()
        elif choice == '3':
            ver_latencia()
        elif choice == '4':
            guardar_log()
        elif choice == '5':
            modo_diagnostico()
        elif choice == '6':
            print(Fore.RED + "👋 Saliendo...")
            break
        else:
            print(Fore.RED + "❌ Opción inválida")
        input(Fore.YELLOW + "\nPresiona ENTER para continuar...")

menu()
