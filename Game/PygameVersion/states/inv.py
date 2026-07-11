import json
import os

# Setup inventory file path
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
INV_JSON_PATH = os.path.join(BASE_DIR, "..", "..", "PygameVersion", "states", "inv.json")


def load_inv():
    inv = {}

    with open(INV_JSON_PATH, "r") as file:
        inv = json.load(file)
        print(inv)

    return inv


def add_inv(inv, item, item_type):
    if item in inv:   
       inv[item]["count"] += 1 
    else:       
        if item_type == "fish":
            



