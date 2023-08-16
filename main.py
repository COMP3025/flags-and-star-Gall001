import sys
import math
import pygame
from pygame.locals import QUIT

pygame.init()
DISPLAYSURF = pygame.display.set_mode((600, 400))
DISPLAYSURF.fill((255, 255, 255))
color_blue = (0, 56, 184)
def draw_star(screen, position, size, angle):
    color_blue = (0, 56, 184)
    x, y = position
    points = []
    for i in range(5):
        angle_rad = math.radians(angle + i * 144)
        if i % 2 == 0:
            x_i = x + size * math.cos(angle_rad)
            y_i = y - size * math.sin(angle_rad)
        else:
            x_i = x + (size / 2) * math.cos(angle_rad)
            y_i = y - (size / 2) * math.sin(angle_rad)
        points.append((x_i, y_i))
    
    pygame.draw.polygon(screen, color_blue, points, 10)

pygame.init()
DISPLAYSURF = pygame.display.set_mode((600, 400))
DISPLAYSURF.fill((255, 255, 255))

pygame.init()
DISPLAYSURF = pygame.display.set_mode((600, 400))
DISPLAYSURF.fill((255, 255, 255))

while True:
  # pygame.draw.line(DISPLAYSURF, color_blue, [0, 30], [400, 30], 50)
  # pygame.draw.line(DISPLAYSURF, color_blue, [0, 245], [400, 245], 50)
  # pygame.draw.polygon(DISPLAYSURF, color_blue,
  #                     [[250, 100], [200, 200], [150, 100]], 10)
  # pygame.draw.polygon(DISPLAYSURF, color_blue,
  #                     [[200, 75], [250, 175], [150, 175]], 10)

  draw_star(DISPLAYSURF, (200, 200), 100, 135)
  
  for event in pygame.event.get():
    if event.type == QUIT:
      pygame.quit()
      sys.exit()
  pygame.display.update()
