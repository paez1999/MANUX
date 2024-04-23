import pygame
import sys
import os

# Inicializar Pygame
pygame.init()

# Definir las dimensiones de la pantalla
WIDTH, HEIGHT = 1330, 745
SCREEN_SIZE = (WIDTH, HEIGHT)

# Definir colores
WHITE = (255, 255, 255)

# Crear la pantalla
screen = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption("Vision Board Digital")

# Obtener la ruta del directorio del script
current_dir = os.path.dirname(__file__)

# Cargar la imagen del fondo
background_image = pygame.image.load(os.path.join(current_dir, "iconos/fondo de pantalla.jpg")).convert()

# Cargar la imagen del botón
button_image = pygame.image.load(os.path.join(current_dir, "iconos/salir.png")).convert_alpha()
button_image = pygame.transform.scale(button_image, (50, 50))

# Cargar la imagen de la carpeta
folder_image = pygame.image.load(os.path.join(current_dir, "iconos/carpeta.png")).convert_alpha()
folder_image = pygame.transform.scale(folder_image, (50, 50))

# Cargar las imágenes de los archivos
file1_image = pygame.image.load(os.path.join(current_dir, "iconos/archivos.png")).convert_alpha()
file1_image = pygame.transform.scale(file1_image, (50, 50))

file2_image = pygame.image.load(os.path.join(current_dir, "iconos/ppt.png")).convert_alpha()
file2_image = pygame.transform.scale(file2_image, (50, 50))

file3_image = pygame.image.load(os.path.join(current_dir, "iconos/excel.png")).convert_alpha()
file3_image = pygame.transform.scale(file3_image, (50, 50))

file4_image = pygame.image.load(os.path.join(current_dir, "iconos/block.png")).convert_alpha()
file4_image = pygame.transform.scale(file4_image, (200, 100))

# Definir la posición de la carpeta
folder_position = (70, 70)
file1_position = (folder_position[0] + 70, folder_position[1])
file2_position = (file1_position[0] + 70, file1_position[1])
file3_position = (file2_position[0] + 70, file2_position[1])
file4_position = (file3_position[0] -10, 40)

# Clase para el botón
class Button:
    def __init__(self, position, image):
        self.position = position
        self.image = image
        self.rect = image.get_rect(topleft=position)

    def draw(self, surface):
        surface.blit(self.image, self.position)

# Crear el botón para salir del programa
button = Button((10, 10), button_image)

# Bucle principal del juego
running = True
while running:
    # Manejo de eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if button.rect.collidepoint(event.pos):
                running = False

    # Dibujar el fondo
    screen.blit(background_image, (0, 0))

    # Dibujar la carpeta
    screen.blit(folder_image, folder_position)

    # Dibujar los archivos
    screen.blit(file1_image, file1_position)
    screen.blit(file2_image, file2_position)
    screen.blit(file3_image, file3_position)
    screen.blit(file4_image, file4_position)

    # Dibujar el botón
    button.draw(screen)

    # Actualizar la pantalla
    pygame.display.flip()

# Salir del juego
pygame.quit()
sys.exit()