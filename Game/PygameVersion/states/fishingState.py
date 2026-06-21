import time
import random

# Fishes Available:
shallowFish = ["Minnow", "Shark", "><))*>"]


def fishingState():
    shallowCatchTime = random.randint(3, 10)
    fishRarity = random.randint(1, 100)

    print("fishing", end="")
    for seconds in range(shallowCatchTime):
        time.sleep(1)
        print(".", end="")

    if fishRarity <= 50:
        fish = shallowFish[0]
    elif fishRarity > 50 and fishRarity <= 80:
        fish = shallowFish[1]
    elif fishRarity > 80:
        fish = shallowFish[2]
    
    print("")
    print(f"caught a {fish}!")
