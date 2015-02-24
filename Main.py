import sys, pygame
import random
from pygame.locals import *

pygame.init()

ball = pygame.image.load("M:/groupPy/img/player.png")
background = pygame.image.load("M:/groupPy/img/background.png")

ballrect = ball.get_rect()
backgroundRect = background.get_rect()

size = (width, height) = background.get_size()
screen = pygame.display.set_mode(size)

b3x = 200
b3y = 768
movex = 2
movey = 0

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
	
	if right == True:
		b3x += movex
		
	if left == True:
		b3x -= movex
	
	screen.blit(background, backgroundRect)
	screen.blit(ball,(b3x,b3y))
	
	pygame.display.flip()