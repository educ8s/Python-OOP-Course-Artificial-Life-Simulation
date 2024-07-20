import pygame, sys

pygame.init()

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 800
LIGHT_BLUE = (175, 238, 238)

window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Artificial Life Simulation")
clock = pygame.time.Clock()

class Cell:
	def __init__(self, cell_id, cell_image, cell_x, cell_y):
		self.id = cell_id
		self.image = cell_image
		self.x = cell_x
		self.y = cell_y

cell_image = pygame.image.load("Graphics/life_1.png")

cells = [
Cell(1, cell_image, 100, 100),
Cell(2, cell_image, 200, 200),
Cell(3, cell_image, 300, 300),
Cell(4, cell_image, 400, 400),
Cell(5, cell_image, 500, 500),
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
					print(f"Cell ID: {cell.id}, Position: ({cell.x}, {cell.y})")

	# 2. Updating Positions
	for cell in cells:
		cell.x += 1 

	# 3. Drawing
	window.fill(LIGHT_BLUE)
	for cell in cells:
		window.blit(cell.image, (cell.x, cell.y)) 


	pygame.display.flip()
	clock.tick(60)