'''

              /$$$$$$  /$$$$$$$   /$$$$$$   /$$$$$$  /$$$$$$$$
            /$$__  $$| $$__  $$ /$$__  $$ /$$__  $$| $$_____/
           | $$  \__/| $$  \ $$| $$  \ $$| $$  \__/| $$
           |  $$$$$$ | $$$$$$$/| $$$$$$$$| $$      | $$$$$
            \____  $$| $$____/ | $$__  $$| $$      | $$__/
            /$$  \ $$| $$      | $$  | $$| $$    $$| $$
           |  $$$$$$/| $$      | $$  | $$|  $$$$$$/| $$$$$$$$
            \______/ |__/      |__/  |__/ \______/ |________/ 



   /$$$$$$ /$$   /$$ /$$    /$$  /$$$$$$  /$$$$$$$  /$$$$$$$$ /$$$$$$$   /$$$$$$
  |_  $$_/| $$$ | $$| $$   | $$ /$$__  $$| $$__  $$| $$_____/| $$__  $$ /$$__  $$ 
    | $$  | $$$$| $$| $$   | $$| $$  \ $$| $$  \ $$| $$      | $$  \ $$| $$  \__/ 
    | $$  | $$ $$ $$|  $$ / $$/| $$$$$$$$| $$  | $$| $$$$$   | $$$$$$$/|  $$$$$$ 
    | $$  | $$  $$$$ \  $$ $$/ | $$__  $$| $$  | $$| $$__/   | $$__  $$ \____  $$ 
    | $$  | $$\  $$$  \  $$$/  | $$  | $$| $$  | $$| $$      | $$  \ $$ /$$  \ $$ 
   /$$$$$$| $$ \  $$   \  $/   | $$  | $$| $$$$$$$/| $$$$$$$$| $$  | $$|  $$$$$$/ 
   |______/|__/  \__/    \_/    |__/  |__/|_______/ |________/|__/  |__/ \______/ 
   
   
   ## SPACE INVADERS

  This is a pygame based game made and to be executed in Python 3.

  # This project does not accept pull requests.

  ## Usage

  You need to install python3 version 3.1 and above to run this game

  To run game, open terminal in SpaceInvader folder and type: "python .\main.py" to run. For MacOS and other exception, use: "python3 .\main.py" or "python3 ./main.py"

  you can change game BGM by putting music .wav file in sounds and changing music file address to new one in main.py code line 90.
   
  Install pygame library using: "pip install pygame" in windows/MacOS/Linux cmd/terminal.
    
  ## Build and maintained by:
  
                                 .x+=:.                                                     ..          .x+=:.   
        xeee    dL ud8Nu  :8c   z`    ^%                                                  dF           z`    ^%  
       d888R    8Fd888888L %8      .   <k                             u.      u.    u.   '88bu.           .   <k 
      d8888R    4N88888888cuR    .@8Ned8"      .u          .    ...ue888b   x@88k u@88c. '*88888bu      .@8Ned8" 
     @ 8888R    4F   ^""%""d   .@^%8888"    ud8888.   .udR88N   888R Y888r ^"8888""8888"   ^"*8888N   .@^%8888"  
   .P  8888R    d       .z8   x88:  `)8b. :888'8888. <888'888k  888R I888>   8888  888R   beWE "888L x88:  `)8b. 
  :F   8888R    ^     z888    8888N=*8888 d888 '88%" 9888 'Y"   888R I888>   8888  888R   888E  888E 8888N=*8888 
 x"    8888R        d8888'     %8"    R88 8888.+"    9888       888R I888>   8888  888R   888E  888E  %8"    R88 
d8eeeee88888eer    888888       @8Wou 9%  8888L      9888      u8888cJ888    8888  888R   888E  888F   @8Wou 9%  
       8888R      :888888     .888888P`   '8888c. .+ ?8888u../  "*888*P"    "*88*" 8888" .888N..888  .888888P`   
       8888R       888888     `   ^"F      "88888%    "8888P'     'Y"         ""   'Y"    `"888*""   `   ^"F     
    "*%%%%%%**~    '%**%                     "YP'       "P'                                  ""                  
   
   
   '''

