# Example file showing a basic pygame "game loop"
import pygame
from fishingState import read_fishes


# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
player_state = False # made to be global

# depth
depth_selected = 0
depth = ['shallow', 'mid', 'deep']


def switchState():
    global player_state
    current_state = player_state

    if current_state == True:
        current_state = False
    
    elif current_state == False:
        current_state = True

    player_state = current_state
    
    if player_state == True:
        # move to fishingState.py
        read_fishes(depth_selected)
        return

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
                    print(depth[depth_selected])
                
                if event.key == pygame.K_UP and depth_selected != 0:
                    depth_selected -= 1
                    print(depth[depth_selected])

        # selection
        
            

        # fill the screen with a color to wipe away anything from last frame
        screen.fill("purple")

        # RENDER YOUR GAME HERE
        # TODO: Display, for the main game.

        # flip() the display to put your work on screen
        pygame.display.flip()

        clock.tick(60)  # limits FPS to 60
        
    pygame.quit()
    return "quit"