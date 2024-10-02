import pygame, sys
from cell import Amoeba
from cell import Stinger
from cell import Jumper
from cell import Hunter
from cell import Plant

def delete_dead_cells(cells):
	new_cells = []
	for cell in cells:
		if cell.is_alive():
			new_cells.append(cell)
	cells = new_cells
	return cells

def print_health_report(cells):
	print("\n\nHealth Report:")
	print("--------------")
	for cell in cells:
		print(f"Cell ID: {cell.get_id():<3} Type: {cell.get_type():<8} Energy: {cell.get_energy_level():<8}")

def print_cell_report(cells):
	print("\n\nCell Report:")
	print("--------------")
	for cell in cells:
		print(f"Cell ID: {cell.get_id():<3} Position: {cell.get_position():<12} Type: {cell.get_type():<8} Energy: {cell.get_energy_level():<8}")

pygame.init()

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 800
LIGHT_BLUE = (175, 238, 238)

window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Artificial Life Simulation")
clock = pygame.time.Clock()

cells = [
Amoeba(1, 100, 100),
Stinger(2, 200, 200),
Hunter(3, 300, 300),
Jumper(4, 400, 400),
Amoeba(5, 500, 500),
Stinger(6, 100, 600),
Stinger(7, 100, 700),
Plant(8, 300, 175),
Plant(9, 650, 500)
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
				print_cell_report(cells)
				print_health_report(cells)

	# 2. Updating Positions
	for cell in cells:
		cell.update(SCREEN_WIDTH, SCREEN_HEIGHT)

	cells = delete_dead_cells(cells)

	# 3. Drawing
	window.fill(LIGHT_BLUE)
	for cell in cells:
		cell.draw(window) 

	pygame.display.flip()
	clock.tick(60)