# 🌐 Crist-Starlink-Control v1.0
Herramienta profesional en Python para auditar, monitorear y administrar sistemas Starlink desde consola (Linux o Termux).
---

## 🚀 ¿Qué hace esta herramienta?

✅ Ver el estado del sistema Starlink  
    📶 Estado de conexión  
    🕒 Tiempo de actividad  
    🌫️ Porcentaje de obstrucción  

✅ Reiniciar el router Starlink (simulado, preparado para endpoint real)  

✅ Ver latencia actual con prueba de ping  
    📡 Ping automático a Google  

✅ Guardar logs técnicos con fecha y hora  
    📁 Logs en carpeta `/logs` en formato `.txt`  

✅ Ejecutar modo diagnóstico completo  
    🔎 Ejecuta todos los análisis uno tras otro  

---

## 🛠️ Requisitos

```bash
pip install requests colorama pyfiglet
```

---

## 📦 Instalación desde GitHub

```bash
git clone https://github.com/hackcrist/Crist-Starlink-Control.git

cd Crist-Starlink-Control

bash install.sh
```

---

## 🧪 Comandos disponibles

```bash
1️⃣   Ver estado del sistema  
    📶 Muestra si Starlink está conectado  
    🕒 Uptime (tiempo en línea)  
    🌫️ Porcentaje de obstrucción  

2️⃣   Reiniciar router (simulado)  
    ♻️ Prepara función para futuro endpoint real de reinicio  

3️⃣   Ver latencia de red  
    📡 Realiza ping a 8.8.8.8 y muestra promedio  

4️⃣   Guardar log actual  
    📝 Crea archivo JSON con datos técnicos en `/logs`  

5️⃣   Modo diagnóstico completo  
    🔎 Ejecuta estado + ping + guardado de log en un paso  

6️⃣   Salir del programa  
    ❌ Cierra el menú y termina la ejecución
```

---

## ❤️ Apoya el proyecto

⭐ Si te gusta este repositorio, regálame una estrella en GitHub  
💸 O una donación a: **miniosjuan89@gmail.com** (PayPal)

---

By Crist Hack - Solo para uso ético  
Licencia Apache 2.0
