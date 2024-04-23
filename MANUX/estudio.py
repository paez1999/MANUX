import pygame
import sys
import os
import webbrowser
from datetime import datetime

# Inicializar Pygame
pygame.init()

# Definir las dimensiones de la pantalla
WIDTH, HEIGHT = 1330, 745
SCREEN_SIZE = (WIDTH, HEIGHT)

# Colores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
RED = (255, 0, 0)

# Crear la pantalla
screen = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption("Interfaz con fondo de pantalla")

# Obtener la ruta del directorio del script
current_dir = os.path.dirname(__file__)

# Cargar la imagen del fondo
background_image = pygame.image.load(os.path.join(current_dir, "iconos/fondo de pantalla.jpg")).convert()

# Cargar las imágenes de los botones izquierdos y ajustar su tamaño
button1_image = pygame.image.load(os.path.join(current_dir, "iconos/logo.jpg")).convert_alpha()
button1_image = pygame.transform.scale(button1_image, (100, 100))

button2_image = pygame.image.load(os.path.join(current_dir, "iconos/salir.png")).convert_alpha()
button2_image = pygame.transform.scale(button2_image, (50, 50))

button3_image = pygame.image.load(os.path.join(current_dir, "iconos/blackboard.png")).convert_alpha()
button3_image = pygame.transform.scale(button3_image, (100, 100))

button4_image = pygame.image.load(os.path.join(current_dir, "iconos/youtube.png")).convert_alpha()
button4_image = pygame.transform.scale(button4_image, (100, 110))

button5_image = pygame.image.load(os.path.join(current_dir, "iconos/Gmail.png")).convert_alpha()  # Nuevo
button5_image = pygame.transform.scale(button5_image, (100, 100))  # Nuevo

# Coordenadas de los botones izquierdos
button1_x, button1_y = 600, 90
button2_x, button2_y = 20, 20
button3_x, button3_y = 750, 90
button4_x, button4_y = 600, 200

# Coordenadas del nuevo botón para Gmail
button5_x, button5_y = 750, 200  # Nuevo

# URL de la página de Google
google_url = "https://www.google.com"

# URL de la página de Blackboard
blackboard_url = "https://ucjc.blackboard.com/ultra/course"

# URL de la página de YouTube
youtube_url = "https://www.youtube.com/"

# URL de la página de Gmail
gmail_url = "https://mail.google.com"

# Variable para almacenar el texto de las notas
notes_text = ""

# Variables para el temporizador Pomodoro
pomodoro_minutes = 1800
pomodoro_seconds = 0
pomodoro_running = False
pomodoro_pause = False

# Cargar las imágenes de los botones de start, pause y reset
start_button_image = pygame.image.load(os.path.join(current_dir, "iconos/play.png")).convert_alpha()
start_button_image = pygame.transform.scale(start_button_image, (100, 50))

pause_button_image = pygame.image.load(os.path.join(current_dir, "iconos/pause.png")).convert_alpha()
pause_button_image = pygame.transform.scale(pause_button_image, (100, 50))

reset_button_image = pygame.image.load(os.path.join(current_dir, "iconos/reset.png")).convert_alpha()
reset_button_image = pygame.transform.scale(reset_button_image, (100, 50))

# Coordenadas de los botones de start, pause y reset
start_button_x, start_button_y = 900, 170
pause_button_x, pause_button_y = 1000, 170
reset_button_x, reset_button_y = 1100, 170

# Función para abrir la página de Google en el navegador web
def open_google():
    webbrowser.open(google_url)

# Función para abrir la página de Blackboard en el navegador web
def open_blackboard():
    webbrowser.open(blackboard_url)

# Función para abrir la página de YouTube en el navegador web
def open_youtube():
    webbrowser.open(youtube_url)

# Función para abrir la página de Gmail en el navegador web
def open_gmail():
    webbrowser.open(gmail_url)  # Nuevo

# Función para cerrar la ventana del juego
def close_window():
    pygame.quit()
    sys.exit()

# Función para obtener la hora actual
def get_current_time():
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    return current_time

# Función para mostrar el reloj en la pantalla
def draw_clock(x, y, font_size):
    font = pygame.font.SysFont(None, font_size)
    current_time = get_current_time()
    text_surface = font.render(current_time, True, WHITE)
    text_rect = text_surface.get_rect()
    text_rect.topleft = (x, y)
    screen.blit(text_surface, text_rect)

# Función para dibujar un rectángulo debajo del reloj
def draw_under_clock_rect(x, y, width, height):
    pygame.draw.rect(screen, GRAY, (x, y, width, height))

