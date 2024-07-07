import pygame
import random

class Cell:
    def __init__(self, cell_id, cell_x, cell_y, cell_size):
        self.id = cell_id
        self.x = cell_x
        self.y = cell_y
        self.direction_x = random.choice([-1, 0, 1]) 
        self.direction_y = random.choice([-1, 0, 1])
        self.speed_x = random.uniform(0.1, 1.0)
        self.speed_y = random.uniform(0.1, 1.0)
        self.change_direction_probability = 0.01
        self.change_speed_probability = 0.01
        self.energy = random.randint(50, 100)
        self.frame_count = 0
        self.alive = True
        self.randomMovement = True
        self.size = cell_size
        self.image = self.scale_image(self.image, self.size.get_scale())

    def update(self, screen_width, screen_height):
        self.move()
        self.constraint_position(screen_width, screen_height)
        self.decrease_energy()
        
    def move(self):
        if self.randomMovement:
            if random.random() < self.change_direction_probability:
                self.direction_x = random.choice([-1, 0, 1])
                self.direction_y = random.choice([-1, 0, 1])

            if random.random() < self.change_speed_probability:
                self.speed_x = random.uniform(0.1, 1)
                self.speed_y = random.uniform(0.1, 1)
        else:
            if random.random() < self.change_direction_probability:
                self.randomMovement = True

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
        self.draw_energy(window)
        #pygame.draw.rect(window, 'red', self.get_rect(), 2)
        #pygame.draw.circle(window, 'red', (self.x, self.y), 5)  # Draw a red circle at the top-left corner

    def decrease_energy(self):
        self.frame_count += 1
        if self.frame_count >= 60:
            self.energy -= 1
            self.frame_count = 0
        if self.energy <= 0:
            self.alive = False

    def is_alive(self):
        return self.alive

    def get_rect(self):
        return pygame.Rect(self.x, self.y, self.image.get_width(), self.image.get_height())

    def scale_image(self, image, scale):
        original_width = image.get_width()
        original_height = image.get_height()
        new_width = int(original_width * scale)
        new_height = int(original_height * scale)
        return pygame.transform.smoothscale(image, (new_width, new_height))

    def draw_energy(self, window):
        if self.energy < 15:
            color = "red"
        elif 15 <= self.energy < 50:
            color = "orange"
        else:
            color = "green"

        bar_width = self.image.get_width()
        bar_height = 5
        energy_bar_width = bar_width * (self.energy / 100)

        bar_x = self.x
        bar_y = self.y - 10

        pygame.draw.rect(window, (0, 0, 0), (bar_x - 1, bar_y - 1, bar_width + 2, bar_height + 2))
        pygame.draw.rect(window, color, (bar_x, bar_y, energy_bar_width, bar_height))

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
    def update(self, screen_width, screen_height):
        pass

    def draw_energy(self, window):
        pass