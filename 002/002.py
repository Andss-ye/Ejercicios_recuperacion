import pygame
import sys

pygame.init()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Tamaño de la ventana
WIDTH, HEIGHT = 800, 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("002")

# Variables 
selected_point = None
selected_points = []
shapes = []

# Bucle principal
drawing_circle = True
drawing_triangle = False
drawing_rectangle = False
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if drawing_circle:
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                selected_point = event.pos
                shapes.append([selected_point])
                drawing_circle = False
                drawing_triangle = True

        elif drawing_triangle:
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                selected_points.append(event.pos)

                if len(selected_points) == 3:
                    shapes.append(selected_points[:])
                    selected_points.clear()
                    drawing_triangle = False
                    drawing_rectangle = True

        elif drawing_rectangle:
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                selected_points.append(event.pos)
                if len(selected_points) == 4:
                    shapes.append(selected_points[:])
                    selected_points.clear()

    # Limpiar
    screen.fill(WHITE)

    # Dibujar las formas
    for shape in shapes:
        if len(shape) == 1:
            pygame.draw.circle(screen, BLACK, shape[0], 20)  
        elif len(shape) == 3:
            pygame.draw.polygon(screen, BLACK, shape, 2)  
        elif len(shape) == 4:
            pygame.draw.polygon(screen, BLACK, shape, 2)  

    # Actualizar
    pygame.display.flip()



# Salir de Pygame
pygame.quit()
sys.exit()
