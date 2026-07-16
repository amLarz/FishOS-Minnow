# import libraries
import pygame
import os

# import other game files
from display import *
from inv import load_inv, sell_fish
from paths import resource_path
    

# font config 
fontPath = resource_path(os.path.join("..", "Game Assets", "determination.ttf"))
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

    inv = load_inv()

    # rect config
    pause_rect = pygame.Rect(50, 50, 220, 400)
    inventory_rect = pygame.Rect(300, 50, 800, 390)

    # FONT CONFIGS AND RENDER
    # FISH OS TEXT config
    fishOS_text = font.render("FISH OS", True, "black")
    fbutton_x = screenWidth - fishOS_text.get_width() - 1025
    fbutton_y = screenHeight - fishOS_text.get_height() - 590
    # menu button config
    menu_buttonA = font.render("Menu", True, "black")
    menu_buttonB = font.render("Menu", True, "brown")
    mbutton_x = screenWidth - menu_buttonA.get_width() - 1055
    mbutton_y = screenHeight - menu_buttonA.get_height() - 460

    # Quit button config
    quit_buttonA = font.render("Quit", True, "black")
    quit_buttonB = font.render("Quit", True, "brown")
    qbutton_x = screenWidth - quit_buttonA.get_width() - 1058
    qbutton_y = screenHeight - quit_buttonA.get_height() - 400

    # Inv button config
    inv_buttonA = font.render("Inv", True, "black")
    inv_buttonB = font.render("Inv", True, "brown")
    ibutton_x = screenWidth - inv_buttonA.get_width() - 1070
    ibutton_y = screenHeight - inv_buttonA.get_height() - 520 

    # selling font
    x_2sell = inv_font.render("'X' to sell", True, "black")
    x_textX = ((screenWidth - x_2sell.get_width()) // 2) + 390
    x_textY = ((screenHeight - x_2sell.get_height()) // 2) + 60

    # selection
    pause_selection = 0
    inv_selection = 0
    is_inv = False
    PAUSE_CAP = 2
    inv_cap = len(inv) - 1
    MIN_CAP = 0
    
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

                    if is_inv == False and pause_selection != MIN_CAP:
                        pause_selection -= 1
                    elif is_inv == True and inv_selection != MIN_CAP:
                        inv_selection -= 1
                        sy_pos -= 40

                if event.key == pygame.K_DOWN:

                    if is_inv == False and pause_selection != PAUSE_CAP:
                        pause_selection += 1
                    elif is_inv == True and inv_selection != inv_cap:
                        inv_selection += 1
                        sy_pos += 40

                if event.key == pygame.K_f:
                    if is_inv == False:
                        if pause_selection == 0:
                            is_inv = True
                        if pause_selection == 1:
                            return "menu"
                        if pause_selection == 2:
                            return "quit"

                if event.key == pygame.K_x:
                    if is_inv == True:
                        sell_fish(inv_selection)
                        inv = load_inv()
                        inv_cap = len(inv)
                        if inv_selection == inv_cap:
                            inv_selection -= 1
                            inv_cap -= 1
                            sy_pos -= 40

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

        # draw small font x to sell
        screen.blit(x_2sell, (x_textX, x_textY))

        if is_inv == True:
            selection_rect = pygame.Rect(300, sy_pos, 800, 50)           
            pygame.draw.rect(screen, "brown", selection_rect)

        # blit fonts
        screen.blit(fishOS_text, (fbutton_x, fbutton_y))

        # selected flashing effect
        if pause_selection == 0 and is_inv == False:
                screen.blit(inv_buttonB, (ibutton_x, ibutton_y))
        else: 
            screen.blit(inv_buttonA, (ibutton_x, ibutton_y))

        if pause_selection == 1 and is_inv == False:
                screen.blit(menu_buttonB, (mbutton_x, mbutton_y))
        else: 
            screen.blit(menu_buttonA, (mbutton_x, mbutton_y))
        
        if pause_selection == 2 and is_inv == False:
                screen.blit(quit_buttonB, (qbutton_x, qbutton_y))
        else: 
            screen.blit(quit_buttonA, (qbutton_x, qbutton_y))



        show_inv()

        pygame.display.flip()

        clock.tick(60)
    
    return "quit"
