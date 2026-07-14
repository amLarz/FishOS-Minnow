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
                pass

        # fill screen with color
        screen.fill("beige")
        
        pygame.display.flip()

        clock.tick(60)
    
    return "quit"
