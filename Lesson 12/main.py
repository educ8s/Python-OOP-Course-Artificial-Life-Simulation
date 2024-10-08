import pygame, sys
from cell import Amoeba
from cell import Stinger
from cell import Jumper
from cell import Hunter
from cell import Plant

def print_cell_report(cells):
    print("\n\nCell Report:")
    print("------------")
    for cell in cells:
        print(f"Cell ID: {cell.id:<3} Position: ({int(cell.x):<4} {int(cell.y):<3})  Type: {cell.type:<8} Energy: {cell.energy:<3}")

def print_health_report(cells):
    print("\n\nHealth Report:")
    print("--------------") 
    for cell in cells:
        print(f"Cell ID: {cell.id:<3} Type: {cell.type:<8} Energy: {cell.energy:<3}")

def remove_dead_cells(cells):
    new_cells = []
    for cell in cells:
        if cell.alive:
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
    Amoeba(1, 100, 100),
    Stinger(2, 100, 200),
    Jumper(3, 100, 300),
    Hunter(4, 100, 400),
    Amoeba(5, 100, 500),
    Stinger(6, 100, 600),
    Stinger(7, 100, 700),
    Plant(8, 300, 175),
    Plant(9, 650, 500),
]

while True:
    #Get Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                print_cell_report(cells)
                print_health_report(cells)
 
    #Update
    for cell in cells:
        cell.update(SCREEN_WIDTH, SCREEN_HEIGHT)

    cells = remove_dead_cells(cells)

    #Drawing
    window.fill(LIGHT_BLUE)
    for cell in cells:
            cell.draw(window)

    pygame.display.flip()
    clock.tick(60)