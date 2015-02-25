# asteroidFactory
import pygame, random

class AsteroidFactory:

	def __init__(self, file_path):
		## variables declared here are unique to each instance

		self.image = pygame.image.load(file_path)

		self.SIZE = 50
		self.MAX_SPEED = 5
		self.MIN_SPEED = 2

		self.counter = 0

		# whenever counter => spawnrate a new asteroid is made
		self.frameBetweenSpawns = 40

		self.asteroids = []

		# how many points to give the player when an asteroid
		# leaves the screen
		self.reward = 10
		# how much to hurt the player if they hit the asteroid
		self.damage = 20

	def spawn(self, width):
		self.counter += 1

		if self.counter >= self.frameBetweenSpawns:
			self.asteroids.append({'rect': pygame.Rect(random.randint(0, width - self.SIZE), 0 - self.SIZE, self.SIZE, self.SIZE),
						'speed': random.randint(self.MIN_SPEED, self.MAX_SPEED),
						'surface':pygame.transform.scale(self.image, (self.SIZE, self.SIZE)),
						'health': 100
						})
			self.counter = 0


	def remove(self, score, height):
			for a in self.asteroids[:]:
				if a['rect'].top > height:
					self.asteroids.remove(a)
					score += self.reward
				elif a['health'] <= 0:
					self.asteroids.remove(a)

	def move(self):
		for a in self.asteroids:
			a['rect'].move_ip(0, a['speed'])

	def draw(self, target):
		for a in self.asteroids:
			target.blit(a['surface'], a['rect'])

	def collide_bullets(self, bullets):
		for a in self.asteroids:
			for b in bullets:
				if (b['rect']).colliderect(a['rect']):
					bullets.remove(b)
					a['health'] -= 10

	def collide_player(self, playerRect, playerHealth):
		for a in self.asteroids:
			if playerRect.colliderect(a['rect']):
				self.asteroids.remove(a)
				return playerHealth - self.damage
		return playerHealth

	def remove_all(self):
		for a in self.asteroids:
			self.asteroids.remove(a)
		asteroids = []