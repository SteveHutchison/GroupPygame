import pygame, sys, random
from pygame.locals import *

import fontRenderer
from fontRenderer import *

def main():
	# set up pygame
	pygame.init()
	mainClock = pygame.time.Clock()

	player_image = pygame.image.load("img/player.png")
	background = pygame.image.load("img/background.png")
	ASTEROID_image = pygame.image.load("img/Rock.png")
	FIGHTER_image = pygame.image.load("img/enemy_1.png")
	BULLET_image = pygame.image.load("img/bullet.png")
	EXPLOSION_image = pygame.image.load("img/explosion_tiles.bmp")

	#set up music
	pygame.mixer.music.load('audio/backgroundmusic.mp3')
	
	backgroundRect = background.get_rect()

	# set up the window
	WINDOWWIDTH = 600
	WINDOWHEIGHT = 800
	screen = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT), 0, 32)
	pygame.display.set_caption('Roid Rage')

	font = pygame.font.Font(None, 36)

	# set up gameplay variables
	moveLeft = False
	moveRight = False
	moveUp = False
	moveDown = False

	MOVESPEED = 8

	gameOver = False
	gameRunning = True

	# set up the colors
	BLACK = (0, 0, 0)
	GREEN = (0, 255, 0)
	RED = (255, 0, 0)
	BLUE = (0, 0, 255)
	RANDOMCOLOUR = (random.randint(0, 255),random.randint(0, 255),random.randint(0, 255))
	WHITE = (255, 255, 255)

	# player variables
	score = 0
	playerHealth = 100
	player = pygame.Rect(300, 700, 32, 32)
	player_x = 316
	player_y = 700
	shooting = False
	max_power = 4
	power = 1
	
	# player bullet variables
	bulletCounter = 0
	NEWBULLET = 5
	BULLETSIZE = 8
	BULLETSPEEDY = -25
	BULLETSPEEDX = 5
	bullets = []

	# asteroid variables
	asteroidCounter = 0
	NEWASTEROID = 20
	ASTEROIDSIZE = 50
	ASTEROIDMAXSPEED = 5
	ASTEROIDMINSPEED = 3
	asteroids = []

	# fighter variables
	fighterCounter = 0
	NEWFIGHTER = 20
	FIGHTERSIZE = 30
	FIGHTERSPEED = 12
	fighters = []
	
	# explosion variables
	frames = 17
	EXPLOSIONSIZE = 200
	EXPLOSIONSCALE = 5
	explosions = []

	fontRenderer = FontRenderer()

	while gameRunning == True:
		# start music loop
		pygame.mixer.music.play(5) 
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
					if event.key == K_SPACE:
						shooting = True
					if event.key == ord('z') and power < max_power:
						power += 1
					if event.key == ord('x') and power > 1:
						power -= 1
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
					if event.key == K_SPACE:
						shooting = False
						
			# draw the black background onto the surface
			screen.blit(background, backgroundRect)	
			# add new enemies
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

			if shooting == True:
				bulletCounter += 1
				if bulletCounter >= NEWBULLET:
					bullets.append({'rect': pygame.Rect(player_x, player_y, BULLETSIZE, BULLETSIZE),
								'speed':  (0, BULLETSPEEDY),
								'surface':pygame.transform.scale(BULLET_image, (BULLETSIZE, BULLETSIZE))
								})
					if power >= 2:
						bullets.append({'rect': pygame.Rect(player_x, player_y, BULLETSIZE, BULLETSIZE),
									'speed': (BULLETSPEEDX, BULLETSPEEDY), 
									'surface':pygame.transform.scale(BULLET_image, (BULLETSIZE, BULLETSIZE))
									})
						bullets.append({'rect': pygame.Rect(player_x, player_y, BULLETSIZE, BULLETSIZE),
									'speed':  (-BULLETSPEEDX, BULLETSPEEDY),
									'surface':pygame.transform.scale(BULLET_image, (BULLETSIZE, BULLETSIZE))
									})
					if power >= 3:			
						bullets.append({'rect': pygame.Rect(player_x, player_y, BULLETSIZE, BULLETSIZE),
									'speed': (2*BULLETSPEEDX, 0.95*BULLETSPEEDY), 
									'surface':pygame.transform.scale(BULLET_image, (BULLETSIZE, BULLETSIZE))
									})
						bullets.append({'rect': pygame.Rect(player_x, player_y, BULLETSIZE, BULLETSIZE),
									'speed':  (-2*BULLETSPEEDX, 0.95*BULLETSPEEDY),
									'surface':pygame.transform.scale(BULLET_image, (BULLETSIZE, BULLETSIZE))
									})
					if power >= 4:	
						bullets.append({'rect': pygame.Rect(player_x, player_y, BULLETSIZE, BULLETSIZE),
									'speed': (3*BULLETSPEEDX, 0.85*BULLETSPEEDY), 
									'surface':pygame.transform.scale(BULLET_image, (BULLETSIZE, BULLETSIZE))
									})
						bullets.append({'rect': pygame.Rect(player_x, player_y, BULLETSIZE, BULLETSIZE),
									'speed':  (-3*BULLETSPEEDX, 0.85*BULLETSPEEDY),
									'surface':pygame.transform.scale(BULLET_image, (BULLETSIZE, BULLETSIZE))
									})
					bulletCounter = 0
			# Delete baddies that have fallen past the bottom.
			for b in asteroids[:]:
				if b['rect'].top > WINDOWHEIGHT:
					asteroids.remove(b)
					score += 10
			
			for b in fighters[:]:
				if b['rect'].top > WINDOWHEIGHT:
					fighters.remove(b)
					score += 10
					
			for b in bullets[:]:
				if b['rect'].bottom < 0:
					bullets.remove(b)
					
			for e in explosions[:]:
				e['frame'] = e['frame'] + 1
				if e['frame'] >= 18:
					explosions.remove(e)


			# draw the black background onto the surface
			screen.blit(background, backgroundRect)		
			
			# move the player
			if moveDown and player.bottom < WINDOWHEIGHT:
				player.top += MOVESPEED
				player_y += MOVESPEED
			if moveUp and player.top > 0:
				player.top -= MOVESPEED
				player_y -= MOVESPEED
			if moveLeft and player.left > 0:
				player.left -= MOVESPEED
				player_x -= MOVESPEED
			if moveRight and player.right < WINDOWWIDTH:
				player.right += MOVESPEED
				player_x += MOVESPEED

			# move the asteroids
			for b in asteroids:
				b['rect'].move_ip(0, b['speed'])
			for b in fighters:
				b['rect'].move_ip(0, b['speed'])
			for b in bullets:
				b['rect'].move_ip(b['speed'])
			# check for collisions

			for i in bullets:
				for b in fighters:
					if (i['rect']).colliderect(b['rect']):
						explosions.append({'frame': 0,
						'rect': pygame.Rect(b['rect'].left, b['rect'].top, EXPLOSIONSIZE, EXPLOSIONSIZE),
						'surface':pygame.transform.scale(EXPLOSION_image, (EXPLOSIONSIZE*17/5, EXPLOSIONSIZE/5))}) 
						score += 100
						bullets.remove(i)
						fighters.remove(b)
						
			for b in asteroids:
				for i in bullets:
					if (i['rect']).colliderect(b['rect']):
						bullets.remove(i)
						
			for b in asteroids:
				if player.colliderect(b['rect']):
					asteroids.remove(b)
					playerHealth -= 20
					print (playerHealth)
					effect = pygame.mixer.Sound('audio\explosion.ogg')
					effect.play()
				
			for b in fighters:
				if player.colliderect(b['rect']):
					fighters.remove(b)
					playerHealth -= 30
					print (playerHealth)
					effect = pygame.mixer.Sound('audio\explosion.ogg')
					effect.play()

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
			for b in bullets:
				screen.blit(b['surface'], b['rect'])	
			for b in explosions:
				screen.blit(b['surface'], b['rect'], pygame.Rect((b['frame']*EXPLOSIONSIZE)/5,0,EXPLOSIONSIZE/5,EXPLOSIONSIZE/5))



			# draw the stats
			fontRenderer.draw_stat("Score: ", score, (10,10), screen)
			fontRenderer.draw_stat("Health: ", playerHealth, (10, 40), screen)


			# draw the window onto the screen
			pygame.display.update()
			mainClock.tick(100)

				
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
						for b in bullets:
							bullets.remove(b)
						bullets = []
						playerHealth = 100
						score = 0
						player = pygame.Rect(300, 700, 32, 32)
						player_x = 316
						player_y = 700
						moveLeft = False
						moveRight = False
						moveUp = False
						moveDown = False
						gameOver = False

			fontRenderer.draw_title("Press R to retry", (100, 300), screen)

			if playerHealth > 0:
					gameOver = False
					
			# draw the window onto the screen
			pygame.display.update()
			mainClock.tick(40)
	
if __name__ == '__main__': main()

