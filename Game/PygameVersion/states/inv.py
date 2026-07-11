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
    if item_type == "fish":
        item_name = item["fish_name"]
    elif item_type == "item":
        item_name = item["item_name"] # unmade csv file for items

    if item in inv:
        inv[item_name]["count"] += 1
    else:
        if item_type == "fish":
            inv[item_name] = {item_name: {"type": "fish", "count": 1, "rarity": item["rarity"]}}
        elif item_type == item:
            inv[item_name] = {item_name: {"type": "fish", "count": 1, "rarity": item["tier"]}}

    return inv[item_name]

def save_inv()

