# import libraries
import pygame
import os

# import other game files
from display import *
    

# font config 
BASE_DIR =  os.path.dirname(os.path.abspath(__file__))
fontPath = os.path.join(BASE_DIR, "..", "Game Assets", "determination.ttf")
font = pygame.font.Font(fontPath, size=50)

def run_gameMenu(): 

    # rect config
    pause_rect = pygame.Rect(50, 50, 220, 400)
    inventory_rect = pygame.Rect(300, 50, 600, 400)

    # resume button config
    resume_button = font.render("Resume", True, "black")
    rbutton_X = screenWidth - resume_button.get_width() 
    rbutton_Y = screenHeight - resume_button.get_height()
    
    
    running = True

    while running:
        # poll for events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return "game"

        # fill screen with color

        # draw rectangle of pause screen
        pygame.draw.rect(screen, "beige", pause_rect)
        pygame.draw.rect(screen, "brown", pause_rect, 5)
        # draw rectangle of inventory screen
        pygame.draw.rect(screen, "beige", inventory_rect)
        pygame.draw.rect(screen, "brown", inventory_rect, 5)

        # blit fonts




        pygame.display.flip()

        clock.tick(60)
    
    return "quit"
