from shapely.geometry import Point # type: ignore
from shapely.geometry.polygon import Polygon # type: ignore
import math
import pygame
import random

# made by las-r on github
# v1.1.1

# init
pygame.init()

# settings
DW, DH = 1000, 1000
TSD = 400
TCX = DW // 2
TCY = int((DH + 0.5 * TSD) / 2)
BGCOL = (0, 0, 0)
TRICOL = (255, 255, 255)
DOTCOL = (127, 127, 255)

# variables
psd = False

# get triangle vertices
v = []
for i in range(3):
    adeg = 90 + (360 / 3) * i
    arad = math.radians(adeg)
    x = TCX + TSD * math.cos(arad)
    y = TCY - TSD * math.sin(arad)
    v.append((int(x), int(y)))
tri = Polygon(v)

# generate inital point in triangle
rx = random.randint(v[1][0], v[2][0])
ry = random.randint(v[0][1], v[1][1])
while not tri.contains(Point(rx, ry)):
    rx = random.randint(v[1][0], v[2][0])
    ry = random.randint(v[0][1], v[1][1])
rv = random.choice(v)
m = ((rx + rv[0]) // 2, (ry + rv[1]) // 2)

# display
scr = pygame.display.set_mode((DW, DH))
pygame.display.set_caption("Sierpinski")
    
# draw triangle
scr.fill(BGCOL)
pygame.draw.polygon(scr, TRICOL, v, 1)
pygame.display.flip()

# main loop
run = True
while run:
    # event loop
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            run = False
        elif e.type == pygame.KEYDOWN:
            if e.key == pygame.K_SPACE:
                psd = not psd
            elif e.key == pygame.K_r:
                scr.fill(BGCOL)
                pygame.draw.polygon(scr, TRICOL, v, 1)
                pygame.display.flip()
                
    # find and draw point
    if not psd:
        rv = random.choice(v)
        m = ((m[0] + rv[0]) // 2, (m[1] + rv[1]) // 2)
        scr.set_at(m, DOTCOL)
        pygame.display.flip()
        
# quit
pygame.quit()
