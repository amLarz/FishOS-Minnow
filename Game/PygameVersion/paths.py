import sys
import os

def resource_path(relative_path):
    if hasattr(sys, "_MEIPASS"):
        base_path = sys._MEIPASS
    else:
        base_path = os.path.dirname(os.path.abspath(__file__))
    
    return os.path.join(base_path)

def save_path(filename):
    if hasattr(sys, "_MEIPASS"):
        base_path = os.path.join(os.path.expanduser("~"), "FishOS-Minnow")
        os.makedirs(base_path,exist_ok=True)
    else:
        base_path = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(base_path, filename)