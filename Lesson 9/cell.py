import pygame
import random

class Cell:
	def __init__(self, cell_id, cell_x, cell_y):
		self.id = cell_id
		self.x = cell_x
		self.y = cell_y
		self.direction_x = random.choice([-1, 0, 1])
		self.direction_y = random.choice([-1, 0, 1])
		self.speed_x = random.uniform(0.2, 1)
		self.speed_y = random.uniform(0.2, 1)
		self.change_direction_probability = 0.01
		self.change_speed_probability = 0.01

	def print_details(self):
		print(f"Cell ID: {self.id}, Position: ({self.x}, {self.y}), Type: {self.type}")

	def update(self, screen_width, screen_height):
		if random.random() < self.change_direction_probability:
			self.direction_x = random.choice([-1, 0, 1])
			self.direction_y = random.choice([-1, 0, 1])
		if random.random() < self.change_speed_probability:
			self.speed_x = random.uniform(0.2, 1)
			self.speed_y = random.uniform(0.2, 1)
		self.x += self.direction_x * self.speed_x
		self.y += self.direction_y * self.speed_y

		if self.x <= 0:
			self.x = 0
			self.direction_x *= -1
		if self.x >= screen_width - self.image.get_width():
			self.x = screen_width - self.image.get_width()
			self.direction_x *= -1
		if self.y <= 0:
			self.y = 0
			self.direction_y *= -1
		if self.y >= screen_height - self.image.get_height():
			self.y = screen_height - self.image.get_height()
			self.direction_y *= -1

	def draw(self, window):
		window.blit(self.image, (self.x, self.y))
		pygame.draw.rect(window, "red", (self.x, self.y, self.image.get_width(), self.image.get_height()), 2)
		pygame.draw.circle(window, "red", (self.x, self.y), 5)

class Stinger(Cell):
	type = "Stinger"
	image = pygame.image.load("Graphics/life_2.png")

class Amoeba(Cell):
	type = "Amoeba"
	image = pygame.image.load("Graphics/life_1.png")

class Hunter(Cell):
	type = "Hunter"
	image = pygame.image.load("Graphics/life_4.png")

class Jumper(Cell):
	type = "Jumper"
	image = pygame.image.load("Graphics/life_3.png")