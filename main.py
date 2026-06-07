import pygame
import settings

pygame.init()

WIDTH, HEIGHT = 800, 800
BACKGROUND_COLOR = settings.BACKGROUND_COLOR
VERTEX_COLOR = settings.VERTEX_COLOR
SHAPE_COLOR = settings.SHAPE_COLOR
LINE_WIDTH = settings.LINE_WIDTH
SIDE_LEN = settings.SIDE_LEN
SCALE = settings.SCALE
FPS = settings.FPS
FOV = settings.FOV

screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
running = True

vertices = []
vertices2d = []

for x in (-SIDE_LEN, SIDE_LEN):
    for y in (-SIDE_LEN, SIDE_LEN):
        for z in (-SIDE_LEN, SIDE_LEN):
            vertices.append([x, y, z])

print(vertices)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(BACKGROUND_COLOR)

    for i in range(len(vertices)):
        projected_x = vertices[i][0] * FOV / (FOV + vertices[i][2])
        projected_y = vertices[i][1] * FOV / (FOV + vertices[i][2])
        screenPos = [projected_x * SCALE + WIDTH/2, projected_y * SCALE + HEIGHT/2]
        vertices2d.append(screenPos)
        pygame.draw.circle(screen, VERTEX_COLOR, screenPos, LINE_WIDTH)

    for i in range(len(vertices2d)):
        for o in range(i + 1, len(vertices2d)):
            pygame.draw.line(screen, SHAPE_COLOR, vertices2d[i], vertices2d[o], LINE_WIDTH)

    pygame.display.update()
