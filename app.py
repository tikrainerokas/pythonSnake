import pygame
import sys
import time
import random
pygame.init()
width = 1000
height = 800
screen = pygame.display.set_mode((width, height))
white = (255,255,255)
red = (255,0,0)
color = (150,40,65)
player_pos = [400, 300]
player_size = 50
pos = [120, 400]
ended = False

x = player_pos[0]
y = player_pos[1]
kryptis = 0
motion = 0
how_much = random.choice([-10,10])

if random.choice(["kryptis", "motion"]) == "kryptis":
    kryptis = how_much
else:
    motion = how_much

while not ended:
  #IF WE PRESS ANYTHING
    time.sleep(0.05)
    for event in pygame.event.get():
       if event.type == pygame.QUIT:
                sys.exit()

       if event.type == pygame.KEYDOWN:
          if event.key == pygame.K_LEFT:
              kryptis = -10
              motion = 0
          elif event.key == pygame.K_RIGHT:
              kryptis = 10
              motion = 0
          elif event.key == pygame.K_DOWN:
              motion = 10
              kryptis = 0
          elif event.key == pygame.K_UP:
              motion = -10
              kryptis = 0
  # NO MATTER IF WE PRESS ANYTHING OR NO

    x += kryptis
    y += motion
    player_pos = [x,y]
    if player_pos[0] == 0 or player_pos[0] == width-player_size:
        ended = True
    if player_pos[1] == 0 or player_pos[1] == height-player_size:
        ended = True

    screen.fill((white))
    pygame.draw.rect(screen, red, (player_pos[0], player_pos[1], player_size, player_size))
    pygame.display.update()


