import pygame, random

class Player:
	rect = pygame.Rect(300, 700, 32, 32)
	x = rect.x + (rect.width/2)
	y = rect.y + (rect.height/2)
	score = 0
	maxHealth = 100
	health = 100
	shooting = False
	maxPower = 4
	power = 1

	def __init__(self):
		pass

	def reset(self, x, y):
		self.rect = pygame.Rect(x, y, 32, 32)
		self.health = 100
		self.score = 0
		self.x = 316
		self.y = 700
		self.shooting = False
		self.power = 1

	def collide_health(self, health, amount):
		for h in health:
				if self.rect.colliderect(h['rect']):
					health.remove(h)

					# add health up to max
					self.health += amount

					# if you get more health than you need add it to your score
					if self.health > self.maxHealth:
						self.score += (self.health - self.maxHealth) * 2
						self.health = self.maxHealth
