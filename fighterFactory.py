import pygame, random

class FighterFactory:
	def __init__(self, image_path, death_image_path, death_sound_path):
		self.image      = pygame.image.load(image_path)
		self.deathImage = pygame.image.load(death_image_path)
		self.deathSound = pygame.mixer.Sound(death_sound_path)
		self.frameBetweenSpawns = 20
		self.counter = 0
		self.speed   = 12
		self.size    = 30
		self.reward  = 50
		self.fighters = []
		self.damage = 30

	def spawn(self, width):
		self.counter += 1
		if self.counter >= self.frameBetweenSpawns:
			self.fighters.append({'rect': pygame.Rect(random.randint(0, width-self.size), 0 - self.size, self.size, self.size),
						'speed': self.speed ,
						'surface':pygame.transform.scale(self.image, (self.size, self.size))
						})
			self.counter = 0

	def remove(self, height):
		for a in self.fighters[:]:
			if a['rect'].top > height:
				self.fighters.remove(a)

	def move(self):
		for f in self.fighters:
			f['rect'].move_ip(0, f['speed'])

	def draw(self, target):
		for f in self.fighters:
			target.blit(f['surface'], f['rect'])

	def collide_bullets(self, bullets, explosions, expsize, expscale, expframes, healthpickups, HEALTHSIZE, HEALTHSPEED, HEALTH_image):
		fightersDestoryed = 0

		for i in bullets:
				for f in self.fighters:
					if (i['rect']).colliderect(f['rect']):
						explosions.append({'frame': 0,
						'rect': pygame.Rect(f['rect'].left, f['rect'].top, expsize, expsize),
						'surface':pygame.transform.scale(self.deathImage, (expsize*expframes/expscale, expsize/expscale))}) 
						self.fighters.remove(f)
						bullets.remove(i)
						fightersDestoryed += 1

						z = random.randint(1, 10)
						if z > 8:
							healthpickups.append({'rect': pygame.Rect(f['rect'].left, f['rect'].top, HEALTHSIZE, HEALTHSIZE),
								'speed': HEALTHSPEED,
								'surface':pygame.transform.scale(HEALTH_image, (HEALTHSIZE, HEALTHSIZE))})
							

						self.deathSound.play()

		# add up the amount of fighters destroyed and modify the score
		return (self.reward * fightersDestoryed)

	def collide_player(self, playerRect, playerHealth):
		for b in self.fighters:
			if playerRect.colliderect(b['rect']):
				self.fighters.remove(b)
				self.deathSound.play()
				return playerHealth - self.damage
		return playerHealth

	def remove_all(self):
		for a in self.fighters:
			self.fighters.remove(a)
		self.fighters = []