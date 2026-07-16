import json
import os
from display import *
from paths import resource_path

# Setup inventory file path
INV_JSON_PATH = resource_path(os.path.join("..", "PygameVersion", "inv.json"))


def load_inv():
    
    inv = {}

    if not os.path.exists(INV_JSON_PATH):
        # Fishing rod is always going to be in your inventory.
        inv = {"Fishing Rod": {"type": "item", "count": 1, "tier": 1, "value": 1}, 
               "Coin Bag": {"type": "item", "count": 1, "tier": 1, "value": 1}}
        
        with open(INV_JSON_PATH, "w") as file:
            json.dump(inv, file, indent=2)
    else:
        with open(INV_JSON_PATH, "r") as file:
            inv = json.load(file)

    return inv

def add_inv(inv, item, item_type):

    if item_type == "fish":
        item_name = item["fish_name"]
    elif item_type == "item":
        item_name = item["item_name"]
    if item_name in inv:
        inv[item_name]["count"] += 1
    else:
        if item_type == "fish":
            inv[item_name] = {"type": "fish", "count": 1, "rarity": item["rarity"], "value": int(item["value"])}
        elif item_type == "item":
            inv[item_name] = {"type": "item", "count": 1, "rarity": item["tier"], "value": int(item["value"])}

    return inv


def save_inv(inv):

    with open(INV_JSON_PATH, "w") as file:
        json.dump(inv, file, indent=2)

    return 

def store_catch(item, item_type):
    # Loading the current inventory
    inv = load_inv()
    # Adding item to inventory
    add_inv(inv, item, item_type)
    # Saving the item to the JSON file, saving the item. 
    save_inv(inv)

    return

def sell_fish(selected_item):
    inv = load_inv()
    item = list(inv.keys())[selected_item]

    if inv[item]["type"] == "item":
        return
    
    fish = inv[item]
    fish_value = fish["value"]

    inv["Coin Bag"]["value"] += fish_value


    if inv[item]["count"] > 1:
        inv[item]["count"] -= 1
    else:
        del inv[item]
        
    save_inv(inv)
    
    return



    

