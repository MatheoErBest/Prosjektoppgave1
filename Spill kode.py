import pygame, sys, os
from pygame import mixer

#sprite

    #spiller
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

#musikk

volume = 0.2
mixer.init()
mixer.music.load('franky.mp3')
mixer.music.set_volume(volume)
mixer.music.play()
music_enabled = True

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

def changeRes():
    global screenX, screenY
    new_resolution = (screenX, screenY) if screenX != 900 else (1280, 720)
    return new_resolution


#meny verdier

optionMenuItem = ['Resolutuion', 'Music ON/OFF']
selectedOptionItem = 0
menuItems = ['Start game', 'Options', 'Exit']
selectedItem = 0
in_options_menu = False

#main loop

Running = True
while Running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Running = False

        if not in_options_menu:

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_DOWN:

                    selectedItem = (selectedItem + 1) % len(menuItems)

                elif event.key == pygame.K_UP:
                    selectedItem = (selectedItem - 1) % len(menuItems)

                elif event.key == pygame.K_RETURN:

                    if selectedItem == 0:
                        print("Start Game valgt")

                    elif selectedItem == 1:
                        print("Options valgt")
                        in_options_menu = True

                    elif selectedItem == 2:
                        pygame.quit()
                        sys.exit()

        elif in_options_menu:
            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_DOWN:
                    selectedOptionItem = (selectedOptionItem + 1) % len(optionMenuItem)
                
                if event.key == pygame.K_UP:
                    selectedOptionItem = (selectedOptionItem - 1) % len(optionMenuItem)

                if event.key == pygame.K_RETURN:
                    
                    if selectedOptionItem == 1:
                        music_enabled = not music_enabled

                        if music_enabled:
                            mixer.music.unpause()

                        else:
                            mixer.music.pause()

                    elif selectedOptionItem == 0:
                        screenX, screenY = changeRes()
                        screen = pygame.display.set_mode((screenX, screenY))
                        

                if event.key == pygame.K_BACKSPACE:
                    in_options_menu = False
    #tegne menyen
    screen.fill((0, 0, 0))

    if not in_options_menu:
        menu_font = pygame.font.Font(None, 36)
        for i, item in enumerate(menuItems):
            color = (255, 255, 255) if i == selectedItem else (128, 128, 128)
            drawText(item, menu_font, color, screenX // 2, 200 + i * 50)
            drawText("Use UP / Down Arrow Keys To Navigate And Enter To Choose", menu_font, (128, 128, 128), screenX // 2, 400)

    else:
        sub_menu_font = pygame.font.Font(None, 36)
        for i, item in enumerate(optionMenuItem):
            color = (255, 255, 255) if i == selectedOptionItem else (128, 128, 128)
            drawText(item, sub_menu_font, color, screenX // 2, 200 + i * 50)

            drawText("Press Backspace to go back", sub_menu_font, (128, 128, 128), screenX // 2, 400)
                    


    screenUpdate()

pygame.quit()
sys.exit()