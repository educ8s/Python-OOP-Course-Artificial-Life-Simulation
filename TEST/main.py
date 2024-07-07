import pygame, sys
from reports import CellReport
from reports import HealthReport
from cell import Amoeba
from cell import Stinger
from cell import Jumper
from cell import Hunter
from cell import Plant
from size import Small
from size import Medium
from size import Large
import random

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 800
LIGHT_BLUE = (175, 238, 238)
NUMBER_OF_CELLS = 90

def remove_dead_cells(cells):
    new_cells = []
    for cell in cells: 
        if cell.alive:
            new_cells.append(cell)
    cells = new_cells
    return cells

def random_cell(cell):
    cell_types = [Plant, Plant, Amoeba, Hunter, Stinger, Jumper]
    cells_sizes = [Small(), Medium(), Large()]
    return random.choice(cell_types)(cell, random.randint(0, SCREEN_WIDTH), random.randint(0, SCREEN_HEIGHT), random.choice(cells_sizes))

pygame.init()
window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Artificial Life Simulator')

clock = pygame.time.Clock()

cells = []

for cell in range(NUMBER_OF_CELLS):
    cells.append(random_cell(cell))
    #cells[i].alive = False

reports = [CellReport(cells), HealthReport(cells)]


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

    #Check for collisions
    for collidor in cells:
        for cell in cells:
            if id(collidor) != id(cell):
                rect = collidor.get_rect()
                if rect.colliderect(cell.get_rect()):
                    if cell.type == "Plant":
                        if collidor.type != "Hunter":
                            cell.alive = False
                            collidor.energy = min(100, collidor.energy + (cell.energy // 3))
                            cell.energy = 0
                        else:
                            collidor.speed_x *= -1
                            collidor.speed_y *= -1
                            collidor.randomMovement = False
                    else:
                        collidor.speed_x *= -1
                        collidor.speed_y *= -1
                        collidor.randomMovement = False
                        if collidor.type == "Stinger":
                            cell.energy //= 2
                            if cell.energy < 10:
                                cell.alive = False
                                cell.energy = 0
                            collidor.energy -= 10
                        if collidor.type == "Jumper":
                            pass
                        if collidor.type == "Amoeba":
                            pass
                        if collidor.type == "Hunter" and cell.type != "Hunter":
                            if collidor.energy > cell.energy:
                                cell.alive = False
                                collidor.energy = min(100, collidor.energy + cell.energy)
                                cell.energy = 0
                            else:
                                collidor.energy += 5
                                cell.energy -= 5
                        collidor.energy -= 1

    cells = remove_dead_cells(cells)

    #Drawing
    window.fill(LIGHT_BLUE)
    for cell in cells:
            cell.draw(window)

    pygame.display.flip()
    clock.tick(60)