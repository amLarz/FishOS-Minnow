import pygame
from menu import run_menu
from game import run_game

# Setup 
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
currentState = run_menu()

# Game loop checks for the state of the game 
while True:
    if currentState == "menu":
        currentState = run_menu()
    
    elif currentState == "game":
        currentState = run_game()
    
    elif currentState == "quit":
        break


