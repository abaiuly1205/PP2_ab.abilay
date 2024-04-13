import pygame
from random import randint

def R(x1, y1, x2, y2):
    x = min(x1, x2)
    y = min(y1, y2)
    w = abs(x1-x2)
    h = abs(y1-y2)
    return (x, y, w, h)
def C(x1, y1, x2, y2):
    x = x1 + abs(x1 - x2)/2
    y = y1 + abs(y1 - y2)/2 
    return (x, y)

pygame.init()
FPS = 60
clock = pygame.time.Clock()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
WIDTH = 600
HEIGHT = 700
x1 = 0
x2 = 0
y1 = 0
y2 = 0

all_colors = []

for _ in range(20):
    all_colors.append((randint(0, 255), randint(0, 255), randint(0, 255)))

screen = pygame.display.set_mode((WIDTH, HEIGHT))
another_layer = pygame.Surface((WIDTH, HEIGHT))
isMouseDown = False
pos = pygame.mouse.get_pos()

screen.fill(pygame.Color('white'))

color = BLACK
tool = 0
'''
0 - pen
1 - rectangle
2 - circle
3 - eraser
'''
all_tools = 4
size = 1

done = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            isMouseDown = True
            if event.button == 1:
                if tool == 0:
                    x1 = event.pos[0]
                    y1 = event.pos[1]
                    x2 = x1
                    y2 = y1
                elif tool == 1:
                    x1 = event.pos[0]
                    y1 = event.pos[1]
                elif tool == 2:
                    x1 = event.pos[0]
                    y1 = event.pos[1]
                elif tool == 3:
                    x1 = event.pos[0]
                    y1 = event.pos[1]
                    
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                tool = (tool + 1) % all_tools
            if event.key == pygame.K_ESCAPE:
                 screen.fill(pygame.Color('white'))
            if event.key == pygame.K_EQUALS:
                 size += 1
            if event.key == pygame.K_MINUS:
                if size > 1: 
                    size -= 1
                else:
                    print("This is the smallest size of line!!!")
            if event.key == pygame.K_0:
                color = BLACK
            if event.key == pygame.K_b:
                color = (0, 0, 255)
            if event.key == pygame.K_r:
                color = (255, 0, 0)
            if event.key == pygame.K_g:
                color = (0, 255, 0)

        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                another_layer.blit(screen, (0, 0))
                isMouseDown = False
        if event.type == pygame.MOUSEMOTION:
                        if isMouseDown:
                            if tool == 0:
                                x1 = x2
                                y1 = y2
                                x2 = event.pos[0]
                                y2 = event.pos[1]
                                pygame.draw.line(screen, color, (x1, y1), (x2, y2), size)
                            elif tool == 1:
                                screen.blit(another_layer, (0, 0))
                                x2 = event.pos[0]
                                y2 = event.pos[1]
                                pygame.draw.rect(screen, color, pygame.Rect(R(x1, y1, x2, y2)), size)
                            elif tool == 2:
                                screen.blit(another_layer, (0, 0))
                                x2 = event.pos[0]
                                y2 = event.pos[1]
                                pygame.draw.circle(screen, color, C(x1, y1, x2, y2), abs(x1 - x2)/2 , size)
                            elif tool == 3:
                                x2 = event.pos[0]
                                y2 = event.pos[1]
                                pygame.draw.circle(screen, WHITE, (x2, y2), size+5)

    each = 28
    for i, col in enumerate(all_colors):
        pygame.draw.rect(screen, col, (20 + i * each, 20, each, 20))
                                 
    pygame.display.flip()
    clock.tick(FPS)