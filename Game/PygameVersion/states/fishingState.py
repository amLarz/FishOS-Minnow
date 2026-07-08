import random
import csv 

# Depth switcher
def permitted_depth():
    if 

# fish csv file
def read_fishes():
    with open ('fish.csv', newline='') as csvfile:
        fishreader = csv.reader(csvfile)
        for row in fishreader:
            if 

# SHALLOW LEVEL FISH 
shallow_fish = ['Clown']

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