import pygame
import random
import math
from pygame import mixer

# initialize game
pygame.init()

# defining screen
screen = pygame.display.set_mode((800, 600))  # <-----screen dimensions
background = pygame.image.load('icons\\Background.jpg')

# game title and icon
pygame.display.set_caption("Space Invaders")
title_icon = pygame.image.load('icons\\ufo.png')
pygame.display.set_icon(title_icon)

# Adding Player
player_icon = pygame.image.load('icons\\spaceship.png')
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
    enemy_icon = pygame.image.load('icons\\Enemy.png')
    enemy_X.append(random.randint(30, 706))
    enemy_Y.append(random.randint(50, 150))
    enemy_speed_X.append(0.3)
    enemy_speed_Y.append(0.02)

# Adding bullets
bullet = pygame.image.load('icons\\player_bullet.png')
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
mixer.music.load('sounds\\background_ost2.wav')  # <----Background ost
mixer.music.play(-1)  # <-----Loop music in infinite state

bullet_sound = mixer.Sound('sounds\\bullet_sound.wav')

explosion_sound = mixer.Sound('sounds\\explosion.wav')

# Game Over screen and sound
font_GameOver = pygame.font.Font('freesansbold.ttf', 64)
game_over_sound = mixer.Sound('sounds\\game_over.wav')

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
    
    
    
    '''
    
    .S_SsS_S.    .S  S.        sSSs          sSSs   .S_sSSs            sSSs   .S       S.    .S_sSSs    sdSS_SSSSSSbs   .S    sSSs 
   .SS~S*S~SS.  .SS  SS.      d%%SP         d%%SP  .SS~YS%%b          d%%SP  .SS       SS.  .SS~YS%%b   YSSS~S%SSSSSP  .SS   d%%SP 
   S%S `Y' S%S  S%S  S%S     d%S'          d%S'    S%S   `S%b        d%S'    S%S       S%S  S%S   `S%b       S%S       S%S  d%S' 
   S%S     S%S  S%S  S%S     S%S           S%S     S%S    S%S        S%S     S%S       S%S  S%S    S%S       S%S       S%S  S%| 
   S%S     S%S  S&S  S&S     S&S           S&S     S%S    d*S        S&S     S&S       S&S  S%S    d*S       S&S       S&S  S&S 
   S&S     S&S  S&S  S&S     S&S_Ss        S&S_Ss  S&S   .S*S        S&S     S&S       S&S  S&S   .S*S       S&S       S&S  Y&Ss 
   S&S     S&S  S&S  S&S     S&S~SP        S&S~SP  S&S_sdSSS         S&S     S&S       S&S  S&S_sdSSS        S&S       S&S  `S&&S 
   S&S     S&S  S&S  S&S     S&S           S&S     S&S~YSY%b         S&S     S&S       S&S  S&S~YSY%b        S&S       S&S    `S*S 
   S*S     S*S  S*S  S*b     S*b           S*b     S*S   `S%b        S*b     S*b       d*S  S*S   `S%b       S*S       S*S     l*S 
   S*S     S*S  S*S  S*S.    S*S.          S*S.    S*S    S%S        S*S.    S*S.     .S*S  S*S    S%S       S*S       S*S    .S*P 
   S*S     S*S  S*S   SSSbs   SSSbs         SSSbs  S*S    S&S         SSSbs   SSSbs_sdSSS   S*S    S&S       S*S       S*S  sSS*S 
   SSS     S*S  S*S    YSSP    YSSP          YSSP  S*S    SSS          YSSP    YSSP~YSSY    S*S    SSS       S*S       S*S  YSS' 
           SP   SP                                 SP                                       SP               SP        SP 
           Y    Y                                  Y                                        Y                Y         Y
           
   '''