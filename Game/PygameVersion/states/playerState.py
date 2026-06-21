import time
import random

# pygame setup


def fishingState():
    shallowCatchTime = random.randint(3, 10)

    print("fishing", end="")
    for seconds in range(shallowCatchTime):
        time.sleep(1)
        print(".", end="")
    print("")
    print("caught!")
