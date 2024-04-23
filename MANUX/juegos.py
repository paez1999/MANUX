import pygame
import sys

# Inicializar Pygame
pygame.init()

# Definir colores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)

# Definir la configuración de la pantalla
WIDTH, HEIGHT = 800, 600
FPS = 60

# Crear la ventana
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Página de juegos")

# Clase para representar un juego
class Game:
    def __init__(self, name, description, price):
        self.name = name
        self.description = description
        self.price = price

# Lista de juegos de ejemplo
games = [
    Game("Juego 1", "Descripción del juego 1", "$19.99"),
    Game("Juego 2", "Descripción del juego 2", "$14.99"),
    Game("Juego 3", "Descripción del juego 3", "$24.99")
]

# Función para mostrar los detalles de un juego
def show_game_details(game):
    print(f"Nombre: {game.name}")
    print(f"Descripción: {game.description}")
    print(f"Precio: {game.price}")
    print()

# Función principal del juego
def main():
    clock = pygame.time.Clock()

    running = True
    while running:
        # Manejo de eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Botón izquierdo del ratón
                    # Verificar si se ha hecho clic en un juego
                    for idx, game in enumerate(games):
                        if game_rects[idx].collidepoint(event.pos):
                            show_game_details(game)

        # Limpiar la pantalla
        screen.fill(WHITE)

        # Dibujar la lista de juegos
        game_rects = []
        font = pygame.font.Font(None, 36)
        for idx, game in enumerate(games):
            text_surface = font.render(game.name, True, BLACK)
            rect = text_surface.get_rect(topleft=(50, 100 + idx * 50))
            screen.blit(text_surface, rect)
            game_rects.append(rect)

        # Actualizar la pantalla
        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()