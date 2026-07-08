import random
import csv 
import pygame
import os

# Setup
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FISH_CSV_PATH = os.path.join(BASE_DIR, "..", "..", "Game Assets", "Fish Data", "fish.csv")

# fish csv file
def read_fishes(depth_selection):

    possible_fishes = []

    with open(FISH_CSV_PATH, newline='') as csvfile:
        fishreader = csv.DictReader(csvfile)
        for row in zip(fishreader, range(0, depth_selection)):
            possible_fishes.append(row)
    
    print(possible_fishes)


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
    catchRNG()
    return 

def catchRNG():
    shallowFish = ["Minnow", "Shark", "><))*>"]
    fishRarity = random.randint(1, 100)

    if fishRarity <= 50:
        fish = shallowFish[0]

    elif fishRarity > 50 and fishRarity <= 80:
        fish = shallowFish[1]
        
    elif fishRarity > 80:
        fish = shallowFish[2]
    
    print(f"caught a {fish}!")
    
    return fish
