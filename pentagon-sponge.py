from shapely.geometry import Point # type: ignore
from shapely.geometry.polygon import Polygon # type: ignore
import math
import pygame
import random

# made by las-r on github
# v1.1

# init
pygame.init()

# settings
DW, DH = 1000, 1000
PS = 400
CX, CY = DW // 2, DH // 2
BGCOL = (0, 0, 0)
PCOL = (255, 255, 255)
DOTCOL = (127, 127, 255)
PPF = 512

# variables
psd = False
lv = [None, None]

# vertices
v = []
for i in range(5):
    adeg = -90 + (360 / 5) * i
    arad = math.radians(adeg)
    x = CX + PS * math.cos(arad)
    y = CY + PS * math.sin(arad)
    v.append((int(x), int(y)))
p = Polygon(v)

# display
scr = pygame.display.set_mode((DW, DH))
pygame.display.set_caption("Pentagon Sponge")

# draw bg color
scr.fill(BGCOL)

# generate inital point
p = p.representative_point()
rx, ry = int(p.x), int(p.y)
rv = random.choice(v)
pv = rv
m = ((rx + rv[0]) // 2, (ry + rv[1]) // 2)

# main loop
run = True
while run:
    # event loop
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            run = False
        elif e.type == pygame.KEYDOWN:
            if e.key == pygame.K_r:
                scr.fill(BGCOL)
                pygame.draw.polygon(scr, PCOL, v, 1)
                pygame.display.flip()
                
    # find and draw point
    for _ in range(PPF):
        rv = random.choice(v)
        if lv[0] == lv[1] and lv[0] is not None:
            idx = v.index(lv[0])
            banned = [v[(idx - 1) % 5], v[(idx + 1) % 5]]
            while rv in banned:
                rv = random.choice(v)
        lv = [lv[1], rv]
        m = ((m[0] + rv[0]) // 2, (m[1] + rv[1]) // 2)
        scr.set_at(m, DOTCOL)
    pygame.draw.polygon(scr, PCOL, v, 1)
    pygame.display.flip()