# Función para dibujar el texto de las notas en la pantalla
def draw_notes_text(x, y, font_size):
    font = pygame.font.SysFont(None, font_size)
    lines = notes_text.split("\n")  # Dividir el texto en líneas
    for i, line in enumerate(lines):
        text_surface = font.render(line, True, BLACK)
        text_rect = text_surface.get_rect()
        text_rect.topleft = (x, y + i * font_size)  # Ajustar la posición de la línea
        screen.blit(text_surface, text_rect)

# Función para manejar los eventos de teclado
def handle_keyboard_events(event):
    global notes_text
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_BACKSPACE:
            # Eliminar el último carácter del texto de las notas
            notes_text = notes_text[:-1]
        elif event.key == pygame.K_RETURN:
            # Agregar un salto de línea al texto de las notas
            notes_text += "\n"
        elif event.key != pygame.K_RETURN:  # Ignorar la tecla Enter
            # Agregar el carácter ingresado al texto de las notas
            notes_text += event.unicode

# Función para dibujar el temporizador Pomodoro
def draw_pomodoro_timer(x, y, font_size):
    font = pygame.font.SysFont(None, font_size)
    timer_text = f"{pomodoro_minutes:02}:{pomodoro_seconds:02}"
    text_surface = font.render(timer_text, True, WHITE)
    text_rect = text_surface.get_rect()
    text_rect.topleft = (x, y)
    screen.blit(text_surface, text_rect)

# Función para actualizar el temporizador Pomodoro
def update_pomodoro_timer():
    global pomodoro_minutes, pomodoro_seconds, pomodoro_running, pomodoro_pause
    if pomodoro_running and not pomodoro_pause:
        if pomodoro_seconds > 0:
            pomodoro_seconds -= 1
        elif pomodoro_minutes > 0:
            pomodoro_seconds = 59
            pomodoro_minutes -= 1
        else:
            # Pomodoro finalizado, se puede agregar aquí una acción al terminar el temporizador
            pomodoro_running = False
    pygame.time.set_timer(pygame.USEREVENT, 1000)

# Función para manejar los eventos de clic en los botones de start, pause y reset
def handle_button_click(event):
    global pomodoro_running, pomodoro_pause, pomodoro_minutes, pomodoro_seconds
    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
        mouse_pos = pygame.mouse.get_pos()
        if start_button_rect.collidepoint(mouse_pos):
            pomodoro_running = True
            pomodoro_pause = False
        elif pause_button_rect.collidepoint(mouse_pos):
            pomodoro_pause = not pomodoro_pause
        elif reset_button_rect.collidepoint(mouse_pos):
            pomodoro_running = False
            pomodoro_pause = False
            pomodoro_minutes = 10000
            pomodoro_seconds = 0
        elif button1_rect.collidepoint(mouse_pos):
            open_google()
        elif button2_rect.collidepoint(mouse_pos):
            close_window()
        elif button3_rect.collidepoint(mouse_pos):
            open_blackboard()
        elif button4_rect.collidepoint(mouse_pos):
            open_youtube()
        elif button5_rect.collidepoint(mouse_pos):  # Nuevo
            open_gmail()

# Bucle principal del juego
while True:
    # Manejo de eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            close_window()
        # Manejar eventos de teclado
        handle_keyboard_events(event)
        # Manejar eventos de clic en los botones de start, pause, reset y el nuevo botón de Gmail
        handle_button_click(event)

    # Actualizar el temporizador Pomodoro
    update_pomodoro_timer()

    # Dibujar el fondo
    screen.blit(background_image, (0, 0))

    # Dibujar los botones izquierdos
    button1_rect = screen.blit(button1_image, (button1_x, button1_y))
    button2_rect = screen.blit(button2_image, (button2_x, button2_y))
    button3_rect = screen.blit(button3_image, (button3_x, button3_y))
    button4_rect = screen.blit(button4_image, (button4_x, button4_y))

    # Dibujar el nuevo botón para Gmail
    button5_rect = screen.blit(button5_image, (button5_x, button5_y))  # Nuevo

    # Dibujar los botones de start, pause y reset
    start_button_rect = screen.blit(start_button_image, (start_button_x, start_button_y))
    pause_button_rect = screen.blit(pause_button_image, (pause_button_x, pause_button_y))
    reset_button_rect = screen.blit(reset_button_image, (reset_button_x, reset_button_y))

    # Dibujar el reloj con un tamaño de fuente de 30
    draw_clock(100, 100, 100)

    # Dibujar el rectángulo debajo del reloj
    draw_under_clock_rect(100, 180, 400, 500)

    # Dibujar el texto de las notas
    draw_notes_text(110, 190, 20)

    # Dibujar el temporizador Pomodoro
    draw_pomodoro_timer(1000, 100, 100)

    # Actualizar la pantalla
    pygame.display.flip()