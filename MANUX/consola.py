#!/usr/bin/env python3  # Cambiar al directorio especificado

import tkinter as tk

from tkinter import ttk

import subprocess

import os
from datetime import date

from tkinter import *

from tkinter import *
from tkinter.ttk import *

today = date.today()
current_date =today.strftime("%d/%B/%Y")
prompt =str(current_date) +">>>Mi_Terminal_Matrix:$"
test = "--------------------"


def cerrar_ventana():
    ventana.destroy()


# Función para ejecutar el comando ingresado por el usuario

def ejecutar_comando(comando):
    comando = comando.strip()  # Eliminar espacios en blanco alrededor del comando

    partes =comando.split()  # Dividir el comando en partes
    

    if not comando:  # Si el comando está en blanco
	
    	return "\n"
        

    elif comando == "clear":
        salida_texto.delete("end-80l linestart", tk.END)
        return "\n"

    elif partes[0] == "cd":  # Si el primer argumento es 'cd'
	
        if len(partes) == 1:  # Si solo se escribió 'cd' sin argumentos
		
            directorio = os.path.expanduser("~")  # Cambiar al directorio de inicio del usuario
            
        

        else:

            directorio = partes[1]  # Cambiar al directorio especificado

        try:

            os.chdir(directorio)  # Cambiar de directorio en el proceso principal

            return "\n"  # No hay salida para el comando 'cd'

        except FileNotFoundError:

            return f"El directorio '{directorio}' no existe.\n"

    else:

        try:

            resultado = subprocess.check_output(comando, shell=True, stderr=subprocess.STDOUT)

            return resultado.decode("utf-8")  # Ejecutar el comando en una shell

        except subprocess.CalledProcessError as e:

            return f"\n Orden «{comando}» no encontrado."
    

# Función para procesar el comando ingresado por el usuario

def procesar_comando(event=None):
    comando_prompt = salida_texto.get("end -2l linestart", tk.END).strip()
    comando_prompt = comando_prompt.split("$")
    
    comando = comando_prompt[1]  # Obtener el comando de la última línea
    

    if comando.lower() == "exit":
        cerrar_ventana()

        return

    resultado = ejecutar_comando(comando)

    if resultado:  # Solo imprimir si hay resultado

        salida_texto.insert(tk.END,"\n"+ str(resultado)+str(prompt))
        return

    # Limpiar el área de entrada

    salida_texto.delete("end-1l linestart", tk.END)


# Crear una ventana

ventana = tk.Tk()

# Establecer el tamaño de la ventana

ventana.geometry("1330x745")

# Establecer el título de la ventana

ventana.title("Proyecto Terminal")

# Configurar el estilo para que se parezca a una terminal

style = ttk.Style()

style.configure("BW.TLabel", foreground="white", background="black")  # Texto blanco sobre fondo negro

style.configure("BW.TButton", foreground="black", background="white")  # Botón con texto negro sobre fondo blanco

# Marco para el área de salida de texto con barra de desplazamiento

marco_texto = tk.Frame(ventana)

marco_texto.pack(fill=tk.BOTH, expand=True)

# Área de salida de texto
salida_texto = tk.Text(marco_texto, bg="black", fg="green", wrap="word")
salida_texto.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
salida_texto.insert(tk.END,str(prompt))

# Vincular la tecla "Enter" para procesar el comando
salida_texto.bind("<Return>", procesar_comando)

# Botón para cerrar la ventana

boton_cerrar = ttk.Button(ventana, text="Cerrar", command=cerrar_ventana, style="BW.TButton")

boton_cerrar.pack(side=tk.BOTTOM, padx=5, pady=5)

# Mostrar la ventana

ventana.mainloop()

# this creates x as a new label to the GU
