import pygame
import sys
import os

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

# Cargar las imágenes
background_image = pygame.image.load(os.path.join(current_dir, "peliculas/p00.jpg")).convert()
button_image = pygame.image.load(os.path.join(current_dir, "iconos/salir.png")).convert_alpha()
button_image = pygame.transform.scale(button_image, (100, 100))

# Lista de Series
series = pygame.image.load(os.path.join(current_dir, "peliculas/L01.jpg")).convert_alpha()
series = pygame.transform.scale(series, (450, 450))

# Lista de imágenes
imagenes = [
    pygame.image.load(os.path.join(current_dir, "peliculas/p01.jpg")).convert_alpha(),
    pygame.image.load(os.path.join(current_dir, "peliculas/p02.jpg")).convert_alpha(),
    pygame.image.load(os.path.join(current_dir, "peliculas/p03.jpg")).convert_alpha(),
    pygame.image.load(os.path.join(current_dir, "peliculas/p04.jpg")).convert_alpha(),
    pygame.image.load(os.path.join(current_dir, "peliculas/p05.jpg")).convert_alpha(),
    pygame.image.load(os.path.join(current_dir, "peliculas/p06.jpg")).convert_alpha(),
]

# Escalar las imágenes a un tamaño uniforme
for i in range(len(imagenes)):
    imagenes[i] = pygame.transform.scale(imagenes[i], (330, 450))

indice_imagen_actual = 0  # Índice de la imagen actual

# Definir los estados de la interfaz
PAGINA_INICIO = 0
PAGINA_OTRA = 1


# Función para cambiar de página
def cambiar_pagina(estado_pagina):
    # Ejecutar el código correspondiente a la otra página
    if estado_pagina == PAGINA_INICIO:
        # Importa el otro script solo cuando se hace clic en la imagen "salir.png"
        import primeraparte
        primeraparte.mostrar_pagina_inicio()


# Bucle principal del juego
estado_pagina = PAGINA_INICIO
while True:
    # Manejo de eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # Detectar clic en el botón
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            button_rect = button_image.get_rect(topleft=(45, 45))
            if button_rect.collidepoint(mouse_pos):
                cambiar_pagina(estado_pagina)

            # Detectar clic en la imagen
            ima_rect = imagenes[indice_imagen_actual].get_rect(topleft=(320, 150))
            if ima_rect.collidepoint(mouse_pos):
                # Cambiar a la siguiente imagen en la lista
                indice_imagen_actual = (indice_imagen_actual + 1) % len(imagenes)

    # Limpiar la pantalla
    screen.fill((0, 0, 0))

    # Dibujar el fondo
    screen.blit(background_image, (0, 0))

    # Dibujar el botón en la página de inicio
    if estado_pagina == PAGINA_INICIO:
        screen.blit(button_image, (45, 45))
        screen.blit(series, (680, 150))
        screen.blit(imagenes[indice_imagen_actual], (320, 150))
    # Actualizar la pantalla
    pygame.display.flip()
