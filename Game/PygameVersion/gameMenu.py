# import libraries
import pygame
import os

# import other game files
from display import *
from inv import load_inv, sell_fish
    

# font config 
BASE_DIR =  os.path.dirname(os.path.abspath(__file__))
fontPath = os.path.join(BASE_DIR, "..", "Game Assets", "determination.ttf")
font = pygame.font.Font(fontPath, size=50)
inv_font = pygame.font.Font(fontPath, size=25)

# showing inventory in the game 
def show_inv():
    inv = load_inv()

    for i, (name, item_details) in enumerate(inv.items()):
        if item_details["type"] == "item":
            row_text = f"{name} | type: {item_details["type"]} | tier: {item_details["tier"]} | value: {item_details["value"]} | {item_details["count"]}x"
        elif item_details["type"] == "fish":
            row_text = f"{name} | type: {item_details["type"]} | rarity: {item_details["rarity"]} | value: {item_details["value"]} | {item_details["count"]}x"
        
        row_text_render = inv_font.render(row_text, True, "black") # change color to black later
        y_pos = 60 + (i * 40)
        screen.blit(row_text_render, (320, y_pos))



def run_gameMenu(): 

    # rect config
    pause_rect = pygame.Rect(50, 50, 220, 400)
    inventory_rect = pygame.Rect(300, 50, 800, 390)

    # FONT CONFIGS AND RENDER
    # FISH OS TEXT config
    fishOS_text = font.render("FISH OS", True, "black")
    fbutton_x = screenWidth - fishOS_text.get_width() - 1025
    fbutton_y = screenHeight - fishOS_text.get_height() - 590
    # resume button config
    resume_button = font.render("Resume", True, "black")
    rbutton_x = screenWidth - resume_button.get_width() - 1030
    rbutton_y = screenHeight - resume_button.get_height() - 520

    # selection
    pause_selection = 0
    inv_selection = 0
    is_inv = False
    
    # position for inv_selection rectangle:
    sy_pos = 50

    running = True
    while running:
        # poll for events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_ESCAPE:
                    return "game"
                
                if event.key == pygame.K_UP:

                    if is_inv == False and pause_selection != 0:
                        pause_selection -= 1
                    elif is_inv == True and inv_selection != 0:
                        inv_selection -= 1
                        sy_pos -= 40

                if event.key == pygame.K_DOWN:

                    if is_inv == False and pause_selection != 3:
                        pause_selection += 1
                    elif is_inv == True and inv_selection != 8:
                        inv_selection += 1
                        sy_pos += 40

                if event.key == pygame.K_x:
                    if is_inv == True:
                        sell_fish(inv_selection)

                if event.key == pygame.K_RIGHT and is_inv != True:
                    is_inv = True
                    
                if event.key == pygame.K_LEFT and is_inv != False:
                    is_inv = False

        

        # draw rectangle of pause screen
        pygame.draw.rect(screen, "beige", pause_rect)
        pygame.draw.rect(screen, "brown", pause_rect, 5)

        # draw rectangle of inventory screen
        pygame.draw.rect(screen, "beige", inventory_rect)
        pygame.draw.rect(screen, "brown", inventory_rect, 5)


        if is_inv == True:
            selection_rect = pygame.Rect(300, sy_pos, 800, 50)           
            pygame.draw.rect(screen, "brown", selection_rect)

        # blit fonts
        screen.blit(fishOS_text, (fbutton_x, fbutton_y))
        screen.blit(resume_button, (rbutton_x, rbutton_y))

        show_inv()

        pygame.display.flip()

        clock.tick(60)
    
    return "quit"
