import pygame, sys, itertools
from cell import Amoeba
from cell import Stinger
from cell import Jumper
from cell import Hunter
from cell import Plant
from report import CellReport
from report import HealthReport

def remove_dead_cells(cells):
    new_cells = []
    for cell in cells:
        if cell.is_alive():
            new_cells.append(cell)
    cells = new_cells
    return cells

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 800
LIGHT_BLUE = (175, 238, 238)

pygame.init()
window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Artificial Life Simulator')

clock = pygame.time.Clock()

cells = [
    Amoeba(1, 10, 100),
    Stinger(2, 100, 200),
    Jumper(3, 800, 300),
    Hunter(4, 230, 400),
    Amoeba(5, 400, 500),
    Stinger(6, 120, 50),
    Stinger(7, 600, 700),
    Plant(8, 500, 175),
    Plant(9, 650, 500),
    Plant(10, 70, 500),
    Plant(11, 320, 100),
    Plant(12, 920, 500),
    Plant(13, 520, 600),
    Hunter(14, 10, 100),
    Hunter(15, 20, 500),
]

reports = [CellReport(), HealthReport()]

while True:
    #Get Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                for report in reports:
                    report.update(cells)
                    report.print()
 
    #Update
    for cell in cells:
        cell.update(SCREEN_WIDTH, SCREEN_HEIGHT)

    # Check for collisions
    for cell1, cell2 in itertools.combinations(cells, 2):
        if cell1.check_collision(cell2):
            cell1.handle_collision(cell2)
            cell2.handle_collision(cell1)

    cells = remove_dead_cells(cells)

    #Drawing
    window.fill(LIGHT_BLUE)
    for cell in cells:
            cell.draw(window)

    pygame.display.flip()
    clock.tick(60)