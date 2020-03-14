import pygame
import neat
import time
import os
import random

WIN_WIDTH = 600
WIN_HEIGHT = 800

BIRD_IMGS = [pygame.transform.scale2x(pygame.image.load(os.path.join("imgs", "bird1.png"))),
             pygame.transform.scale2x(pygame.image.load(os.path.join("imgs", "bird2.png"))),
             pygame.transform.scale2x(pygame.image.load(os.path.join("imgs", "bird3.png")))]
PIPE_IMG = pygame.transform.scale2x(pygame.image.load(os.path.join("imgs", "pipe.png")))
BASE_IMG = pygame.transform.scale2x(pygame.image.load(os.path.join("imgs", "base.png")))
BG_IMG = pygame.transform.scale2x(pygame.image.load(os.path.join("imgs", "bg.png")))


def main():
    #bird = Bird(200, 200)
    location = 40
    x_axis = 40
    image_num =0
    win = pygame.display.set_mode((600, 600))
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                location -= 4
                x_axis += 4
            if event.key == pygame.K_DOWN:
                location += 1
            if event.key == pygame.K_LEFT:
                x_axis -= 1
            if event.key == pygame.K_RIGHT:
                x_axis += 4
            if event.key == pygame.K_1:
                x_axis -= 1
                location += 1

        x_axis -= 1
        location += 1

        win.blit(BG_IMG, (0, 0))
        win.blit(BIRD_IMGS[image_num], (x_axis,location))
        pygame.display.update()
        image_num += 1
        if image_num == 2:
            image_num = 0

    pygame.quit()
    quit()

main()