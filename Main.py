import sys, pygame
import random
from pygame.locals import *

pygame.init()
mainClock = pygame.time.Clock()

player = pygame.image.load("M:/groupPy/img/player.png")
background = pygame.image.load("M:/groupPy/img/background.png")
enemy_image = pygame.image.load("M:/groupPy/img/enemy_1.png")

playerRect = player.get_rect()
backgroundRect = background.get_rect()

size = (width, height) = background.get_size()
screen = pygame.display.set_mode(size)

b3x = 200
b3y = 750
movex = 6
movey = 0

enemyCounter = 0
NEWENEMY = 8
ENEMYSIZE = 50
ENEMYSPEED = 6
enemies = []

left = False
right = False

while 1:
	for event in pygame.event.get():
		if event.type == pygame.QUIT: sys.exit()
		
		if event.type == pygame.KEYDOWN:
			if event.key == K_LEFT:
				left = True
			if event.key == K_RIGHT:
				right = True
				
		if event.type == pygame.KEYUP:
			if event.key==pygame.K_LEFT:
				left = False
			if event.key==pygame.K_RIGHT:
				right = False
	
	if b3x + movex < 0:
		left = False
		
	if b3x + playerRect.width + movex > backgroundRect.width:
		right = False
	
	if right == True:
		b3x += movex
		
	if left == True:
		b3x -= movex
		
	enemyCounter += 1
	if enemyCounter >= NEWENEMY:
		# add new enemy
		#newEnemySpawn = {'rect': pygame.Rect(random.randint(0, WINDOWWIDTH-ENEMYSIZE), 0 - ENEMYSIZE, ENEMYSIZE, ENEMYSIZE),
        #            'speed': random.randint(ENEMYSPEEDMIN, ENEMYSPEEDMAX),
        #            }
					
		enemies.append({'rect': pygame.Rect(random.randint(0, backgroundRect.width-ENEMYSIZE), 0 - ENEMYSIZE, ENEMYSIZE, ENEMYSIZE),
                    'speed': ENEMYSPEED,
                    'surface':pygame.transform.scale(enemy_image, (ENEMYSIZE, ENEMYSIZE))
                    })
		enemyCounter = 0
		
	# move the enemies
	for b in enemies:
		b['rect'].move_ip(0, ENEMYSPEED)
	# check for collisions
	for b in enemies:
		if playerRect.colliderect(b['rect']):
			#pygame.quit()
			#sys.exit()
			print "collision"
	
	# Draw the Background
	screen.blit(background, backgroundRect)
	
	# Draw the enemies
	for b in enemies:
		screen.blit(enemy_image, b['rect'])
		
	# Draw the Player
	screen.blit(player,(b3x,b3y))
	
	pygame.display.flip()
	mainClock.tick(40)