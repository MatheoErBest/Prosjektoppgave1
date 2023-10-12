import pygame, sys, os

#sprite

class Player(pygame.sprite.Sprite):
    def __init__():
        super().__init__()


#display

pygame.init()

clock = pygame.time.Clock()
screenX, screenY = 900, 1000

screen = pygame.display.set_mode((screenX, screenY))                                                               
pygame.display.set_caption('Super Duper Kul')    

#Farger

white = (255, 255, 255)
green = (0, 255, 0)
blue = (0, 0, 128)
black = (0, 0, 0)
red = (255, 0, 0)

#funksjoner

def screenUpdate():
    screen.fill((blue))
    pygame.display.flip()
    pygame.display.update()
    clock.tick(60)

#main loop

Running = True
while Running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Running = False
    screenUpdate()

pygame.quit()
sys.exit()