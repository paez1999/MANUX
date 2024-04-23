import pygame
import sys
import os
import subprocess

# Inicializar Pygame
pygame.init()

# Definir las dimensiones de la pantalla
WIDTH, HEIGHT = 1330, 745
SCREEN_SIZE = (WIDTH, HEIGHT)

# Crear la pantalla
screen = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption("Interfaz con fondo de pantalla")

# Obtener la ruta del directorio del script
current_dir = os.path.dirname(__file__)

# Definir los estados de la interfaz
PAGINA_INICIO = 0
PAGINA_ESTUDIO = 1
PAGINA_COSAS_PERSONALES = 2
PAGINA_JUEGOS = 3
PAGINA_INVERTIR = 4
PAGINA_SERIE = 5
PAGINA_CONSOLA = 6

# Estado inicial
estado_pagina = PAGINA_INICIO

# Cargar la imagen del fondo
background_image = pygame.image.load(os.path.join(current_dir, "iconos/fondo de pantalla.jpg")).convert()

# Cargar las imágenes de los botones
button_images = [
    pygame.image.load(os.path.join(current_dir, "iconos/estudios.png")).convert_alpha(),
    pygame.image.load(os.path.join(current_dir, "iconos/cosas personales.jpg")).convert_alpha(),
    pygame.image.load(os.path.join(current_dir, "iconos/juegos.png")).convert_alpha(),
    pygame.image.load(os.path.join(current_dir, "iconos/invertir.png")).convert_alpha(),
    pygame.image.load(os.path.join(current_dir, "iconos/serie.png")).convert_alpha(),
    pygame.image.load(os.path.join(current_dir, "iconos/mando.png")).convert_alpha(),
    pygame.image.load(os.path.join(current_dir, "iconos/logo.jpg")).convert_alpha()
]

# Escalar las imágenes de los botones para que se ajusten al tamaño deseado
button_size = (50, 50)
button_images = [pygame.transform.scale(img, button_size) for img in button_images]

# Posiciones de los botones
button_positions = [(40, 50), (40, 130), (40, 210), (40, 290), (40, 370), (40, 450), (40, 650)]

# Crear rectángulos para los botones
button_rects = [pygame.Rect(pos, button_size) for pos in button_positions]


# Definir funciones para cada página
def mostrar_pagina_inicio():
    pass  # No se muestra ninguna página especial en la página de inicio


def ejecutar_estudio():
    subprocess.run(["python", "estudio.py"])
    return


def ejecutar_cosas_personales():
    subprocess.run(["python", "cosas_personales.py"])


def ejecutar_juegos():
    abrir_acceso_directo("C:\\Users\\paez1\\Desktop\\MANUX\\steam.lnk")     # Ingresar el path de steam
    return


def abrir_acceso_directo(ruta_acceso_directo):
    os.system('start "" "{}"'.format(ruta_acceso_directo))


def ejecutar_invertir():
    subprocess.run(["python", "invertir.py"])


def ejecutar_serie():
    subprocess.run(["python", "serie.py"])


def ejecutar_consola():
    subprocess.run(["python", "consola.py"])


# Bucle principal del juego
while True:
    # Manejo de eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        # Detectar clic en los botones
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            for i, rect in enumerate(button_rects):
                if rect.collidepoint(mouse_pos):
                    estado_pagina = i + 1  # Actualizar el estado de la página

    # Limpiar la pantalla
    screen.fill((0, 0, 0))

    # Dibujar el fondo
    screen.blit(background_image, (0, 0))

    # Dibujar los botones
    for button_pos, button_img in zip(button_positions, button_images):
        screen.blit(button_img, button_pos)

    # Mostrar la página correspondiente
    if estado_pagina == PAGINA_INICIO:
        mostrar_pagina_inicio()
        estado_pagina = ""
    elif estado_pagina == PAGINA_ESTUDIO:
        ejecutar_estudio()
        estado_pagina = ""
    elif estado_pagina == PAGINA_COSAS_PERSONALES:
        ejecutar_cosas_personales()
        estado_pagina = ""
    elif estado_pagina == PAGINA_JUEGOS:
        ejecutar_juegos()
        estado_pagina = ""
    elif estado_pagina == PAGINA_INVERTIR:
        ejecutar_invertir()
        estado_pagina = ""
    elif estado_pagina == PAGINA_SERIE:
        ejecutar_serie()
        estado_pagina = ""
    elif estado_pagina == PAGINA_CONSOLA:
        ejecutar_consola()
        estado_pagina = ""

    # Actualizar la pantalla
    pygame.display.flip()
