import pygame, sys, itertools
from cell import Amoeba
from cell import Stinger
from cell import Jumper
from cell import Hunter
from cell import Plant
from report import CellReport
from report import HealthReport
from size import Small
from size import Medium
from size import Large
from size import Tiny

def delete_dead_cells(cells):
	new_cells = []
	for cell in cells:
		if cell.is_alive():
			new_cells.append(cell)
	cells = new_cells
	return cells

pygame.init()

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 800
LIGHT_BLUE = (175, 238, 238)

window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Artificial Life Simulation")
clock = pygame.time.Clock()

cells = [
Amoeba(1, 100, 100, Small()),
Stinger(2, 200, 200, Large()),
Hunter(3, 300, 300, Medium()),
Jumper(4, 400, 400, Small()),
Amoeba(5, 500, 500, Large()),
Stinger(6, 100, 600, Medium()),
Stinger(7, 100, 700, Small()),
Plant(8, 300, 175, Large()),
Plant(9, 650, 500, Small()),
Plant(10, 800, 800, Small()),
Plant(11, 700, 200, Medium()),
Plant(12, 200, 600, Large()),
Hunter(13, 800, 125, Medium()),
Hunter(14, 100, 50, Small()),
Hunter(15, 200, 50, Large()),
Hunter(16, 30, 30, Tiny()),
Plant(17, 1030, 730, Large()),
Plant(18, 830, 630, Large()),
Plant(19, 800, 250, Large()),
Amoeba(20, 900, 50, Large())
]

reports = [CellReport(), HealthReport()]

#Game Loop
while True:
	# 1. Event Handling
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_SPACE:
				for report in reports:
					report.update(cells)
					report.print()
					
	# 2. Updating Positions
	for cell in cells:
		cell.update(SCREEN_WIDTH, SCREEN_HEIGHT)

	for cell1, cell2 in itertools.combinations(cells, 2):
		if cell1.check_collision(cell2):
			cell1.handle_collision(cell2)
			cell2.handle_collision(cell1)

	cells = delete_dead_cells(cells)

	# 3. Drawing
	window.fill(LIGHT_BLUE)
	for cell in cells:
		cell.draw(window) 

	pygame.display.flip()
	clock.tick(60)