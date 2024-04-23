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

# Cargar la imagen del fondo
background_image = pygame.image.load(os.path.join(current_dir, "iconos/fondo de pantalla.jpg")).convert()

# Cargar la imagen del botón
button_image = pygame.image.load(os.path.join(current_dir, "iconos/ibex35.png")).convert_alpha()
button_size=(550,450)
crypto_size=(600,375)
barra_size=(300,75)
ethereum_size=(50,50)
binance_size=(50,50)
banco_size=(50,50)
crypto_image =  pygame.image.load(os.path.join(current_dir, "iconos/crypto.jpg")).convert_alpha()
barra_image = pygame.image.load(os.path.join(current_dir, "iconos/barra.PNG")).convert_alpha()
ethereum_image = pygame.image.load(os.path.join(current_dir, "iconos/ethereum.png")).convert_alpha()
binance_image = pygame.image.load(os.path.join(current_dir, "iconos/binance.png")).convert_alpha()
banco_image = pygame.image.load(os.path.join(current_dir, "iconos/banco.png")).convert_alpha()
salir_image = pygame.image.load(os.path.join(current_dir, "iconos/salir.png")).convert_alpha()
# Escalar la imagen del botón para que se ajuste al tamaño deseado
button_image = pygame.transform.scale(button_image,button_size)
crypto_image = pygame.transform.scale(crypto_image,crypto_size)
barra_image = pygame.transform.scale(barra_image,barra_size)
ethereum_image = pygame.transform.scale(ethereum_image,ethereum_size)
binance_image = pygame.transform.scale(binance_image,binance_size)
banco_image = pygame.transform.scale(banco_image,banco_size)
salir_image=pygame.transform.scale(salir_image,banco_size)
salir_rect = screen.blit(salir_image, (10, 10))
# Definir los estados de la interfaz
PAGINA_INICIO = 0
PAGINA_OTRA = 1

# Estado inicial
estado_pagina = PAGINA_INICIO

def close_window():
    pygame.quit()
    sys.exit()
# Función para cambiar de página
def cambiar_pagina():
    global estado_pagina
    estado_pagina = PAGINA_OTRA

    # Ejecutar el segundo script
    subprocess.run(["python", "segunda_interfaz.py"])

# Bucle principal del juego
while True:
    # Manejo de eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # Detectar clic en el botón
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            button_rect = button_image.get_rect(topleft=(300, 300))
            if button_rect.collidepoint(mouse_pos):
                cambiar_pagina()
            elif salir_rect.collidepoint(mouse_pos):
                close_window()

    # Limpiar la pantalla
    screen.fill((0, 0, 0))

    # Dibujar el fondo
    screen.blit(background_image, (0, 0))

    # Dibujar el botón en la página de inicio
    if estado_pagina == PAGINA_INICIO:
        screen.blit(button_image, (75, 50))
        screen.blit(crypto_image, (650, 100))
        screen.blit(barra_image, (475, 550))
        screen.blit(binance_image, (500, 560))
        screen.blit(ethereum_image, (600, 560))
        screen.blit(banco_image, (700, 560))
        screen.blit(salir_image, (10, 10))
    # Actualizar la pantalla
    pygame.display.flip()