import pygame, sys

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 800
LIGHT_BLUE = (173, 216, 230)

window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Artificial Life Simulator')

clock = pygame.time.Clock()

cell_image = pygame.image.load("Graphics/life_1.png").convert_alpha()

x1, y1 = 100, 100
x2, y2 = 100, 200
x3, y3 = 100, 300
x4, y4 = 100, 400

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    #Update
    x1 += 1
    x2 += 1
    x3 += 1
    x4 += 1

    #Drawing
    window.fill(LIGHT_BLUE)
    window.blit(cell_image, (x1, y1))
    window.blit(cell_image, (x2, y2))
    window.blit(cell_image, (x3, y3))
    window.blit(cell_image, (x4, y4))

    pygame.display.flip()
    clock.tick(60)