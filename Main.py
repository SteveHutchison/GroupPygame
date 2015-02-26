import pygame, sys, random
from pygame.locals import *

import fontRenderer
from fontRenderer import *

import asteroidFactory
from asteroidFactory import *

import fighterFactory
from fighterFactory import *

import player
from player import *

def main():
	# set up pygame
	pygame.init()
	mainClock = pygame.time.Clock()

	player_image = pygame.image.load("img/player.png")
	background = pygame.image.load("img/background.png")
	ASTEROID_image = pygame.image.load("img/Rock.png")
	BOSS_image = pygame.image.load("M:/groupPy/img/Spaceship.png")

	EXPLOSION_image = pygame.image.load("img/explosion_tiles.bmp")
	HEALTH_image = pygame.image.load("img/HealthPowerUp.png")

	BULLET_image = pygame.image.load("img/bullet.png")
	bulletSound_1  = pygame.mixer.Sound("M:/groupPy/audio/shoot_1.wav")
	bulletSound_2  = pygame.mixer.Sound("M:/groupPy/audio/shoot_2.wav")
	bulletSound_3  = pygame.mixer.Sound("M:/groupPy/audio/shoot_3.wav")

	#set up music
	pygame.mixer.music.load("audio/backgroundmusic.mp3")

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

	player = Player()
	
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

	# explosion variables
	EXPLOSIONFRAMES = 17
	EXPLOSIONSIZE = 200
	EXPLOSIONSCALE = 5
	explosions = []
	
	# health pick up variables
	HEALTHSIZE = 32
	HEALTHSPEED = 6
	healthpickups = []
	

	fontRenderer = FontRenderer()
	asteroids    = AsteroidFactory("M:/groupPy/img/Rock.png")
	fighters     = FighterFactory("img/enemy_1.png", "img/explosion_tiles.bmp", "audio\explosion_1.wav")

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
						#moveRight = False
						moveLeft = True
					if event.key == K_RIGHT or event.key == ord('d'):
						#moveLeft = False
						moveRight = True
					if event.key == K_UP or event.key == ord('w'):
						#moveDown = False
						moveUp = True
					if event.key == K_DOWN or event.key == ord('s'):
						#moveUp = False
						moveDown = True
					if event.key == K_SPACE:
						player.shooting = True
					if event.key == ord('z') and player.power < player.maxPower:
						player.power += 1
					if event.key == ord('x') and player.power > 1:
						player.power -= 1
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
						player.shooting = False
						bulletCounter = NEWBULLET

			# UPDATE EVERYTHING
			asteroids.spawn(WINDOWWIDTH)

			fighters.spawn(WINDOWWIDTH)
			
			bossfighterCounter += 1
			if bossfighterCounter == NEWBOSS:
							
				bossfighters.append({'rect': pygame.Rect(316, 0 - BOSSSIZE, BOSSSIZE, BOSSSIZE),
							'speed': (BOSSSPEEDX, BOSSSPEEDY),
							'surface':pygame.transform.scale(BOSS_image, (BOSSSIZE, BOSSSIZE))
							})
				boss_x = 316
				boss_y = 800 - (0 - BOSSSIZE)

			if player.shooting == True:
				bulletCounter += 1
				if bulletCounter >= NEWBULLET:
					bulletSound_1.play()
					bullets.append({'rect': pygame.Rect(player.x, player.y, BULLETSIZE, BULLETSIZE),
								'speed':  (0, BULLETSPEEDY),
								'surface':pygame.transform.scale(BULLET_image, (BULLETSIZE, BULLETSIZE))
								})
					if player.power >= 2:
						bulletSound_2.play()
						bullets.append({'rect': pygame.Rect(player.x, player.y, BULLETSIZE, BULLETSIZE),
									'speed': (BULLETSPEEDX, 0.95*BULLETSPEEDY), 
									'surface':pygame.transform.scale(BULLET_image, (BULLETSIZE, BULLETSIZE))
									})
						bullets.append({'rect': pygame.Rect(player.x, player.y, BULLETSIZE, BULLETSIZE),
									'speed':  (-BULLETSPEEDX, 0.95*BULLETSPEEDY),
									'surface':pygame.transform.scale(BULLET_image, (BULLETSIZE, BULLETSIZE))
									})
					if player.power >= 3:	
						bulletSound_3.play()		
						bullets.append({'rect': pygame.Rect(player.x, player.y, BULLETSIZE, BULLETSIZE),
									'speed': (2*BULLETSPEEDX, 0.9*BULLETSPEEDY), 
									'surface':pygame.transform.scale(BULLET_image, (BULLETSIZE, BULLETSIZE))
									})
						bullets.append({'rect': pygame.Rect(player.x, player.y, BULLETSIZE, BULLETSIZE),
									'speed':  (-2*BULLETSPEEDX, 0.9*BULLETSPEEDY),
									'surface':pygame.transform.scale(BULLET_image, (BULLETSIZE, BULLETSIZE))
									})
					if player.power >= 4:	
						bullets.append({'rect': pygame.Rect(player.x, player.y, BULLETSIZE, BULLETSIZE),
									'speed': (3*BULLETSPEEDX, 0.8*BULLETSPEEDY), 
									'surface':pygame.transform.scale(BULLET_image, (BULLETSIZE, BULLETSIZE))
									})
						bullets.append({'rect': pygame.Rect(player.x, player.y, BULLETSIZE, BULLETSIZE),
									'speed':  (-3*BULLETSPEEDX, 0.8*BULLETSPEEDY),
									'surface':pygame.transform.scale(BULLET_image, (BULLETSIZE, BULLETSIZE))
									})
					bulletCounter = 0

			# Delete things that are outside the screen
			player.score += asteroids.remove(WINDOWHEIGHT)

			fighters.remove(WINDOWHEIGHT)
					
			for b in bullets[:]:
				if b['rect'].bottom < 0:
					bullets.remove(b)
					
			for e in explosions[:]:
				e['frame'] = e['frame'] + 1
				if e['frame'] >= 18:
					explosions.remove(e)

			# move the player
			if moveDown and player.rect.bottom < WINDOWHEIGHT:
				player.rect.top += MOVESPEED
				player.y += MOVESPEED
			if moveUp and player.rect.top > 0:
				player.rect.top -= MOVESPEED
				player.y -= MOVESPEED
			if moveLeft and player.rect.left > 0:
				player.rect.left -= MOVESPEED
				player.x -= MOVESPEED
			if moveRight and player.rect.right < WINDOWWIDTH:
				player.rect.right += MOVESPEED
				player.x += MOVESPEED

			# move the asteroids
			asteroids.move()

			fighters.move()

			# for b in fighters:
			# 	b['rect'].move_ip(0, b['speed'])

			for b in bossfighters:
				if boss_y > 650:
					b['rect'].move_ip(0, BOSSSPEEDY)
					boss_y -= BOSSSPEEDY
					#print (boss_y)
				if boss_x < player.x-48:
					b['rect'].move_ip(BOSSSPEEDX, 0)
					boss_x += BOSSSPEEDX
				if boss_x > player.x-48:
					b['rect'].move_ip(-BOSSSPEEDX, 0)
					boss_x -= BOSSSPEEDX
				
			for b in bullets:
				b['rect'].move_ip(b['speed'])
				
			for b in healthpickups:
				b['rect'].move_ip(0, b['speed'])



			player.score += fighters.collide_bullets(bullets, explosions, EXPLOSIONSIZE, EXPLOSIONSCALE, EXPLOSIONFRAMES, healthpickups, HEALTHSIZE, HEALTHSPEED, HEALTH_image)


			# TODO make this the other way round,
			# bullets should be removed if they are touching asteroids
			asteroids.collide_bullets(bullets)
			
			player.health = asteroids.collide_player(player.rect, player.health)

			player.health = fighters.collide_player(player.rect, player.health)

			for b in healthpickups:
				if player.rect.colliderect(b['rect']):
					healthpickups.remove(b)
					player.health += 20
					if player.health > 100:
						player.health = 100
					
			#check player health
			if player.health <= 0:
				gameOver = True


			# DRAW PHASE

			# draw the scrolling backgound
			backgroundY = backgroundY + 1
			if backgroundY == 800:
				backgroundY = 0
				
			screen.blit(background, (0,backgroundY))
			screen.blit(background,(0, backgroundY-800))

			screen.blit(player_image,(player.rect))

			asteroids.draw(screen)

			fighters.draw(screen)

			# for f in fighters:
			# 	screen.blit(f['surface'], f['rect'])

			for b in bullets:
				screen.blit(b['surface'], b['rect'])	
			for b in bossfighters:
				screen.blit(b['surface'], b['rect'])
			for b in healthpickups:
				screen.blit(b['surface'], b['rect'])
			for e in explosions:
				screen.blit(e['surface'], e['rect'], pygame.Rect((e['frame']*EXPLOSIONSIZE)/5,0,EXPLOSIONSIZE/5,EXPLOSIONSIZE/5))

			# draw the stats
			fontRenderer.draw_stat("Score: ", player.score, (10,10), screen)
			fontRenderer.draw_stat("Health: ", player.health, (10, 40), screen)

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
						# reset everything
						asteroids.remove_all()
						fighters.remove_all()
						for b in bullets:
							bullets.remove(b)
						bullets = []
						for b in bossfighters:
							bossfighters.remove(b)
						bossfighters = []
						for b in healthpickups:
							healthpickups.remove(b)
						healthpickups = []
						bossfighterCounter = 0
						player.health = 100
						player.score = 0
						player.rect = pygame.Rect(300, 700, 32, 32)
						player.x = 316
						player.y = 700
						player.shooting = False
						gameOver = False
						moveLeft = False
						moveRight = False
						moveDown = False
						moveUp = False

			fontRenderer.draw_title("Press R to retry", (100, 300), screen)

			if player.health > 0:
					gameOver = False
					
			# draw the window onto the screen
			pygame.display.update()
			mainClock.tick(40)

	
if __name__ == '__main__': main()

