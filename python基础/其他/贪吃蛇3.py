import pygame

pygame.init()
pygame.display.set_mode(400,500)
pygame.display.set_caption('123')


while True:
    for event in pygame.event.get():
        print(event)
        if event.type==pygame.QUIT():
            exit()
