# library imports
import pygame
import os

# in-game-file imports
from fishingState import catch_fish
from display import screen, clock
from inv import load_inv

fishing_state = False

# depth
depth_selected = 0
DEPTH_LIST = ['shallow', 'mid', 'deep']

# font setup
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
fontPath = os.path.join(BASE_DIR, "..", "Game Assets", "determination.ttf")
font = pygame.font.Font(fontPath, size=100)
subfont = pygame.font.Font(fontPath, size=50)


def switchState():
    global fishing_state
    current_state = fishing_state

    if current_state == True:
        current_state = False
    
    elif current_state == False:
        current_state = True

    fishing_state = current_state
    
    if fishing_state == True:
        # move to fishingState.py
        catch_fish(DEPTH_LIST, depth_selected)

    return

# Gets value from json file
def coin_view():
    inv = load_inv()
    coins = inv["Coin Bag"]["value"]

    return coins

# Rendering the font 
def font_render():
    coins = coin_view()

    coins_text = font.render(coins, True, (255, 255, 255))

# running and rendering the game 
def run_game():
    # setup and render
    global depth_selected
    running = True
    

    while running:
        # poll for events
        # pygame.QUIT event means the user clicked X to close your window
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_x:
                    switchState()

                if event.key == pygame.K_DOWN and depth_selected != 2:
                    depth_selected += 1
                    print(DEPTH_LIST[depth_selected])
                
                if event.key == pygame.K_UP and depth_selected != 0:
                    depth_selected -= 1
                    print(DEPTH_LIST[depth_selected])

        # selection
        
            

        # fill the screen with a color to wipe away anything from last frame
        screen.fill("black")

        # RENDER YOUR GAME HERE
        # TODO: Display, for the main game.
        


        # flip() the display to put your work on screen
        pygame.display.flip()

        clock.tick(60)  # limits FPS to 60
           
    return "quit"