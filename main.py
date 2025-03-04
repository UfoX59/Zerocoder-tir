import pygame
import random

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.display.set_caption("Игра Тир")
icon = pygame.image.load("img/Red_apple_icon.jpg")
pygame.display.set_icon(icon)

target_img = pygame.image.load("img/apple_aim_80x80.png")
target_wight = 80
target_height = 80
target_x = random.randint(0, SCREEN_WIDTH - target_wight)
target_y = random.randint(0, SCREEN_HEIGHT - target_height)

color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

running = True
while running:
    screen.fill(color)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.blit(target_img, (target_x, target_y))
    pygame.display.update()



pygame.quit()