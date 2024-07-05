import pygame, sys

class Cell:
    def __init__(self, cell_id, cell_image, cell_x, cell_y):
        self.id = cell_id
        self.image = cell_image
        self.x = cell_x
        self.y = cell_y

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 800
LIGHT_BLUE = (173, 216, 230)

window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Artificial Life Simulator')

clock = pygame.time.Clock()

cell_image = pygame.image.load("Graphics/life_1.png").convert_alpha()

cells = [
    Cell(1, cell_image, 100, 100),
    Cell(2, cell_image, 100, 200),
    Cell(3, cell_image, 100, 300),
    Cell(4, cell_image, 100, 400),
    Cell(5, cell_image, 100, 500),
]

while True:
    #Get Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                # Print the report when spacebar is pressed
                print("\n\nCell Report:")
                for cell in cells:
                    print(f"Cell ID: {cell.id}, Position: ({cell.x}, {cell.y})")

    #Update
    for cell in cells:
        cell.x += 1 # cell[2] is the x-coordinate

    #Drawing
    window.fill(LIGHT_BLUE)
    for cell in cells:
        window.blit(cell.image, (cell.x, cell.y))

    pygame.display.flip()
    clock.tick(60)