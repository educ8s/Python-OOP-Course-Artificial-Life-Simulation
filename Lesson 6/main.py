import pygame, sys

class Cell:
    def __init__(self, cell_id, cell_image, cell_x, cell_y, cell_type):
        self.id = cell_id
        self.image = cell_image
        self.x = cell_x
        self.y = cell_y
        self.type = cell_type

    def update(self):
        self.x += 1
        self.y += 1

    def draw(self, window):
        window.blit(self.image, (self.x, self.y))

    def print_details(self):
        print(f"Cell ID: {self.id}, Position: ({self.x}, {self.y}), Type: {self.type}")       

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 800
LIGHT_BLUE = (173, 216, 230)

pygame.init()
window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Artificial Life Simulator')

clock = pygame.time.Clock()

cell_images = {
    "Blob": pygame.image.load("Graphics/life_1.png").convert_alpha(),
    "Spiker": pygame.image.load("Graphics/life_2.png").convert_alpha(),
    "Jumper": pygame.image.load("Graphics/life_3.png").convert_alpha(),
    "Hunter": pygame.image.load("Graphics/life_4.png").convert_alpha(),
}

cells = [
    Cell(1, cell_images["Blob"], 100, 100, "Blob"),
    Cell(2, cell_images["Spiker"], 100, 200, "Spiker"),
    Cell(3, cell_images["Jumper"], 100, 300, "Jumper"),
    Cell(4, cell_images["Hunter"], 100, 400, "Hunter"),
    Cell(5, cell_images["Blob"], 100, 500, "Blob"),
    Cell(6, cell_images["Spiker"], 100, 600, "Spiker"),
    Cell(7, cell_images["Spiker"], 100, 700, "Spiker"),
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