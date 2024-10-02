import pygame, sys

pygame.init()

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 800
LIGHT_BLUE = (175, 238, 238)

window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Artificial Life Simulation")
clock = pygame.time.Clock()

class Cell:
	def __init__(self, cell_id, cell_x, cell_y):
		self.id = cell_id
		self.x = cell_x
		self.y = cell_y

	def print_details(self):
		print(f"Cell ID: {self.id}, Position: ({self.x}, {self.y}), Type: {self.type}")

	def update(self):
		self.x += 1
		self.y += 1

	def draw(self, window):
		window.blit(self.image, (self.x, self.y))

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

cells = [
Amoeba(1, 100, 100),
Stinger(2, 200, 200),
Hunter(3, 300, 300),
Jumper(4, 400, 400),
Amoeba(5, 500, 500),
Stinger(6, 100, 600),
Stinger(7, 100, 700),
]

#Game Loop
while True:
	# 1. Event Handling
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_SPACE:
				print("\n\nCell Report:")
				for cell in cells:
					cell.print_details()

	# 2. Updating Positions
	for cell in cells:
		cell.update()

	# 3. Drawing
	window.fill(LIGHT_BLUE)
	for cell in cells:
		cell.draw(window) 

	pygame.display.flip()
	clock.tick(60)