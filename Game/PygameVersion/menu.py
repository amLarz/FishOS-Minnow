import pygame
import time
import os
from display import *

selection = 0

# font setup
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
fontPath = os.path.join(BASE_DIR, "..", "Game Assets", "determination.ttf")
font = pygame.font.Font(fontPath, size=100)
subfont = pygame.font.Font(fontPath, size=50)


def run_menu():
    global selection

    # Main menu texts
    titleText1 = font.render("FishOS: ", True, (0, 107, 166))
    titleText2 = font.render("Minnow", True, (135, 206, 250))
    playText = subfont.render("press ENTER to start", True, (0, 107, 166))
    fishText = subfont.render("><))>", True, (135, 206, 250))

    # Centering Title text
    titleTextWidth = titleText1.get_width() + titleText2.get_width()
    titleTextHeight = max(titleText1.get_height(), titleText2.get_width())
    titleX = (screenWidth - titleTextWidth) // 2
    titleY = (screenHeight - titleTextHeight) // 2

    # Centering Start Button Text
    playTextWidth = playText.get_width()
    playTextHeight = playText.get_height()
    playX = (screenWidth - playTextWidth) // 2
    playY = (screenHeight - playTextHeight) // 2

    # Centering Fish Text
    fishTextWidth = fishText.get_width()
    fishTextHeight = fishText.get_height()
    fishX = (screenWidth - fishTextWidth) // 2
    fishY = (screenHeight - fishTextHeight) // 2

    running = True
    while running:
        # poll for events
        # pygame.QUIT event means the user clicked X to close your window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    return "game"
 
        # fill the screen with a color to wipe away anything from last frame
        screen.fill("black")

        # RENDER YOUR GAME HERE
        
        # Rendering  the position of the text
        screen.blit(titleText1, (titleX, titleY - 100)) # Getting the wanted height
        screen.blit(titleText2, (titleX + titleText1.get_width(), titleY - 100))
        screen.blit(fishText, (fishX, fishY - 100))

        # Blinking enter text
        if time.time() % 1 > 0.5:
            screen.blit(playText, (playX, playY + 250))
            
        # flip() the display to put your work on screen
        pygame.display.flip()

        clock.tick(60)  # limits FPS to 60

    return "quit"