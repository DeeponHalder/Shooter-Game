import pygame

pygame.init()

# Making Window
win = pygame.display.set_mode((1000, 700))

# Making title and icon
pygame.display.set_caption("Ball Shooter")
icon = pygame.image.load('flaming.png')
pygame.display.set_icon(icon)

#Shooter
#Ball
shooterImg=pygame.image.load('square-shape-shadow.png')
shooterX=436
shooterY=318

#Ball
ballImg=pygame.image.load('soccer-ball (1).png')
ballX=0
ballY=0
ballXc=0
BallYc=0

def shooter(x,y):
    win.blit(shooterImg,(x,y))
def ball(x,y):
    win.blit(ballImg,(x,y))

# Game Loop
running = True
while running:

    # filling window
    win.fill((0, 200, 50))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    shooter(shooterX,shooterY)
    pygame.display.update()
