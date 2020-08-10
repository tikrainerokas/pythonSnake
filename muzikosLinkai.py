import pygame
import sys

pygame.init()
muzikos_linkai = []
width = 800
height = 600
screen = pygame.display.set_mode((width, height))
base_font = pygame.font.Font(None, 32)
user_text = ''
white = (255,255,255)
color = (150,40,65)
black = (0,0,0)
ended = False
input_rect = pygame.Rect(150,300,500,32)


while not ended:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                user_text = user_text[:-1]
            else:
                user_text += event.unicode
            if event.key == pygame.K_RETURN:
                muzikos_linkai.append(user_text)
                print (muzikos_linkai)
                user_text = ''



    screen.fill((white))
    pygame.draw.rect(screen, color, input_rect,2)
    text_surface = base_font.render(user_text, True, (black))
    screen.blit(text_surface, (input_rect.x +5, input_rect.y +5))
    pygame.display.update()





