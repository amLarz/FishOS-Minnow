# import libraries
import pygame
import os

# import other game files
from display import *
from inv import load_inv
    

# font config 
BASE_DIR =  os.path.dirname(os.path.abspath(__file__))
fontPath = os.path.join(BASE_DIR, "..", "Game Assets", "determination.ttf")
font = pygame.font.Font(fontPath, size=50)
inv_font = pygame.font.Font(fontPath, size=25)

def on_inv():
    inv = load_inv()

    for i, (name, item_details) in enumerate(inv.items()):
        if item_details["type"] == "item":
            row_text = f"{name} | type: {item_details["type"]} | tier: {item_details["tier"]} | value: {item_details["value"]} | {item_details["count"]}x"
        elif item_details["type"] == "fish":
            row_text = f"{name} | type: {item_details["type"]} | rarity: {item_details["rarity"]} | value: {item_details["value"]} | {item_details["count"]}x"
        
        row_text_render = inv_font.render(row_text, True, "black") # change color to black later
        separation = inv_font.render("__________________________________________________", True, "black")
        y_pos = 80 + (i * 40)
        screen.blit(row_text_render, (320, y_pos))
        screen.blit(separation, (320, y_pos + 10))

def run_gameMenu(): 

    # rect config
    pause_rect = pygame.Rect(50, 50, 220, 400)
    inventory_rect = pygame.Rect(300, 50, 800, 400)

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
    selection = 0

    running = True
    while running:
        # poll for events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return "game"
                if event.key == pygame.K_UP and selection != 0:
                    selection -= 1

        

        # draw rectangle of pause screen
        pygame.draw.rect(screen, "beige", pause_rect)
        pygame.draw.rect(screen, "brown", pause_rect, 5)

        # draw rectangle of inventory screen
        pygame.draw.rect(screen, "beige", inventory_rect)
        pygame.draw.rect(screen, "brown", inventory_rect, 5)

        # blit fonts
        screen.blit(fishOS_text, (fbutton_x, fbutton_y))
        screen.blit(resume_button, (rbutton_x, rbutton_y))

        on_inv()

        pygame.display.flip()

        clock.tick(60)
    
    return "quit"
