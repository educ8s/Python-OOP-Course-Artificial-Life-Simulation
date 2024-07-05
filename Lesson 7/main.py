import pygame, sys

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 800
LIGHT_BLUE = (173, 216, 230)

pygame.init()
window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Artificial Life Simulator')

class Cell:
    def __init__(self, cell_id, cell_x, cell_y):
        self.id = cell_id
        self.x = cell_x
        self.y = cell_y

    def update(self):
        self.x += 1
        self.y += 1

    def draw(self, window):
        window.blit(self.image, (self.x, self.y))

    def print_details(self):
        print(f"Cell ID: {self.id}, Position: ({self.x}, {self.y}), Type: {self.type}")

class Stinger(Cell):
    type = "Stinger"
    image = pygame.image.load("Graphics/life_2.png").convert_alpha()

class Amoeba(Cell):
    type = "Amoeba"
    image = pygame.image.load("Graphics/life_1.png").convert_alpha()

class Hunter(Cell):
    type = "Hunter"
    image = pygame.image.load("Graphics/life_4.png").convert_alpha()

class Jumper(Cell):
    type = "Jumper"
    image = pygame.image.load("Graphics/life_3.png").convert_alpha()

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