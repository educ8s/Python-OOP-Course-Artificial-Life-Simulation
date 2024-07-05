import pygame
import random

class Cell:
    def __init__(self, cell_id, cell_x, cell_y):
        self.id = cell_id
        self.x = cell_x
        self.y = cell_y
        self.direction_x = random.choice([-1, 0, 1]) 
        self.direction_y = random.choice([-1, 0, 1])
        self.speed_x = random.uniform(0.1, 1.0)
        self.speed_y = random.uniform(0.1, 1.0)
        self.change_direction_probability = 0.01
        self.change_speed_probability = 0.01

    def update(self, screen_width, screen_height):
        self.move()
        self.constraint_position(screen_width, screen_height)
        
    def move(self):
        if random.random() < self.change_direction_probability:
            self.direction_x = random.choice([-1, 0, 1])
            self.direction_y = random.choice([-1, 0, 1])

        if random.random() < self.change_speed_probability:
            self.speed_x = random.uniform(0.1, 1)
            self.speed_y = random.uniform(0.1, 1)

        self.x += self.direction_x * self.speed_x
        self.y += self.direction_y * self.speed_y

    def constraint_position(self, screen_width, screen_height):
        if self.x <= 0:
            self.x = 0
            self.direction_x *= -1
        elif self.x >= screen_width - self.image.get_width():
            self.x = screen_width - self.image.get_width()
            self.direction_x *= -1

        if self.y <= 0:
            self.y = 0
            self.direction_y *= -1
        elif self.y >= screen_height - self.image.get_height():
            self.y = screen_height - self.image.get_height()
            self.direction_y *= -1
       
    def draw(self, window):
        window.blit(self.image, (self.x, self.y))
        pygame.draw.rect(window, 'red', (self.x, self.y, self.image.get_width(), self.image.get_height()), 2)
        pygame.draw.circle(window, 'red', (self.x, self.y), 5)  # Draw a red circle at the top-left corner

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

    def move(self):
        if random.random() < self.change_direction_probability:
            self.direction_x = random.choice([-1, 0, 0, 1])
            self.direction_y = random.choice([-1, 0, 0, 1])

        if random.random() < self.change_speed_probability:
            self.speed_x = random.uniform(1, 3)
            self.speed_y = random.uniform(1, 3)

        self.x += self.direction_x * self.speed_x
        self.y += self.direction_y * self.speed_y

class Plant(Cell):
    type = "Plant"
    image = pygame.image.load("Graphics/plant.png")

    def move(self):
        pass