# import libraries
import pygame
import os

# import other game files
from display import *

def run_gameMenu():

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
        pygame.draw.rect(screen, "white", (50, 50, 200, 100))
        
        pygame.display.flip()

        clock.tick(60)
    
    return "quit"
