import pygame
import random

class Cell:
	def __init__(self, cell_id, cell_x, cell_y, cell_size):
		self.__id = cell_id
		self._x = cell_x
		self._y = cell_y
		self._direction_x = random.choice([-1, 0, 1])
		self._direction_y = random.choice([-1, 0, 1])
		self._speed_x = random.uniform(0.2, 1)
		self._speed_y = random.uniform(0.2, 1)
		self._change_direction_probability = 0.01
		self._change_speed_probability = 0.01
		self._energy = random.randint(50, 100)
		self._alive = True
		self.__frame_count = 0
		self.__size = cell_size.get_size()
		self._image = self.__scale_image(self._image, cell_size.get_scale())

	def get_size(self):
		return self.__size

	def __scale_image(self, image, scale):
		original_width = image.get_width()
		original_height = image.get_height()
		new_width = int(original_width * scale)
		new_height = int(original_height * scale)
		return pygame.transform.smoothscale(image, (new_width, new_height))

	def is_alive(self):
		return self._alive

	def get_id(self):
		return self.__id

	def get_position(self):
		x = int(self._x)
		y = int(self._y)
		return f"({x}, {y})"

	def get_type(self):
		return self._type

	def get_energy_level(self):
		if self._energy < 15:
			energy_level = "Critical"
		elif 15 <= self._energy <= 50:
			energy_level = "Moderate"
		elif 50 < self._energy <= 80:
			energy_level = "High"
		else:
			energy_level = "Very High"

		return energy_level

	def _draw_energy(self, window):
		if self._energy < 15:
			color = "red"
		elif 15 <= self._energy < 50:
			color = "orange"
		else:
			color = "green"

		bar_width = self._image.get_width()
		bar_height = 5
		energy_bar_width = bar_width * (self._energy/100)

		bar_x = self._x
		bar_y = self._y - 10

		pygame.draw.rect(window, "black", (bar_x -1, bar_y - 1, bar_width + 2, bar_height + 2))
		pygame.draw.rect(window, color, (bar_x, bar_y, energy_bar_width, bar_height))

	def __decrease_energy(self):
		self.__frame_count += 1
		if self.__frame_count >= 60:
			self._energy -= 1
			self.__frame_count = 0
		if self._energy == 0:
			self._alive = False		

	def update(self, screen_width, screen_height):
		self._move()
		self.__constraint_position(screen_width, screen_height)
		self.__decrease_energy()
		
	def _move(self):
		if random.random() < self._change_direction_probability:
			self._direction_x = random.choice([-1, 0, 1])
			self._direction_y = random.choice([-1, 0, 1])
		if random.random() < self._change_speed_probability:
			self._speed_x = random.uniform(0.2, 1)
			self._speed_y = random.uniform(0.2, 1)
		self._x += self._direction_x * self._speed_x
		self._y += self._direction_y * self._speed_y

	def __constraint_position(self, screen_width, screen_height):
		if self._x <= 0:
			self._x = 0
			self._direction_x *= -1
		if self._x >= screen_width - self._image.get_width():
			self._x = screen_width - self._image.get_width()
			self._direction_x *= -1
		if self._y <= 0:
			self._y = 0
			self._direction_y *= -1
		if self._y >= screen_height - self._image.get_height():
			self._y = screen_height - self._image.get_height()
			self._direction_y *= -1

	def draw(self, window):
		window.blit(self._image, (self._x, self._y))
		self._draw_energy(window)
		#pygame.draw.rect(window, "red", self.get_rect(), 2)
		#pygame.draw.circle(window, "red", (self._x, self._y), 5)

	def get_rect(self):
		return pygame.Rect (self._x, self._y, self._image.get_width(), self._image.get_height())

	def check_collision(self, other_cell):
		rect1 = self.get_rect()
		rect2 = other_cell.get_rect()
		return rect1.colliderect(rect2)

	def handle_collision(self, other_cell):
		if isinstance(other_cell, Plant):
			self._energy = min((self._energy + (other_cell.get_energy()//2)), 100)
		elif isinstance(other_cell, Hunter):
			self._alive = False
		else:
			self._direction_x *= -1
			self._direction_y *= -1
			if isinstance(other_cell, Stinger):
				self._energy -= 20
				if self._energy <= 0:
					self._alive = False

	def get_energy(self):
		return self._energy

class Stinger(Cell):
	_type = "Stinger"
	_image = pygame.image.load("Graphics/life_2.png")

	def handle_collision(self, other_cell):
		if isinstance(other_cell, Plant):
			self._energy = min((self._energy + (other_cell.get_energy()//2)), 100)
		elif isinstance(other_cell, Hunter):
			self._alive = False
		else:
			self._direction_x *= -1
			self._direction_y *= -1

class Amoeba(Cell):
	_type = "Amoeba"
	_image = pygame.image.load("Graphics/life_1.png")

class Hunter(Cell):
	_type = "Hunter"
	_image = pygame.image.load("Graphics/life_4.png")

	def handle_collision(self, other_cell):
		if isinstance(other_cell, Plant) or isinstance(other_cell, Hunter):
			self._direction_x *= -1
			self._direction_y *= -1
		else:
			self._energy = min((self._energy + (other_cell.get_energy()//2)),100)
			if isinstance(other_cell, Stinger):
				self._energy -=20
				if self._energy <= 0:
					self._alive = False

class Jumper(Cell):
	_type = "Jumper"
	_image = pygame.image.load("Graphics/life_3.png")

	def _move(self):
		if random.random() < self._change_direction_probability:
			self._direction_x = random.choice([-1, 0, 0, 1])
			self._direction_y = random.choice([-1, 0, 0, 1])
		if random.random() < self._change_speed_probability:
			self._speed_x = random.uniform(1, 3)
			self._speed_y = random.uniform(1, 3)
		self._x += self._direction_x * self._speed_x
		self._y += self._direction_y * self._speed_y

class Plant(Cell):
	_type = "Plant"
	_image = pygame.image.load("Graphics/plant.png")

	def update(self, screen_width, screen_height):
		pass

	def _draw_energy(self, window):
		pass

	def handle_collision(self, other_cell):
		if not isinstance(other_cell, Hunter):
			self._alive = False
