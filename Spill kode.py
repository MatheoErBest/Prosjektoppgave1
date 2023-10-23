import pygame, sys, os
from pygame import mixer

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

#musikk

volume = 0.2
mixer.init()
mixer.music.load('franky.mp3')
mixer.music.set_volume(volume)
mixer.music.play()

m1 = 1

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

#meny verdier

menuItems = ['Start game', 'Options', 'Exit']
selectedItem = 0

#main loop

Running = True
while Running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                selectedItem  = (selectedItem + 1) % len(menuItems)

            elif event.key == pygame.K_UP:
                selectedItem = (selectedItem - 1) % len(menuItems)

            elif event.key == pygame.K_RETURN:
                if selectedItem == 0:
                    print("Start Game valgt")

                elif selectedItem == 1:
                    print("Options valgt")

                elif selectedItem == 2:
                    pygame.quit()
                    sys.exit()

    #tegne menyen
    screen.fill((0, 0, 0))  # Sett bakgrunnsfargen

    menu_font = pygame.font.Font(None, 36)
    for i, item in enumerate(menuItems):
        color = (255, 255, 255) if i == selectedItem else (128, 128, 128)
        drawText(item, menu_font, color, screenX // 2, 200 + i * 50)


    screenUpdate()

pygame.quit()
sys.exit()