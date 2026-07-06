# Example file showing a basic pygame "game loop"
import pygame
import random
import time
from fishingState import catchRNG



# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
player_state = False # made to be global

def callState():
    global player_state
    return player_state

def switchState():
    global player_state
    current_state = player_state

    if current_state == True:
        current_state = False
    
    elif current_state == False:
        current_state = True

    player_state = current_state
    stateMachine()  

# Changes State from idle to fishing
def stateMachine():

    fishing_state = callState()
    
    # Proceed to wait fish
    if fishing_state == True:
        waitFish()
    else:
        pass

# TODO: sprite integration
def waitFish():

    # Set up for time 
    global player_state
    shallow_catch_time = random.randint(3000, 10000)
    time_start = pygame.time.get_ticks()
    time_end = time_start + shallow_catch_time

    last_tick = time_start # every second start
    current_time = time_start # ever milisecond start

    # Keeps fishing not be the add (have the chance to add dots)
    print("fishing", end="")

    while current_time <= time_end:
        
        current_time = pygame.time.get_ticks()

        if last_tick <= current_time - 1000:
            last_tick += 1000
            print(".", end="")

    print("")
    catchRNG()

    return 
    

# TODO: work on sprites here
# running and rendering the game 
def run_game():
    # setup and render
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

        # fill the screen with a color to wipe away anything from last frame
        screen.fill("purple")

        # RENDER YOUR GAME HERE
        # TODO: Display, for the main game.

        # flip() the display to put your work on screen
        pygame.display.flip()

        clock.tick(60)  # limits FPS to 60
        
    pygame.quit()
    return "quit"