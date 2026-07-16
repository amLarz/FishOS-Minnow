import random
import csv 
import os
import time

from inv import store_catch
from sprite import fish_sprite, catch_sprite
from display import *
from tilemap import draw_tile
from paths import resource_path

# Setup
FISH_CSV_PATH = resource_path(os.path.join("Game", "Game Assets", "Fish Data", "fish.csv"))

# font setup
fontPath = resource_path(os.path.join("Game", "Game Assets", "determination.ttf"))
f_font = pygame.font.Font(fontPath, size = 40)


# fish csv file
def load_fishes(depth_scope):

    possible_fishes = []

    with open(FISH_CSV_PATH, newline='') as csvfile:
        fishreader = csv.DictReader(csvfile)
        for row in fishreader: 
            if row['depth'] in depth_scope:
                possible_fishes.append(row)

    return possible_fishes

def waitFish():

    # Set up for time 
    catch_time = random.randint(3, 10)
    time_start = time.monotonic()
    time_end = time_start + catch_time

    last_tick = time_start # every second start 
    current_time = time_start # ever milisecond start

    # Keeps space for adding dots
    print("fishing", end="")

    fishing_text = ["fishing"]

    while current_time <= time_end:

        fish_sprite.draw(screen)

        current_time = time.monotonic()

        if last_tick <= current_time - 1:
            fishing_text.append(".")
            joined_list = "".join(fishing_text)
            render_dots = f_font.render(joined_list, True, "black")

            screen.blit(render_dots, (820, 250))

            last_tick += 1
            print(".", end="")
        
        pygame.display.flip()

    print("")
    
    return 

#TODO: FINISH CATCHING RNG SYSTEM
def catchRNG(fishes, depth_scope):

    RARITY_LIST = {
            'common': (1, 40), 
            'uncommon': (41, 70),
            'rare': (71, 85), 
            'legendary': (86, 95),
            'exotic': (96, 100),
       }
    
    ndepth_scope = len(depth_scope)
    rarity_cap = 100
    
    if ndepth_scope == 1:
        rarity_cap = 85
    elif ndepth_scope == 2:
        rarity_cap = 95

    rng = random.randint(1, rarity_cap)

    for rarity, (low, high) in RARITY_LIST.items():
        if low <= rng <= high:
            selected_rarity = rarity

    possible_rarity_fishes = [matching_fishes for matching_fishes in fishes if matching_fishes['rarity'] == selected_rarity]

    selected_fish = random.choice(possible_rarity_fishes)

    return selected_fish

def catch_fish(DEPTH_LIST, depth_selected):
    # Takes a list of the depth scope
    depth_scope = DEPTH_LIST[:depth_selected + 1]
    # Loads all the fishes 
    fishes = load_fishes(depth_scope)
    # Time/waiting for reel algorithm
    waitFish()
    # Getting the fish caught with the RNG
    selected_fish = catchRNG(fishes, depth_scope)

    start_time = time.monotonic()
    end_time =start_time + 1.4
    current_time = start_time

    while current_time <= end_time:
        draw_tile()
        current_time = time.monotonic()

        fish_caught = f_font.render(f"caught an {selected_fish['rarity']} {selected_fish['fish_name']}!", True, (255, 255, 0))
        screen.blit(fish_caught, (250, 150))
        catch_sprite.draw(screen)

        pygame.display.flip()
    # Starting storing to inventory algorithm
    store_catch(selected_fish, "fish")
    fishing_state = False

    return fishing_state
    