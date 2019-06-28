import pygame
import random

pygame.init()

width = 800
height = 600
size = (width, height)

# create some color variables
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
randomColor = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

Game_screen = pygame.display.set_mode(size)
pygame.display.set_caption("отдача")

done = False

clock = pygame.time.Clock()

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN:
            print("Key Pressed")
            if event.key == pygame.K_UP:

        print(event)

    pygame.display.update()
    clock.tick(60)

pygame.quit()