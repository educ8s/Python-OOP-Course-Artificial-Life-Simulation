import pygame, sys

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 800
LIGHT_BLUE = (173, 216, 230)

window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Artificial Life Simulator')

clock = pygame.time.Clock()

cell_image = pygame.image.load("Graphics/life_1.png").convert_alpha()

cells = [
    [1, cell_image, 100, 100],
    [2, cell_image, 100, 200],
    [3, cell_image, 100, 300],
    [4, cell_image, 100, 400],
    [5, cell_image, 100, 500]
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
                    cell_id, img, x, y = cell
                    print(f"Cell ID: {cell_id}, Position: ({x}, {y})")

    #Update
    for cell in cells:
        cell[2] += 1 # cell[2] is the x-coordinate

    #Drawing
    window.fill(LIGHT_BLUE)
    for cell_id, img, x, y in cells:
        window.blit(img, (x, y))

    pygame.display.flip()
    clock.tick(60)