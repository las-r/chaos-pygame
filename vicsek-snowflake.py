import pygame
import random

# made by las-r on github
# v1.1

# init
pygame.init()

# settings
DW, DH = 1000, 1000
CX, CY = DW // 2, DH // 2
SQS = 800
BGCOL = (0, 0, 0)
SQCOL = (255, 255, 255)
DOTCOL = (127, 127, 255)
PPF = 512

# variables
psd = False

# vertices and center
T = CY - SQS // 2
B = CY + SQS // 2
L = CX - SQS // 2
R = CX + SQS // 2
vm = [(L, T),
      (R, T),
      (L, B),
      (R, B),
      (CX, CY)]


# display
scr = pygame.display.set_mode((DW, DH))
pygame.display.set_caption(("Vicsek Snowflake"))

# initial point
rx = random.randint(L, R)
ry = random.randint(T, B)
rv = random.choice(vm)
rx = int((rx / 3) + (2 / 3) * rv[0])
ry = int((ry / 3) + (2 / 3) * rv[1])

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
                pygame.draw.rect(scr, SQCOL, (CX - SQS // 2, CY - SQS // 2, SQS, SQS), 1)
                pygame.display.flip()
                
    # find and draw point
    for _ in range(PPF):
        rv = random.choice(vm)
        rx = int((rx / 3) + (2 / 3) * rv[0])
        ry = int((ry / 3) + (2 / 3) * rv[1])
        scr.set_at((rx, ry), DOTCOL)
    pygame.draw.rect(scr, SQCOL, (CX - SQS // 2, CY - SQS // 2, SQS, SQS), 1)
    pygame.display.flip()
