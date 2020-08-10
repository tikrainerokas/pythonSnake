import pygame
import sys

pygame.init()
width = 800
height = 600
screen = pygame.display.set_mode((width, height))
white = (255,255,255)
red = (255,0,0)
color = (150,40,65)
player_pos = [400, 300]
player_size = 50
pos = [120, 400]
ended = False



while not ended:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
          x = player_pos[0]
          y = player_pos[1]

          if event.key == pygame.K_LEFT:
            x -= player_size
          elif event.key == pygame.K_RIGHT:
            x += player_size
          elif event.key == pygame.K_DOWN:
            y += player_size
          elif event.key == pygame.K_UP:
            y -= player_size

          player_pos = [x,y]
    screen.fill((white))
    pygame.draw.rect(screen, red, (player_pos[0], player_pos[1], player_size, player_size))
    pygame.display.update()


