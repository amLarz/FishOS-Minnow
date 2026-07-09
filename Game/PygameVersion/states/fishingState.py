import random
import csv 
import pygame
import os

# Setup
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FISH_CSV_PATH = os.path.join(BASE_DIR, "..", "..", "Game Assets", "Fish Data", "fish.csv")

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
    catch_time = random.randint(3000, 10000)
    time_start = pygame.time.get_ticks() 
    time_end = time_start + catch_time

    last_tick = time_start # every second start 
    current_time = time_start # ever milisecond start

    # Keeps space for adding dots
    print("fishing", end="")

    while current_time <= time_end:
        
        current_time = pygame.time.get_ticks()

        if last_tick <= current_time - 1000:
            last_tick += 1000
            print(".", end="")

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

    return print(f"caught a {selected_rarity} {selected_fish['fish_name']}!")

def catch_fish(DEPTH_LIST, depth_selected):
    depth_scope = DEPTH_LIST[:depth_selected + 1]
    print(depth_scope)
    fishes = load_fishes(depth_scope)
    waitFish()
    catchRNG(fishes, depth_scope)

    return