import random



# Fishes Available:

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
