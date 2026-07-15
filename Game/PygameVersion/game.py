# library imports
import pygame
import os
from tilemap import *
import time

# in-game-file imports
from fishingState import catch_fish
from display import *
from inv import load_inv

fishing_state = False

# depth
depth_selected = 0
DEPTH_LIST = ['shallow', 'mid', 'deep']

# font setup and screen size
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
fontPath = os.path.join(BASE_DIR, "..", "Game Assets", "determination.ttf")
font = pygame.font.Font(fontPath, size=50)
d_font = pygame.font.Font(fontPath, size = 40)


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

    # render depth meter
    depth_text = d_font.render("depth: ", True, (0, 0, 0))
    dshallow_text = d_font.render("shallow", True, (0, 60, 95))
    dmid_text = d_font.render("mid", True, (25, 25, 112))
    ddeep_text = d_font.render("deep", True, (0, 0, 0))

    # render full inventory text 
    full_inv_text = d_font.render("Inventory is full.", True, (70, 0, 0))
    full_invX = (screenWidth - full_inv_text.get_width()) // 2
    full_invY = (screenHeight - full_inv_text.get_height()) // 2

    while running:
        # poll for events
        # pygame.QUIT event means the user clicked X to close your window
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_ESCAPE:
                    return "pause"

                if event.key == pygame.K_f:
                    inv = load_inv()
                    if len(inv) == 9:
                        time_start = time.monotonic()
                        time_end = time_start + 0.4
                        current_time = time_start

                        while current_time <= time_end:

                            current_time = time.monotonic()
                            screen.blit(full_inv_text, (full_invX, full_invY - 100))
                            pygame.display.flip()

                    else:
                        switchState()

                if event.key == pygame.K_DOWN and depth_selected != 2:
                    depth_selected += 1
                
                if event.key == pygame.K_UP and depth_selected != 0:
                    depth_selected -= 1

        # fill the screen with a color to wipe away anything from last frame
        screen.fill("black")

        # getting coins
        coins = get_coins()
        # rendering coins and it's position
        coins_text = font.render(f"coins: {str(coins)}", True, (255, 215, 0))
        # getting measurements of the value
        ctext_width = coins_text.get_width()
        ctext_height = coins_text.get_height()
        # getting the desired position
        coin_textX = (screenWidth - ctext_width)
        coins_textY = (screenHeight - ctext_height)
        
        # draw tiles
        draw_tile()

        # depth texts
        # change the depth text according to depth
        depth_textX = 0
        depth_textY = 0
        if DEPTH_LIST[depth_selected] == "shallow":
            dshallow_s = dshallow_text.get_width() - 30

            screen.blit(depth_text, (depth_textX, depth_textY))
            screen.blit(dshallow_text, (depth_textX + dshallow_s, depth_textY))

        elif DEPTH_LIST[depth_selected] == "mid":
            dmid_s = (ddeep_text.get_width() + depth_text.get_width()) - 90

            screen.blit(depth_text, (depth_textX, depth_textY))
            screen.blit(dmid_text, (depth_textX + dmid_s, depth_textY))

        elif DEPTH_LIST[depth_selected] == "deep":
            ddeep_s = (ddeep_text.get_width() + depth_text.get_width()) - 90

            screen.blit(depth_text, (depth_textX, depth_textY))
            screen.blit(ddeep_text, (depth_textX + ddeep_s, depth_textY))
        

        # show coin text
        screen.blit(coins_text, (coin_textX, coins_textY))
        # flip() the display to put your work on screen
        pygame.display.flip()

        clock.tick(60)  # limits FPS to 60
           
    return "quit"