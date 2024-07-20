import pygame, sys

pygame.init()

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 800
LIGHT_BLUE = (175, 238, 238)

window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Artificial Life Simulation")
clock = pygame.time.Clock()

class Cell:
	def __init__(self, cell_id, cell_image, cell_x, cell_y, cell_type):
		self.id = cell_id
		self.image = cell_image
		self.x = cell_x
		self.y = cell_y
		self.type = cell_type

	def print_details(self):
		print(f"Cell ID: {self.id}, Position: ({self.x}, {self.y}), Type: {self.type}")

	def update(self):
		self.x += 1
		self.y += 1

	def draw(self, window):
		window.blit(self.image, (self.x, self.y))

cell_images = {
	"Blob": pygame.image.load("Graphics/life_1.png"),
	"Spiker": pygame.image.load("Graphics/life_2.png"),
	"Jumper": pygame.image.load("Graphics/life_3.png"),
	"Hunter": pygame.image.load("Graphics/life_4.png"),
}

cells = [
Cell(1, cell_images["Blob"], 100, 100, "Blob"),
Cell(2, cell_images["Spiker"], 200, 200, "Spiker"),
Cell(3, cell_images["Hunter"], 300, 300, "Hunter"),
Cell(4, cell_images["Jumper"], 400, 400, "Jumper"),
Cell(5, cell_images["Blob"], 500, 500, "Blob"),
Cell(6, cell_images["Spiker"], 100, 600, "Spiker"),
Cell(7, cell_images["Spiker"], 100, 700, "Spiker"),
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