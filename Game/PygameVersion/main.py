from display import *
from menu import run_menu
from game import run_game
from gameMenu import run_gameMenu
import pygame

currentState = run_menu()

# Game loop checks for the state of the game 
while True:
    if currentState == "menu":
        currentState = run_menu()
    
    elif currentState == "game":
        currentState = run_game()

    elif currentState == "pause":
        currentState = run_gameMenu()
    
    elif currentState == "quit":
        break

pygame.quit()
