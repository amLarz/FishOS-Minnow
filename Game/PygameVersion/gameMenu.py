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

def on_inv():
    inv = load_inv()

    item_text_array = []
    detail_text_array = []

    for item in inv:
        item_text_array.append(item)

        if item["type"] == "item":
            detail_text_array.append(f"type: item, tier: {item["tier"]}, value: {item["value"]}, {item["count"]}x")
        elif item["type"] == "fish":
            detail_text_array.append(f"type: fish, rarity: {item["rarity"]}, value: {item["value"]}, {item["count"]}x")

    # render text
    for item in item_text_array:
        item_name_text = font.render(item, True, "white")
        nitem_x = screenWidth - item.get_width() - 600
        nitem_y = screenHeight - item.get_height() - 100

        screen.blit(item_name_text, (nitem_x, nitem_y))


def run_gameMenu(): 

    # rect config
    pause_rect = pygame.Rect(50, 50, 220, 400)
    inventory_rect = pygame.Rect(300, 50, 600, 400)

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



        pygame.display.flip()

        clock.tick(60)
    
    return "quit"
