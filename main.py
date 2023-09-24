import pygame
import random
import math
from pygame import mixer

# initialize game
pygame.init()

# defining screen
screen = pygame.display.set_mode((800, 600))  # <-----screen dimensions
background = pygame.image.load('SpaceInvaders\\icons\\Background.jpg')

# game title and icon
pygame.display.set_caption("Space Invaders")
title_icon = pygame.image.load('SpaceInvaders\\icons\\ufo.png')
pygame.display.set_icon(title_icon)

# Adding Player
player_icon = pygame.image.load('SpaceInvaders\\icons\\spaceship.png')
player_X = 370
player_Y = 480
player_speed_X = 0
player_speed_Y = 0

# Adding Enemies
no_of_enemies = 7  # <-----specifing no. of enemies

enemy_X = []  # <-----Creating lists of enemy attributes
enemy_Y = []
enemy_speed_X = []
enemy_speed_Y = []

for i in range(no_of_enemies):
    enemy_icon = pygame.image.load('SpaceInvaders\\icons\\Enemy.png')
    enemy_X.append(random.randint(30, 706))
    enemy_Y.append(random.randint(50, 150))
    enemy_speed_X.append(0.3)
    enemy_speed_Y.append(0.02)

# Adding bullets
bullet = pygame.image.load('SpaceInvaders\\icons\\player_bullet.png')
bullet_X = 0  # <-----These can be anything as we just need parameter,
bullet_Y = 0  # <-----later these will be overwritten anyways.
bullet_speed_Y = 0.45
bullet_status = "ready"

def player(x, y):
    screen.blit(player_icon, (x, y))

def enemy(x, y, i):
    screen.blit(enemy_icon, (x, y))

def fire_bullet(x, y):
    global bullet_status
    bullet_status = "fire"
    screen.blit(bullet, (x+16, y))

# Bullet Enemy Collision detection
def isCollision(enemy_X, enemy_Y, bullet_X, bullet_Y):
    distance = math.sqrt(pow((enemy_X-bullet_X), 2)+pow((enemy_Y-bullet_Y), 2))
    if distance < 27 and bullet_status == "fire":
        explosion_sound.play()  # <-----play exposion sound effect
        return True
    else:
        return False

# Player collision detection
def isPlayerCollision(enemy_X, enemy_Y, player_X, player_Y):
    distance = math.sqrt(pow((enemy_X-player_X), 2)+pow((enemy_Y-player_Y), 2))
    if distance < 27:
        explosion_sound.play()  # <-----play exposion sound effect
        return True
    elif enemy_Y==2000:  # <-----since at y=2000, our transported enemies are in case of collision, stating collision occured and GAME OVER
        return True
    else:
        return False

# Defining score
current_score = 0
score_font = pygame.font.Font('freesansbold.ttf', 32)
score_X = 10
score_Y = 10

def showScore(x, y):
    score = score_font.render(
        "Score: " + str(current_score), True, (255, 255, 255))
    screen.blit(score, (x, y))

# Defining sounds
mixer.music.load('SpaceInvaders\\sounds\\background_ost2.wav')  # <----Background ost
mixer.music.play(-1)  # <-----Loop music in infinite state

bullet_sound = mixer.Sound('SpaceInvaders\\sounds\\bullet_sound.wav')

explosion_sound = mixer.Sound('SpaceInvaders\\sounds\\explosion.wav')

# Game Over screen and sound
font_GameOver = pygame.font.Font('freesansbold.ttf', 64)
game_over_sound = mixer.Sound('SpaceInvaders\\sounds\\game_over.wav')

end=1  #<----helps to play GAME OVER sound once only
def game_over(end):
    game_over_text = font_GameOver.render("GAME OVER", True, (255, 0, 0))
    screen.blit(game_over_text, (200, 250))
    if end == 1:
        mixer.Sound.play(game_over_sound)

# Game screen sustaining loop
running = True

