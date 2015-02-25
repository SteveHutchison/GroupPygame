import pygame, sys, random
from pygame.locals import *

import fontRenderer
from fontRenderer import *

import asteroidFactory
from asteroidFactory import *

def main():
	# set up pygame
	pygame.init()
	mainClock = pygame.time.Clock()

	player_image = pygame.image.load("img/player.png")
	background = pygame.image.load("img/background.png")
	ASTEROID_image = pygame.image.load("img/Rock.png")
	FIGHTER_image = pygame.image.load("img/enemy_1.png")
	BOSS_image = pygame.image.load("M:/groupPy/img/Spaceship.png")
	BULLET_image = pygame.image.load("img/bullet.png")
	EXPLOSION_image = pygame.image.load("img/explosion_tiles.bmp")

	#set up music
	pygame.mixer.music.load('audio/backgroundmusic.mp3')

	backgroundRect = background.get_rect()
	backgroundArea = backgroundRect
	backgroundY = 0;

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
	
	# boss fighter variables
	bossfighterCounter = 0
	boss_x = 0
	boss_y = 0
	NEWBOSS = 200
	BOSSSIZE = 96
	BOSSSPEEDY = 4
	BOSSSPEEDX = 4
	bossfighters = []

	# fighter variables
	fighterCounter = 0
	NEWFIGHTER = 20
	FIGHTERSIZE = 30
	FIGHTERSPEED = 12
	fighters = []
	
	# explosion variables
	EXPLOSIONFRAMES = 17
	EXPLOSIONSIZE = 200
	EXPLOSIONSCALE = 5
	explosions = []

	fontRenderer = FontRenderer()

	asteroids    = AsteroidFactory("M:/groupPy/img/Rock.png")

	while gameRunning == True:
		# start music loop
		pygame.mixer.music.play(5) 
		while gameOver == False:
			# PROCCESS EVENTS
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

			# UPDATE EVERYTHING
			asteroids.spawn(WINDOWWIDTH)

				
			fighterCounter += 1
			if fighterCounter >= NEWFIGHTER:
							
				fighters.append({'rect': pygame.Rect(random.randint(0, WINDOWWIDTH-FIGHTERSIZE), 0 - FIGHTERSIZE, FIGHTERSIZE, FIGHTERSIZE),
							'speed': FIGHTERSPEED,
							'surface':pygame.transform.scale(FIGHTER_image, (FIGHTERSIZE, FIGHTERSIZE))
							})
				fighterCounter = 0
			
			bossfighterCounter += 1
			if bossfighterCounter == NEWBOSS:
							
				bossfighters.append({'rect': pygame.Rect(316, 0 - BOSSSIZE, BOSSSIZE, BOSSSIZE),
							'speed': (BOSSSPEEDX, BOSSSPEEDY),
							'surface':pygame.transform.scale(BOSS_image, (BOSSSIZE, BOSSSIZE))
							})
				boss_x = 316
				boss_y = 800 - (0 - BOSSSIZE)

			
			if shooting == True:
				bulletCounter += 1
				if bulletCounter >= NEWBULLET:
					bullets.append({'rect': pygame.Rect(player_x, player_y, BULLETSIZE, BULLETSIZE),
								'speed':  (0, BULLETSPEEDY),
								'surface':pygame.transform.scale(BULLET_image, (BULLETSIZE, BULLETSIZE))
								})
					if power >= 2:
						bullets.append({'rect': pygame.Rect(player_x, player_y, BULLETSIZE, BULLETSIZE),
									'speed': (BULLETSPEEDX, 0.95*BULLETSPEEDY), 
									'surface':pygame.transform.scale(BULLET_image, (BULLETSIZE, BULLETSIZE))
									})
						bullets.append({'rect': pygame.Rect(player_x, player_y, BULLETSIZE, BULLETSIZE),
									'speed':  (-BULLETSPEEDX, 0.95*BULLETSPEEDY),
									'surface':pygame.transform.scale(BULLET_image, (BULLETSIZE, BULLETSIZE))
									})
					if power >= 3:			
						bullets.append({'rect': pygame.Rect(player_x, player_y, BULLETSIZE, BULLETSIZE),
									'speed': (2*BULLETSPEEDX, 0.9*BULLETSPEEDY), 
									'surface':pygame.transform.scale(BULLET_image, (BULLETSIZE, BULLETSIZE))
									})
						bullets.append({'rect': pygame.Rect(player_x, player_y, BULLETSIZE, BULLETSIZE),
									'speed':  (-2*BULLETSPEEDX, 0.9*BULLETSPEEDY),
									'surface':pygame.transform.scale(BULLET_image, (BULLETSIZE, BULLETSIZE))
									})
					if power >= 4:	
						bullets.append({'rect': pygame.Rect(player_x, player_y, BULLETSIZE, BULLETSIZE),
									'speed': (3*BULLETSPEEDX, 0.8*BULLETSPEEDY), 
									'surface':pygame.transform.scale(BULLET_image, (BULLETSIZE, BULLETSIZE))
									})
						bullets.append({'rect': pygame.Rect(player_x, player_y, BULLETSIZE, BULLETSIZE),
									'speed':  (-3*BULLETSPEEDX, 0.8*BULLETSPEEDY),
									'surface':pygame.transform.scale(BULLET_image, (BULLETSIZE, BULLETSIZE))
									})
					bulletCounter = 0

			# Delete things that are outside the screen
			asteroids.remove(score, WINDOWHEIGHT)

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
			asteroids.move()

			for b in fighters:
				b['rect'].move_ip(0, b['speed'])
			for b in bossfighters:
				if boss_y > 650:
					b['rect'].move_ip(0, BOSSSPEEDY)
					boss_y -= BOSSSPEEDY
					#print (boss_y)
				if boss_x < player_x-48:
					b['rect'].move_ip(BOSSSPEEDX, 0)
					boss_x += BOSSSPEEDX
				if boss_x > player_x-48:
					b['rect'].move_ip(-BOSSSPEEDX, 0)
					boss_x -= BOSSSPEEDX
				
			for b in bullets:
				b['rect'].move_ip(b['speed'])

			# check for collisions
			for i in bullets:
				for b in fighters:
					if (i['rect']).colliderect(b['rect']):
						explosions.append({'frame': 0,
						'rect': pygame.Rect(b['rect'].left, b['rect'].top, EXPLOSIONSIZE, EXPLOSIONSIZE),
						'surface':pygame.transform.scale(EXPLOSION_image, (EXPLOSIONSIZE*EXPLOSIONFRAMES/EXPLOSIONSCALE, EXPLOSIONSIZE/EXPLOSIONSCALE))}) 
						score += 100
						bullets.remove(i)
						fighters.remove(b)

			# TODO make this the other way round,
			# bullets should be removed if they are touching asteroids
			asteroids.remove_if_touching(bullets)
			
			playerHealth = asteroids.collide_and_hurt(player, playerHealth)

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


			# DRAW PHASE
			# draw the black background onto the surface
			backgroundY = backgroundY + 1
			if backgroundY == 800:
				backgroundY = 0
				
			screen.blit(background, (0,backgroundY))
			screen.blit(background,(0, backgroundY-800))

			screen.blit(player_image,(player))

			asteroids.draw(screen)

			for f in fighters:
				screen.blit(f['surface'], f['rect'])	
			for b in bullets:
				screen.blit(b['surface'], b['rect'])	
			for b in bossfighters:
				screen.blit(b['surface'], b['rect'])	
			for e in explosions:
				screen.blit(e['surface'], e['rect'], pygame.Rect((e['frame']*EXPLOSIONSIZE)/5,0,EXPLOSIONSIZE/5,EXPLOSIONSIZE/5))

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
						asteroids.remove_all()

						for b in fighters:
							fighters.remove(b)
						fighters = []
						for b in bullets:
							bullets.remove(b)
						bullets = []
						for b in bossfighters:
							bossfighters.remove(b)
						bossfighters = []
						bossfighterCounter = 0
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

