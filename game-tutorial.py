import pygame
import random
pygame.init()

# Create screen
screen = pygame.display.set_mode((800, 600))

# Background img
background = pygame.image.load('2474216-2.jpg')

# Set title and icon
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load("alien.png")
pygame.display.set_icon(icon)

# PLayer
playerImg = pygame.image.load("space-invaders.png")
playerX = 370
playerY = 480
playerX_change = 0
playerY_change = 0

# Enemy
enemyImg = pygame.image.load("space-invader.png")
enemyX = random.randint(0, 800)
enemyY = random.randint(50, 150)
enemyX_change = 4
enemyY_change = 40

# Bullet
# Ready - hidden; Fire - Being fired and is visible
bulletImg = pygame.image.load("space-invader.png")
bulletX = 0
bulletY = 480
bulletX_change = 0
bulletY_change = 40
bullet_state = 'ready'


def player(x, y):
    screen.blit(playerImg, (x, y))

def enemy(x, y):
    screen.blit(enemyImg, (x, y))

def fire_bullet(x, y):
    global bullet_state
    bullet_state = 'fire'
    screen.blit(bulletImg, (x, y))

# Infinite game loop
running = True
while running:
    # RBG values - underneath background img
    screen.fill((0, 0, 0))
    screen.blit(background, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # if keystroke event, check whether right or left
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -5
            if event.key == pygame.K_RIGHT:
                playerX_change = 5

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0
    
    # Keeping player in boundary
    playerX += playerX_change
    if playerX <= 0:
        playerX = 0
    elif playerX >=736:
        playerX = 736

    # Keeping enemy in boundary
    enemyX += enemyX_change
    if enemyX <= 0:
        enemyX_change = 4
        enemyY += enemyY_change
    elif enemyX >=736:
        enemyX_change = -4
        enemyY += enemyY_change
    
    player(playerX, playerY)
    enemy(enemyX, enemyY)
    pygame.display.update()
