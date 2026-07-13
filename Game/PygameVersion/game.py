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

# font setup and screen size
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
fontPath = os.path.join(BASE_DIR, "..", "Game Assets", "determination.ttf")
font = pygame.font.Font(fontPath, size=50)
screen_width = 1280
screen_height = 720


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

    return 0

def get_coins():
    inv = load_inv()

    return inv["Coin Bag"]["value"]


# running and rendering the game 
def run_game():
    # setup and render
    global depth_selected
    running = True
    # getting coins
    coins = get_coins()

    # rendering coins and it's position
    coins_text = font.render(str(coins), True, (135, 206, 250))
    # getting measurements of the value
    ctext_width = coins_text.get_width()
    ctext_height = coins_text.get_height()
    # getting the desired position
    coin_textX = (screen_width - ctext_width)
    coins_textY = (screen_height - ctext_height)

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

        # fill the screen with a color to wipe away anything from last frame
        screen.fill("black")

        # show coin text
        screen.blit(coins_text, (coin_textX, coins_textY))

        # flip() the display to put your work on screen
        pygame.display.flip()

        clock.tick(60)  # limits FPS to 60
           
    return "quit"