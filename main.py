import pygame
import settings

pygame.init()

WIDTH, HEIGHT = 800, 800
BACKGROUND_COLOR = settings.BACKGROUND_COLOR
DOT_COLOR = settings.DOT_COLOR
SHAPE_COLOR = settings.SHAPE_COLOR
LINE_WIDTH = settings.LINE_WIDTH
SIDE_LEN = settings.SIDE_LEN
SCALE = settings.SCALE
FPS = settings.FPS
FOV = settings.FOV

screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
running = True

points = []

for x in (-SIDE_LEN, SIDE_LEN):
    for y in (-SIDE_LEN, SIDE_LEN):
        for z in (-SIDE_LEN, SIDE_LEN):
            points.append(x, y, z)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(BACKGROUND_COLOR)


