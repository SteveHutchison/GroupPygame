import sys, pygame
import random
pygame.init()

ball = pygame.image.load("ball.bmp")
background = pygame.image.load("BG.bmp")

ballrect = ball.get_rect()
backgroundRect = background.get_rect()

size = (width, height) = background.get_size()
screen = pygame.display.set_mode(size)

b3x = 200
b3y = 0
movex = 0
movey = 0

while 1:
	for event in pygame.event.get():
		if event.type == pygame.QUIT: sys.exit()
		
		if event.type==pygame.KEYDOWN:
			if event.key==pygame.K_LEFT:
				movex =- 1
			elif event.key==pygame.K_RIGHT:
				movex =+ 1
				
		if event.type==pygame.KEYUP:
			if event.key==pygame.K_LEFT:
				movex = 0
			elif event.key==pygame.K_RIGHT:
				movex = 0
				
	if b3x + movex < 0 or b3x + ballrect.width + movex > backgroundRect.width:
		movex = 0

	b3x +=movex
	
	screen.blit(background, backgroundRect)
	screen.blit(ball,(b3x,b3y))
	
	pygame.display.flip()