import pygame, sys

class Cell:
    def __init__(self, cell_id, cell_image, cell_x, cell_y):
        self.id = cell_id
        self.image = cell_image
        self.x = cell_x
        self.y = cell_y

    def update(self):
        self.x += 1
        self.y += 1

    def draw(self, window):
        window.blit(self.image, (self.x, self.y))

    def print_details(self):
        print(f"Cell ID: {self.id}, Position: ({self.x}, {self.y})")       

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
                print("\n\nCell Report:")
                for cell in cells:
                    cell.print_details()

    #Update
    for cell in cells:
        cell.update()

    #Drawing
    window.fill(LIGHT_BLUE)
    for cell in cells:
        cell.draw(window)

    pygame.display.flip()
    clock.tick(60)