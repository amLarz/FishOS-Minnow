import pygame
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# sprite paths
idle_path = os.path.join(BASE_DIR, "..", "Game Assets", "Art", "Right_Idle.png")
fish_path = os.path.join(BASE_DIR, "..", "Game Assets", "Art", "Right_fish.png")
catch_path = os.path.join(BASE_DIR, "..", "Game Assets", "Art", "Right_catch.png")

# sprite characters
class Character:
    def __init__(self, sprite, x, y):
        # get the image from the path
        original = pygame.image.load(sprite).convert_alpha()
        w, h = original.get_size()
        self.sprite = pygame.transform.scale(original, (w * 10, h * 10))
        self.x = x
        self.y = y
        
    def draw(self, screen):
        screen.blit(self.sprite, (self.x, self.y))

# sprites config
idle_sprite = Character(idle_path, 480, 220)
fish_sprite = Character(fish_path, 480, 220)
catch_sprite = Character(catch_path, 480, 220)