while running:
    
    # RGB background
    screen.fill((0, 0, 0))  # <-----first we put screen
    screen.blit(background, (0, 0))  # <-----adding backgroud to game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Player Controls
        if event.type == pygame.KEYDOWN:  # <------player X-axis speed
            if (event.key == pygame.K_LEFT):
                player_speed_X -= 0.3
            elif event.key == pygame.K_RIGHT:
                player_speed_X += 0.3

            elif event.key == pygame.K_SPACE and bullet_status == "ready":  # <-----only when status is ready we fire bullet
                bullet_X = player_X  # <------recording position where
                bullet_Y = player_Y  # bullet is fired.
                bullet_sound.play()  # <-----bullet diring sound effect
                fire_bullet(bullet_X, bullet_Y)

            if (event.key == pygame.K_UP):  # <------player Y-axis speed
                player_speed_Y -= 0.3
            elif event.key == pygame.K_DOWN:
                player_speed_Y += 0.3

        if event.type == pygame.KEYUP:  # player stops
            if (event.key == pygame.K_LEFT) or (event.key == pygame.K_RIGHT):
                player_speed_X = 0
            if (event.key == pygame.K_UP) or (event.key == pygame.K_DOWN):
                player_speed_Y = 0

    # Setting boundary conditions
    if player_X <= 30:
        player_X = 30  # <-----Player's X-axis boundaries
    elif player_X >= 706:
        player_X = 706

    if player_Y <= 400:
        player_Y = 400  # <-----Player's Y-axis boundaries
    elif player_Y >= 560:
        player_Y = 560

    for i in range(no_of_enemies):
        if enemy_X[i] <= 30:
            enemy_speed_X[i] = 0.3  # <-----Enemy's X-axis boundaries
        elif enemy_X[i] >= 706:
            enemy_speed_X[i] = -0.3

        if enemy_Y[i] >= 706 and enemy_Y[i] != 2000:  # <-----Enemy's Y-axis boundaries, y=2000 is game over transport point
            enemy_X[i] = random.randint(30, 706)
            enemy_Y[i] = random.randint(50, 150)

    if bullet_Y <= 0:  # <-----Bullet's position
        bullet_Y = player_Y
        bullet_status = "ready"
        bullet_X = player_X
        bullet_Y = player_Y

    # Game behavior while playing
    # Note: If background size is large, characters will move slowly, therefore, increase their speed accordingly in that case.
    player_X += player_speed_X
    player_Y += player_speed_Y

    for i in range(no_of_enemies):
        enemy_X[i] += enemy_speed_X[i]
        enemy_Y[i] += enemy_speed_Y[i]

    player(player_X, player_Y)  # <-----putting our player

    for i in range(no_of_enemies):     # <-----putting our enemies
        enemy(enemy_X[i], enemy_Y[i], i)

    if bullet_status == "fire":
        fire_bullet(bullet_X, bullet_Y)
        bullet_Y -= bullet_speed_Y

    showScore(score_X, score_Y)  # <-----displaying score

    # Collision check for bullet
    for i in range(no_of_enemies):
        Collision_status = isCollision(enemy_X[i], enemy_Y[i], bullet_X, bullet_Y)
        if Collision_status:
            bullet_X = player_X
            bullet_Y = player_Y
            bullet_status = "ready"
            current_score += 1
            enemy_X[i] = random.randint(30, 706)
            enemy_Y[i] = random.randint(50, 150)

    # Collision check for player with enemies
    for i in range(no_of_enemies):
        player_Collision_status = isPlayerCollision(enemy_X[i], enemy_Y[i], player_X, player_Y)
        if player_Collision_status:
            for j in range(no_of_enemies):
                enemy_speed_Y[j] = 0
                enemy_speed_X[j] = 0
                enemy_Y[j] = 2000  # <----transport all enemies to out of screen and stop their movements
            mixer.music.stop()  # <-----stop game ost
            game_over(end)
            end+=1
            break

    # Update game screen
    pygame.display.update()