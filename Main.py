import pygame, sys, random
from pygame.locals import *

def main():
	# set up pygame
	pygame.init()
	mainClock = pygame.time.Clock()

	player_image = pygame.image.load("M:/groupPy/img/player.png")
	background = pygame.image.load("M:/groupPy/img/background.png")
	enemy_image = pygame.image.load("M:/groupPy/img/enemy_1.png")

	backgroundRect = background.get_rect()

	# set up the window
	WINDOWWIDTH = 600
	WINDOWHEIGHT = 800
	screen = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT), 0, 32)
	pygame.display.set_caption('Input')

	# set up the colors
	BLACK = (0, 0, 0)
	GREEN = (0, 255, 0)
	RED = (255, 0, 0)
	BLUE = (0, 0, 255)
	RANDOMCOLOUR = (random.randint(0, 255),random.randint(0, 255),random.randint(0, 255))
	WHITE = (255, 255, 255)


	enemyCounter = 0
	NEWENEMY = 8
	ENEMYSIZE = 50
	ENEMYSPEED = 6
	enemies = []


	player = pygame.Rect(300, 700, 32, 32)


	playerHealth = 100

	moveLeft = False
	moveRight = False
	moveUp = False
	moveDown = False

	gameOver = False
	gameRunning = True

	MOVESPEED = 8
	while gameRunning == True:
		while gameOver == False:
			# check for events
			for event in pygame.event.get():
				if event.type == QUIT:
					pygame.quit()
					sys.exit()
				if event.type == KEYDOWN:
					# change the keyboard variables
					if event.key == K_LEFT or event.key == ord('a'):
						moveRight = False
						moveLeft = True
					if event.key == K_RIGHT or event.key == ord('d'):
						moveLeft = False
						moveRight = True
					if event.key == K_UP or event.key == ord('w'):
						moveDown = False
						moveUp = True
					if event.key == K_DOWN or event.key == ord('s'):
						moveUp = False
						moveDown = True
				if event.type == KEYUP:
					if event.key == K_ESCAPE:
						pygame.quit()
						sys.exit()
					if event.key == K_LEFT or event.key == ord('a'):
						moveLeft = False
					if event.key == K_RIGHT or event.key == ord('d'):
						moveRight = False
					if event.key == K_UP or event.key == ord('w'):
						moveUp = False
					if event.key == K_DOWN or event.key == ord('s'):
						moveDown = False
						
			enemyCounter += 1
			if enemyCounter >= NEWENEMY:
							
				enemies.append({'rect': pygame.Rect(random.randint(0, WINDOWWIDTH-ENEMYSIZE), 0 - ENEMYSIZE, ENEMYSIZE, ENEMYSIZE),
							'speed': ENEMYSPEED,
							'surface':pygame.transform.scale(enemy_image, (ENEMYSIZE, ENEMYSIZE))
							})
				enemyCounter = 0
				
			# Delete baddies that have fallen past the bottom.
			for b in enemies[:]:
				if b['rect'].top > WINDOWHEIGHT:
					enemies.remove(b)

			# draw the black background onto the surface
			screen.blit(background, backgroundRect)		
			# move the player
			if moveDown and player.bottom < WINDOWHEIGHT:
				player.top += MOVESPEED
			if moveUp and player.top > 0:
				player.top -= MOVESPEED
			if moveLeft and player.left > 0:
				player.left -= MOVESPEED
			if moveRight and player.right < WINDOWWIDTH:
				player.right += MOVESPEED
			# move the enemies
			for b in enemies:
				b['rect'].move_ip(0, ENEMYSPEED)
			# check for collisions

			for b in enemies:
				if player.colliderect(b['rect']):
					enemies.remove(b)
					playerHealth -= 20
					print (playerHealth)
			#check player health
			if playerHealth <= 0:
				gameOver = True

			# draw the player onto the surface
			screen.blit(player_image,(player))
			# draw the enemies
			for b in enemies:
				screen.blit(b['surface'], b['rect'])
			# draw the window onto the screen
			pygame.display.update()
			mainClock.tick(40)

				
		while gameOver == True:
			for event in pygame.event.get():
				if event.type == QUIT:
					pygame.quit()
					sys.exit()
				if event.type == KEYDOWN:
					if event.key == K_ESCAPE:
						pygame.quit()
						sys.exit()
					if event.key == ord('r'):
						for b in enemies:
							enemies.remove(b)
						enemies = []
						playerHealth = 100
						player = pygame.Rect(300, 700, 32, 32)
						moveLeft = False
						moveRight = False
						moveUp = False
						moveDown = False
						gameOver = False
			if playerHealth > 0:
					gameOver = False
				# draw the window onto the screen
			pygame.display.update()
			mainClock.tick(40)
	
if __name__ == '__main__': main()

