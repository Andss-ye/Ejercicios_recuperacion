import pygame
import math
import sys

# Inicializa Pygame
pygame.init()

# Configuración de la pantalla
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Dibujar Figuras")

# Colores
white = (255, 255, 255)
black = (0, 0, 0)

# Variables para el dibujo
shapes = []  # Lista para almacenar las figuras dibujadas
current_shape = ["circle", None]
drawing = False
start_pos = None
points = []  # Lista para almacenar los puntos del triángulo o el rectángulo

# Función para dibujar una figura
def draw_shape(shape):
    if shape is not None:
        if shape[0] == "circle" and shape[1] is not None:
            start_point, end_point = shape[1]
            radius = int(math.hypot(end_point[0] - start_point[0], end_point[1] - start_point[1]))
            pygame.draw.circle(screen, black, start_point, radius, 2)
        elif shape[0] == "triangle" and len(shape[1]) == 3:
            pygame.draw.polygon(screen, black, shape[1], 2)
        elif shape[0] == "rectangle" and len(shape[1]) == 2:
            pygame.draw.rect(screen, black, pygame.Rect(shape[1][0], (shape[1][1][0] - shape[1][0][0], shape[1][1][1] - shape[1][0][1])), 2)

# Bucle principal
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            if current_shape is None:
                current_shape = ["circle", None]
            start_pos = event.pos
            drawing = True

        if event.type == pygame.MOUSEBUTTONUP:
            if drawing:
                end_pos = event.pos
                if current_shape[0] == "triangle" or current_shape[0] == "rectangle":
                    points.append(end_pos)
                drawing = False
                if current_shape[0] == "triangle" and len(points) == 3:
                    current_shape[1] = points
                    shapes.append(current_shape)
                    current_shape = ["circle", None]
                    points = []
                elif current_shape[0] == "rectangle" and len(points) == 2:
                    current_shape[1] = points
                    shapes.append(current_shape)
                    current_shape = ["circle", None]
                    points = []

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_c:
                current_shape = ["circle", None]
            elif event.key == pygame.K_t:
                current_shape = ["triangle", None]
            elif event.key == pygame.K_r:
                current_shape = ["rectangle", None]

    screen.fill(white)
    for shape in shapes:
        draw_shape(shape)
    if current_shape is not None:
        if drawing:
            end_pos = pygame.mouse.get_pos()
            if current_shape[0] == "circle":
                current_shape[1] = (start_pos, end_pos)
            elif current_shape[0] == "triangle":
                current_shape[1] = [start_pos, end_pos, (end_pos[0], start_pos[1])]
            elif current_shape[0] == "rectangle":
                current_shape[1] = pygame.Rect(start_pos, (end_pos[0] - start_pos[0], end_pos[1] - start_pos[1]))
        draw_shape(current_shape)
    pygame.display.flip()

# Salir de Pygame
pygame.quit()
sys.exit()
