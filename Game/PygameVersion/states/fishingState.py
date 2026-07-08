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
        for row in fishreader: # WORK ON THIS ITS ONLY PUTTING BASED ON THE LITERAL LOOP NOT THE DEPTH
            if row['depth'] in depth_scope:
                possible_fishes.append(row)

    return possible_fishes

def waitFish():

    # Set up for time 
    shallow_catch_time = random.randint(3000, 10000)
    time_start = pygame.time.get_ticks()
    time_end = time_start + shallow_catch_time

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

#TODO: FINISH CATCHING RNG SYSTEM
def catchRNG(fishes, depth_scope):
    pass

def catch_fish(DEPTH_LIST, depth_selected):
    depth_scope = DEPTH_LIST[:depth_selected + 1]
    fishes = load_fishes(depth_scope)
    waitFish()
    catchRNG(fishes, depth_scope)
