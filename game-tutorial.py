import pygame
pygame.init()

# Create screen
screen = pygame.display.set_mode((800, 600))

# Set title and icon
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load("alien.png")
pygame.display.set_icon(icon)

# PLayer
playerImg = pygame.image.load("space-invaders.png")
playerX = 370
playerY = 480

def player(x, y):
    screen.blit(playerImg, (x, y))

# Infinite game loop
running = True
while running:
    # RBG values
    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # if keystroke event, check whether right or left
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                print('left arrow pressed')
            if event.key == pygame.K_RIGHT:
                print('right arrow pressed')

    player(playerX, playerY)
    pygame.display.update()
