import pygame, sys, os

#sprite

    #spiller
class Player(pygame.sprite.Sprite):
    def __init__():
        super().__init__()

    #meny


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

def drawText(text, font, color, x, y):
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.center = (x, y)
    screen.blit(text_surface, text_rect)

def screenUpdate():
    pygame.display.flip()
    pygame.display.update()
    clock.tick(60)

#main loop

Running = True
while Running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Running = False

    #tegne menyen
    screen.fill((0, 0, 0))  # Sett bakgrunnsfargen
    menu_font = pygame.font.Font(None, 36)

    drawText("Main Menu", menu_font, (255, 255, 255), screenX // 2, 100)
    drawText("Start Game", menu_font, (255, 255, 255), screenX // 2, 200)
    drawText("Options", menu_font, (255, 255, 255), screenX // 2, 250)
    drawText("Exit", menu_font, (255, 255, 255), screenX // 2, 300)


    screenUpdate()

pygame.quit()
sys.exit()