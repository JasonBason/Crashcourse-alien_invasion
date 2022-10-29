import pygame


screen = pygame.display.set_mode((300,300))

pygame.init()

pygame.display.flip()

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            print(event.key)
            