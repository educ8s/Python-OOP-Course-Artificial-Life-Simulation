import pygame

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
    image = pygame.image.load("Graphics/life_2.png")

class Amoeba(Cell):
    type = "Amoeba"
    image = pygame.image.load("Graphics/life_1.png")

class Hunter(Cell):
    type = "Hunter"
    image = pygame.image.load("Graphics/life_4.png")

class Jumper(Cell):
    type = "Jumper"
    image = pygame.image.load("Graphics/life_3.png")