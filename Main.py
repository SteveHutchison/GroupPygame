import pygame, sys, random
from pygame.locals import *

def main():
	# set up pygame
	pygame.init()
	mainClock = pygame.time.Clock()

	player_image = pygame.image.load("M:/groupPy/img/player.png")
	background = pygame.image.load("M:/groupPy/img/background.png")
	ASTEROID_image = pygame.image.load("M:/groupPy/img/Rock.png")
	FIGHTER_image = pygame.image.load("M:/groupPy/img/enemy_1.png")

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
	

	score = 0


	asteroidCounter = 0
	NEWASTEROID = 20
	ASTEROIDSIZE = 50
	ASTEROIDMAXSPEED = 5
	ASTEROIDMINSPEED = 3
	asteroids = []

	fighterCounter = 0
	NEWFIGHTER = 20
	FIGHTERSIZE = 30
	FIGHTERSPEED = 12
	fighters = []

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
						

			asteroidCounter += 1
			if asteroidCounter >= NEWASTEROID:

							
				asteroids.append({'rect': pygame.Rect(random.randint(0, WINDOWWIDTH-ASTEROIDSIZE), 0 - ASTEROIDSIZE, ASTEROIDSIZE, ASTEROIDSIZE),
							'speed': random.randint(ASTEROIDMINSPEED, ASTEROIDMAXSPEED),
							'surface':pygame.transform.scale(ASTEROID_image, (ASTEROIDSIZE, ASTEROIDSIZE))
							})
				asteroidCounter = 0
				
			fighterCounter += 1
			if fighterCounter >= NEWFIGHTER:
							
				fighters.append({'rect': pygame.Rect(random.randint(0, WINDOWWIDTH-FIGHTERSIZE), 0 - FIGHTERSIZE, FIGHTERSIZE, FIGHTERSIZE),
							'speed': FIGHTERSPEED,
							'surface':pygame.transform.scale(FIGHTER_image, (FIGHTERSIZE, FIGHTERSIZE))
							})
				fighterCounter = 0
				
			# Delete baddies that have fallen past the bottom.
			for b in asteroids[:]:
				if b['rect'].top > WINDOWHEIGHT:
					asteroids.remove(b)
					score += 10
			
			for b in fighters[:]:
				if b['rect'].top > WINDOWHEIGHT:
					fighters.remove(b)
					score += 10


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
			# move the asteroids
			for b in asteroids:
				b['rect'].move_ip(0, b['speed'])
			for b in fighters:
				b['rect'].move_ip(0, FIGHTERSPEED)
			# check for collisions

			for b in asteroids:
				if player.colliderect(b['rect']):
					asteroids.remove(b)
					playerHealth -= 20
					print (playerHealth)
			
			for b in fighters:
				if player.colliderect(b['rect']):
					fighters.remove(b)
					playerHealth -= 30
					print (playerHealth)
			#check player health
			if playerHealth <= 0:
				gameOver = True

			# draw the player onto the surface
			screen.blit(player_image,(player))

			# draw the asteroids
			for b in asteroids:
				screen.blit(b['surface'], b['rect'])
			for b in fighters:
				screen.blit(b['surface'], b['rect'])		
			#draw score
			#draw text on screen
			font = pygame.font.Font(None, 36)
			text = font.render("Score: ", 1, (255, 0, 0))
			scoreDisplay = font.render(str(score), 1, (255, 0, 0))
			Scorepos = (100, 10)
			textpos = (10, 10)
			screen.blit(text, textpos)
			screen.blit(scoreDisplay, Scorepos)
			
			#draw health
			#draw text on screen
			#healthfont = pygame.font.Font(None, 36)
			healthtext = font.render("Health: ", 1, (255, 0, 0))
			healthDisplay = font.render(str(playerHealth), 1, (255, 0, 0))
			healthpos = (100, 40)
			healthtextpos = (10, 40)
			screen.blit(healthtext, healthtextpos)
			screen.blit(healthDisplay, healthpos)

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
						for b in asteroids:
							asteroids.remove(b)
						asteroids = []
						for b in fighters:
							fighters.remove(b)
						fighters = []
						playerHealth = 100
						score = 0
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

