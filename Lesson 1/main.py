import pygame, sys

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 800
LIGHT_BLUE = (173, 216, 230)  # Light blue

window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Artificial Life Simulator')

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    #Update

    #Drawing
    window.fill(LIGHT_BLUE)

    pygame.display.flip()
    clock.tick(60)