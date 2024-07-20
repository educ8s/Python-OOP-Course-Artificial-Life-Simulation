import pygame, sys

pygame.init()

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 800
LIGHT_BLUE = (175, 238, 238)

window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Artificial Life Simulation")
clock = pygame.time.Clock()

cell_image = pygame.image.load("Graphics/life_1.png")

x1, y1 = 100, 100
x2, y2 = 200, 200
x3, y3 = 300, 300
x4, y4 = 400, 400

#Game Loop
while True:
	# 1. Event Handling
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()

	# 2. Updating Positions
	x1 += 1
	x2 += 1
	x3 += 1
	x4 += 1

	# 3. Drawing
	window.fill(LIGHT_BLUE)
	window.blit(cell_image, (x1, y1))
	window.blit(cell_image, (x2, y2))
	window.blit(cell_image, (x3, y3))
	window.blit(cell_image, (x4, y4))

	pygame.display.flip()
	clock.tick(60)